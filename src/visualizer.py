import matplotlib.pyplot as plt
import os
 
def plot_monthly(monthly, output_dir='output'):
    os.makedirs(output_dir, exist_ok=True)
    fig, ax = plt.subplots(figsize=(10, 5))
    monthly.plot(kind='bar', ax=ax, color='#1A56DB')
    ax.set_title('Receita Mensal', fontsize=14, fontweight='bold')
    ax.set_xlabel('Mês')
    ax.set_ylabel('Receita (R$)')
    plt.tight_layout()
    path = os.path.join(output_dir, 'monthly_revenue.png')
    plt.savefig(path, dpi=150)
    plt.close()
    return path
 
def plot_category(by_category, output_dir='output'):
    fig, ax = plt.subplots(figsize=(7, 7))
    by_category.plot(kind='pie', ax=ax, autopct='%1.1f%%')
    ax.set_title('Receita por Categoria', fontsize=14, fontweight='bold')
    ax.set_ylabel('')
    plt.tight_layout()
    path = os.path.join(output_dir, 'category_pie.png')
    plt.savefig(path, dpi=150)
    plt.close()
    return path
