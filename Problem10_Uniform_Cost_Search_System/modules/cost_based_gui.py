import tkinter as tk
from tkinter import messagebox
from uniform_cost_search import uniform_cost_search
from weighted_graph_utils import add_weighted_edge, clear_graph

graph = {}


def add_edge():
    node1 = node1_entry.get().strip().upper()
    node2 = node2_entry.get().strip().upper()
    cost = cost_entry.get().strip()

    if not node1 or not node2 or not cost:
        messagebox.showwarning("Input Error", "Please fill all fields.")
        return

    if not cost.isdigit():
        messagebox.showwarning("Input Error", "Cost must be a number.")
        return

    add_weighted_edge(graph, node1, node2, int(cost))

    result_box.insert(
        tk.END,
        f"Added Edge: {node1} ↔ {node2} | Cost = {cost}\n"
    )

    node1_entry.delete(0, tk.END)
    node2_entry.delete(0, tk.END)
    cost_entry.delete(0, tk.END)


def run_search():
    start = start_entry.get().strip().upper()
    goal = goal_entry.get().strip().upper()

    result_box.delete("1.0", tk.END)

    path, total_cost, explored = uniform_cost_search(graph, start, goal)

    result_box.insert(tk.END, "=== Uniform Cost Search Result ===\n\n")

    if path:
        result_box.insert(
            tk.END,
            f"Optimal Path : {' -> '.join(path)}\n"
        )
        result_box.insert(
            tk.END,
            f"Total Cost   : {total_cost}\n"
        )
    else:
        result_box.insert(tk.END, "No valid path found.\n")

    result_box.insert(
        tk.END,
        f"Nodes Explored: {len(explored)} -> {explored}\n"
    )


def reset_all():
    clear_graph(graph)
    result_box.delete("1.0", tk.END)

    for entry in [
        node1_entry, node2_entry, cost_entry,
        start_entry, goal_entry
    ]:
        entry.delete(0, tk.END)


root = tk.Tk()
root.title("Problem 10 - Uniform Cost Search System")
root.geometry("780x620")
root.config(bg="#eef2f7")

title = tk.Label(
    root,
    text="Uniform Cost Search System",
    font=("Arial", 18, "bold"),
    bg="#eef2f7",
    fg="#1a1a1a"
)
title.pack(pady=12)

for text in ["Node 1", "Node 2", "Cost"]:
    tk.Label(root, text=text, bg="#eef2f7").pack()

node1_entry = tk.Entry(root, width=35)
node1_entry.pack()

node2_entry = tk.Entry(root, width=35)
node2_entry.pack()

cost_entry = tk.Entry(root, width=35)
cost_entry.pack()

tk.Button(
    root,
    text="Add Weighted Edge",
    command=add_edge,
    width=22,
    bg="#2563eb",
    fg="white"
).pack(pady=8)

for text in ["Start Node", "Goal Node"]:
    tk.Label(root, text=text, bg="#eef2f7").pack()

start_entry = tk.Entry(root, width=35)
start_entry.pack()

goal_entry = tk.Entry(root, width=35)
goal_entry.pack()

button_frame = tk.Frame(root, bg="#eef2f7")
button_frame.pack(pady=10)

tk.Button(
    button_frame,
    text="Run UCS",
    command=run_search,
    width=15,
    bg="#16a34a",
    fg="white"
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame,
    text="Reset",
    command=reset_all,
    width=15,
    bg="#dc2626",
    fg="white"
).grid(row=0, column=1, padx=5)

result_box = tk.Text(root, height=20, width=90, font=("Consolas", 10))
result_box.pack(pady=12)

root.mainloop()