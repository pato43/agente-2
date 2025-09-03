import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from streamlit_calendar import calendar
from datetime import datetime, timedelta
import time, random

st.set_page_config(page_title="FinSecure Hub", layout="wide")

# ---------------- HEADER ----------------
st.title("💳 FinSecure Hub — Plataforma Integral de Fraudes y Clientes")
st.markdown("""
**FinSecure Hub** es una demo integral para **banca y fintech en México**.  
Ofrece **detección de fraudes, análisis de clientes, ML no-code, dashboards, mapas, reportes e integraciones externas**.  
""")

# ---------------- STACK TECNOLÓGICO ----------------
st.markdown("### ⚙️ Stack Tecnológico")

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

cols = st.columns(len(techs))
for (name,url),col in zip(techs,cols):
    col.image(url,caption=name,use_container_width=True)

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
st.plotly_chart(px.line(data, x="Fecha", y=["Fraudes","Clientes activos"], title="Tendencia 30 días"), use_container_width=True)

st.write("---")

# ---------------- DETECCIÓN FRAUDES ----------------
st.subheader("🔎 Detección de Fraudes en Tiempo Real")
colA,colB = st.columns(2)
with colA:
    if st.button("Consultar base de datos"):
        with st.spinner("Gemma3 analizando registros..."):
            time.sleep(2)
        df = pd.DataFrame({
            "Usuario":[f"U{1000+i}" for i in range(60)],
            "Monto": np.random.randint(100,10000,60),
            "Ciudad":np.random.choice(["CDMX","GDL","MTY","Cancún","Tijuana"],60),
            "Fraude sospechoso":np.random.choice([True,False],60,p=[0.3,0.7])
        })
        st.dataframe(df, use_container_width=True, hide_index=True)
with colB:
    st.info("⚠️ Fraudes resaltados")
    fraudes = pd.DataFrame({
        "Usuario":[f"U{2000+i}" for i in range(8)],
        "Monto": np.random.randint(5000,20000,8),
        "Ciudad":np.random.choice(["CDMX","MTY"],8)
    })
    st.dataframe(fraudes,use_container_width=True,hide_index=True)

st.plotly_chart(px.histogram(df, x="Ciudad", color="Fraude sospechoso", title="Distribución por ciudad"), use_container_width=True)

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
    st.plotly_chart(px.box(df_aband,x="Uso app móvil",y="Prob. abandono"),use_container_width=True)

st.write("---")

# ---------------- TICKETS DE SOPORTE ----------------
st.subheader("🎟️ Tickets de soporte")
tickets=pd.DataFrame({
    "ID":[f"T{i}" for i in range(1,11)],
    "Asunto":np.random.choice(["Acceso bloqueado","Tarjeta clonada","Error en app","Consulta saldo"],10),
    "Status":np.random.choice(["Abierto","En progreso","Cerrado"],10),
    "Asignado":np.random.choice(["Agente1","Agente2","Agente3"],10)
})
st.dataframe(tickets,use_container_width=True,hide_index=True)

st.write("---")

# ---------------- ALERTAS INTERACTIVAS ----------------
st.subheader("🚨 Alertas dinámicas")
alertas=["Múltiples accesos sospechosos","Intentos de retiro en cajeros","Compra internacional","Transferencia inusual"]
colX,colY=st.columns(2)
with colX:
    alerta_sel=st.selectbox("Selecciona alerta",alertas)
    if st.button("Generar alerta"):
        st.error(f"⚠️ {alerta_sel} detectada")
with colY:
    st.success("Última alerta gestionada con éxito")

st.write("---")

# ---------------- PANEL FINANCIERO ----------------
st.subheader("💰 Panel financiero")
fin=pd.DataFrame({
    "Mes":pd.date_range("2024-01-01",periods=12,freq="M"),
    "Ingresos":np.random.randint(200000,400000,12),
    "Gastos":np.random.randint(100000,250000,12)
})
st.plotly_chart(px.bar(fin,x="Mes",y=["Ingresos","Gastos"],barmode="group"),use_container_width=True)

st.write("---")

# ---------------- BENCHMARK MODELOS ----------------
st.subheader("📈 Benchmark Modelos ML")
bench=pd.DataFrame({
    "Modelo":["Reg. logística","Árbol","Random Forest","KMeans","XGBoost"],
    "Precisión":[0.91,0.86,0.93,0.79,0.95],
    "Tiempo (s)":[3,1,5,2,6]
})
st.dataframe(bench,use_container_width=True,hide_index=True)

st.write("---")

# ---------------- CALENDARIO Y NOTAS ----------------
st.subheader("🗓️ Herramientas de oficina")
colN1,colN2=st.columns(2)
with colN1:
    st.write("📅 Calendario")
    events=[{"title":"Revisión diaria","start":datetime.now().strftime("%Y-%m-%d")},
            {"title":"Auditoría semanal","start":(datetime.now()+timedelta(days=3)).strftime("%Y-%m-%d")}]
    calendar(events=events,options={"editable":True,"selectable":True})
with colN2:
    st.write("📝 Notas rápidas")
    nota=st.text_area("Escribe notas",height=120)
    if st.button("Guardar nota"): st.success("Nota guardada")

st.write("---")

# ---------------- INTEGRACIONES EXTERNAS ----------------
st.subheader("🔗 Integraciones")
integraciones=pd.DataFrame({
    "Servicio":["API Sandbox","CRM","Webhook","DataLake"],
    "Estado":np.random.choice(["Conectado","Pendiente"],4)
})
st.table(integraciones)

st.caption("FinSecure Hub — Demo integral horizontal, logos uniformes, cargado de contenido.")
