from components.page_utils import render_commodity_page

def render():
    oats_description = """
    <style>
        .oats-hover {
          display: inline-block;
          transition: color 0.3s, text-shadow 0.3s;
          font-weight: bold;
          color: inherit;
        }

        .oats-hover:hover {
          color: #D2B48C;
          text-shadow: 0 0 10px rgba(210, 180, 140, 0.8), 0 0 20px rgba(210, 180, 140, 0.6);
        }  
    </style>

    <div>
      <p>
        <span class="oats-hover">Oats</span> are a versatile cereal grain valued for both human consumption and livestock feed, with increasing importance in health-focused diets:
        <ul>
          <li>Consumed globally in oatmeal, cereals, and bakery products</li>
          <li>Used as a feed crop for horses, cattle, and other livestock</li>
          <li>Rich in fiber and nutrients, aligning with wellness trends</li>
        </ul>
        Oats prices reflect agricultural productivity and shifting dietary preferences.  
        They are influenced by:
        <ul>
          <li>Weather conditions affecting northern U.S. and Canadian crops</li>
          <li>Demand for health-oriented food products</li>
          <li>Livestock feed demand dynamics</li>
          <li>Competition from alternative grains like wheat and barley</li>
        </ul>
        As both a nutritional staple and an essential feed crop, oats remain a resilient commodity closely linked to consumer health and agricultural sustainability trends.
      </p>
    </div>
    """

    render_commodity_page(
        page_title="Oats CBOT Analytics (ZO)",
        ticker="ZO=F",
        description_html=oats_description,
        image_path="images/raw-barley-grain-old-dark-background.jpg",
        # Remplace par ton vrai chemin d'image pour l'avoine
        image_caption="Oats",
        line_color="#D2B48C"  # Tan (beige clair, couleur de l'avoine)
    )