def change_theme(curr_frame, color='dark gray'):
    curr_frame.configure(bg=color)
    print(curr_frame)
    for widget in curr_frame.winfo_children():

        if widget.winfo_children() is not None:
            try:
                print(widget.widgetName)
                if (widget.widgetName != 'button') and (widget.widgetName != 'text'):
                    widget.configure(bg=color)
                    change_theme(widget, color)
                    print(widget.widgetName)
            except tk.TclError:
                # print(f' Warning: {widget}')
                pass