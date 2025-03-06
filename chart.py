import altair as alt

def get_chart_pce(data):
    hover = alt.selection_single(
        fields=["date"],
        nearest=True,
        on="mouseover",
        empty="none",
    )

    lines = (
        alt.Chart(data, title="Grafik Real PCE AS VS Prediksi PCE AS Jika Tidak Terjadi Pandemi COVID-19",height=360).mark_line().encode(
            x=alt.X("date:T",title='Bulan',),
            #="value:Q",
            y=alt.Y('value:Q', scale=alt.Scale(domain=[12000, 17500]),title='Miliar USD'),
            color="variable:N",
            strokeDash="variable:N",
        )
    )

    points = lines.transform_filter(hover).mark_circle(size=65)

    base = alt.Chart(data).encode(x=alt.X("date:T",title='Bulan'))
    columns = sorted(data.variable.unique())
    tooltips = base.transform_pivot('variable', value='value', groupby=['date']).mark_rule().encode(
                    opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
                    tooltip=[alt.Tooltip(c, type='quantitative',format=',.0f',) for c in columns]+[alt.Tooltip("date:T", title="Bulan",format = ("%b %Y"),)],
                            ).add_selection(hover)

    return (lines + points + tooltips).interactive()


def get_chart_cc(data):
    hover = alt.selection_single(
        fields=["date"],
        nearest=True,
        on="mouseover",
        empty="none",
    )

    lines = (
        alt.Chart(data, title="Persentase Pertambahan Kasus Covid AS Dibandingkan Dengan Bulan Sebelumnya",height=400).mark_line().encode(
            x=alt.X("date:T",title='Bulan'),
            y=alt.Y('grwt_perc:Q',scale=alt.Scale(domain=[-100, 350]), title='Persentase (%)'),
            color=alt.value("#FF5733"),
        )
    )

    points = lines.transform_filter(hover).mark_circle(size=65)

    tooltips = (
        alt.Chart(data).mark_rule().encode(
            x=alt.X("date:T",title='Bulan'),
            y=alt.Y('grwt_perc:Q',scale=alt.Scale(domain=[-100, 350]), title='Persentase (%)'),
            opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
            tooltip=[
                alt.Tooltip("date:T", title="Bulan",format = ("%b %Y")),
                alt.Tooltip("grwt_perc:Q", title="Persentase",format=',.2f'),
                alt.Tooltip("conf_cases:Q", title="Kasus Positif"),
                alt.Tooltip("prev_ccs:Q", title="Kasus Bulan Sebelumnya"),
            ],
        )
        .add_selection(hover)
    )

    return (lines + points + tooltips).interactive()

def get_chart_mob(data):
    hover = alt.selection_single(
        fields=["date"],
        nearest=True,
        on="mouseover",
        empty="none",
    )

    lines = (
        alt.Chart(data, title="Perubahan Pengunjung Setiap Kategori Tempat Selama Pandemi COVID-19",height=400).mark_line().encode(
            x=alt.X("date:T",title='Bulan'),
            y=alt.Y('value:Q', title='Persentase % (rata-rata per bulan)',scale=alt.Scale(domain=[-55, 40])),
            color="variable:N",
            strokeDash="variable:N",
        )
    )

    points = lines.transform_filter(hover).mark_circle(size=65)

    base = alt.Chart(data).encode(x=alt.X("date:T",title='Bulan'))
    columns = sorted(data.variable.unique())
    tooltips = base.transform_pivot('variable', value='value', groupby=['date']).mark_rule().encode(
                    opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
                    tooltip=[alt.Tooltip(c, type='quantitative',format=',.2f',) for c in columns]+[alt.Tooltip("date:T", title="Bulan",format = ("%b %Y"))],
                            ).add_selection(hover)

    return (lines + points + tooltips).interactive()

def get_chart_unp(data):
    hover = alt.selection_single(
        fields=["date"],
        nearest=True,
        on="mouseover",
        empty="none",
    )

    lines = (
        alt.Chart(data, title="Persentase Pengangguran Per Bulan di AS",height=360).mark_line().encode(
            x=alt.X("date:T",title='Bulan'),
            y=alt.Y('value:Q', title='Persentase % (Terhadap jumlah seluruh tenaga kerja)'),
            color=alt.value("#2CA02C"),
        )
    )

    points = lines.transform_filter(hover).mark_circle(size=65)

    tooltips = (
        alt.Chart(data).mark_rule().encode(
            x=alt.X("date:T",title='Bulan'),
            y=alt.Y('value:Q', title='Persentase % (Terhadap jumlah seluruh tenaga kerja)'),
            opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
            tooltip=[
                alt.Tooltip("date:T", title="Bulan",format = ("%b %Y")),
                alt.Tooltip("value:Q", title="Persentase",format=',.1f'),
            ],
        )
        .add_selection(hover)
    )

    return (lines + points + tooltips).interactive()   

def get_chart_day_mob(data):
    hover = alt.selection_single(
        fields=["date"],
        nearest=True,
        on="mouseover",
        empty="none",
    )

    lines = (
        alt.Chart(data, title="Perubahan Pengunjung Setiap Kategori Tempat Selama Pandemi COVID-19 (Per Hari)",height=400).mark_line().encode(
            x=alt.X("date:T",title='Tanggal'),
            y=alt.Y('value:Q', title='Persentase (%)',scale=alt.Scale(domain=[-55, 40])),
            color="variable:N",
            strokeDash="variable:N",
        )
    )

    points = lines.transform_filter(hover).mark_circle(size=65)

    base = alt.Chart(data).encode(x=alt.X("date:T",title='Tanggal'))
    columns = sorted(data.variable.unique())
    tooltips = base.transform_pivot('variable', value='value', groupby=['date']).mark_rule().encode(
                    opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
                    tooltip=[alt.Tooltip(c, type='quantitative',format=',.2f') for c in columns]+[alt.Tooltip("date:T", title="Tanggal")],
                            ).add_selection(hover)
    return (lines + points + tooltips).interactive()