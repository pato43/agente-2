import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from streamlit_calendar import calendar
from datetime import datetime, timedelta
import time, random

st.set_page_config(page_title="💳 FinSecure Hub", layout="wide")

# ---------------- HEADER ----------------
st.markdown("""
# 💳 FinSecure Hub
Plataforma Integral de Fraudes y Clientes en banca y fintech mexicana.  
Incluye **detección de fraudes, análisis de clientes, dashboards, ML no-code, mapas, alertas y herramientas de oficina.**
""")

# ---------------- STACK TECNOLÓGICO ----------------
st.subheader("⚙️ Stack Tecnológico")

techs = [
    ("Gemma3","https://ai.google.dev/static/gemma/images/gemma3.png?hl=es-419"),
    ("Google Gemini","https://seeklogo.com/images/G/google-gemini-logo-CC90F10B3E-seeklogo.com.png"),
    ("LangChain","https://assets.streamlinehq.com/image/private/w_300,h_300,ar_1/f_auto/v1/icons/logos/langchain-ipuhh4qo1jz5ssl4x0g2a.png/langchain-dp1uxj2zn3752pntqnpfu2.png?_a=DATAg1AAZAA0"),
    ("OpenRouter","https://openrouter.ai/logo.png"),
    ("HuggingFace","https://huggingface.co/front/assets/huggingface_logo-noborder.svg"),
    ("TensorFlow","https://upload.wikimedia.org/wikipedia/commons/2/2d/Tensorflow_logo.svg"),
    ("PyTorch","https://upload.wikimedia.org/wikipedia/commons/9/96/PyTorch_logo_icon.svg"),
    ("Google Sheets","https://mailmeteor.com/logos/assets/PNG/Google_Sheets_Logo_512px.png"),
    ("Power BI","https://upload.wikimedia.org/wikipedia/commons/c/cf/New_Power_BI_Logo.svg"),
    ("SQL Server","https://cdn-icons-png.flaticon.com/512/5968/5968364.png"),
    ("PostgreSQL","https://upload.wikimedia.org/wikipedia/commons/a/ad/Logo_PostgreSQL.png"),
    ("BigQuery","https://upload.wikimedia.org/wikipedia/commons/4/4e/Google_BigQuery_Logo.png"),
    ("Azure Cloud","https://swimburger.net/media/ppnn3pcl/azure.png")
]

rows = [techs[i:i+5] for i in range(0,len(techs),5)]
for row in rows:
    cols = st.columns(len(row))
    for (name,url),col in zip(row,cols):
        with col:
            st.markdown(
                f"""
                <div style="border:1px solid #ddd; border-radius:12px; padding:10px; text-align:center; background-color:white;">
                    <img src="{url}" style="height:60px; object-fit:contain;"><br>
                    <small><b>{name}</b></small>
                </div>
                """,
                unsafe_allow_html=True
            )

st.write("---")

# ---------------- KPI DASHBOARD ----------------
st.subheader("📊 Dashboard General")
k1,k2,k3,k4 = st.columns(4)
k1.metric("Fraudes hoy", random.randint(10,30), delta="+3")
k2.metric("Monto recuperado", f"${random.randint(20000,100000)}")
k3.metric("Clientes en riesgo", random.randint(20,50), delta="-4")
k4.metric("Tiempo detección", f"{random.randint(2,9)} min")

data = pd.DataFrame({
    "Fecha": pd.date_range(datetime.today()-timedelta(days=30), periods=30),
    "Fraudes": np.random.randint(1,30,30),
    "Clientes activos": np.random.randint(500,800,30)
})
st.plotly_chart(px.line(data, x="Fecha", y=["Fraudes","Clientes activos"], title="Tendencia últimos 30 días"), use_container_width=True)

st.write("---")

# ---------------- DETECCIÓN FRAUDES ----------------
st.subheader("🔎 Detección de Fraudes en Tiempo Real")

colA,colB = st.columns(2)
with colA:
    if st.button("🚀 Consultar base de datos"):
        with st.spinner("Gemma3 analizando registros..."):
            time.sleep(2)
        df = pd.DataFrame({
            "Usuario":[f"U{1000+i}" for i in range(60)],
            "Monto": np.random.randint(100,10000,60),
            "Ciudad":np.random.choice(["CDMX","GDL","MTY","Cancún","Tijuana"],60),
            "Fraude sospechoso":np.random.choice([True,False],60,p=[0.3,0.7])
        })
        st.session_state["df_fraude"] = df
if "df_fraude" in st.session_state:
    st.dataframe(st.session_state["df_fraude"], use_container_width=True, hide_index=True)
    st.plotly_chart(
        px.histogram(st.session_state["df_fraude"], x="Ciudad", color="Fraude sospechoso", 
                     title="Distribución por ciudad"), 
        use_container_width=True
    )
else:
    st.info("Haz clic en **Consultar base de datos** para ver fraudes simulados.")

with colB:
    st.info("⚠️ Fraudes destacados")
    fraudes = pd.DataFrame({
        "Usuario":[f"U{2000+i}" for i in range(8)],
        "Monto": np.random.randint(5000,20000,8),
        "Ciudad":np.random.choice(["CDMX","MTY"],8)
    })
    st.dataframe(fraudes,use_container_width=True,hide_index=True)

st.write("---")

# ---------------- CLIENTES ----------------
st.subheader("🙋‍♂️ Clientes en Riesgo")
col1,col2=st.columns(2)
with col1:
    df_aband=pd.DataFrame({
        "Cliente":[f"C{i}" for i in range(1,41)],
        "Uso app móvil":np.random.choice(["Alto","Medio","Bajo"],40),
        "Prob. abandono":np.random.rand(40).round(2)
    })
    st.dataframe(df_aband,use_container_width=True,hide_index=True)
with col2:
    st.plotly_chart(px.box(df_aband,x="Uso app móvil",y="Prob. abandono",title="Prob. abandono por tipo de uso"),use_container_width=True)

st.write("---")

# ---------------- NOTICIAS SEGURIDAD ----------------
st.subheader("📰 Últimas noticias de seguridad")
news = [
    "Hackers intentan clonar tarjetas en cajeros de CDMX.",
    "Fraude por compras internacionales en aumento 20%.",
    "App móvil bancaria añade autenticación biométrica.",
    "Reportan phishing con links falsos de premios."
]
for n in news:
    st.warning("🔔 "+n)

st.write("---")

# ---------------- RANKING FRAUDES ----------------
st.subheader("🏦 Ranking de fraudes por banco")
ranking=pd.DataFrame({
    "Banco":["Banco Azteca","BBVA","Santander","Banorte","HSBC"],
    "Fraudes detectados":np.random.randint(50,200,5)
})
st.plotly_chart(px.bar(ranking,x="Banco",y="Fraudes detectados",color="Banco"),use_container_width=True)

st.write("---")

# ---------------- CALENDARIO Y NOTAS ----------------
st.subheader("🗓️ Herramientas de Oficina")
colN1,colN2=st.columns(2)
with colN1:
    events=[{"title":"Revisión diaria","start":datetime.now().strftime("%Y-%m-%d")},
            {"title":"Auditoría semanal","start":(datetime.now()+timedelta(days=3)).strftime("%Y-%m-%d")}]
    calendar(events=events,options={"editable":True,"selectable":True})
with colN2:
    nota=st.text_area("Notas rápidas",height=120)
    if st.button("Guardar nota"): st.success("Nota guardada con éxito")

st.write("---")

# ---------------- REPORTES ----------------
st.subheader("📑 Generador de reportes")
colR1,colR2=st.columns(2)
with colR1:
    st.selectbox("Formato",["PDF","Excel","CSV"])
    if st.button("Generar reporte"):
        with st.spinner("Generando..."):
            time.sleep(1.5)
        st.success("Reporte generado ✅")
with colR2:
    st.info("Los reportes incluyen fraudes detectados, clientes en riesgo y KPIs financieros.")
