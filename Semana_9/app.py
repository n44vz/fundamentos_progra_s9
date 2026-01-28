import streamlit as st
import pandas as pd
import numpy as np

# Equivalente a # Título
st.title("App de Streamlit") 

# Equivalente a ## Encabezado
st.header("Este es un encabezado")

# Equivalente a ### Subencabezado
st.subheader("Este es un subencabezado")

# Equivalente a escribir el texto como "texto"
st.write("Este es un párrafo")
st.write("Este es un segundo párrafo")
st.write("Este es un tercer párrafo")
"______________________________________"

df = pd.DataFrame(np.random.randn(10, 2), columns=['Precio', 'Ventas'])
st.line_chart(df, x_label="Posición", y_label="Valor", color=["#B439B0", "#C16B20"])
st.dataframe(df)

"______________________________________"

# Ejemplos de cómo insertar markdown

# Explicita
st.markdown("""
## hola 

```
import streamlit as st
import pandas as pd
import numpy as np         
```                       
""")

# Implicito
"""
 ### Linea del conflicto 2         
"""

"""
 ### Ejemplo de traer cambios       
"""
"""
 ### Ejemplo de traer cambios       
"""
"""
 ### Ejemplo de traer cambios       
""""""
 ### Ejemplo de traer cambios       
""""""
 ### Ejemplo de traer cambios       
""""""
 ### Ejemplo de traer cambios       
"""
