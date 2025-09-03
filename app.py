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
Plataforma integral de **fraudes y clientes** en banca y fintech mexicana.  
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

cols = st.columns(len(techs))
for (name, url), col in zip(techs, cols):
    with col:
        st.image(url, caption=name, use_container_width=True)

st.write("---")

# ---------------- KPI DASHBOARD ----------------
st.subheader("📊 Dashboard General")
k1,k2,k3,k4 = st.columns(4)
k1.metric("Fraudes hoy", 27, delta="+4")
k2.metric("Monto recuperado", "$132,400")
k3.metric("Clientes en riesgo", 52, delta="-6")
k4.metric("Tiempo detección", "4 min")

data = pd.DataFrame({
    "Fecha": pd.date_range(datetime.today()-timedelta(days=30), periods=30),
    "Fraudes": np.random.randint(5,40,30),
    "Clientes activos": np.random.randint(500,900,30)
})
st.plotly_chart(px.line(data, x="Fecha", y=["Fraudes","Clientes activos"], 
                        title="Tendencia últimos 30 días"), use_container_width=True)

st.write("---")

# ---------------- DETECCIÓN FRAUDES ----------------
st.subheader("🔎 Detección de Fraudes en Tiempo Real")
df_fraude = pd.DataFrame({
    "Usuario":[f"U{1000+i}" for i in range(50)],
    "Monto": np.random.randint(500,15000,50),
    "Ciudad":np.random.choice(["CDMX","GDL","MTY","Querétaro","Cancún"],50),
    "Fraude sospechoso":np.random.choice([True,False],50,p=[0.3,0.7])
})
colA,colB = st.columns(2)
with colA:
    st.dataframe(df_fraude, use_container_width=True, hide_index=True)
with colB:
    st.plotly_chart(px.histogram(df_fraude, x="Ciudad", color="Fraude sospechoso", 
                                 title="Distribución por ciudad"), use_container_width=True)

st.write("---")

# ---------------- CLIENTES ----------------
st.subheader("🙋‍♂️ Clientes en Riesgo")
df_aband=pd.DataFrame({
    "Cliente":[f"C{i}" for i in range(1,31)],
    "Uso app móvil":np.random.choice(["Alto","Medio","Bajo"],30),
    "Prob. abandono":np.random.rand(30).round(2)
})
col1,col2=st.columns(2)
with col1:
    st.dataframe(df_aband,use_container_width=True,hide_index=True)
with col2:
    st.plotly_chart(px.box(df_aband,x="Uso app móvil",y="Prob. abandono",
                           title="Prob. abandono por tipo de uso"),use_container_width=True)

st.write("---")

# ---------------- NOTICIAS SEGURIDAD (REALISTAS) ----------------
st.subheader("📰 Últimas alertas SOC")
news = [
    "45 intentos de login fallidos en menos de 10 min desde IPs en Europa del Este.",
    "12 transacciones sospechosas bloqueadas en terminales de autoservicio (CDMX).",
    "Clientes reportan smishing con links de 'actualización de tarjeta'.",
    "18% de incremento en fraudes por compras en línea la última quincena."
]
for n in news:
    st.warning("🔔 "+n)

st.write("---")

# ---------------- TAREAS Y NOTAS ----------------
st.subheader("📝 Tareas y Notas del Equipo")
colN1,colN2=st.columns(2)
with colN1:
    st.write("**Tareas pendientes:**")
    tareas = pd.DataFrame({
        "Tarea":["Revisar logs de BBVA","Actualizar reglas antifraude","Capacitación SOC","Validar alertas CDMX"],
        "Responsable":["Ana","Luis","Marta","Carlos"],
        "Estado":["En curso","Pendiente","Programada","En curso"]
    })
    st.dataframe(tareas,use_container_width=True,hide_index=True)
with colN2:
    st.write("**Notas rápidas:**")
    st.text_area("Notas del equipo", "⚠️ Revisar aumento en fraudes de compras en apps móviles.\n✅ Auditoría programada viernes 10 AM.")

st.write("---")

# ---------------- DRAG & DROP SIMULADO ----------------
st.subheader("📦 Modelos ML (simulación drag & drop)")
st.info("Arrastra y suelta componentes (simulado).")

cols_dd = st.columns(4)
for i,mod in enumerate(["📌 Entrada CSV","⚙️ Preprocesamiento","🤖 Modelo ML","📈 Resultados"]):
    with cols_dd[i]:
        st.markdown(f"""
        <div style="border:2px dashed #888; border-radius:12px; padding:20px; text-align:center; min-height:100px;">
            {mod}
        </div>
        """, unsafe_allow_html=True)

st.success("Pipeline configurado con éxito: Regresión logística entrenada con 93% precisión.")

st.write("---")

# ---------------- GENERADOR REPORTES ----------------
st.subheader("📑 Reportes ejecutivos")
colR1,colR2=st.columns(2)
with colR1:
    formato = st.selectbox("Formato",["PDF","Excel","CSV"])
    if st.button("Generar reporte"):
        with st.spinner("Generando reporte..."):
            time.sleep(1.5)
        st.success(f"Reporte en {formato} generado ✅")
with colR2:
    st.info("Incluye KPIs de fraudes, clientes en riesgo y métricas de desempeño del SOC.")
