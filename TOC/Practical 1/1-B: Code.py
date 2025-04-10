Q. generate tokens and visualize using word cloud

print("Name:Sufyan Ansari Roll no:5008")
from wordcloud import WordCloud
import matplotlib.pyplot as plt
text="I am a student of Maharashtra College of Arts Science and Commerce in Computer Science department"
wordcloud=WordCloud().generate(text)
plt.figure(figsize=(12,12))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
