from IPython.display import display, HTML

js = """
    <script>IPython.notebook.kernel.execute(
        "current_ipynb=('" + IPython.notebook.notebook_name + "')"
    );</script>
"""
             
display(HTML(js))