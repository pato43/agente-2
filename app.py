import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta
from streamlit_calendar import calendar
import random, time

# -------- CONFIGURACIÓN GENERAL --------
st.set_page_config(page_title="💳 FinSecure Hub", layout="wide")

# -------- ENCABEZADO --------
st.markdown("""
# 💳 FinSecure Hub
**Plataforma integral para la gestión de fraudes y clientes en banca y fintech mexicana.**  
Incluye **detección de fraudes en tiempo real, análisis de clientes, machine learning no-code, dashboards, alertas y herramientas corporativas.**
""")

st.write("---")

# -------- STACK TECNOLÓGICO --------
st.subheader("⚙️ Stack Tecnológico Utilizado")

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

# Grid horizontal uniforme
st.markdown(
    """
    <style>
    .tech-grid {
        display: flex;
        flex-wrap: nowrap;
        overflow-x: auto;
        gap: 25px;
        justify-content: center;
        align-items: center;
        padding: 15px 0;
    }
    .tech-card {
        flex: 0 0 auto;
        text-align: center;
        padding: 10px;
    }
    .tech-card img {
        height: 45px;
        max-width: 80px;
        object-fit: contain;
        margin-bottom: 5px;
    }
    .tech-card div {
        font-size: 12px;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="tech-grid">', unsafe_allow_html=True)
for name, url in techs:
    st.markdown(
        f"""
        <div class="tech-card">
            <img src="{url}">
            <div>{name}</div>
        </div>
        """,
        unsafe_allow_html=True
    )
st.markdown('</div>', unsafe_allow_html=True)

st.write("---")

# -------- KPI DASHBOARD --------
st.subheader("📊 Dashboard General")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Fraudes hoy", 32, delta="+7")
col2.metric("Monto recuperado", "$145,200")
col3.metric("Clientes en riesgo", 61, delta="-3")
col4.metric("Tiempo detección", "3.5 min")

# Datos de tendencia
data_tendencia = pd.DataFrame({
    "Fecha": pd.date_range(datetime.today()-timedelta(days=30), periods=30),
    "Fraudes": np.random.randint(8,35,30),
    "Clientes activos": np.random.randint(600,1000,30)
})

fig_tendencia = px.line(
    data_tendencia,
    x="Fecha",
    y=["Fraudes","Clientes activos"],
    title="📈 Tendencia de fraudes y clientes activos (últimos 30 días)"
)
st.plotly_chart(fig_tendencia, use_container_width=True)

st.write("---")

# -------- DETECCIÓN DE FRAUDES --------
st.subheader("🔎 Detección de Fraudes en Tiempo Real")

df_fraude = pd.DataFrame({
    "Usuario":[f"U{1000+i}" for i in range(60)],
    "Monto": np.random.randint(300,20000,60),
    "Ciudad":np.random.choice(["CDMX","GDL","MTY","Querétaro","Cancún","Tijuana"],60),
    "Fraude sospechoso":np.random.choice([True,False],60,p=[0.28,0.72])
})

colA, colB = st.columns(2)
with colA:
    st.dataframe(df_fraude, use_container_width=True, hide_index=True)
with colB:
    fig_ciudad = px.histogram(
        df_fraude,
        x="Ciudad",
        color="Fraude sospechoso",
        title="Distribución de fraudes por ciudad"
    )
    st.plotly_chart(fig_ciudad, use_container_width=True)

st.write("---")

# -------- CLIENTES EN RIESGO --------
st.subheader("🙋‍♂️ Clientes en Riesgo")

df_aband = pd.DataFrame({
    "Cliente":[f"C{i}" for i in range(1,41)],
    "Uso app móvil":np.random.choice(["Alto","Medio","Bajo"],40),
    "Prob. abandono":np.random.rand(40).round(2)
})

col1, col2 = st.columns(2)
with col1:
    st.dataframe(df_aband, use_container_width=True, hide_index=True)
with col2:
    fig_aband = px.box(
        df_aband,
        x="Uso app móvil",
        y="Prob. abandono",
        title="Probabilidad de abandono según nivel de uso de la app"
    )
    st.plotly_chart(fig_aband, use_container_width=True)

st.write("---")

# -------- ALERTAS SOC --------
st.subheader("📰 Últimas alertas de seguridad (SOC)")

alerts = [
    "🔔 54 intentos de login fallidos desde IPs desconocidas en menos de 15 min.",
    "🔔 9 transacciones internacionales sospechosas bloqueadas.",
    "🔔 Aumento del 21% en fraudes por compras digitales en apps móviles.",
    "🔔 Nuevo patrón detectado: retiros pequeños consecutivos en cajeros de CDMX."
]

for alert in alerts:
    st.warning(alert)

st.write("---")
# -------- TAREAS Y NOTAS DEL EQUIPO --------
st.subheader("📝 Tareas y notas del equipo SOC")

colN1, colN2 = st.columns(2)

with colN1:
    st.write("**Tareas pendientes:**")
    tareas_df = pd.DataFrame({
        "Tarea":[
            "Revisar logs de BBVA",
            "Actualizar reglas antifraude",
            "Capacitación interna SOC",
            "Validar alertas en CDMX",
            "Analizar fraude recurrente en cajeros",
            "Coordinar reunión con área legal"
        ],
        "Responsable":["Ana","Luis","Marta","Carlos","Rocío","David"],
        "Estado":["En curso","Pendiente","Programada","En curso","Pendiente","Pendiente"]
    })
    st.dataframe(tareas_df, use_container_width=True, hide_index=True)

with colN2:
    st.write("**Notas rápidas:**")
    notas_previas = """⚠️ Revisar aumento en fraudes en apps móviles.
✅ Auditoría programada viernes 10 AM.
📌 Recordar actualizar dashboard de KPIs para comité mensual.
"""
    st.text_area("Notas del equipo", notas_previas, height=180)

st.write("---")

# -------- DRAG & DROP ML PIPELINES --------
st.subheader("📦 Construcción de modelos ML (simulación drag & drop)")

st.caption("Organiza un pipeline arrastrando componentes.")

cols_dd = st.columns(4)
modulos = ["📂 Entrada de datos","⚙️ Preprocesamiento","🤖 Entrenamiento modelo","📈 Resultados"]
for i,mod in enumerate(modulos):
    with cols_dd[i]:
        st.markdown(f"""
        <div style="border:2px dashed #888; border-radius:12px; padding:20px; text-align:center; min-height:120px;">
            {mod}
        </div>
        """, unsafe_allow_html=True)

st.success("Pipeline configurado con éxito: Regresión logística entrenada con 92.7% precisión sobre datos de fraude.")

st.write("---")

# -------- PANEL FINANCIERO --------
st.subheader("💰 Panel financiero de la operación")

fin_df = pd.DataFrame({
    "Mes": pd.date_range("2024-01-01", periods=12, freq="M"),
    "Ingresos": np.random.randint(250000,400000,12),
    "Gastos": np.random.randint(120000,250000,12),
    "Pérdidas por fraude": np.random.randint(30000,80000,12)
})

colF1, colF2 = st.columns(2)
with colF1:
    st.dataframe(fin_df, use_container_width=True, hide_index=True)

with colF2:
    fig_fin = px.bar(fin_df, x="Mes", y=["Ingresos","Gastos","Pérdidas por fraude"], 
                     barmode="group", title="Evolución financiera")
    st.plotly_chart(fig_fin, use_container_width=True)

st.write("---")

# -------- CALENDARIO CORPORATIVO --------
st.subheader("🗓️ Calendario corporativo")

eventos = [
    {"title":"Revisión SOC diaria","start":datetime.now().strftime("%Y-%m-%d")},
    {"title":"Auditoría externa","start":(datetime.now()+timedelta(days=2)).strftime("%Y-%m-%d")},
    {"title":"Comité de riesgos","start":(datetime.now()+timedelta(days=5)).strftime("%Y-%m-%d")},
    {"title":"Capacitación antifraude","start":(datetime.now()+timedelta(days=10)).strftime("%Y-%m-%d")}
]

calendar(events=eventos, options={"editable":False,"selectable":False,"initialView":"dayGridMonth"})

st.write("---")

# -------- NOTICIAS CORPORATIVAS --------
st.subheader("📰 Noticias corporativas recientes")

noticias = [
    "Nuevo reporte del Banco de México alerta sobre incremento de fraudes digitales en tarjetas de débito.",
    "FinSecure Hub recibió certificación ISO 27001 en gestión de seguridad de la información.",
    "Se lanzó integración con sistemas de detección biométrica en cajeros automáticos.",
    "La CNBV advierte sobre campañas de phishing en WhatsApp dirigidas a clientes bancarios.",
    "El área de compliance validó nuevas regulaciones contra lavado de dinero aplicables desde 2025."
]

for n in noticias:
    st.info("📌 "+n)

st.write("---")
# -------- TICKETS DE SOPORTE --------
st.subheader("🎟️ Tickets de soporte activos")

tickets_df = pd.DataFrame({
    "ID":[f"TKT-{i:03d}" for i in range(1,16)],
    "Asunto":np.random.choice([
        "Acceso bloqueado","Tarjeta clonada","Error en app móvil",
        "Consulta de saldo","Transferencia rechazada","Fraude en e-commerce"
    ],15),
    "Estado":np.random.choice(["Abierto","En progreso","Cerrado"],15,p=[0.4,0.4,0.2]),
    "Agente asignado":np.random.choice(["Ana","Luis","Marta","Carlos","Rocío"],15),
    "Tiempo respuesta (min)":np.random.randint(5,60,15)
})

colT1, colT2 = st.columns([2,1])
with colT1:
    st.dataframe(tickets_df, use_container_width=True, hide_index=True)
with colT2:
    fig_tickets = px.pie(
        tickets_df,
        names="Estado",
        title="Distribución de tickets por estado"
    )
    st.plotly_chart(fig_tickets, use_container_width=True)

st.write("---")

# -------- ALERTAS DINÁMICAS --------
st.subheader("🚨 Alertas dinámicas SOC")

alertas_posibles = [
    "Múltiples accesos sospechosos desde el mismo dispositivo",
    "Intentos de retiro fallidos en cajeros CDMX",
    "Compra internacional en horario atípico",
    "Transferencia repetitiva en cuentas relacionadas",
    "Fraude recurrente detectado en tarjetas virtuales"
]

colA1, colA2 = st.columns(2)

with colA1:
    alerta_sel = st.selectbox("Selecciona una alerta para activar:", alertas_posibles)
    if st.button("Activar alerta"):
        st.error(f"⚠️ {alerta_sel} detectada y registrada en el sistema.")

with colA2:
    st.success("✅ Última alerta gestionada con éxito a las 09:42 AM.")

st.write("---")

# -------- BENCHMARK DE MODELOS ML --------
st.subheader("📈 Benchmark de modelos ML")

bench_df = pd.DataFrame({
    "Modelo":["Regresión logística","Árbol de decisión","Random Forest","KMeans","XGBoost"],
    "Precisión":[0.91,0.86,0.93,0.79,0.95],
    "Recall":[0.89,0.84,0.91,0.74,0.94],
    "Tiempo de entrenamiento (s)":[3,1,5,2,6]
})

colB1, colB2 = st.columns([2,1])
with colB1:
    st.dataframe(bench_df, use_container_width=True, hide_index=True)
with colB2:
    fig_bench = px.bar(
        bench_df,
        x="Modelo",
        y="Precisión",
        color="Modelo",
        title="Precisión de modelos comparados"
    )
    st.plotly_chart(fig_bench, use_container_width=True)

st.write("---")

# -------- GENERADOR DE REPORTES EJECUTIVOS --------
st.subheader("📑 Generador de reportes ejecutivos")

colR1, colR2 = st.columns(2)
with colR1:
    formato = st.selectbox("Selecciona el formato del reporte:",["PDF","Excel","CSV"])
    if st.button("Generar reporte"):
        with st.spinner("Generando reporte corporativo..."):
            time.sleep(2)
        st.success(f"Reporte en formato {formato} generado exitosamente ✅")

with colR2:
    st.info("""
Los reportes incluyen:
- Resumen de fraudes detectados
- Clientes en riesgo
- KPIs financieros
- Alertas SOC y tickets activos
    """)

st.write("---")

# -------- RANKING DE FRAUDES --------
st.subheader("🏦 Ranking de fraudes por institución")

ranking_df = pd.DataFrame({
    "Institución":["Banco Azteca","BBVA","Santander","Banorte","HSBC","Scotiabank"],
    "Fraudes detectados":np.random.randint(80,250,6)
})

colRk1, colRk2 = st.columns([1,2])
with colRk1:
    st.dataframe(ranking_df, use_container_width=True, hide_index=True)
with colRk2:
    fig_rank = px.bar(
        ranking_df,
        x="Institución",
        y="Fraudes detectados",
        color="Institución",
        title="Fraudes detectados por institución"
    )
    st.plotly_chart(fig_rank, use_container_width=True)

st.write("---")
# -------- GESTIÓN DE USUARIOS Y ROLES --------
st.subheader("👥 Gestión de usuarios y roles")

usuarios_df = pd.DataFrame({
    "Usuario": ["admin01","soporte02","fraude03","analista04","gerente05"],
    "Rol": ["Administrador","Soporte","SOC","Analista","Gerente"],
    "Acceso": ["Total","Tickets y alertas","Fraudes","ML y reportes","General"],
    "Estado": ["Activo","Activo","Inactivo","Activo","Activo"]
})

st.dataframe(usuarios_df, use_container_width=True, hide_index=True)

st.write("---")

# -------- PANEL DE ACCESOS RECIENTES --------
st.subheader("📍 Accesos recientes al sistema")

accesos_df = pd.DataFrame({
    "Usuario": np.random.choice(usuarios_df["Usuario"], 15),
    "Ciudad": np.random.choice(["CDMX","Monterrey","Guadalajara","Toluca"], 15),
    "IP": [f"187.23.45.{i}" for i in np.random.randint(10,250,15)],
    "Estado": np.random.choice(["Permitido","Sospechoso"], 15, p=[0.8,0.2])
})

colAcc1, colAcc2 = st.columns([2,1])
with colAcc1:
    st.dataframe(accesos_df, use_container_width=True, hide_index=True)
with colAcc2:
    fig_acc = px.histogram(accesos_df, x="Ciudad", color="Estado",
                           title="Distribución de accesos por ciudad")
    st.plotly_chart(fig_acc, use_container_width=True)

st.write("---")

# -------- INTEGRACIONES EXTERNAS --------
st.subheader("🔗 Integraciones externas")

tech_logos = {
    "Google Sheets":"https://mailmeteor.com/logos/assets/PNG/Google_Sheets_Logo_512px.png",
    "SQL Server":"https://cdn-icons-png.flaticon.com/512/5968/5968364.png",
    "PostgreSQL":"https://upload.wikimedia.org/wikipedia/commons/a/ad/Logo_PostgreSQL.png",
    "Azure Cloud":"https://upload.wikimedia.org/wikipedia/commons/f/fa/Microsoft_Azure.svg",
    "LangChain":"https://assets.streamlinehq.com/image/private/w_300,h_300,ar_1/f_auto/v1/icons/logos/langchain-ipuhh4qo1jz5ssl4x0g2a.png/langchain-dp1uxj2zn3752pntqnpfu2.png?_a=DATAg1AAZAA0",
    "Gemma3":"https://ai.google.dev/static/gemma/images/gemma3.png?hl=es-419",
    "OpenRouter":"https://openrouter.ai/images/logo.png",
    "Google Gemini":"https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Gemini.max-400x400.png"
}

cols = st.columns(len(tech_logos))
for (name, url), col in zip(tech_logos.items(), cols):
    with col:
        st.image(url, caption=name, use_container_width=True)

st.write("---")

# -------- PANEL DE PRODUCTIVIDAD --------
st.subheader("📆 Panel de productividad")

colP1, colP2, colP3 = st.columns(3)

with colP1:
    st.markdown("### 📝 Notas rápidas")
    notas = st.text_area("Escribe tus notas:", height=150)
    if notas:
        st.info("Nota guardada localmente.")

with colP2:
    st.markdown("### ✅ Tareas pendientes")
    tareas = [
        "Revisar alertas SOC",
        "Generar reporte ejecutivo",
        "Actualizar modelo ML",
        "Revisar accesos sospechosos",
        "Atender ticket de fraude"
    ]
    for t in tareas:
        st.checkbox(t, value=False)

with colP3:
    st.markdown("### 📅 Calendario")
    fecha = st.date_input("Selecciona una fecha")
    st.write(f"Agenda del {fecha}:")
    st.success("Reunión de seguimiento con comité de riesgos")

st.write("---")

# -------- KPIs DE EQUIPO --------
st.subheader("📊 KPIs de equipo")

kpis_df = pd.DataFrame({
    "Métrica":["Tickets atendidos","Fraudes detectados","Modelos entrenados","Reportes generados"],
    "Hoy":[25,19,3,5],
    "Semana":[140,92,12,25],
    "Mes":[580,410,48,99]
})

colK1, colK2 = st.columns([1,2])
with colK1:
    st.dataframe(kpis_df, use_container_width=True, hide_index=True)
with colK2:
    fig_kpi = px.line(kpis_df, x="Métrica", y=["Hoy","Semana","Mes"], markers=True,
                      title="Evolución de KPIs del equipo")
    st.plotly_chart(fig_kpi, use_container_width=True)

st.write("---")
