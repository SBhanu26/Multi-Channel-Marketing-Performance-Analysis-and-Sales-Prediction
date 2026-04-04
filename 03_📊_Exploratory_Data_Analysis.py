import streamlit as st
import polars  as pl
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import polars.selectors as cs
import numpy as np
st.set_page_config(layout="wide")

df = pl.read_csv(r"C:\Users\bhanu\OneDrive\Desktop\Case Study\data\Data_set.csv")

def fun1(df):
    # Styled container
    st.markdown("""
    <style>
    .card {
        background-color: #1E293B;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #f3d9a4;
    }
    </style>
    """, unsafe_allow_html=True)

    # Expander (collapsible section)
    with st.expander("📁 Dataset Overview", expanded=True):

        #Shape
        st.markdown(
            f"<h4 style='text-align:center;'>Shape: {df.shape}</h4>",
            unsafe_allow_html=True
        )
        # st.write(f"{df.shape}")

        # Table preview
        # st.dataframe(df.head(), use_container_width=True)
        st.write(df)
fun1(df)

def fun2():
    with st.expander("📚 Columns Description", expanded=True):
        st.markdown("""
        <ul>
            <li><b>id :</b>Unique identifier for each record (campaign entry)</li>
            <li><b>date :</b>Date when the campaign data was recorded</li>
            <li><b>region :</b>Geographic region where the campaign was run</li>
            <li><b>channel :</b>Type of advertising platform used (Social Media, Search, Affiliate).</li>
            <li><b>product_type :</b>indicates the category of product being advertised or sold in the campaign.</li>
            <li><b>customer_segment :</b>Category of customers targeted (e.g., High Value, Budget, New Customers).</li>
            <li><b>ad_spend :</b>Amount of money spent on the campaign.</li>
            <li><b>price :</b>Selling price of the product during the campaign.</li>
            <li><b>discount_rate :</b>Percentage discount applied to the product.</li>
            <li><b>market_reach :</b>Estimated number of people who could potentially see the ad.</li>
            <li><b>impressions :</b>Total number of times the ad was displayed.</li>
            <li><b>click_through_rate :</b>Percentage of users who clicked the ad after seeing it.</li>
            <li><b>competition_index :</b>Indicates how competitive the market is (higher = more competition).</li>
            <li><b>seasonality_index :</b>Represents seasonal effects (e.g., holidays, peak shopping periods).</li>
            <li><b>campaign_duration_days :</b>Number of days the campaign ran.</li>
            <li><b>customer_lifetime_value :</b>Estimated total revenue a customer generates over their lifetime.</li>
            <li><b>sales_revenue :</b>Total revenue generated from the campaign.</li>        
        </ul>
        """, unsafe_allow_html=True)
fun2()

def fun3():
    with st.expander("ℹ️ Dataset info", expanded=True):

        #Shape
        st.markdown(
            f"<h4 style='text-align:center;'>Shape: {df.shape}</h4>",
            unsafe_allow_html=True
        )

        def polars_info(df):
            Col_name=[]
            Data_type=[]
            Null_Values_Count=[]
            Null_Values_Percentage=[]
        
            for col, dtype in zip(df.columns, df.dtypes):
                Col_name.append(col)
                Data_type.append(dtype)
                Null_Values_Count.append(df[col].null_count())
                Null_Values_Percentage.append((f"{df[col].is_null().mean()*100:.2f} %"))

            info=pl.DataFrame({
                "Col names" : Col_name,
                "Data types" : Data_type,
                "Null Values Count":Null_Values_Count,
                "Null Values Percentage":Null_Values_Percentage
            })

            return info
        st.write(polars_info(df))
fun3()


def fun5():
    with st.expander("🔢 Numerical Columns", expanded=True):
        st.write(pl.Series(df.select(cs.numeric()).columns))

    with st.expander("🏷️ Categorical Columns", expanded=True):
        st.write(pl.Series(df.select(~cs.numeric()).columns))
fun5()


with st.expander("📊 Univariate Analysis", expanded=True):
    with st.expander("🔢 Numerical Columns", expanded=True):
        df = pl.read_csv(r"data\Cleaned_Data_set2.csv")
        numeric_cols = ["price","discount_rate","market_reach","campaign_duration_days"]

        column = st.selectbox(
            "Select column for univariate analysis",
            numeric_cols
        )

        plot_type = st.radio(
            "Plot Type",
            ["Histogram", "Boxplot", "KDE"]
        )

        bins = None
        if plot_type == "Histogram":
            bins = st.slider("Number of bins", 5, 1000, 30)

        fig, ax = plt.subplots(figsize=(6,4)) 

        if plot_type == "Histogram":
            if column=="price":
                sns.histplot(df[column], bins=bins, kde=False, ax=ax)
                ax.set_title("Price Distribution")
                st.pyplot(fig)
                if st.button("Show insight"):
                        st.markdown("""
                        <ul>
                            <li>Most products are priced between $10–$50</li>
                            <li>Only few expensive products above are $200</li>
                            <li>Prices above 500 appear rarely</li>
                        </ul>""", unsafe_allow_html=True)

            elif column=="discount_rate":
                sns.histplot(df[column], bins=bins, kde=False, ax=ax)
                ax.set_title("discount_rate Distribution")
                st.pyplot(fig)
                if st.button("Show insight"):
                        st.markdown("""
                        <ul>
                            <li>Most discount values are small to moderate, Few campaigns offer very high discounts</li>
                            <li>Some products are sold with minimal or no discount, These may be high-demand or premium items</li>
                            <li>The business uses multiple discount strategies depending on the campaign or product category.</li>
                        </ul>""", unsafe_allow_html=True)

            elif column=="market_reach":
                sns.histplot(df[column], bins=bins, kde=False, ax=ax)
                ax.set_title("market_reach Distribution")
                st.pyplot(fig)
                if st.button("Show insight"):
                        st.markdown("""
                        <ul>
                            <li>Only Few campaigns reach wider audiences</li>
                            <li>Most campaigns reach between 100 and 400 users</li>
                            <li>The right-skewed distribution highlights that large audience reach is extremely rare.</li>
                        </ul>""", unsafe_allow_html=True)

            elif column=="campaign_duration_days":
                sns.histplot(df[column], bins=bins, kde=False, ax=ax)
                ax.set_xticks(np.arange(0, 100, 5))
                ax.set_title("campaign_duration_days")
                st.pyplot(fig)
                if st.button("Show insight"):
                        st.markdown("""
                        <ul>
                            <li>Campaign durations follow predefined intervals such as 7, 14, 21, 30, 60, and 90 days, indicating that marketing campaigns are scheduled</li>
                            <li>Campaign durations are fixed values, not continuous numbers.</li>
                            <li>60-day campaigns are the most common marketing strategy.</li>
                            <li>Smaller spikes appear at 7 – 14 days may be indicates flash sales and limited-time offers</li>
                        </ul>""", unsafe_allow_html=True)

        elif plot_type == "Boxplot":
            if column=="price":
                sns.boxplot(x=df[column], ax=ax)
                ax.set_title("Boxplot")
                st.pyplot(fig)
                if st.button("Show insight"):
                        st.markdown("""
                        <ul>
                            <li>Most of the data is compressed near the lower price range</li>
                            <li>The vertical line inside the box represents the median price. At least 50% of products are low-priced.</li>
                            <li>There are numerous high-price outliers.</li>
                        </ul>""", unsafe_allow_html=True)

            elif column=="discount_rate":
                sns.boxplot(x=df[column], ax=ax)
                ax.set_title("Boxplot")
                st.pyplot(fig)
                if st.button("Show insight"):
                        st.markdown("""
                        <ul>
                            <li>The discount_rate distribution shows that most campaigns offer discounts between 12% and 32%</li>
                            <li>There are no potential ouliers.</li>
                        </ul>""", unsafe_allow_html=True)

            elif column=="market_reach":
                sns.boxplot(x=df[column], ax=ax)
                ax.set_title("Boxplot")
                st.pyplot(fig)
                if st.button("Show insight"):
                        st.markdown("""
                        <ul>
                            <li>Most campaigns reach between 30 and 850 audience</li>
                            <li>Half of the campaigns reach fewer than ~270 users.Half reach more than ~270 users.</li>
                            <li>Some campaigns achieve extremely large reach.</li>
                            <li>There are potential ouliers ranging from (~850 to ~1500)</li>
                        </ul>""", unsafe_allow_html=True)

            elif column=="campaign_duration_days":
                sns.boxplot(x=df[column], ax=ax)
                ax.set_title("Boxplot")
                ax.set_xticks(np.arange(0, 100, 5))
                st.pyplot(fig)
                if st.button("Show insight"):
                        st.markdown("""
                        <ul>
                            <li>Campaigns typically run between 1 week and 3 months.</li>
                            <li>50% of campaigns last less than 30 days</li>
                            <li>boxplot does not show any outliers</li>
                        </ul>""", unsafe_allow_html=True)

        elif plot_type == "KDE":
            if column=="price":
                sns.kdeplot(df[column], fill=True, ax=ax)
                ax.set_title("Kde plot")
                st.pyplot(fig)
            elif column=="discount_rate":
                sns.kdeplot(df[column], fill=True, ax=ax)
                ax.set_title("Kde plot")
                st.pyplot(fig)
            elif column=="market_reach":
                sns.kdeplot(df[column], fill=True, ax=ax)
                ax.set_title("Kde plot")
                st.pyplot(fig)
            elif column=="campaign_duration_days":
                sns.kdeplot(df[column], fill=True, ax=ax)
                ax.set_title("Kde plot")
                st.pyplot(fig)
            
    with st.expander("🏷️ Categorical Columns", expanded=True):

        df = pl.read_csv(r"data\Cleaned_Data_set2.csv")
        categorical_cols=df.select(~cs.numeric()).columns

        column = st.selectbox(
            "Select column for univariate analysis",
            categorical_cols)
         
        plot_type = st.radio(
            "Plot Type",
            ["Count Plot", "Pie Chart","Donut Chart"]
        )

        fig, ax = plt.subplots(figsize=(6,4))
        if plot_type == "Count Plot":
            if column=="region":
                sns.countplot(data=df, x=column)
                st.pyplot(fig)
                if st.button("Show_insight"):
                        st.markdown("""
                        <ul>
                            <li>The North region has an extremely large number of campaigns compared to all other regions.</li>
                            <li>Regions like Central, West, and South have very few campaigns.</li>
                            <li>The dataset is highly imbalanced in terms of regional distribution.</li>
                        </ul>""", unsafe_allow_html=True)

            elif column=="channel":
                sns.countplot(data=df, x=column)
                st.pyplot(fig)
                if st.button("Show_insight"):
                        st.markdown("""
                        <ul>
                            <li>Social Media Is the Most Used Marketing Channel</li>
                            <li>Email and Search campaigns are also widely used.</li>
                            <li>TV and Influencer marketing have the lowest campaign counts.</li>
                            <li>Overall, the retailer relies heavily on digital marketing channels.</li>
                        </ul>""", unsafe_allow_html=True)

            elif column=="product_category":
                sns.countplot(data=df, x=column)
                st.pyplot(fig)
                if st.button("Show_insight"):
                        st.markdown("""
                        <ul>
                            <li>The General product category has the highest number of campaigns.</li>
                            <li>Stationery and Kitchen categories have fewer campaigns.</li>
                            <li>Lighting products have the lowest representation in the dataset.</li>
                        </ul>""", unsafe_allow_html=True)

            elif column=="customer_segment":

                sns.countplot(data=df, x=column)
                st.pyplot(fig)
                if st.button("Show_insight"):
                        st.markdown("""
                        <ul>
                            <li>Premium customers represent the largest segment in the dataset.</li>
                            <li>Standard customers form the second largest group.</li>
                            <li>Marketing campaigns appear to focus primarily on Premium customers.</li>
                        </ul>""", unsafe_allow_html=True)

        elif plot_type == "Pie Chart":
            if column=="region":
                count=df[column].value_counts()
                explode = [0.5, 0.5, 0.5,0.5,0.5]
                plt.pie(count["count"],labels=count[column],autopct="%1.2f%%",explode=explode)
                plt.title("Pie Chart")
                plt.xlabel(column)
                st.pyplot(fig)
                if st.button("Show_insight"):
                        st.markdown("""
                        <ul>
                            <li>The North region dominates the dataset with about 96.7% of campaigns.</li>
                            <li>Other regions such as East, Central, West, and South contribute very small proportions.</li>
                            <li>Marketing efforts appear to be heavily concentrated in the North region.</li>
                        </ul>""", unsafe_allow_html=True)

            elif column=="channel":
                count=df[column].value_counts()
                fig, ax = plt.subplots(figsize=(5,3))
                plt.pie(count["count"],labels=count[column],autopct="%1.2f%%")
                plt.title("Pie Chart")
                plt.xlabel(column)
                st.pyplot(fig, use_container_width=False)
                if st.button("Show_insight"):
                        st.markdown("""
                        <ul>
                            <li>Social Media is the most used marketing channel (~25% of campaigns).</li>
                            <li>Email and Search channels each contribute about 20% of campaigns.</li>
                            <li>Overall, the retailer relies heavily on digital marketing channels.</li>
                        </ul>""", unsafe_allow_html=True)

            elif column=="product_category":
                count=df[column].value_counts()
                fig, ax = plt.subplots(figsize=(5,3))
                plt.pie(count["count"],labels=count[column],autopct="%1.2f%%",radius=0.8)
                plt.title("Pie Chart")
                plt.xlabel(column)
                st.pyplot(fig, use_container_width=False)
                if st.button("Show_insight"):
                        st.markdown("""
                        <ul>
                            <li>General products dominate the campaigns (~50%).</li>
                            <li>Storage products represent the second largest share (~21%).</li>
                            <li>Lighting products have the lowest representation in the dataset.</li>
                        </ul>""", unsafe_allow_html=True)

            elif column=="customer_segment":
                count=df[column].value_counts()
                fig, ax = plt.subplots(figsize=(5,3))
                plt.pie(count["count"],labels=count[column],autopct="%1.2f%%",radius=0.8)
                plt.title("Pie Chart")
                plt.xlabel(column)
                st.pyplot(fig, use_container_width=False)
                if st.button("Show_insight"):
                        st.markdown("""
                        <ul>
                            <li>Premium customers dominate the dataset (~80% of campaigns).</li>
                            <li>Standard customers account for about 15% of campaigns.</li>
                            <li>Marketing efforts appear to focus heavily on high-value (Premium) customers.</li>
                        </ul>""", unsafe_allow_html=True)
                    
        elif plot_type == "Donut Chart":
            if column=="region":
                count=df[column].value_counts()
                plt.pie(count["count"],labels=count[column],autopct="%1.2f%%",wedgeprops={"width": 0.7})
                plt.title("Donut Chart")
                plt.xlabel(column)
                st.pyplot(fig)
                if st.button("Show_insight"):
                        st.markdown("""
                        <ul>
                            <li>The North region dominates the dataset with about 96.7% of campaigns.</li>
                            <li>Other regions such as East, Central, West, and South contribute very small proportions.</li>
                            <li>Marketing efforts appear to be heavily concentrated in the North region.</li>
                        </ul>""", unsafe_allow_html=True)

            elif column=="channel":
                count=df[column].value_counts()
                fig, ax = plt.subplots(figsize=(5,3))
                plt.pie(count["count"],labels=count[column],autopct="%1.2f%%",wedgeprops={"width": 0.7})
                plt.title("Donut Chart")
                plt.xlabel(column)
                st.pyplot(fig, use_container_width=False)
                if st.button("Show_insight"):
                        st.markdown("""
                        <ul>
                            <li>Social Media is the most used marketing channel (~25% of campaigns).</li>
                            <li>Email and Search channels each contribute about 20% of campaigns.</li>
                            <li>Overall, the retailer relies heavily on digital marketing channels.</li>
                        </ul>""", unsafe_allow_html=True)

            elif column=="product_category":
                count=df[column].value_counts()
                fig, ax = plt.subplots(figsize=(5,3))
                plt.pie(count["count"],labels=count[column],autopct="%1.2f%%",wedgeprops={"width": 0.7})
                plt.title("Donut Chart")
                plt.xlabel(column)
                st.pyplot(fig, use_container_width=False)
                if st.button("Show_insight"):
                        st.markdown("""
                        <ul>
                            <li>General products dominate the campaigns (~50%).</li>
                            <li>Storage products represent the second largest share (~21%).</li>
                            <li>Lighting products have the lowest representation in the dataset.</li>
                        </ul>""", unsafe_allow_html=True)

            elif column=="customer_segment":
                count=df[column].value_counts()
                fig, ax = plt.subplots(figsize=(5,3))
                plt.pie(count["count"],labels=count[column],autopct="%1.2f%%",wedgeprops={"width": 0.7})
                plt.title("Donut Chart")
                plt.xlabel(column)
                st.pyplot(fig, use_container_width=False)
                if st.button("Show_insight"):
                        st.markdown("""
                        <ul>
                            <li>Premium customers dominate the dataset (~80% of campaigns).</li>
                            <li>Standard customers account for about 15% of campaigns.</li>
                            <li>Marketing efforts appear to focus heavily on high-value (Premium) customers.</li>
                        </ul>""", unsafe_allow_html=True)

with st.expander("📊 Bivariate Analysis", expanded=True):
    with st.expander("Numerical vs Numerical", expanded=True):
        df = pl.read_csv(r"data\Cleaned_Data_set5.csv")
        x_numeric_cols = ["ad_spend","discount_rate","price",]
        y_numeric_cols = ["sales_revenue"]

        x = st.selectbox(
            "X_axis",
            x_numeric_cols
        )
        y = st.selectbox(
            "Y_axis",
            y_numeric_cols
        )

        if x=="ad_spend":
            fig, ax = plt.subplots(figsize=(5,3))
            sns.regplot(data=df, x="ad_spend", y="sales_revenue")
            plt.xlabel("Ad Spend")
            plt.ylabel("Sales Revenue")
            plt.title("Ad Spend vs Sales Revenue")
            plt.show()
            st.pyplot(fig, use_container_width=False)
            if st.button("Show_Insight"):
                    st.markdown("""
                    <ul>
                        <li>Ad spend shows a weak positive relationship with sales revenue.</li>
                        <li>Higher ad spend does not mean higher revenue.</li>
                        <li>Many campaigns operate with very low advertising budgets.</li>
                    </ul>""", unsafe_allow_html=True)

        if x=="discount_rate":
            fig, ax = plt.subplots(figsize=(5,3))
            sns.scatterplot(data=df, x="discount_rate", y="sales_revenue")
            plt.xlabel("Discount_rate")
            plt.ylabel("Sales Revenue")
            plt.title("Discount_rate vs Sales Revenue")
            plt.show()
            st.pyplot(fig, use_container_width=False)
            if st.button("Show_Insight"):
                    st.markdown("""
                    <ul>
                        <li>There is no strong linear relationship between discount rate and sales revenue.</li>
                        <li>Sales revenue remains relatively consistent across different discount levels.</li>
                        <li>Higher discounts do not mean higher revenue.</li>
                    </ul>""", unsafe_allow_html=True)

        if x=="price":
            fig, ax = plt.subplots(figsize=(5,3))
            sns.scatterplot(data=df, x="price", y="sales_revenue")
            plt.xlabel("Price")
            plt.ylabel("Sales Revenue")
            plt.title("Price vs Sales Revenue")
            plt.show()
            st.pyplot(fig, use_container_width=False)
            if st.button("Show_Insight"):
                    st.markdown("""
                    <ul>
                        <li>There is no strong linear relationship between price and sales revenue.</li>
                        <li>Higher revenue values mostly appear at lower price levels.</li>
                    </ul>""", unsafe_allow_html=True)

    with st.expander("Categorical vs Numerical", expanded=True):
        df = pl.read_csv(r"data\Cleaned_Data_set5.csv")
        x_numeric_cols = df.select(~cs.numeric()).columns
        y_numeric_cols = ["sales_revenue"]

        x = st.selectbox(
            "x_axis",
            x_numeric_cols
        )
        y = st.selectbox(
            "y_axis",
            y_numeric_cols
        )

        if x=="channel":
            fig, ax = plt.subplots(figsize=(5,3))
            sns.barplot(data=df, x="channel", y="sales_revenue")
            plt.title("Sales Revenue by Marketing Channel")
            plt.xlabel("Channel")
            plt.ylabel("Sales Revenue")
            plt.tight_layout()
            plt.xticks(rotation=45)
            plt.show()
            st.pyplot(fig, use_container_width=False)
            if st.button("Insights"):
                    st.markdown("""
                    <ul>
                        <li>Influencer campaigns generate the highest average sales revenue.</li>
                        <li>Social Media and Search channels perform strongly in terms of revenue.</li>
                        <li>TV advertising generates the lowest average sales revenue.</li>
                    </ul>""", unsafe_allow_html=True)

        if x=="region":
            fig, ax = plt.subplots(figsize=(5,3))
            plt.barh(df["region"],df["sales_revenue"])
            plt.title("Sales Revenue by Region")
            plt.ylabel("Region")
            plt.xlabel("Sales Revenue")
            plt.tight_layout()
            plt.xticks(rotation=45)
            plt.show()
            st.pyplot(fig, use_container_width=False)
            if st.button("Insights"):
                    st.markdown("""
                    <ul>
                        <li>North region generates the highest sales revenue.</li>
                        <li>East region is the second strongest market.</li>
                        <li>Campaign performance varies significantly across regions.</li>
                    </ul>""", unsafe_allow_html=True)

        if x=="customer_segment":
            fig, ax = plt.subplots(figsize=(5,3))
            sns.barplot(data=df, x="region", y="sales_revenue",hue="customer_segment")
            plt.title("Sales Revenue by Region")
            plt.xlabel("Region")
            plt.ylabel("Sales Revenue")
            plt.tight_layout()
            plt.legend(loc='upper right')
            plt.xticks(rotation=45)
            plt.show()
            st.pyplot(fig, use_container_width=False)
            if st.button("Insights"):
                    st.markdown("""
                    <ul>
                        <li>Premium customers generate the highest sales revenue across most regions.</li>
                        <li>Budget customers consistently show the lowest revenue levels.</li>
                        <li>Sales performance varies across regions and customer segments.</li>
                    </ul>""", unsafe_allow_html=True)

    with st.expander("Categorical vs Categorical", expanded=True):
        df = pl.read_csv(r"data\Cleaned_Data_set5.csv")
        List = ["Region vs Channel","channel vs Product Category"]

        x = st.selectbox(
            "Select the one combination for analysis",
            List
        )

        if x=="Region vs Channel":
            fig, ax = plt.subplots(figsize=(5,3))
            sns.countplot(data=df, x="region", hue="channel")
            plt.title("Marketing Channels Across Regions")
            plt.tight_layout()
            plt.show()
            st.pyplot(fig, use_container_width=False)
            if st.button("Show Insights"):
                    st.markdown("""
                    <ul>
                        <li>Most marketing campaigns are concentrated in the North region.</li>
                        <li>Social Media is the most used marketing channel in the North.</li>
                        <li>Other regions have significantly fewer campaigns.</li>
                    </ul>""", unsafe_allow_html=True)

        if x=="channel vs Product Category":
            fig, ax = plt.subplots(figsize=(5,3))
            ct = pd.crosstab(df["channel"],df["product_category"])
            sns.heatmap(ct, annot=True, cmap="Blues",fmt=".0f")
            plt.title("product_category vs Channel Frequency")
            plt.tight_layout()
            plt.show()
            st.pyplot(fig, use_container_width=False)
            if st.button("Show Insights"):
                    st.markdown("""
                    <ul>
                        <li>General products dominate campaigns across all marketing channels.</li>
                        <li>Social Media is the most frequently used marketing channel.</li>
                        <li>Digital channels dominate the overall marketing strategy.</li>
                    </ul>""", unsafe_allow_html=True)

with st.expander("Multivarite Analysis", expanded=True):
        df = pl.read_csv(r"data\Cleaned_Data_set5.csv")
        List = ["Ad Spend vs Channel vs Sales Revenue","Price vs Discount Rate vs Sales Revenue","Region vs Channel vs Sales Revenue"]

        x = st.selectbox(
            "Select the one combination for analysis",
            List
        )

        if x=="Ad Spend vs Channel vs Sales Revenue":
            fig, ax = plt.subplots(figsize=(5,3))
            sns.scatterplot(
            data=df,
            x="ad_spend",
            y="sales_revenue",
            hue="channel")
            plt.tight_layout()
            plt.show()
            st.pyplot(fig, use_container_width=False)
            if st.button("Show_Insights"):
                    st.markdown("""
                    <ul>
                        <li>Ad spend shows a weak relationship with sales revenue across channels.</li>
                        <li>Revenue values are similar across different marketing channels.</li>
                    </ul>""", unsafe_allow_html=True)

        if x=="Price vs Discount Rate vs Sales Revenue":
            fig, ax = plt.subplots(figsize=(5,3))
            sns.scatterplot(
            data=df,
            x="price",
            y="sales_revenue",
            hue="discount_rate")
            plt.tight_layout()
            plt.show()
            st.pyplot(fig, use_container_width=False)
            if st.button("Show_Insights"):
                    st.markdown("""
                    <ul>
                        <li>Highest sales revenue occurs mostly at lower price levels.</li>
                        <li>Discount rate does not show a strong relationship with revenue.</li>
                    </ul>""", unsafe_allow_html=True)

        if x=="Region vs Channel vs Sales Revenue":
            fig, ax = plt.subplots(figsize=(5,3))
            sns.barplot(
            data=df,
            x="region",
            y="sales_revenue",
            hue="channel")
            plt.legend(loc='upper right')
            plt.tight_layout()
            plt.show()
            st.pyplot(fig, use_container_width=False)
            if st.button("Show_Insights"):
                    st.markdown("""
                    <ul>
                        <li>Influencer marketing generates high revenue across most regions.</li>
                        <li>Social Media and Search channels show strong and consistent performance.</li>
                        <li>Central region shows comparatively lower revenue levels.</li>
                    </ul>""", unsafe_allow_html=True)