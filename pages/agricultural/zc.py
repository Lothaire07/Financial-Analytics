from components.page_utils import render_commodity_page

def render():
    corn_description = """
    <style>
        .corn-hover {
          display: inline-block;
          transition: color 0.3s, text-shadow 0.3s;
          font-weight: bold;
          color: inherit;
        }

        .corn-hover:hover {
          color: yellow;
          text-shadow: 0 0 10px rgba(255, 223, 0, 0.8), 0 0 20px rgba(255, 223, 0, 0.6);
        }  
    </style>

    <div>
      <p>
        <span class="corn-hover">Corn</span> is one of the most widely produced and traded agricultural commodities in the world, serving as a vital input for both food and energy markets:
        <ul>
          <li>Used as livestock feed, human food, and industrial starch</li>
          <li>A major component in biofuel production, especially ethanol</li>
          <li>Traded globally, with the U.S., Brazil, and Argentina as top exporters</li>
        </ul>
        Corn prices reflect both agricultural fundamentals and broader macroeconomic forces.  
        They are influenced by:
        <ul>
          <li>Weather patterns and crop yields (e.g., droughts or floods)</li>
          <li>Global demand for feed, food, and fuel</li>
          <li>Government policies, subsidies, and biofuel mandates</li>
          <li>Export competition and trade agreements</li>
        </ul>
        As a benchmark agricultural future, corn is a key indicator of global food supply and demand dynamics — closely monitored by traders, economists, and policymakers alike.
      </p>
    </div>
    """

    render_commodity_page(
        page_title="Corn CBOT Analytics (ZC)",
        ticker="ZC=F",
        description_html=corn_description,
        image_path="images/julia-vivcharyk-AWbf-SPYJNE-unsplash.jpg",
        image_caption="Corn",
        line_color="yellow"
    )