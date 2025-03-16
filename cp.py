import streamlit as st
import pandas as pd
from datetime import datetime
from chart import *


df_pce=pd.read_csv('pce_cl.csv')
df_unp_us=pd.read_csv('unp_us.csv')
df_mon_mob=pd.read_csv('mon_mob.csv')
df_day_mob=pd.read_csv('day_mob.csv')

st.set_page_config(layout="wide")

def space(num_lines=1):
    """Adds empty lines to the Streamlit app."""
    for _ in range(num_lines):
        st.write("")

space(1)
title = '<p style="text-align: center;font-size: 30px;"><strong>Work-Life Changes in the United States During the Early COVID-19 Pandemic</strong></p>'
st.markdown(title, unsafe_allow_html=True)

"""The year 2020 will undoubtedly be a year that will never be forgotten. That year still leaves behind memories, events, and emotions 
that may remain etched in our minds due to COVID-19. The pandemic has significantly impacted various aspects of life for people worldwide. Even the United States, 
long regarded as a superpower, could not escape the effects of this pandemic. One indicator that reflects this is the U.S. Personal Consumption Expenditures (PCE) during the COVID-19 pandemic."""

space(1)

col1, col2=st.columns([1,2])
with col1 :
    space(11)
    """PCE (Personal Consumption Expenditures) represents the total expenditures made 
    by all households in the United States for daily needs, which can include food, service-based products, transportation costs, and goods. 
    The US PCE trend had always increased year on year, but when the pandemic began to surge, the PCE dropped sharply, 
    reaching it's lowest point in April 2020. We can also compare the PCE during the pandemic with the estimated PCE if the COVID-19 pandemic had not occurred."""
with col2 : 
    st.info("""#### The US PCE Dropped Sharply During Early COVID-19 Pandemic""")
    tab1, tab2 = st.tabs(["2018-Present", ""])
    with tab1:
        text = '<p style="font-size: 10px;"><strong>*PCE Prediction based on United States PCE Data during 2010-2019</strong></p>'
        st.markdown(text, unsafe_allow_html=True)
        source=df_pce[(df_pce['date']>'2018')&(df_pce['date']<'2022-05')]
        chart = get_chart_pce(source)
        st.altair_chart(chart, use_container_width=True)
        
    # with tab2:
    #    "Table below shows US PCE from 1959 (Billion USD)"
    #    df_pce_us_ft=df_pce[df_pce['variable']=='PCE'].set_index('date')
    #    df_pce_us_ft=df_pce_us_ft['value']
    #    df_pce_us_ft.columns=['PCE']
    #    st.dataframe(df_pce_us_ft.astype(int))
    st.write("&emsp;&emsp;Source: [*https://fred.stlouisfed.org/*](https://fred.stlouisfed.org/series/PCE)")

"""We might assume that the US PCE dropped due to the lockdown in March 2020, 
which led people in the US to reduce their mobility, thereby lowering transportation costs and other out-of-home expenses. But is this true?"""
space(1)
col1, col2=st.columns([2,1])
with col1 :
    st.info("""#### US Unemployment rate Increased Significantly on The Early COVID-19 Pandemic""")
    tab1, tab2 = st.tabs(["2018-Present", "1960-Present"])
    with tab1:
        source4=df_unp_us[(df_unp_us['date']>'2018')&(df_unp_us['date']<'2022-05')]
        chart=get_chart_unp(source4)
        st.altair_chart(chart, use_container_width=True)

    with tab2:
        source4=df_unp_us[(df_unp_us['date']>'1960')&(df_unp_us['date']<'2022-05')]
        chart=get_chart_unp(source4)
        st.altair_chart(chart, use_container_width=True)
    st.write("&emsp;&emsp;Source: [*https://data.oecd.org/*](https://data.oecd.org/unemp/unemployment-rate.htm#indicator-chart)")

with col2 :
    space(15)
    """The US Unemployment rate increased significantly during the early COVID-19 Pandemic and reaching it's highest point in April 2020. This point also marked an all-time high for over last 60 years.
    Expenditures likely decreased due to many US citizens losing their jobs."""
      
st.warning("""The similarity between US PCE Trends and the unemployment rate is the gradual decrease after the significant changes in April 2020 and approaching normal levels by the year 2022.""")
        

with st.expander("Click to show PCE Trends and the unemployment rate again"):
    col1, col2=st.columns([1,1])
    with col1 :
        source=df_pce[(df_pce['date']>'2018')&(df_pce['date']<'2022-05')]
        chart = get_chart_pce(source)
        st.altair_chart(chart, use_container_width=True)
        space(2)
    with col2 :
        source4=df_unp_us[(df_unp_us['date']>'2018')&(df_unp_us['date']<'2022-05')]
        chart=get_chart_unp(source4)
        st.altair_chart(chart, use_container_width=True)
"""Does this mean that US citizens are returning to their normal lives (especially their work lives) as before?""" 
"""We will analyze US Citizens mobility trends on various locations to validate our assumptions."""

space(1)

col1, col2=st.columns([1,2])
with col2:
    st.info("""#### US Citizens Mobility Trends During Pandemic""")
    source3=df_mon_mob[(df_mon_mob['date']<'2022-07')&(df_mon_mob['code']=='USA')]
    source3=source3[['date','variable','value']]
    all_symbols = source3.variable.unique()
    symbols = st.multiselect("Choose Category to Visualize", all_symbols, all_symbols)

    chc = st.checkbox('Show Trends Per Day')
    text = '<p style="font-size: 11px;"><strong>*NRM determined based on median visitors on 03 January 2020 Until 06 February 2020</strong></p>'
    st.markdown(text, unsafe_allow_html=True)
    if chc :
        tab1, tab2=st.tabs(["Average Per Month", "Per Day"])
        with tab1 :
            source = source3[source3.variable.isin(symbols)]
            for i in source.date.unique():
                add=pd.DataFrame({'date': [i], 'variable':['NRM'],'value':[0]})
                source=pd.concat([source,add])
            chart = get_chart_mob(source)
            st.altair_chart(chart, use_container_width=True)
        with tab2 :
            source5=df_day_mob[(df_day_mob['date']<'2022-07')&(df_day_mob['code']=='USA')]
            source5=source5[['date','variable','value']]
            source = source5[source5.variable.isin(symbols)]
            for i in source.date.unique():
                add=pd.DataFrame({'date': [i], 'variable':['NRM'],'value':[0]})
                source=pd.concat([source,add])
            chart = get_chart_day_mob(source)
            st.altair_chart(chart, use_container_width=True)
    else :
        source = source3[source3.variable.isin(symbols)]
        for i in source.date.unique():
            add=pd.DataFrame({'date': [i], 'variable':['NRM'],'value':[0]})
            source=pd.concat([source,add])
        chart = get_chart_mob(source)
        st.altair_chart(chart, use_container_width=True)
    st.write("&emsp;&emsp;Source: [*https://ourworldindata.org/*](https://ourworldindata.org/covid-google-mobility-trends)")
with col1:
    space(5)
    text = '<p style="font-size: 12px;"><strong>KTR : Workplaces</strong></p>'
    st.markdown(text, unsafe_allow_html=True)
    text = '<p style="font-size: 12px;"><strong>TP&ensp;&nbsp;: Public transport stations</strong></p>'
    st.markdown(text, unsafe_allow_html=True)
    text = '<p style="font-size: 12px;"><strong>RCF : Restaurants, cafes, movie theaters, etc.</strong></p>'
    st.markdown(text, unsafe_allow_html=True)
    text = '<p style="font-size: 12px;"><strong>SAP : Grocery and Pharmacy Stores</strong></p>'
    st.markdown(text, unsafe_allow_html=True)
    text = '<p style="font-size: 12px;"><strong>NRM : Normal baseline before pandemic emerged</strong></p>'
    st.markdown(text, unsafe_allow_html=True)

    space(3)
    """All category show the same trend patterns, with only a difference in the range of value.
    Fluctuating events that occurred between late 2020 to early 2021 and late 2021 to early 2022 were caused by the winter season in the US, 
    which led to citizens tending to stay at home. Additionally, we can observe that the KTR and TP categories did not reach their normal values, not even for a single day."""


st.warning("As we already know that unemployment rate decreased along the time means that US citizens change over to *WFH* (*Work From Home*)")
st.write("Then why did the PCE trends still increase while US citizens shifted to *WFH* (transportations cost reduced)? This was caused by a change in spending habit among US citizens after the pandemic starts[[1]](https://www.boj.or.jp/en/research/wps_rev/rev_2020/rev20e07.htm/)[[2]](https://www2.deloitte.com/us/en/insights/economy/us-consumer-spending-after-covid.html).")
"""US citizens tends to reduce their cost on service-based products and increased their spend on basic needs.
        That's why we can see that SAP category increases some times compared to normal value before pandemic."""

with st.expander("Other countries? Click Here!"):
    symbols2 = st.multiselect("Choose Category to Visualizen", all_symbols, ['TP','KTR'],key=1)
    col1, col2=st.columns([1,1])
    with col1 :
        option1 = st.selectbox('Choose Country (1):',
        ('United States','Canada','United Kingdom','France', 'Singapore','Japan','Australia'))
        tab1, tab2=st.tabs(["Average Per Month", "Per Day"])
        with tab1 :
            source3=df_mon_mob[(df_mon_mob['date']<'2022-07')&(df_mon_mob['country']==option1)]
            source3=source3[['date','variable','value']]
            source = source3[source3.variable.isin(symbols2)]
            for i in source.date.unique():
                add=pd.DataFrame({'date': [i], 'variable':['NRM'],'value':[0]})
                source=pd.concat([source,add])
            chart = get_chart_mob(source)
            st.altair_chart(chart, use_container_width=True)
        with tab2 :
            source5=df_day_mob[(df_day_mob['date']<'2022-07')&(df_day_mob['country']==option1)]
            source5=source5[['date','variable','value']]
            source = source5[source5.variable.isin(symbols2)]
            for i in source.date.unique():
                add=pd.DataFrame({'date': [i], 'variable':['NRM'],'value':[0]})
                source=pd.concat([source,add])
            chart = get_chart_day_mob(source)
            st.altair_chart(chart, use_container_width=True)

    with col2 :
        option2 = st.selectbox('Choose Country (2):',
        ('Indonesia','Brazil','Mexico','Poland','Hungary','India','South Africa'))
        tab1, tab2=st.tabs(["Average Per Month", "Per Day"])
        with tab1 :
            source3=df_mon_mob[(df_mon_mob['date']<'2022-07')&(df_mon_mob['country']==option2)]
            source3=source3[['date','variable','value']]
            source = source3[source3.variable.isin(symbols2)]
            for i in source.date.unique():
                add=pd.DataFrame({'date': [i], 'variable':['NRM'],'value':[0]})
                source=pd.concat([source,add])
            chart = get_chart_mob(source)
            st.altair_chart(chart, use_container_width=True)
        with tab2 :
            source5=df_day_mob[(df_day_mob['date']<'2022-07')&(df_day_mob['country']==option2)]
            source5=source5[['date','variable','value']]
            source = source5[source5.variable.isin(symbols2)]
            for i in source.date.unique():
                add=pd.DataFrame({'date': [i], 'variable':['NRM'],'value':[0]})
                source=pd.concat([source,add])
            chart = get_chart_day_mob(source)
            st.altair_chart(chart, use_container_width=True)

    """Citizens in developing countries tends to return to their previous state in terms of *WFO (Work From Office)*.
       Meanwhile citizens in developed countries tend to become more comfortable with WFH (Work From Home), although there is a possibility that it will approach normalcy over time, 
       but at a slower pace compared to developing countries. All of this can be observed in the TP and KTR categories."""
    """On RCF and SAP categories also have a same patterns but with a faster pace than TP and KTR. 
       All of this is likely caused by the differences in the ease and affordability of doing things online among those countries."""

space(3)
end = '<p style="text-align: center;font-size: 14px;"><strong>Pragasto Aji Hendro Puadi</strong></p>'
st.markdown(end, unsafe_allow_html=True)

hide_streamlit_style = """
<style>
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
