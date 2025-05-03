from components.page_utils import render_commodity_page

def render():
    silver_description = """
    <style>
        .silver-hover {
            display: inline-block;
            transition: color 0.3s, text-shadow 0.3s;
            font-weight: bold;
            color: inherit;
        }

        .silver-hover:hover {
            color: silver;
            text-shadow: 0 0 10px rgba(192, 192, 192, 0.8), 0 0 20px rgba(192, 192, 192, 0.6);
        }
    </style>

    <div>
      <p>
        <span class="silver-hover">Silver</span> is a precious and industrial metal with unique dual-use value in both economic and technological domains:
        <ul>
          <li>The best natural electrical conductor, used in electronics, batteries, and solar panels</li>
          <li>Historically used as currency and store of value, often seen as "Gold’s cousin"</li>
          <li>Highly reflective and antimicrobial, with applications in medicine and optics</li>
        </ul>
        Silver is both a financial asset and a key industrial component.  
        Its price is influenced by:
        <ul>
          <li>Global demand in electronics and green tech (solar, EVs)</li>
          <li>Investment demand (coins, ETFs, futures)</li>
          <li>Inflation and interest rate expectations</li>
          <li>Correlation with gold and other commodities</li>
        </ul>
        As both a hedge and a growth metal, silver sits at the crossroads of finance and industry — volatile, but strategically significant.
      </p>
    </div>
    """

    render_commodity_page(
        page_title="Silver COMEX Analytics (SI)",
        ticker="SI=F",
        description_html=silver_description,
        image_path="images/scottsdale-mint-M6f-OZK0N6w-unsplash.jpg",
        image_caption="Silver Coins",
        line_color="silver"
    )