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
Bienvenido a **FinSecure Hub**, una demo integral para el sector **banca y fintech en México**.  
Incluye **detección de fraudes, análisis de clientes, ML no-code, dashboards, mapas,
reportes y herramientas internas**, con tecnologías de última generación.
""")

# ---------------- STACK TECNOLÓGICO ----------------
st.markdown("### ⚙️ Stack Tecnológico")
cols = st.columns(7)
techs = [
    ("Gemma3","https://ai.google.dev/static/gemma/images/gemma3.png?hl=es-419"),
    ("LangChain","https://assets.streamlinehq.com/image/private/w_300,h_300,ar_1/f_auto/v1/icons/logos/langchain-ipuhh4qo1jz5ssl4x0g2a.png/langchain-dp1uxj2zn3752pntqnpfu2.png?_a=DATAg1AAZAA0"),
    ("OpenRouter","https://avatars.githubusercontent.com/u/139895814?s=200&v=4"),
    ("Google Sheets","https://mailmeteor.com/logos/assets/PNG/Google_Sheets_Logo_512px.png"),
    ("SQL Server","https://cdn-icons-png.flaticon.com/512/5968/5968364.png"),
    ("PostgreSQL","https://upload.wikimedia.org/wikipedia/commons/a/ad/Logo_PostgreSQL.png"),
    ("Azure Cloud","https://swimburger.net/media/ppnn3pcl/azure.png")
]
for (name,url),col in zip(techs,cols):
    col.image(url,caption=name,use_container_width=True)

st.write("---")

# ---------------- KPI DASHBOARD ----------------
st.subheader("📊 Dashboard General")
k1,k2,k3,k4 = st.columns(4)
k1.metric("Fraudes hoy", random.randint(10,30), delta="+3")
k2.metric("Monto recuperado", f"${random.randint(20000,100000)}")
k3.metric("Clientes en riesgo", random.randint(20,50), delta="-4")
k4.metric("Tiempo medio detección", f"{random.randint(2,9)} min")

data = pd.DataFrame({
    "Fecha": pd.date_range(datetime.today()-timedelta(days=30), periods=30),
    "Fraudes": np.random.randint(1,30,30),
    "Clientes activos": np.random.randint(500,800,30)
})
st.plotly_chart(px.line(data, x="Fecha", y=["Fraudes","Clientes activos"], title="Tendencia 30 días"), use_container_width=True)

st.write("---")

# ---------------- DETECCIÓN FRAUDES ----------------
st.subheader("🔎 Detección de Fraudes en Tiempo Real")
if st.button("Consultar base de datos"):
    with st.spinner("Gemma3 analizando registros..."):
        time.sleep(3)
    df = pd.DataFrame({
        "Usuario":[f"U{1000+i}" for i in range(60)],
        "Monto": np.random.randint(100,10000,60),
        "Hora":[f"{random.randint(0,23)}:{random.randint(0,59):02d}" for _ in range(60)],
        "Ciudad":np.random.choice(["CDMX","Guadalajara","Monterrey","Cancún","Tijuana"],60),
        "Fraude sospechoso":np.random.choice([True,False],60,p=[0.3,0.7])
    })
    st.dataframe(df, use_container_width=True, hide_index=True)
    fraudes=df[df["Fraude sospechoso"]==True]
    st.error(f"⚠️ {len(fraudes)} fraudes detectados")
    st.dataframe(fraudes, use_container_width=True, hide_index=True)
    st.plotly_chart(px.histogram(df, x="Ciudad", color="Fraude sospechoso", title="Distribución por ciudad"), use_container_width=True)

st.write("---")

# ---------------- CLIENTES ----------------
st.subheader("🙋‍♂️ Clientes en riesgo de abandono")
df_aband=pd.DataFrame({
    "Cliente":[f"C{i}" for i in range(1,41)],
    "Uso app móvil":np.random.choice(["Alto","Medio","Bajo"],40),
    "Probabilidad abandono":np.random.rand(40).round(2)
})
st.dataframe(df_aband,use_container_width=True,hide_index=True)
st.plotly_chart(px.box(df_aband,x="Uso app móvil",y="Probabilidad abandono",title="Distribución abandono"),use_container_width=True)

st.write("---")

# ---------------- MODELOS ML ----------------
st.subheader("🧠 Modelos ML")
with st.expander("Abrir modelos disponibles"):
    modelo=st.selectbox("Modelo",["Regresión logística","Árbol de decisión","Random Forest","KMeans","ARIMA"])
    if st.button("Ejecutar modelo"):
        with st.spinner("Gemma3 entrenando..."):
            time.sleep(3)
        if modelo=="Regresión logística":
            st.success("Precisión: 91%")
            st.plotly_chart(px.scatter(x=np.random.rand(60),y=np.random.rand(60),color=np.random.choice(["Fraude","No"],60)),use_container_width=True)
        elif modelo=="Árbol de decisión":
            st.success("Árbol entrenado, profundidad 6")
        elif modelo=="Random Forest":
            st.success("200 árboles entrenados")
            st.plotly_chart(px.bar(x=["Fraude","No"],y=[random.randint(20,40),random.randint(50,80)]),use_container_width=True)
        elif modelo=="KMeans":
            st.success("Clustering (k=4)")
            clusters=pd.DataFrame({"x":np.random.rand(80),"y":np.random.rand(80),"cluster":np.random.choice([1,2,3,4],80)})
            st.plotly_chart(px.scatter(clusters,x="x",y="y",color="cluster"),use_container_width=True)
        elif modelo=="ARIMA":
            st.success("Pronóstico 14 días")
            serie=pd.DataFrame({"fecha":pd.date_range(datetime.today(),periods=30),"valor":np.random.randint(100,500,30)})
            st.plotly_chart(px.line(serie,x="fecha",y="valor"),use_container_width=True)

st.write("---")

# ---------------- MAPA ----------------
st.subheader("🌍 Hotspots de Fraude")
df_map=pd.DataFrame({
    "lat":[19.43,20.67,25.67,21.16,32.52],
    "lon":[-99.13,-103.35,-100.31,-86.85,-117.03],
    "Ciudad":["CDMX","Guadalajara","Monterrey","Cancún","Tijuana"],
    "Fraudes":np.random.randint(5,30,5)
})
st.map(df_map)

st.write("---")

# ---------------- HERRAMIENTAS INTERNAS ----------------
st.subheader("🗂️ Herramientas internas")
c1,c2,c3=st.columns(3)
with c1:
    st.write("📝 Notas rápidas")
    nota=st.text_area("Escribe notas",height=120)
    if st.button("Guardar nota"): st.success("Nota guardada")
with c2:
    st.write("📂 Tareas")
    tareas=st.multiselect("Pendientes",["Revisar alertas","Contactar cliente","Generar reporte","Auditoría"])
    if st.button("Confirmar tareas"): st.info("Tareas confirmadas")
with c3:
    st.write("💬 Mensajes")
    mensaje=st.text_input("Escribe mensaje")
    if st.button("Enviar mensaje"): st.success("Mensaje enviado")

st.write("---")

# ---------------- CALENDARIO ----------------
st.subheader("📅 Calendario de seguimiento")
events=[{"title":"Revisión diaria","start":datetime.now().strftime("%Y-%m-%d")},
        {"title":"Auditoría semanal","start":(datetime.now()+timedelta(days=3)).strftime("%Y-%m-%d")}]
calendar(events=events,options={"editable":True,"selectable":True})

st.write("---")

# ---------------- REPORTES ----------------
st.subheader("📑 Reportes")
reporte=pd.DataFrame({
    "Fecha":pd.date_range(datetime.today(),periods=7),
    "Fraudes detectados":np.random.randint(1,20,7),
    "Monto recuperado":np.random.randint(1000,50000,7)
})
st.dataframe(reporte,use_container_width=True,hide_index=True)
st.download_button("📥 Descargar CSV",reporte.to_csv(index=False).encode("utf-8"),"reporte.csv")

st.write("---")

# ---------------- AUDITORÍA ----------------
st.subheader("🧾 Auditoría interna")
aud=pd.DataFrame({
    "Revisión":["Logs","Accesos","Base de datos","API externa"],
    "Estado":np.random.choice(["Correcto","Pendiente","Falla"],4)
})
st.table(aud)

st.markdown("---")
st.caption("FinSecure Hub — Demo integral para banca y fintech, menos de 500 líneas.")
