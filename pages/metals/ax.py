from components.page_utils import render_commodity_page

def render():
    aluminum_description = """
            <style>
                .aluminum-hover {
                  display: inline-block;
                  transition: color 0.3s, text-shadow 0.3s;
                  font-weight: bold;
                  color: inherit;
                }

                .aluminum-hover:hover {
                  color: lightblue;
                  text-shadow: 0 0 10px rgba(153, 233, 255, 0.8), 0 0 20px rgba(153, 233, 255, 0.6);
                }  

            </style>

        </style>

        <div>
          <p>
            <span class="aluminum-hover">Aluminum</span> is a lightweight, highly versatile metal known for its physical and economic utility:
            <ul>
              <li>Exceptionally light and strong, ideal for transportation and aerospace</li>
              <li>Resistant to corrosion due to its natural oxide layer</li>
              <li>Abundant and easily recyclable, making it key in sustainable industries</li>
            </ul>
            As a critical industrial metal, aluminum demand is tied closely to global infrastructure and economic cycles.  
            Its price is influenced by:
            <ul>
              <li>Global manufacturing activity</li>
              <li>Energy costs (notably electricity for smelting)</li>
              <li>Supply from major producers like China and Russia</li>
              <li>Trade policies and tariffs</li>
            </ul>
            Valued for both its industrial and environmental role, aluminum continues to shape modern economies through innovation and scale.
          </p>
        </div>
            """

    render_commodity_page(
        page_title="Aluminum COMEX Analytics (ALI)",
        ticker="ALI=F",
        description_html=aluminum_description,
        image_path="images/s-tsuchiya-0o5F-A-FsYw-unsplash.jpg",
        image_caption="Aluminum Structure",
        line_color="lightblue"
    )