# Tercer cambio de prueba
from fastapi import Depends, FastAPI

from .auth import get_current_customer_id
from .services.busqueda import buscar_movimientos
from .services.reportes import generar_reporte

app = FastAPI(title=&quot;Reportes conversacionales&quot;, version=&quot;0.2.0&quot;)

@app.get(&quot;/reportes&quot;)
def get_reporte(customer_id: str = Depends(get_current_customer_id)) -&gt; dict:
return generar_reporte(customer_id)

@app.get(&quot;/buscar&quot;)
def get_buscar(customer_id: str, q: str) -&gt; dict:
&quot;&quot;&quot;Búsqueda conversacional sobre los movimientos del cliente.&quot;&quot;&quot;
return buscar_movimientos(customer_id, q)

@app.get(&quot;/health&quot;)
def health() -&gt; dict:
return {&quot;status&quot;: &quot;ok&quot;}
