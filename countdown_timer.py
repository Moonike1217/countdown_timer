import tkinter as tk
from tkinter import messagebox

class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("倒计时器")
        self.root.geometry("200x150")
        self.root.resizable(False, False)
        
        # 初始化时间
        self.default_time = 15
        self.remaining_time = self.default_time
        self.running = False
        self.timer_id = None  # 用于存储after的返回值
        
        # 显示倒计时
        self.label = tk.Label(root, text=self.format_time(self.remaining_time), font=("Arial", 30))
        self.label.pack(pady=20)
        
        # 按钮容器
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=5)
        
        # 重新计时按钮
        self.reset_button = tk.Button(self.button_frame, text="重新计时", command=self.reset_timer)
        self.reset_button.pack(side=tk.LEFT, padx=10)
        
        # 置于最顶按钮
        self.top_button = tk.Button(self.button_frame, text="置于最顶", command=self.set_topmost)
        self.top_button.pack(side=tk.LEFT, padx=10)
        
        # 开始倒计时
        self.start_timer()

    def format_time(self, seconds):
        """格式化时间为 MM:SS"""
        mins = seconds // 60
        secs = seconds % 60
        return f"{mins:02}:{secs:02}"

    def update_timer(self):
        """更新倒计时显示"""
        if self.remaining_time > 0:
            self.remaining_time -= 1
            self.label.config(text=self.format_time(self.remaining_time))
            self.timer_id = self.root.after(1000, self.update_timer)  # 存储返回值
        else:
            self.running = False
            # messagebox.showinfo("提示", "倒计时结束！")
    
    def start_timer(self):
        """启动倒计时"""
        if not self.running:
            self.running = True
            self.update_timer()

    def reset_timer(self):
        """重置倒计时"""
        if self.timer_id is not None:
            self.root.after_cancel(self.timer_id)  # 取消之前的调度
        self.remaining_time = self.default_time
        self.label.config(text=self.format_time(self.remaining_time))
        self.running = False
        self.start_timer()

    def set_topmost(self):
        """将窗口置于最顶层"""
        self.root.attributes("-topmost", True)
        self.root.after(200, lambda: self.root.attributes("-topmost", False))  # 恢复原状

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownTimer(root)
    root.mainloop()
