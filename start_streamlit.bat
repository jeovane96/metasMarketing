@echo off
cd /d E:\BI\Python\Sindata
streamlit run Sindata.py --server.port 8501 --server.headless true --server.address=0.0.0.0
pause