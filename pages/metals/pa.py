from components.page_utils import render_commodity_page

def render():
    palladium_description = """
    <style>
        .palladium-hover {
          display: inline-block;
          transition: color 0.3s, text-shadow 0.3s;
          font-weight: bold;
          color: inherit;
        }

        .palladium-hover:hover {
          color: #C0C0C0;
          text-shadow: 0 0 10px rgba(192, 192, 192, 0.8), 0 0 20px rgba(192, 192, 192, 0.6);
        }  
    </style>

    <div>
      <p>
        <span class="palladium-hover">Palladium</span> is a rare precious metal with critical importance in industrial manufacturing, especially within the automotive sector:
        <ul>
          <li>Used predominantly in catalytic converters to reduce harmful vehicle emissions</li>
          <li>Applied in electronics, dentistry, and hydrogen purification technologies</li>
          <li>Considered an alternative to platinum in various industrial uses</li>
        </ul>
        Palladium prices are highly sensitive to shifts in automotive and industrial demand.  
        They are influenced by:
        <ul>
          <li>Automotive production cycles and stricter emission regulations</li>
          <li>Mining output, heavily concentrated in Russia and South Africa</li>
          <li>Supply chain disruptions and geopolitical risks</li>
          <li>Investment activity in precious metals markets</li>
        </ul>
        As a strategic metal at the intersection of technology, energy, and industry, palladium plays an essential role in shaping future mobility and clean energy solutions.
      </p>
    </div>
    """

    render_commodity_page(
        page_title="Palladium NYMEX Analytics (PA)",
        ticker="PA=F",
        description_html=palladium_description,
        image_path="images/zhenzhong-liu-DbL4mjIl_rk-unsplash.jpg",  # Remplace par ton chemin réel pour l'image du palladium
        image_caption="Palladium Ore",
        line_color="#C0C0C0"  # Argenté léger (Silver)
    )