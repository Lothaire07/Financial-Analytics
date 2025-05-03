from components.page_utils import render_commodity_page

def render():
    platinum_description = """
    <style>
        .platinum-hover {
          display: inline-block;
          transition: color 0.3s, text-shadow 0.3s;
          font-weight: bold;
          color: inherit;
        }

        .platinum-hover:hover {
          color: #E5E4E2;
          text-shadow: 0 0 10px rgba(229, 228, 226, 0.8), 0 0 20px rgba(229, 228, 226, 0.6);
        }  
    </style>

    <div>
      <p>
        <span class="platinum-hover">Platinum</span> is a rare and highly valuable precious metal with significant industrial and investment demand:
        <ul>
          <li>Extensively used in automotive catalytic converters to reduce emissions</li>
          <li>Valued for jewelry due to its strength, rarity, and bright finish</li>
          <li>Essential in chemical, petroleum, and medical applications</li>
        </ul>
        Platinum prices are driven by a complex interplay of industrial utility and investment demand.  
        They are influenced by:
        <ul>
          <li>Automotive production trends and emission standards</li>
          <li>Jewelry demand, particularly in Asia and North America</li>
          <li>Mining output, with South Africa being the largest producer</li>
          <li>Investment flows into ETFs and precious metal portfolios</li>
        </ul>
        As a dual-role metal—industrial and precious—platinum holds a unique position, offering a barometer for both economic health and market sentiment.
      </p>
    </div>
    """

    render_commodity_page(
        page_title="Platinum NYMEX Analytics (PL)",
        ticker="PL=F",
        description_html=platinum_description,
        image_path="images/chris-dreyer-lbsGPq_9daU-unsplash.jpg",  # Remplacer par ton image réelle du platine
        image_caption="Platinum Cubes",
        line_color="#E5E4E2"  # Gris platine clair
    )