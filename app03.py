import pandas as pd
import yfinance as yf
import altair as alt
import streamlit as st

def app():
    st.title('app / Visualization of stock prices')

    st.sidebar.write("""
    # Option
    You can change the display days & the price range from the following options.
    """)

    st.sidebar.write("""
    ## Display days
    """)

    days = st.sidebar.slider('Pls select display days',1,50,20)

    st.write(f"""
    ### Stock Price for **{days}days**
    # """)

    @st.cache 
    def get_data(days, tickers):
        df = pd.DataFrame()
        for company in tickers.keys():
            tkr = yf.Ticker(tickers[company])
            hist = tkr.history(period =f'{days}d')
            hist.index = hist.index.strftime('%d %B %y')
            hist = hist[['Close']]
            hist.columns = [company]
            hist = hist.T
            hist.index.name='Name'
            df = pd.concat([df,hist])
        return df

    try:
        st.sidebar.write("""
        ## Price range
        """)
        ymin, ymax = st.sidebar.slider(
            'Pls select Price range',
            0.0, 3500.0, (0.0, 4000.0)
        )

        tickers = {
            'apple': 'AAPL',
            'facebook': 'FB',
            'google': 'GOOGL',
            'microsoft': 'MSFT',
            'netflix': 'NFLX',
            'amazon': 'AMZN'
        }

        df = get_data(days, tickers)
        companies = st.multiselect(
            'Pls select some companies.',
            list(df.index),
            ['google','amazon','facebook','apple']
        )

        if not companies:
            st.error('Pls choose at least one company.')
        else:
            data =df.loc[companies]
            st.write("### Stock Price（USD）",data.sort_index())
            data = data.T.reset_index()
            data = pd.melt(data,id_vars=['Date']).rename(
                columns={'value':'Stock Price(USD)'}
            )

            chart = (
                alt.Chart(data)
                .mark_line(opacity = 0.8,clip=True)
                .encode(
                    x="Date:T",
                    y=alt.Y("Stock Price(USD):Q", stack=None, scale=alt.Scale(domain=[ymin, ymax])),
                    color='Name:N'
                )
            )

            st.altair_chart(chart, use_container_width=True)

    except:
        st.error(
            "Whoops --  Something went wrong !"
        )
