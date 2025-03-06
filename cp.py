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
title = '<p style="text-align: center;font-size: 30px;"><strong>Perubahan <em>Work-life</em> di Amerika Serikat Pada Awal Pandemi COVID-19</strong></p>'
st.markdown(title, unsafe_allow_html=True)

"""Tahun 2020 jelas akan menjadi tahun yang tidak akan pernah terlupakan. Tahun tersebut masih meninggalkan kenangan, peristiwa dan rasa haru yang mungkin masih membekas dalam pikiran
karena COVID-19. Pandemi tersebut telah banyak mempengaruhi aspek kehidupan semua manusia di dunia. Bahkan Amerika Serikat yang telah lama disebut sebagai Negara Adikuasa pun 
tidak dapat menghindar dari efek pandemi satu ini. Negara Adikuasa tersebut malah terpukul cukup telak saat kasus terkonfimasi yang terjadi disana mulai meledak.
Salah satu indikator yang menunjukkan hal tersebut adalah PCE(*Personal Consumption Expenditures*)  Amerikat Serikat selama masa pandemi COVID-19."""

space(1)

col1, col2=st.columns([1,2])
with col1 :
    space(11)
    """PCE(Personal Consumption Expenditures) menunjukkan  total pengeluaran yang dikeluarkan oleh seluruh rumah tangga di Amerika Serikat (AS) untuk 
    kebutuhan sehari-hari yang dapat berupa makanan, produk berupa layanan, biaya transportasi dan barang untuk jangka waktu pendek maupun panjang. 
    Tren PCE AS selalu meningkat dari tahun ke tahun namun saat pandemi mulai meledak, PCE menurun secara tajam yang mencapai titik terendah pada bulan April 2020.
    Kita juga dapat membandingkan PCE yang terjadi selama masa pandemi dengan perkiraan PCE jika tidak terjadi pandemi COVID-19."""
with col2 : 
    st.info("""#### PCE Amerika Serikat Terjun Bebas Saat Awal Pandemi COVID-19""")
    tab1, tab2 = st.tabs(["2018-Sekarang", "Tabel"])
    with tab1:
        text = '<p style="font-size: 10px;"><strong>*Prediksi PCE dibuat berdasar data PCE Amerika Serikat Selama 2010-2019</strong></p>'
        st.markdown(text, unsafe_allow_html=True)
        source=df_pce[(df_pce['date']>'2018')&(df_pce['date']<'2022-05')]
        chart = get_chart_pce(source)
        st.altair_chart(chart, use_container_width=True)
        
    with tab2:
       "Berikut ini tabel yang menunjukkan nilai PCE AS sejak tahun 1959 (dalam miliar USD)"
       df_pce_us_ft=df_pce[df_pce['variable']=='PCE'].set_index('date')
       df_pce_us_ft=df_pce_us_ft['value']
       df_pce_us_ft.columns=['PCE']
       st.dataframe(df_pce_us_ft.astype(int))
    st.write("&emsp;&emsp;Sumber: [*https://fred.stlouisfed.org/*](https://fred.stlouisfed.org/series/PCE)")

"""Mungkin kita akan mengira bahwa PCE AS menurun dikarenakan adanya lockdown yang dimulai pada bulan Maret 2020 sehingga masyarakat di AS mengurangi mobilitas yang kemudian mengurangi biaya transportasi serta biaya
    di luar rumah lainnya. Namun apakah hanya itu saja yang mempengaruhi menurunnya PCE di AS?"""
space(1)
col1, col2=st.columns([2,1])
with col1 :
    st.info("""#### Pengangguran di AS Meningkat Tajam Saat Awal Pandemi COVID-19""")
    tab1, tab2 = st.tabs(["2018-Sekarang", "1960-Sekarang"])
    with tab1:
        source4=df_unp_us[(df_unp_us['date']>'2018')&(df_unp_us['date']<'2022-05')]
        chart=get_chart_unp(source4)
        st.altair_chart(chart, use_container_width=True)

    with tab2:
        source4=df_unp_us[(df_unp_us['date']>'1960')&(df_unp_us['date']<'2022-05')]
        chart=get_chart_unp(source4)
        st.altair_chart(chart, use_container_width=True)
    st.write("&emsp;&emsp;Sumber: [*https://data.oecd.org/*](https://data.oecd.org/unemp/unemployment-rate.htm#indicator-chart)")

with col2 :
    space(15)
    """Tingkat pengangguran di AS juga meningkat tajam saat awal pandemi COVID-19 yang juga mencapai titik tertinggi di bulan april 2020.
    Pengeluaran yang berkurang kemungkinan besar juga terjadi akibat banyak dari mereka yang kehilangan pekerjaannya. 
    Bahkan tingkat pengangguran ini menjadi yang tertinggi dalam sejarah 
    Amerika serikat selama lebih dari 60 tahun terakhir!"""
      
st.warning("""Persamaan antara grafik PCE and tingkat pengangguran di AS adalah tren melandai yang terjadi setelah mengalami perubahan 
                yang cukup tajam di bulan April 2020 dan semakin mendekati normal menjelang tahun 2022.""")
        

with st.expander("Klik untuk melihat kembali grafik PCE dan Tingkat pengangguran di AS"):
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
"""Apakah hal ini berarti masyarakat AS mulai menjalani kehidupan (terutama dalam hal pekerjaan) yang semakin mendekati normal seperti dahulu?""" 
"""Untuk mengetahui hal tersebut kita akan melihat grafik pola mobilitas masyarakat AS yang diukur berdasar perubahan pengunjung pada setiap kategori tempat."""

space(1)

col1, col2=st.columns([1,2])
with col2:
    st.info("""#### Perubahan Mobilitas Masyarakat AS Selama Pandemi""")
    source3=df_mon_mob[(df_mon_mob['date']<'2022-07')&(df_mon_mob['code']=='USA')]
    source3=source3[['date','variable','value']]
    all_symbols = source3.variable.unique()
    symbols = st.multiselect("Pilih Kategori Untuk Divisualisasikan", all_symbols, all_symbols)

    chc = st.checkbox('Tampilkan juga perubahan pengunjung per hari')
    text = '<p style="font-size: 11px;"><strong>*NRM ditentukan berdasarkan median pengunjung pada 03 Januari 2020 sampai 06 Februari 2020</strong></p>'
    st.markdown(text, unsafe_allow_html=True)
    if chc :
        tab1, tab2=st.tabs(["Rataan Per Bulan", "Per Hari"])
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
    st.write("&emsp;&emsp;Sumber: [*https://ourworldindata.org/*](https://ourworldindata.org/covid-google-mobility-trends)")
with col1:
    space(5)
    text = '<p style="font-size: 12px;"><strong>KTR : Kantor, tempat kerja dan sejenisnya</strong></p>'
    st.markdown(text, unsafe_allow_html=True)
    text = '<p style="font-size: 12px;"><strong>TP&ensp;&nbsp;: Stasiun, bandara dan tempat transportasi publik lainnya</strong></p>'
    st.markdown(text, unsafe_allow_html=True)
    text = '<p style="font-size: 12px;"><strong>RCF : Restaurant, cafe, bioskop dan sejenisnya</strong></p>'
    st.markdown(text, unsafe_allow_html=True)
    text = '<p style="font-size: 12px;"><strong>SAP : Supermarket, pasar, toko dan sejenisnya</strong></p>'
    st.markdown(text, unsafe_allow_html=True)
    text = '<p style="font-size: 12px;"><strong>NRM : Nilai awal sebelum pandemi</strong></p>'
    st.markdown(text, unsafe_allow_html=True)

    space(3)
    """Semua kategori mempunyai pola fluktuatif yang hampir sama namun memiliki rentang nilai yang berbeda. 
    Fluktuatif yang terjadi pada awal dan akhir tahun 2020-2021 serta 2021-2022 terjadi akibat musim dingin di AS
    sehingga masyrakat AS cenderung untuk tinggal di dalam rumah dibandingkan hari lainnya. 
    Kita pun dapat melihat kalau kategori KTR dan TP tidak pernah dalam sehari pun menyentuh titik normal seperti sebelum pandemi."""


st.warning("Sambil mengingat kembali grafik tingkat pengangguran yang terus berkurang menandakan semakin banyaknya *WFH* (*Work From Home*)")
st.write("Lalu mengapa PCE AS juga terus meningkat saat masyarakat AS banyak yang *WFH* (berkurangnya biaya transportasi)? Hal tersebut terjadi karena masyarakat di AS telah mempunyai *spending habit* yang berbeda selama masa pandemi[[1]](https://www.boj.or.jp/en/research/wps_rev/rev_2020/rev20e07.htm/)[[2]](https://www2.deloitte.com/us/en/insights/economy/us-consumer-spending-after-covid.html).")
"""Masyarakat AS cenderung mengurangi layanan produk berupa servis dan kebutuhan tersier namun menambah pengeluaran untuk kebutuhan pokok.
        Hal tersebut cukup terlihat pada kategori SAP yang beberapa kali mengalami peningkatan dibandingkan masa sebelum pandemi."""

with st.expander("Bagaimana dengan negara lain? Klik disini!"):
    symbols2 = st.multiselect("Pilih Kategori Untuk Divisualisasikan", all_symbols, ['TP','KTR'],key=1)
    col1, col2=st.columns([1,1])
    with col1 :
        option1 = st.selectbox('Pilih Negara (1):',
        ('United States','Canada','United Kingdom','France', 'Singapore','Japan','Australia'))
        tab1, tab2=st.tabs(["Rataan Per Bulan", "Per Hari"])
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
        option2 = st.selectbox('Pilih Negara (2):',
        ('Indonesia','Brazil','Mexico','Poland','Hungary','India','South Africa'))
        tab1, tab2=st.tabs(["Rataan Per Bulan", "Per Hari"])
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

    """Masyarakat di negara-negara berkembang cenderung lebih cepat kembali pada keadaan semula atau bahkan meningkat dalam hal *WFO (Work From Office)*.
       Sedangkan masyarakat di negara-negara maju cenderung mulai nyaman dengan *WFH (Work From Home)* meskipun ada kemungkinan akan
       mendekati normal seiring berjalan waktu namun lebih lambat dibandingkan dengan negara-negara berkembang. Semua itu dapat
       kita lihat pada kategori TP dan KTR."""
    """Pada kategori RCF dan SAP pun juga memiliki pola yang sama namun lebih cepat terjadi dibandingkan dengan kategori TP dan KTR. Semua itu
    kemungkinan disebabkan karena adanya perbedaan kemudahan ataupun kemurahan dalam melakukan segala sesuatu secara online pada negara maju dan negara berkembang."""

space(3)
end = '<p style="text-align: center;font-size: 14px;"><strong>Pragasto Aji Hendro Puadi - Tetris Capstone Project</strong></p>'
st.markdown(end, unsafe_allow_html=True)

hide_streamlit_style = """
<style>
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
