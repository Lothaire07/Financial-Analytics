from components.page_utils import render_commodity_page

def render():
    copper_description = """
    <style>
        .copper-hover {
            display: inline-block;
            transition: color 0.3s, text-shadow 0.3s;
            font-weight: bold;
            color: inherit;
        }

        .copper-hover:hover {
            color: #b87333;
            text-shadow: 0 0 10px rgba(184, 115, 51, 0.8), 0 0 20px rgba(184, 115, 51, 0.6);
        }
    </style>

    <div>
      <p>
        <span class="copper-hover">Copper</span> is a critical industrial metal valued for both its physical properties and its economic significance:
        <ul>
          <li>Highly conductive, making it essential for electrical wiring and electronics</li>
          <li>Ductile and malleable, used in construction and manufacturing</li>
          <li>Resistant to corrosion, especially in plumbing and renewable energy systems</li>
        </ul>
        Copper plays a vital role in the global transition to clean energy and electrification.  
        Its price is influenced by:
        <ul>
          <li>Global industrial activity and construction demand</li>
          <li>Supply levels from top producers like Chile and Peru</li>
          <li>Trends in renewable energy infrastructure (e.g., EVs, solar)</li>
          <li>Macroeconomic indicators and inventories</li>
        </ul>
        Often called “Dr. Copper” for its ability to reflect economic health, copper remains a fundamental indicator of growth and industrial momentum worldwide.
      </p>
    </div>
    """

    render_commodity_page(
        page_title="Copper COMEX Analytics (HG)",
        ticker="HG=F",
        description_html=copper_description,
        image_path="images/calitore-xPVUA7Jrl58-unsplash.jpg",
        image_caption="Copper Wires",
        line_color="darkorange"
    )