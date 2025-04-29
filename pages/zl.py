from components.page_utils import render_commodity_page

soybean_oil_description = """
<style>
    .soybean-oil-hover {
      display: inline-block;
      transition: color 0.3s, text-shadow 0.3s;
      font-weight: bold;
      color: inherit;
    }

    .soybean-oil-hover:hover {
      color: #DAA520;
      text-shadow: 0 0 10px rgba(218, 165, 32, 0.8), 0 0 20px rgba(218, 165, 32, 0.6);
    }  
</style>

<div>
  <p>
    <span class="soybean-oil-hover">Soybean Oil</span> is a key product derived from crushed soybeans, essential in food production, industrial use, and renewable energy:
    <ul>
      <li>Widely used in cooking oils, margarine, and processed foods</li>
      <li>A critical feedstock for biodiesel production in the U.S. and beyond</li>
      <li>Influenced by both agricultural yields and energy market dynamics</li>
    </ul>
    The price of soybean oil reflects a combination of agricultural and energy sector forces.  
    It is influenced by:
    <ul>
      <li>Crop yields and global soybean supplies</li>
      <li>Biodiesel demand and government renewable energy policies</li>
      <li>Prices of competing vegetable oils (e.g., palm oil, canola oil)</li>
      <li>Global trade relations and tariffs on agricultural products</li>
    </ul>
    As a commodity linking agriculture and energy, soybean oil occupies a strategic position in both food and fuel markets worldwide.
  </p>
</div>
"""

render_commodity_page(
    page_title="Soybean Oil CBOT Analytics (ZL)",
    ticker="ZL=F",
    description_html=soybean_oil_description,
    image_path="images/susan-wilkinson-ReiMJUT19uI-unsplash.jpg",  # Remplace par ton chemin réel pour l'huile
    image_caption="Soybean Oil",
    line_color="#DAA520"  # Doré (Goldenrod)
)