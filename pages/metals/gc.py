from components.kpi import sma
from components.page_utils import render_commodity_page

def render():
    gold_description = """
    <style>
        .gold-hover {
          display: inline-block;
          transition: color 0.3s, text-shadow 0.3s;
          font-weight: bold;
          color: inherit;
        }

        .gold-hover:hover {
          color: goldenrod;
          text-shadow: 0 0 10px rgba(255, 215, 0, 0.8), 0 0 20px rgba(255, 215, 0, 0.6);
        }  

    </style>

    <div>
      <p>
        <span class="gold-hover">Gold</span> is a precious metal with a unique blend of physical and economic properties:
        <ul>
          <li>Chemically stable and resistant to corrosion</li>
          <li>Highly conductive, used in electronics and industry</li>
          <li>Historically valued as a store of wealth and a symbol of status</li>
        </ul>
        In the global economy, gold plays the role of a “safe haven” asset, attracting investors in times of uncertainty or inflation.  
        Its price is influenced by:
        <ul>
          <li>Interest rates</li>
          <li>Inflation expectations</li>
          <li>Geopolitical tensions</li>
          <li>Central bank reserves</li>
        </ul>
        Whether seen as a hedge against currency devaluation or a speculative instrument, gold remains one of the most traded and watched commodities in the world.
      </p>
    </div>
    """

    render_commodity_page(
        page_title="Gold COMEX Analytics (GC)",
        ticker="GC=F",
        description_html=gold_description,
        image_path="images/scottsdale-mint-2jjc94apOCY-unsplash.jpg",
        image_caption="Gold Ingot",
        line_color="gold"
    )

    sma("GC=F")