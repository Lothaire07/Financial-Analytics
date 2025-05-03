from components.page_utils import render_commodity_page

def render():
    soybean_description = """
    <style>
        .soy-hover {
          display: inline-block;
          transition: color 0.3s, text-shadow 0.3s;
          font-weight: bold;
          color: inherit;
        }

        .soy-hover:hover {
          color: #A0522D;
          text-shadow: 0 0 10px rgba(160, 82, 45, 0.8), 0 0 20px rgba(160, 82, 45, 0.6);
        }  
    </style>

    <div>
      <p>
        <span class="soy-hover">Soybeans</span> are a globally important oilseed crop, playing a central role in food, animal feed, and industrial applications:
        <ul>
          <li>Crushed into soybean meal for livestock and poultry feed</li>
          <li>Processed into soybean oil, used in food and biofuel industries</li>
          <li>Exported massively by the U.S., Brazil, and Argentina</li>
        </ul>
        Soybeans are not only a key food commodity but also a strategic trade asset in global agriculture.  
        Their price is influenced by:
        <ul>
          <li>Weather conditions across key producing regions</li>
          <li>Global demand for protein (feed and food)</li>
          <li>Biofuel policies affecting soybean oil usage</li>
          <li>Geopolitical factors and trade relations (notably U.S.–China)</li>
        </ul>
        As one of the "big three" crops in agricultural futures (alongside corn and wheat), soybeans are actively traded and highly sensitive to shifts in global supply chains and consumption trends.
      </p>
    </div>
    """

    render_commodity_page(
        page_title="Soybean CBOT Analytics (ZS)",
        ticker="ZS=F",
        description_html=soybean_description,
        image_path="images/soy-bean.jpg",
        image_caption="Soybeans",
        line_color="#A0522D"
    )