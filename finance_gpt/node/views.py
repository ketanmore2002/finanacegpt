from django.shortcuts import render,redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from .models import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.middleware import csrf
from django.http import JsonResponse
from .serializers import *
from django.contrib.auth.models import User
import yfinance as yf
from decimal import Decimal
import json
import instructor
from pydantic import BaseModel
from openai import OpenAI
from langchain.chains import APIChain
from .docs import api_docs
from langchain_openai import OpenAI
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
from nselib import capital_market



userid = get_object_or_404(User, id=1)


def get_csrf_token(request):
    # Obtain the CSRF token value
    csrf_token = csrf.get_token(request)
    # Return the CSRF token value in a JSON response
    return JsonResponse({'csrf_token': csrf_token})


@api_view(['POST'])
def create_message(request):
    serializer = MessagesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_messages_by_user_id(request, user_id):
    result = messages.objects.filter(user_id=userid)
    serializer = MessagesSerializer(result, many=True)
    return Response(serializer.data)


def get_stock_price_demo(ticker):
    stock = yf.Ticker(f"{ticker}.NS")
    return float((stock.info)['currentPrice'])

    # if trade_stock(ticker,quantity,'BUY',1) :
def trade_stock(ticker,quantity,transaction_type,user_id):
   
    user_id = 1  

    if not all([ticker, quantity, transaction_type, user_id]):
        return Response({"error": "Please provide all required fields."}, status=status.HTTP_400_BAD_REQUEST)

    if transaction_type not in ['SELL', 'BUY']:
        return Response({"error": "Invalid transaction type."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

    # Create transaction
    transaction_data = {
        'user_id': userid,
        'ticker': ticker,
        'quantity': quantity,
        'type': transaction_type
    }
    # transaction_serializer = TransactionsSerializer(data=transaction_data)
    # if transaction_serializer.is_valid():
    #     transaction = transaction_serializer.save()

    Transactions.objects.create(**transaction_data)
    if transaction_type == "SELL":
        if stocks.objects.filter(user_id=1, ticker=ticker).exists():
            stock = stocks.objects.get(user_id=1, ticker=ticker)
            if stock.quantity >= quantity:
                stock.quantity -= quantity
                stock.valuation -= Decimal(quantity) * Decimal(get_stock_price_demo(ticker))
                stock.save()
                if stock.quantity == 0:
                    stock.delete()
                    return True
                
        else: return HttpResponse("You dont have enough stocks", content_type='text/plain; charset=utf-8') 
    
    elif transaction_type == "BUY":
        print("=============================")
        if stocks.objects.filter(user_id=1, ticker=ticker).exists():
            stock = stocks.objects.get(user_id=1, ticker=ticker)
            stock.quantity += quantity
            stock.valuation += Decimal(quantity) * Decimal(get_stock_price_demo(ticker))
            stock.save()
            return True
        else:
            stocks.objects.create(user_id=1, ticker=ticker, quantity=quantity, valuation= Decimal(quantity * get_stock_price_demo(ticker)))
            return True

    # return Response(transaction_serializer.data, status=status.HTTP_201_CREATED)
    


@api_view(['GET'])
def days_stock_price(request,ticker,days):
    
    stock_data = yf.download(ticker+".NS", period=f"{days}d", interval="1d",progress=False)
    stock_data.index = stock_data.index.strftime("%d/%m/%Y")
    stock_json = stock_data.to_json(orient="index")
    stock_prices = json.loads(stock_json)

    return JsonResponse(stock_prices)
    


@api_view(['GET'])
def get_stock_price(request,ticker):
    stock = yf.Ticker(f"{ticker}.NS")
    return HttpResponse (f" The price of the {ticker} is {(stock.info)['currentPrice']}.")


@api_view(['GET'])
def get_stock_past_performace (request,ticker,days) :

    today_date = datetime.now()

    past_date = today_date - timedelta(days=3)

    today_date_str = today_date.strftime('%d-%m-%Y')
    past_date_str = past_date.strftime('%d-%m-%Y')

    data = capital_market.price_volume_and_deliverable_position_data(symbol=ticker, from_date=past_date_str, to_date=today_date_str)

    return HttpResponse ((data[["Date","ClosePrice"]]).to_string(index=False))
    


@api_view(['GET'])
def get_company_information (request,ticker) :
    stock = yf.Ticker(ticker+".NS")
    stock_info = stock.info
    return HttpResponse (((stock_info)["longBusinessSummary"]))



@api_view(['GET'])
def get_major_holders (request,ticker) :
    stock = yf.Ticker(ticker+".NS")
    major_holders = stock.major_holders
    return HttpResponse (major_holders.to_string())


@api_view(['GET'])
def sell_stocks (request,ticker,quantity) :
    if trade_stock(ticker,quantity,'SELL',request.user.id) :
        Transactions.objects.create(user_id = userid, type = "SELL", ticker=ticker, quantity=quantity , price = get_stock_price_demo(ticker)*float(quantity))
        return HttpResponse ("Stock Sold Successfully")
    else:
        return HttpResponse ("Transaction Unsuccessfull")


@api_view(['GET'])
def purchase_stocks (request,ticker,quantity) :
    print("=============================")

    if trade_stock(ticker,quantity,'BUY',1) == True :
        Transactions.objects.create(user_id = userid, type = "BUY", ticker=ticker, quantity=quantity , price = get_stock_price_demo(ticker)*float(quantity))
        return HttpResponse ("Stock Purchased Successfully")
    else:
        return HttpResponse ("Transaction Unsuccessfull")
    




llm = OpenAI(temperature=0, base_url="http://localhost:8000/v1",api_key="ketan")

@api_view(['GET'])
def chat (requests) :
    text = requests.data.get('text')
    note_book = requests.data.get('note_book')
    username = requests.data.get('username')
    password = requests.data.get('password')

    # print(username,password)
    user = authenticate(requests, username=username, password=password)

    messages.objects.create(note_book=note_book,user_id=user,message = text , type = "USER")

    # print(user)
    if user is not None:
        login(requests, user)
        chain = APIChain.from_llm_and_api_docs(
        llm=llm,
        api_docs=api_docs,
        verbose=False,
        limit_to_domains=["http://localhost:9000/"],
        )
        result = (chain.run(text))
        messages.objects.create(note_book=note_book,user_id=user,message = result , type = "SYSTEM")
        return HttpResponse(result, content_type='text/plain; charset=utf-8')
    else:
        return HttpResponse("Authorization error", content_type='text/plain; charset=utf-8')