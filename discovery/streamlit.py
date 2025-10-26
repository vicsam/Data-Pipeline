# discovery/streamlit_app.py
import streamlit as st
import json
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

st.title("Data Discovery Engine")
query = st.text_input("Search for content (e.g., AI ethics)")

if st.button("Discover"):
    with st.spinner("Searching..."):
        urls = [f"https://example.com/article-{i}" for i in range(1, 6)]
        for i, url in enumerate(urls, 1):
            meta = {
                "url": url,
                "title": f"Article {i}",
                "source": "web",
                "sector": "tech",
                "timestamp": "2025-04-05T12:00:00Z"
            }
            producer.send('discovery-queue', meta)
        st.success(f"Sent {len(urls)} URLs to Kafka!")