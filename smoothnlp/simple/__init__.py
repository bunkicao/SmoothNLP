import smoothnlp
from smoothnlp.jvm import LazyLoadingJClass,SafeJClass
ner = LazyLoadingJClass("com.smoothnlp.nlp.simple.NormalizedNER")
sentiment = LazyLoadingJClass("com.smoothnlp.nlp.simple.SentimentAnalyzer")
DocumentAnalyzer = LazyLoadingJClass("com.smoothnlp.nlp.simple.DocumentAnalyzer")