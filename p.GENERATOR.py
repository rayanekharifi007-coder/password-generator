import tkinter as tk
from tkinter import messagebox, filedialog
import secrets
import string
import math
import base64
import hashlib


class ExecutiveTerminal:
    def __init__(self, root):
        self.root = root
        self.root.title("Rayanes PG")
        self.root.geometry("500x450")
        self.root.configure(bg="#0d0d0d")
        self.root.resizable(False, False)

       
        tk.Label(root, text="Rayanes PG", 
                 font=("Courier New", 12, "bold"), bg="#0d0d0d", fg="#ff0000").pack(pady=10)

      
        self.console = tk.Text(root, height=6, bg="#050505", fg="#00ff00", 
                               font=("Courier New", 10), relief="flat", borderwidth=2)
        self.console.pack(fill="x", padx=20)
        self.log("> System Boot Sequence Complete.")
        self.log("> Security Protocols Enabled.")
        self.log("> Awaiting Module Selection...")

      
        btn_frame = tk.Frame(root, bg="#0d0d0d")
        btn_frame.pack(pady=15)

       
        self.create_module_btn(btn_frame, "[ A: PASSWORD GEN ]", "#00ff00", "#1a1a1a", self.launch_generator)
        self.create_module_btn(btn_frame, "[ B: AUDITOR ]", "#ff9900", "#1a1a1a", self.launch_auditor)
        self.create_module_btn(btn_frame, "[ C: ENCRYPTION ]", "#00bfff", "#1a1a1a", self.launch_encryption)
        self.create_module_btn(btn_frame, "[ D: STEGANOGRAPHY ]", "#ff00ff", "#1a1a1a", self.launch_stego)

        tk.Label(root, text="Select a module to initialize", 
                 font=("Courier New", 8), bg="#0d0d0d", fg="#444444").pack(side="bottom", pady=10)

    def create_module_btn(self, parent, text, fg, bg, cmd):
        btn = tk.Button(parent, text=text, font=("Courier New", 11, "bold"), 
                        bg=bg, fg=fg, activebackground=fg, activeforeground="black",
                        relief="flat", cursor="hand2", width=22, command=cmd)
        btn.pack(pady=4)

    def log(self, text):
        self.console.insert("end", f"> {text}\n")
        self.console.see("end")

    def launch_generator(self):
        self.log("Initializing Generator Module..."); GeneratorApp(tk.Toplevel(self.root))

    def launch_auditor(self):
        self.log("Initializing Auditor Module..."); AuditorApp(tk.Toplevel(self.root))

    def launch_encryption(self):
        self.log("Initializing Encryption Module..."); EncryptionApp(tk.Toplevel(self.root))

    def launch_stego(self):
        self.log("Initializing Steganography Module..."); StegoApp(tk.Toplevel(self.root))



class GeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Module A: Generator")
        self.root.geometry("500x680"); self.root.configure(bg="#1e1e1e")
        self.colors = {"bg": "#1e1e1e", "card": "#252526", "text": "#cccccc", "accent": "#0e639c", "input": "#4ec9b0"}
        
       
        self.container = tk.Frame(root, bg=self.colors["bg"]); self.container.pack(fill="both", expand=True, padx=20, pady=10)
        tk.Label(self.container, text="GENERATOR", font=("Segoe UI", 18, "bold"), bg=self.colors["bg"], fg="#00ff00").pack(pady=5)
        
    
        out_frame = tk.Frame(self.container, bg=self.colors["card"]); out_frame.pack(fill="x", pady=5)
        self.pw_var = tk.StringVar()
        tk.Entry(out_frame, textvariable=self.pw_var, font=("Consolas", 14), bg=self.colors["card"], fg=self.colors["input"], relief="flat", justify="center").pack(fill="x", padx=10, pady=10)
        
     
        tk.Button(self.container, text="COPY", command=lambda: self.copy(), bg=self.colors["card"], fg="white", relief="flat").pack(fill="x", pady=2)
        tk.Button(self.container, text="GENERATE", command=self.generate, font=("Bold", 12), bg="#0e639c", fg="white", relief="flat").pack(fill="x", pady=5)
        
        self.len_var = tk.IntVar(value=16)
        tk.Scale(self.container, from_=8, to=64, variable=self.len_var, bg=self.colors["bg"], fg=self.colors["text"], troughcolor=self.colors["card"]).pack(fill="x")
        
        opts = tk.Frame(self.container, bg=self.colors["bg"]); opts.pack(fill="x")
        self.u = tk.BooleanVar(value=True); self.l = tk.BooleanVar(value=True); self.n = tk.BooleanVar(value=True); self.s = tk.BooleanVar(value=True)
        tk.Checkbutton(opts, "ABC", variable=self.u, bg=self.colors["bg"], fg="white", selectcolor=self.colors["card"]).pack(side="left")
        tk.Checkbutton(opts, "abc", variable=self.l, bg=self.colors["bg"], fg="white", selectcolor=self.colors["card"]).pack(side="left")
        tk.Checkbutton(opts, "123", variable=self.n, bg=self.colors["bg"], fg="white", selectcolor=self.colors["card"]).pack(side="left")
        tk.Checkbutton(opts, "!@#", variable=self.s, bg=self.colors["bg"], fg="white", selectcolor=self.colors["card"]).pack(side="left")

    def generate(self):
        pool = ""
        if self.u.get(): pool += string.ascii_uppercase
        if self.l.get(): pool += string.ascii_lowercase
        if self.n.get(): pool += string.digits
        if self.s.get(): pool += "!@#$%^&*()"
        if not pool: return
        self.pw_var.set(''.join(secrets.choice(pool) for _ in range(self.len_var.get())))

    def copy(self):
        self.root.clipboard_clear(); self.root.clipboard_append(self.pw_var.get()); messagebox.showinfo("Copied", "Done")



class AuditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Module B: Auditor"); self.root.geometry("400x400"); self.root.configure(bg="#1a1a1a")
        tk.Label(root, text="SECURITY AUDITOR", bg="#1a1a1a", fg="#ff9900", font=("Segoe UI", 16, "bold")).pack(pady=10)
        
        self.pw_var = tk.StringVar(); self.pw_var.trace_add("write", self.analyze)
        tk.Entry(root, textvariable=self.pw_var, font=("Consolas", 14), bg="#0d0d0d", fg="white", justify="center").pack(fill="x", padx=20, pady=10)
        
        self.res = tk.Text(root, height=10, bg="#0d0d0d", fg="#00ff00", font=("Consolas", 10)); self.res.pack(fill="both", expand=True, padx=20, pady=10)

    def analyze(self, *args):
        pw = self.pw_var.get(); self.res.delete(1.0, "end")
        if not pw: return
        score = 0
        if len(pw) >= 8: score += 1
        if len(pw) >= 12: score += 1
        if any(c.isupper() for c in pw): score += 1
        if any(c.islower() for c in pw): score += 1
        if any(c.isdigit() for c in pw): score += 1
        if any(c in string.punctuation for c in pw): score += 2
        
        import hashlib
        crack_time = "Instantly"
        if score > 3: crack_time = "Few Hours"
        if score > 5: crack_time = "Centuries"
        
        self.res.insert("end", f"Score: {score}/7\nCrack Time: {crack_time}\n\nRecommendation:\n{'Strong' if score > 5 else 'Add complexity'}")


class EncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Module C: Encryption")
        self.root.geometry("500x450"); self.root.configure(bg="#001f2e")
        
        tk.Label(root, text="ENCRYPTION STATION", bg="#001f2e", fg="#00bfff", font=("Segoe UI", 16, "bold")).pack(pady=10)
        tk.Label(root, text="Symmetric Encryption (Key Required)", bg="#001f2e", fg="#888").pack()

    
        key_frame = tk.Frame(root, bg="#001f2e"); key_frame.pack(fill="x", padx=20, pady=5)
        tk.Label(key_frame, text="Secret Key:", bg="#001f2e", fg="white").pack(side="left")
        self.key_var = tk.StringVar()
        tk.Entry(key_frame, textvariable=self.key_var, show="*", bg="#003f5c", fg="white", relief="flat").pack(side="right", fill="x", expand=True, padx=5)

       
        tk.Label(root, text="Input Data:", bg="#001f2e", fg="white").pack(anchor="w", padx=20)
        self.input_text = tk.Text(root, height=5, bg="#003f5c", fg="white", font=("Consolas", 10), relief="flat")
        self.input_text.pack(fill="x", padx=20, pady=5)

     
        btn_frame = tk.Frame(root, bg="#001f2e"); btn_frame.pack(fill="x", padx=20)
        tk.Button(btn_frame, text="LOCK (Encrypt)", command=self.encrypt, bg="#00bfff", fg="black", relief="flat").pack(side="left", expand=True, fill="x", padx=2)
        tk.Button(btn_frame, text="UNLOCK (Decrypt)", command=self.decrypt, bg="#008fb3", fg="white", relief="flat").pack(side="right", expand=True, fill="x", padx=2)

       
        tk.Label(root, text="Output:", bg="#001f2e", fg="white").pack(anchor="w", padx=20, pady=(10,0))
        self.output_text = tk.Text(root, height=5, bg="#002b3d", fg="#00ff00", font=("Consolas", 10), relief="flat")
        self.output_text.pack(fill="x", padx=20, pady=5)
        
     
        tk.Button(root, text="Copy Output", command=lambda: self.copy(), bg="#001f2e", fg="#00bfff").pack()

    def get_key_bytes(self):
       
        return hashlib.sha256(self.key_var.get().encode()).digest()

    def encrypt(self):
        text = self.input_text.get("1.0", "end").strip()
        key = self.get_key_bytes()
        if not text or not self.key_var.get():
            messagebox.showwarning("Error", "Need text and a key!"); return
        
     
        cipher_bytes = bytearray()
        for i, c in enumerate(text.encode()):
            cipher_bytes.append(c ^ key[i % len(key)])
        
        encoded = base64.b64encode(cipher_bytes).decode()
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", encoded)

    def decrypt(self):
        text = self.input_text.get("1.0", "end").strip()
        key = self.get_key_bytes()
        if not text or not self.key_var.get():
            messagebox.showwarning("Error", "Need text and a key!"); return
        
        try:
            decoded_bytes = base64.b64decode(text)
            plain_bytes = bytearray()
            for i, c in enumerate(decoded_bytes):
                plain_bytes.append(c ^ key[i % len(key)])
            
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", plain_bytes.decode())
        except Exception:
            messagebox.showerror("Error", "Decryption Failed. Wrong Key or Corrupt Data.")

    def copy(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.output_text.get("1.0", "end"))



class StegoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Module D: Steganography")
        self.root.geometry("500x500"); self.root.configure(bg="#1a001a")
        
        tk.Label(root, text="INVISIBLE INK", bg="#1a001a", fg="#ff00ff", font=("Segoe UI", 16, "bold")).pack(pady=10)
        tk.Label(root, text="Hide messages using Zero-Width Characters", bg="#1a001a", fg="#888").pack()

       
        hide_frame = tk.LabelFrame(root, text="Hide Message", bg="#1a001a", fg="white", font=("Bold", 10))
        hide_frame.pack(fill="x", padx=20, pady=10)
        
        tk.Label(hide_frame, text="Public Text (Cover):", bg="#1a001a", fg="white").pack(anchor="w", padx=5)
        self.cover_text = tk.Entry(hide_frame, bg="#330033", fg="white", font=("Arial", 12), relief="flat")
        self.cover_text.insert(0, "The weather is nice today.") # Default suggestion
        self.cover_text.pack(fill="x", padx=5, pady=2)

        tk.Label(hide_frame, text="Secret Message:", bg="#1a001a", fg="white").pack(anchor="w", padx=5)
        self.secret_text = tk.Entry(hide_frame, bg="#330033", fg="#ff00ff", font=("Arial", 12), relief="flat")
        self.secret_text.pack(fill="x", padx=5, pady=2)

        tk.Button(hide_frame, text="EMBED SECRET", command=self.hide, bg="#ff00ff", fg="black", relief="flat").pack(fill="x", padx=5, pady=5)
        
       
        reveal_frame = tk.LabelFrame(root, text="Reveal Message", bg="#1a001a", fg="white", font=("Bold", 10))
        reveal_frame.pack(fill="x", padx=20, pady=10)

        tk.Label(reveal_frame, text="Paste Text (with hidden data):", bg="#1a001a", fg="white").pack(anchor="w", padx=5)
        self.stego_input = tk.Text(reveal_frame, height=3, bg="#330033", fg="white", font=("Arial", 12), relief="flat")
        self.stego_input.pack(fill="x", padx=5, pady=2)
        
        tk.Button(reveal_frame, text="REVEAL SECRET", command=self.reveal, bg="#990099", fg="white", relief="flat").pack(fill="x", padx=5, pady=5)
        
       
        tk.Label(root, text="Result:", bg="#1a001a", fg="#888").pack(anchor="w", padx=20)
        self.result_text = tk.Text(root, height=3, bg="#0d000d", fg="#00ff00", font=("Consolas", 12), relief="flat")
        self.result_text.pack(fill="x", padx=20, pady=5)
        tk.Button(root, text="Copy Result", command=lambda: self.copy(), bg="#1a001a", fg="#ff00ff").pack()

    def hide(self):
        cover = self.cover_text.get()
        secret = self.secret_text.get()
        if not cover or not secret:
            messagebox.showwarning("Error", "Need cover text and secret"); return

        binary_secret = ''.join(format(ord(x), 'b') for x in secret)
        
       
        zws = '\u200B' 
        zwnj = '\u200C' 
        zwj = '\u200D' 
        
        hidden_binary = ""
        for bit in binary_secret:
            if bit == '0': hidden_binary += zws
            else: hidden_binary += zwnj
            
       
        mid = len(cover) // 2
        stego_text = cover[:mid] + zwj + hidden_binary + zwj + cover[mid:]
        
        self.result_text.delete("1.0", "end")
        self.result_text.insert("1.0", stego_text)
        messagebox.showinfo("Done", "Secret embedded! Copy the result. It looks identical to the original.")

    def reveal(self):
        text = self.stego_input.get("1.0", "end")
        
     
        bits = ""
        found_start = False
        for char in text:
            if char == '\u200D': # Delimiter
                if found_start: break # Stop at second delimiter
                found_start = True
                continue
            
            if found_start:
                if char == '\u200B': bits += "0"
                elif char == '\u200C': bits += "1"
        
       
        try:
           
            chars = []
            for i in range(0, len(bits), 7): 
                byte = bits[i:i+7]
                if len(byte) == 7:
                    chars.append(chr(int(byte, 2)))
            
            result = "".join(chars)
            self.result_text.delete("1.0", "end")
            if result:
                self.result_text.insert("1.0", f"FOUND: {result}")
            else:
                self.result_text.insert("1.0", "No hidden message found.")
        except Exception as e:
            self.result_text.insert("1.0", "Error decoding hidden data.")

    def copy(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.result_text.get("1.0", "end"))


if __name__ == "__main__":
    root = tk.Tk()
    app = ExecutiveTerminal(root)
    root.mainloop()