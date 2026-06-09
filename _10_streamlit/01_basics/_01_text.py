import streamlit as st

#streamlit run [파일명].py

st.title('Hello World!')
st.header("text",divider='rainbow')
st.subheader(":green[sub] header",divider='red')
'''
- st.text
    - text는 단순글자
- st.write
    - 단순글자일 뿐만 아니라 마크다운, ,표, 리스트, 차트, 입력 타입 등에 따라 출력
'''
st.text('write 테스트')# 단순글자

st.write('write **markdown** 지원')

st.write("`write`")

st.markdown("### markdown")

st.html("<h3>html도 지원<h3>")

st.subheader(body=':red[magic]')

'treamlit magic'
'변수나 리터럴 값이 출력 구문내에 없어도 화면에 갑슬 기록하는 기능'

{'1':'2','2':'3','3':'4','4':'5','5':'6'}



code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language="python",line_numbers=True)


st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

st.badge("New")
st.badge("Success", icon=":material/check:", color="green")

st.markdown(
    ":violet-badge[:material/star: Favorite] :orange-badge[⚠️ Needs review] :gray-badge[Deprecated]"
)

st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

st.metric(
    label="Gas price", value=4, delta=-0.5, delta_color="inverse"
)

st.metric(
    label="Active developers",
    value=123,
    delta=123,
    delta_color="off",
)

changes = list(rng(4).standard_normal(20))
data = [sum(changes[:i]) for i in range(20)]
delta = round(data[-1], 2)
