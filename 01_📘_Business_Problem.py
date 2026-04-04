import streamlit as st
st.set_page_config(layout="wide")

st.markdown("""
<h1 style='text-align: center; color: #E2E8F0; font-weight: bold;'>
 Business Problem
</h1>""", unsafe_allow_html=True)

st.markdown("""
<div style="
    background-color: #1E293B;
    color: #E2E8F0;
    padding: 30px;
    border-radius: 12px;
    border-left: 6px solid #2a7de1;
    font-size: 20px;
    line-height: 1.8;
">

<p>
In the competitive world of digital retail, businesses invest heavily across multiple advertising channels
such as social media, search engines, and affiliate marketing to drive sales. However, many organizations
struggle to accurately measure the effectiveness of these campaigns and optimize their marketing spend.
</p>
            
<p>
While traditional approaches rely on isolated metrics like impressions or click-through rates, they fail to
capture the combined impact of key factors such as pricing, discount strategies, market reach, competition
intensity, and seasonal trends.
</p>

<p>
As a result, companies often face inefficient budget allocation, suboptimal campaign performance, and
missed revenue opportunities due to the lack of a holistic, data-driven forecasting approach.
</p>

</div>""", unsafe_allow_html=True)


st.markdown("""
<h1 style='text-align: center; color: #E2E8F0; font-weight: bold;'>
🌍 Background
</h1>""", unsafe_allow_html=True)

# Styled Card
st.markdown("""
<div style="
    background-color: #1E293B;
    padding: 30px;
    border-radius: 12px;
    border-left: 6px solid #2a7de1;
    font-size: 20px;
    line-height: 1.8;
    color: #E2E8F0;
">
            

<p style="text-align:center;">
Recent advancements in digital marketing have led businesses to invest heavily across multiple advertising
channels such as Social Media, Search Engines, and Affiliate platforms. However, despite the availability of
large volumes of campaign data, many organizations still struggle to fully understand the true impact of
their marketing efforts on revenue generation.
</p>
            
<br>
<p style="text-align:center;"><b>Current marketing strategies often:</b></p>

<ul style="list-style-type: none; padding-left: 0; text-align:center;">
    <li>📊 Focus heavily on isolated metrics like impressions and click-through rates</li>
    <li>⚠️ Fail to capture the combined influence of pricing, discounts, and customer behavior</li>
    <li>❌ Overlook external factors such as competition and seasonality</li>
</ul>

<br>
</div>""", unsafe_allow_html=True)

st.markdown("""
<h1 style='text-align: center; color: #E2E8F0; font-weight: bold;'>
Constraints & Considerations
</h1>""", unsafe_allow_html=True)

st.markdown("""
<div style="
    background-color: #1E293B;
    padding: 30px;
    border-radius: 12px;
    border-left: 6px solid #2a7de1;
    font-size: 20px;
    line-height: 1.8;
    color: #E2E8F0;
">

<ul style="list-style-type: none; padding-left: 0;">

<li><b>Data Quality : </b>Some campaign data may contain missing values or inconsistencies, which can impact model accuracy and insights.</li>
<li><b>Regional Variability : </b>Customer behavior, purchasing power, and marketing effectiveness can vary significantly across different regions.</li>
<li><b>Dynamic Market Conditions : </b>External factors like competition, seasonality, and economic trends can change over time, making predictions less stable.</li>
<li><b>Model Deployment Efficiency : </b>The predictive model should be optimized for performance and scalability to enable real-time or near real-time decision-making.(e.g., Hugging Face Spaces)</li>

</ul>
</div>""", unsafe_allow_html=True)