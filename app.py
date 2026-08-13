import gradio as gr
import numpy as np
import matplotlib.pyplot as plt
import math

# ---------- Basic Calculator ----------
def calculate(num1, operation, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except (TypeError, ValueError):
        return "Enter valid numbers"

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "×":
        result = num1 * num2
    elif operation == "÷":
        if num2 == 0:
            return "Error: Division by zero"
        result = num1 / num2
    elif operation == "^":
        result = num1 ** num2
    else:
        return "Unknown operation"

    return f"Result: {result}"


# ---------- Function Plotter ----------
def plot_function(expression, x_min, x_max):
    try:
        x = np.linspace(float(x_min), float(x_max), 400)

        # Safe namespace: only numpy + math functions allowed
        allowed_names = {
            "x": x, "np": np, "sin": np.sin, "cos": np.cos, "tan": np.tan,
            "exp": np.exp, "log": np.log, "sqrt": np.sqrt, "pi": np.pi,
            "abs": np.abs
        }
        y = eval(expression, {"__builtins__": {}}, allowed_names)

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(x, y, color="#2563eb", linewidth=2)
        ax.axhline(0, color="black", linewidth=0.5)
        ax.axvline(0, color="black", linewidth=0.5)
        ax.set_title(f"y = {expression}")
        ax.grid(True, alpha=0.3)
        return fig
    except Exception as e:
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.text(0.5, 0.5, f"Error: {e}", ha="center", va="center", color="red")
        ax.axis("off")
        return fig


# ---------- Gradio UI ----------
with gr.Blocks(title="Calculator + Graph Plotter") as demo:
    gr.Markdown("# 🧮 Calculator & Function Plotter")

    with gr.Tab("Basic Calculator"):
        with gr.Row():
            num1 = gr.Number(label="First Number")
            operation = gr.Dropdown(["+", "-", "×", "÷", "^"], label="Operation", value="+")
            num2 = gr.Number(label="Second Number")
        calc_btn = gr.Button("Calculate", variant="primary")
        calc_output = gr.Textbox(label="Output")
        calc_btn.click(calculate, inputs=[num1, operation, num2], outputs=calc_output)

    with gr.Tab("Function Plotter"):
        expr = gr.Textbox(label="Function of x (e.g. sin(x), x**2 + 3*x - 1)", value="sin(x)")
        with gr.Row():
            x_min = gr.Number(label="x min", value=-10)
            x_max = gr.Number(label="x max", value=10)
        plot_btn = gr.Button("Plot", variant="primary")
        plot_output = gr.Plot(label="Graph")
        plot_btn.click(plot_function, inputs=[expr, x_min, x_max], outputs=plot_output)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 7860))
    demo.launch(server_name="0.0.0.0", server_port=port)
