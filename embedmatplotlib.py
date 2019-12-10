from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt


irsData ={'Contact Method':['Phone Call: Landline','Phone',
                            'Phone Call: Mobile/Cell','Internet/E-mail',
                            'Mobile: Text/Email/ IM', 'Mail','I Initiated Contact',
                            'Unknown', 'Internet Web Site','In Person',
                            'Internet (Other)','Wireless', 'Fax', 'Print', 'TV/Radio'],
          'Total': [10044, 2769, 2543, 226, 58, 57, 36, 34, 30, 16, 11, 7, 3, 3, 1]}
df1 = DataFrame(irsData, columns = ['Contact Method', 'Total'])
df1 = df1[['Contact Method', 'Total']].groupby('Contact Method').sum()
root = tk.Tk()
root.title('Contact Method')
root.geometry("800x800")
figure1 = plt.Figure(figsize=(6, 4), dpi=100)
ax1 = figure1.add_subplot(111)
ax1.set_xlabel('Contact Methods')
bar1 = FigureCanvasTkAgg(figure1, root)
bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df1.plot(kind='bar', legend=True, ax=ax1)
ax1.set_title('Contact Method Vs. Total')

root.mainloop()



