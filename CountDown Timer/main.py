from tkinter import *
import tkinter as tk

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.pack()
        self.createWidgets()
        
        self.master.geometry("400x350")
        self.master.configure(bg='#2c3e50')
        self.master.resizable(False, False)
        
        self._alarm_id = None
        self._paused = False
        self._starttime = 0
        self._remaining = 0
        self._is_running = False
    
    def createWidgets(self):
        # Title
        title = Label(self, text="Countdown Timer", font=("Helvetica", 20, "bold"),
                      bg='#2c3e50', fg='white')
        title.pack(pady=10)
        
        # Time display (MM:SS format)
        self.labelvariable = StringVar()
        self.labelvariable.set("00:00")
        self.thelabel = Label(self, textvariable=self.labelvariable, 
                              font=('Helvetica', 60, 'bold'),
                              bg='#2c3e50', fg='#2ecc71')
        self.thelabel.pack(pady=20)
        
        # Input frame
        input_frame = Frame(self, bg='#2c3e50')
        input_frame.pack(pady=10)
        
        Label(input_frame, text="Enter seconds:", font=('Helvetica', 12),
              bg='#2c3e50', fg='white').pack(side=LEFT, padx=5)
        
        self.input_time = tk.Entry(input_frame, width=10, font=('Calibri', 14))
        self.input_time.insert(0, "60")
        self.input_time.pack(side=LEFT, padx=5)
        self.input_time.bind("<Return>", lambda e: self.startTime())
        
        # Preset buttons (10s, 30s, 60s)
        preset_frame = Frame(self, bg='#2c3e50')
        preset_frame.pack(pady=5)
        
        Label(preset_frame, text="Presets:", font=('Helvetica', 10),
              bg='#2c3e50', fg='white').pack(side=LEFT, padx=5)
        
        Button(preset_frame, text="10s", font=('Helvetica', 10),
               command=lambda: self.set_preset(10),
               bg='#3498db', fg='white', width=5).pack(side=LEFT, padx=2)
        
        Button(preset_frame, text="30s", font=('Helvetica', 10),
               command=lambda: self.set_preset(30),
               bg='#3498db', fg='white', width=5).pack(side=LEFT, padx=2)
        
        Button(preset_frame, text="60s", font=('Helvetica', 10),
               command=lambda: self.set_preset(60),
               bg='#3498db', fg='white', width=5).pack(side=LEFT, padx=2)
        
        # Button frame
        self.someFrame = Frame(self, bg='#2c3e50')
        self.someFrame.pack(pady=15)
        
        self.startButton = Button(self.someFrame, text="Start", font=('Helvetica', 12),
                                  bg='#2ecc71', fg='white', command=self.startTime, width=10)
        self.startButton.pack(side=LEFT, padx=5)
        
        self.pauseButton = Button(self.someFrame, text="Pause", font=('Helvetica', 12),
                                  bg='#f1c40f', fg='white', command=self.togglePause, width=10)
        self.pauseButton.pack(side=LEFT, padx=5)
        
        self.resetButton = Button(self.someFrame, text="Reset", font=('Helvetica', 12),
                                  bg='#e74c3c', fg='white', command=self.resetTime, width=10)
        self.resetButton.pack(side=LEFT, padx=5)
        
        self.closeButton = Button(self.someFrame, text="Close", font=('Helvetica', 12),
                                  bg='#95a5a6', fg='white', command=self.closeApp, width=10)
        self.closeButton.pack(side=LEFT, padx=5)
        
        # Progress bar
        self.progress_canvas = Canvas(self, width=300, height=20, bg='#34495e', highlightthickness=0)
        self.progress_canvas.pack(pady=15)
        self.progress_bar = self.progress_canvas.create_rectangle(0, 0, 0, 20, fill='#2ecc71')
    
    def set_preset(self, seconds):
        """Set preset time"""
        self.input_time.delete(0, END)
        self.input_time.insert(0, str(seconds))
    
    def update_progress(self, current, total):
        """Update the progress bar"""
        if total > 0:
            percentage = (current / total) * 300
            self.progress_canvas.coords(self.progress_bar, 0, 0, percentage, 20)
            
            # Change color based on remaining time
            if current / total < 0.2:
                self.progress_canvas.itemconfig(self.progress_bar, fill='#e74c3c')  # Red
            elif current / total < 0.5:
                self.progress_canvas.itemconfig(self.progress_bar, fill='#f1c40f')  # Yellow
            else:
                self.progress_canvas.itemconfig(self.progress_bar, fill='#2ecc71')  # Green
    
    def format_time(self, seconds):
        """Convert seconds to MM:SS format"""
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02d}:{seconds:02d}"
    
    def togglePause(self):
        """Toggle between Pause and Resume"""
        if self._paused:
            # Currently paused, so resume
            self.resumeTime()
        else:
            # Currently running, so pause
            self.pauseTime()
    
    def pauseTime(self):
        """Pause the timer"""
        if self._is_running and not self._paused:
            self._paused = True
            self.pauseButton.config(text="Resume", bg='#e67e22')
    
    def resumeTime(self):
        """Resume the timer"""
        if self._is_running and self._paused:
            self._paused = False
            self.pauseButton.config(text="Pause", bg='#f1c40f')
            # The countdown loop will automatically continue
            # because it checks self._paused in the loop
    
    def startTime(self):
        """Start the timer"""
        if self._is_running:
            return
        
        try:
            self._starttime = int(self.input_time.get())
            if self._starttime <= 0:
                return
        except ValueError:
            return
        
        self._remaining = self._starttime
        self._is_running = True
        self._paused = False
        self.startButton.config(text="Running", bg='#27ae60')
        self.pauseButton.config(text="Pause", bg='#f1c40f')
        self.countdown(self._remaining)
    
    def resetTime(self):
        """Reset the timer to zero"""
        if self._alarm_id is not None:
            self.master.after_cancel(self._alarm_id)
            self._alarm_id = None
        
        self._is_running = False
        self._paused = False
        self._remaining = 0
        self.labelvariable.set("00:00")
        self.progress_canvas.coords(self.progress_bar, 0, 0, 0, 20)
        self.progress_canvas.itemconfig(self.progress_bar, fill='#2ecc71')
        self.startButton.config(text="Start", bg='#2ecc71')
        self.pauseButton.config(text="Pause", bg='#f1c40f')
    
    def closeApp(self):
        """Close the application"""
        if self._alarm_id is not None:
            self.master.after_cancel(self._alarm_id)
        self.master.destroy()
    
    def countdown(self, timeInSeconds):
        """Countdown timer logic"""
        if timeInSeconds <= 0:
            self.labelvariable.set("00:00")
            self._is_running = False
            self.startButton.config(text="Start", bg='#2ecc71')
            self.pauseButton.config(text="Pause", bg='#f1c40f')
            self.progress_canvas.coords(self.progress_bar, 0, 0, 0, 20)
            return
        
        if self._paused:
            # If paused, check again in 500ms
            self._alarm_id = self.master.after(500, self.countdown, timeInSeconds)
            return
        
        # Update display
        self._remaining = timeInSeconds
        self.labelvariable.set(self.format_time(timeInSeconds))
        self.update_progress(timeInSeconds, self._starttime)
        
        # Continue countdown
        self._alarm_id = self.master.after(1000, self.countdown, timeInSeconds - 1)

if __name__ == '__main__':
    root = Tk()
    root.title("Countdown Timer")
    root.configure(bg='#2c3e50')
    app = Application(root)
    root.mainloop()