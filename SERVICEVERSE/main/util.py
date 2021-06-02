import matplotlib.pyplot as plot
import base64
from io import BytesIO


def get_graph():
    buffer = BytesIO()
    plot.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_plot(y):
    plot.switch_backend('AGG')
    plot.figure(figsize=(5, 5))
    plot.pie(y)
    plot.tight_layout()
    graph = get_graph()
    return graph
