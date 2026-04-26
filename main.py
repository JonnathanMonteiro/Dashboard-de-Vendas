from src.loader import load_data
from src.analyzer import get_summary, monthly_revenue, revenue_by_category
from src.visualizer import plot_monthly, plot_category
 
def main():
    df = load_data('data/sales.csv')
    summary = get_summary(df)
    print('\n=== RESUMO DE VENDAS ===')
    for key, value in summary.items():
        print(f'{key}: {value}')
    plot_monthly(monthly_revenue(df))
    plot_category(revenue_by_category(df))
    print('Gráficos salvos na pasta output/')
if __name__ == '__main__':
    main()
