import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import threading

# ---------------------------------------------------------
# LISTE DES LOGICIELS WINGET (ID officiels)
# ---------------------------------------------------------
PACKS = {
    "Mozilla Firefox": "Mozilla.Firefox",
    "Google Chrome": "Google.Chrome",
    "VLC Media Player": "VideoLAN.VLC",
    "Git": "Git.Git",
    "Notepad++": "Notepad++.Notepad++",
    "7-Zip": "7zip.7zip",
    "Visual Studio Code": "Microsoft.VisualStudioCode"
}

# ---------------------------------------------------------
# INSTALLATION VIA WINGET
# ---------------------------------------------------------
def install_windows_winget(winget_id, log_callback):
    try:
        log_callback(f"Installation de {winget_id} via Winget…")

        subprocess.check_call([
            "winget", "install", "--id", winget_id,
            "--silent",
            "--accept-package-agreements",
            "--accept-source-agreements"
        ])

        log_callback(f"{winget_id} installé avec succès.")
    except Exception as e:
        log_callback(f"Erreur installation {winget_id}: {e}")

# ---------------------------------------------------------
# THREAD D’INSTALLATION
# ---------------------------------------------------------
def run_install(selected, log_callback, update_progress, on_complete):
    try:
        total = len(selected)
        count = 0

        for name in selected:
            winget_id = PACKS[name]
            install_windows_winget(winget_id, log_callback)

            count += 1
            progress_val = (count / total) * 100
            update_progress(progress_val)

        log_callback("Installation terminée.")
    finally:
        # Toujours réactiver l'interface à la fin, même en cas d'erreur
        on_complete()

# ---------------------------------------------------------
# INTERFACE GRAPHIQUE
# ---------------------------------------------------------
def start_gui():
    root = tk.Tk()
    root.title("install-winget")
    root.geometry("520x500")

    ttk.Label(root, text="Sélectionnez les logiciels à installer :", font=("Arial", 14)).pack(pady=10)

    frame = ttk.Frame(root)
    frame.pack()

    vars = {}
    checkbuttons = []
    for name in PACKS.keys():
        var = tk.BooleanVar()
        chk = ttk.Checkbutton(frame, text=name, variable=var)
        chk.pack(anchor="w")
        vars[name] = var
        checkbuttons.append(chk)

    progress = ttk.Progressbar(root, length=450)
    progress.pack(pady=15)

    log_box = tk.Text(root, height=12, width=65)
    log_box.pack()

    def log_callback(msg):
        def update_text():
            log_box.insert(tk.END, msg + "\n")
            log_box.see(tk.END)
        root.after(0, update_text)

    def update_progress(val):
        root.after(0, lambda: progress.config(value=val))

    def on_complete():
        def reset_ui():
            btn_install.config(state="normal", text="Installer")
            for chk in checkbuttons:
                chk.config(state="normal")
        root.after(0, reset_ui)

    def start_install():
        selected = [name for name, v in vars.items() if v.get()]
        if not selected:
            messagebox.showwarning("Aucun logiciel", "Sélectionnez au moins un logiciel.")
            return

        # Désactivation du bouton et des options pendant le travail du thread
        btn_install.config(state="disabled", text="Installation en cours...")
        for chk in checkbuttons:
            chk.config(state="disabled")
        progress["value"] = 0

        threading.Thread(
            target=run_install,
            args=(selected, log_callback, update_progress, on_complete),
            daemon=True
        ).start()

    btn_install = ttk.Button(root, text="Installer", command=start_install)
    btn_install.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    start_gui()
