package theeverythingshop.world.submarkets;

/** RogueLike Shop: Exiled Sector star charts. */
public class RoguelikeStarCharts extends RoguelikeShopBase {

    @Override
    protected Kind kind() {
        return Kind.STAR_CHARTS;
    }

    @Override
    protected String getDisplayName() {
        return "Star\nCharts";
    }
}