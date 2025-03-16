import altair as alt

def get_chart_pce(data):
    hover = alt.selection_single(
        fields=["date"],
        nearest=True,
        on="mouseover",
        empty="none",
    )

    lines = (
        alt.Chart(data, title="Real US PCE VS US PCE Prediction if COVID-19 Pandemic Had not Occured",height=360).mark_line().encode(
            x=alt.X("date:T",title='Month',),
            #="value:Q",
            y=alt.Y('value:Q', scale=alt.Scale(domain=[12000, 17500]),title='Billion USD'),
            color="variable:N",
            strokeDash="variable:N",
        )
    )

    points = lines.transform_filter(hover).mark_circle(size=65)

    base = alt.Chart(data).encode(x=alt.X("date:T",title='Month'))
    columns = sorted(data.variable.unique())
    tooltips = base.transform_pivot('variable', value='value', groupby=['date']).mark_rule().encode(
                    opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
                    tooltip=[alt.Tooltip(c, type='quantitative',format=',.0f',) for c in columns]+[alt.Tooltip("date:T", title="Month",format = ("%b %Y"),)],
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
        alt.Chart(data, title="Month on Month Percentage Increase in US COVID-19 Cases",height=400).mark_line().encode(
            x=alt.X("date:T",title='Month'),
            y=alt.Y('grwt_perc:Q',scale=alt.Scale(domain=[-100, 350]), title='Percentage (%)'),
            color=alt.value("#FF5733"),
        )
    )

    points = lines.transform_filter(hover).mark_circle(size=65)

    tooltips = (
        alt.Chart(data).mark_rule().encode(
            x=alt.X("date:T",title='Month'),
            y=alt.Y('grwt_perc:Q',scale=alt.Scale(domain=[-100, 350]), title='Percentage (%)'),
            opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
            tooltip=[
                alt.Tooltip("date:T", title="Month",format = ("%b %Y")),
                alt.Tooltip("grwt_perc:Q", title="Percentage",format=',.2f'),
                alt.Tooltip("conf_cases:Q", title="Positive Cases Count"),
                alt.Tooltip("prev_ccs:Q", title="Previous Cases Count"),
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
        alt.Chart(data, title="Visitor Changes For Each Place Category During COVID-19 Pandemic",height=400).mark_line().encode(
            x=alt.X("date:T",title='Month'),
            y=alt.Y('value:Q', title='Percentage % (Avg per Month)',scale=alt.Scale(domain=[-55, 40])),
            color="variable:N",
            strokeDash="variable:N",
        )
    )

    points = lines.transform_filter(hover).mark_circle(size=65)

    base = alt.Chart(data).encode(x=alt.X("date:T",title='Month'))
    columns = sorted(data.variable.unique())
    tooltips = base.transform_pivot('variable', value='value', groupby=['date']).mark_rule().encode(
                    opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
                    tooltip=[alt.Tooltip(c, type='quantitative',format=',.2f',) for c in columns]+[alt.Tooltip("date:T", title="Month",format = ("%b %Y"))],
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
        alt.Chart(data, title="US Unemployment Rate",height=360).mark_line().encode(
            x=alt.X("date:T",title='Bulan'),
            y=alt.Y('value:Q', title='Percentage % (Of All Labor Force)'),
            color=alt.value("#2CA02C"),
        )
    )

    points = lines.transform_filter(hover).mark_circle(size=65)

    tooltips = (
        alt.Chart(data).mark_rule().encode(
            x=alt.X("date:T",title='Month'),
            y=alt.Y('value:Q', title='Percentage % (Of All Labor Force)'),
            opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
            tooltip=[
                alt.Tooltip("date:T", title="Month",format = ("%b %Y")),
                alt.Tooltip("value:Q", title="Percentage",format=',.1f'),
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
        alt.Chart(data, title="Visitor Changes For Each Place Category During COVID-19 Pandemic (Daily)",height=400).mark_line().encode(
            x=alt.X("date:T",title='Date'),
            y=alt.Y('value:Q', title='Percentage (%)',scale=alt.Scale(domain=[-55, 40])),
            color="variable:N",
            strokeDash="variable:N",
        )
    )

    points = lines.transform_filter(hover).mark_circle(size=65)

    base = alt.Chart(data).encode(x=alt.X("date:T",title='Date'))
    columns = sorted(data.variable.unique())
    tooltips = base.transform_pivot('variable', value='value', groupby=['date']).mark_rule().encode(
                    opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
                    tooltip=[alt.Tooltip(c, type='quantitative',format=',.2f') for c in columns]+[alt.Tooltip("date:T", title="Date")],
                            ).add_selection(hover)
    return (lines + points + tooltips).interactive()