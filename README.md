# Youtube_Treading_Analysis

## Final Report
Report is in Trending_Youtube_Video_Analysis.ipynb.

## Key findings:
1. The U.S. and the U.K. lead in YouTube video views among top-trending videos.
2. Content preferences vary by country: music videos dominate in the U.S. and U.K., while entertainment videos are most popular in Canada, India, and Germany.
3. The repeated spikes in these categories suggest possible cyclic trends in content consumption
4. Most countries gain the majority of their views within the first 5 days of posting, but in the U.S. and U.K., videos continue to attract views for up to 20 days.
5. In countries like Canada, France, Germany, the U.K., and the U.S., videos posted on Fridays receive the highest views. In India, Wednesday posts generate the most views, likes, and comments.
6. Videos with titles between 30 and 70 characters tend to receive higher total views.

## Motivation
As YouTube users, particularly as we consider potentially entering this industry in the future (which we are contemplating), our team is highly interested in relevant information. Our curiosity drives us to explore a series of practical and meaningful questions. For example, what are the differences in content preferences among viewers from different countries or regions? How do these differences influence the creation and dissemination of content? Additionally, we are eager to understand which areas currently host popular topics and how the popularity of these fields changes over time. For instance, some regions may lean more toward entertainment content, while others may show a greater interest in educational videos, affecting how content creators position themselves and develop strategies.

Another thought-provoking question is the impact of content titles on video view counts. We want to investigate how different title choices may influence viewer attraction in similar fields. Does a creative and compelling title really lead to a significant increase in click-through rates? These inquiries stem not only from our curiosity but also reflect a desire to understand the deeper dynamics behind content creation and consumption. Through an in-depth analysis of the YouTube dataset, we hope to unveil these trends, which could assist content creators in more effectively targeting their audiences and optimizing their content strategies.

In summary, the significance of this project lies in its ability to provide users, content creators, and platforms with valuable business insights drawn from the data, shedding light on the current YouTube ecosystem. These insights may influence future strategic iterations on the platform, helping content creators discover trending topics more efficiently and capture a larger audience and traffic. We might also visualize geographic trends and topic trends on YouTube, revealing which regions show particular interest in specific types of content. Overall, we are very much looking forward to this data exploration journey.

## Questions
What are the key factors contributing to the success of top Youtube Channels (subscriber growth) and differentiate them from others?
Value proposition: This question will help content creators in Youtube to figure out which factors, such as number of uploads, channel type and category that will play an important role in booting subscription. Therefore, for those content creators who seek subscription growth, they can reference these factors to make content. Plan to address the question: Plan to use a machine learning model, such as linear regression, to predict subscriber growth. Inputs would include features such as video views, uploads, and channel category. We may also use feature importance analysis to highlight the factors most closely linked to success (i.e. subscriber)..

How are successful YouTube channels distributed globally, and what regional socio-economic factors (e.g., urban population, unemployment rate, and gross tertiary education enrollment) are most closely correlated with their success?
Value proposition: This analysis will uncover the similarities and differences among content creators across different regions, enabling YouTube and marketers to better target their audiences. By understanding regional trends, platforms can optimize user engagement, and advertisers can create more tailored and effective campaigns. Plan to address the question: Implement clustering algorithms (e.g. K-means) to group regions with similar characteristics and channel success metrics. Then we will identify patterns in regional clusters that could inform targeted marketing strategies.

How do earnings correlate with channel’s performance metrics, such as subscribers and video views?
Value proposition: Analyzing the relationship between earnings and channel’s performance can provide insights into monetization strategies for creators. It can help identify whether higher views or subscribers directly lead to increased earnings. If so, they can use the answer from the first question to see how they can improve their content to get more subscribers or views and then earn more. Plan to address the question: First, we will perform a correlation analysis to quantify the relationships between estimated earnings, subscribers, and video views. Next, we will develop a regression model to assess how effectively subscribers and video views can predict earnings. Finally, we will visualize the results using scatter plots to illustrate these relationships and interpret the findings.

## Data
Data Source URL: https://www.kaggle.com/datasets/datasnaek/youtube-new/data

The data is organized in a single table, consisting of 27 columns and 995 rows. Each column represents a distinct variable, providing valuable information about the content and its performance metrics. The rows correspond to individual data entries, capturing a variety of aspects related to the videos being analyzed.

While the data is generally well-structured, it may require some cleaning and preprocessing before it can be fully utilized for analysis. Potential issues include handling missing values, which might skew results if not addressed. Additionally, standardizing formats—such as date formats—to ensure consistency is crucial for time-series analysis. It’s also important to verify that categorical variables are consistent, as discrepancies in labeling can lead to inaccuracies in insights.

Regarding existing uses, this type of dataset has been leveraged in a multitude of academic research projects, marketing analyses, and trend evaluations. It has proven to be pertinent across various fields related to digital marketing and content creation, providing insights that inform strategies for content optimization, audience engagement, and platform growth. This demonstrates the dataset's relevance and potential for generating actionable insights in both academic and practical contexts.

