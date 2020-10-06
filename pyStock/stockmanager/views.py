import pandas as pd
import plotly
import plotly.graph_objs as go
import plotly.figure_factory as ff
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def index(request):
    return HttpResponse("Stock manager")


def detail(request, stock_id):
    # template = loader.get_template('stockmanager/detail.html')
    requested_urls = f'https://finance.naver.com/item/sise_day.nhn?code={stock_id}'
    df = pd.DataFrame()
    for page in range(1, 21):
        jusik_df = pd.read_html(f'{requested_urls}&page={page}', header=0)[0]
        df = df.append(jusik_df)

    df = df.rename(
        columns={'날짜': 'date', '종가': 'close', '전일비': 'diff', '시가': 'open', '고가': 'high', '저가': 'low', '거래량': 'volume'})
    df['date'] = pd.to_datetime(df['date'], format='%Y.%m.%d', errors='raise')
    df = df.dropna()
    df = df.sort_values(by='date', ascending=True)
    tail = df.tail(60)
    context = {}

    fig = ff.create_table(df)
    candlestick = plotly.offline.plot(figure_or_data={
        'data': plotly.graph_objects.Candlestick(
            close=df['close'], high=df['high'], open=df['open'], low=df['low'], x=df['date'],
            increasing_line_color='blue', decreasing_line_color='red')
    }, auto_open=False, output_type='div', image_width=400, image_height=300,)
    context['graph'] = candlestick
    context['table'] = fig.to_html()
    return render(request, 'stockmanager/detail.html', context)


def results(request):
    reponse = "You're looking at the result page"
    return HttpResponse(reponse)
