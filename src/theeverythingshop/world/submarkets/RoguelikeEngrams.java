package theeverythingshop.world.submarkets;

/** RogueLike Shop: Exiled Sector engrams. */
public class RoguelikeEngrams extends RoguelikeShopBase {

    @Override
    protected Kind kind() {
        return Kind.ENGRAMS;
    }

    @Override
    protected String getDisplayName() {
        return "Engrams";
    }
}