

[[module CSS]]
#edit-page-form .buttons.alignleft::before {
  content: "Please make sure you understand the warning at the top of the page source before saving your edits!";
  display: block;
  margin-bottom: 1em;
  font-weight: bold;
  color: red;
}

#page-content ul > li {
  margin-top: 0.5em;
  line-height: 1.25em;
}

#page-content ul > li li {
  margin-top: 0.25em;
  list-style: circle;
}
[[/module]]

> This page has a comprehensive list of tags available on the wiki.  For help with actually deciding which tags to use, please refer to the [[[tech-hub-tag | tag guide]]].

When choosing tags for an article, keep in mind that you want to keep the list as short as possible; the goal should be to choose tags that are already being used, rather than create a new one. If staff should determine that a new tag is necessary, they can always retroactively tag articles as necessary. If you would like to suggest a new tag, please do so in the [https://scp-wiki.wikidot.com/forum/c-51015/proposals-and-policy stickied tag suggestion thread].

//For Wiki staff: to update this page, see [[[tag list manifest|]]]//

[[tabview]]
[[tab Top Level]]
++ Top Level

All pages on the wiki should have exactly one top-level tag that determines what kind of page it is.

+++ Fictional works

The following tags are for pages that contain fiction.

* **[https://scpwiki.com/system:page-tags/tag/scp scp]** -- All SCP articles from the main blocks, [https://scp-wiki.wikidot.com/scp-001 001 proposals], [https://scp-wiki.wikidot.com/joke-scps jokes] (-J), [https://scp-wiki.wikidot.com/archived-scps archives] (-ARC), and [https://scp-wiki.wikidot.com/scp-ex explained] (-EX) articles should be tagged with //scp//.
 * //Requires any of category 'object-class'//
 * //Conflicts with 'foundation-format'//
* **[https://scpwiki.com/system:page-tags/tag/goi-format goi-format]** -- The page has been written up from the perspective of a specific Group of Interest, and conforms to the format(s) laid out in that GoI's hub page. GoI Formats should also be tagged with the tag of their GoI, as well as the underscore tag for the GoI format.
 * //Requires any of category 'goi-format'//
* **[https://scpwiki.com/system:page-tags/tag/tale tale]** -- Any fiction that is set in the SCP universe but is not an SCP, GoI Format, site page or supplement.
* **[https://scpwiki.com/system:page-tags/tag/supplement supplement]** -- //supplement// pages are defined as pages which require context from their parent page to understand. These pages should also have their parent page set to their originating article in order to maintain relevance and automatically create breadcrumb navigation. A page should only be tagged as //supplement// if they were created by the original author of the page, or with the original author's permission. Documents that are tributes or parodies should be tagged as //tale// instead, even if they are in the format of a log or transcript.
* **[https://scpwiki.com/system:page-tags/tag/site site]** -- //site// pages are hub pages that document specific Foundation facilities, and provide information such as the objects stored at the site, site history, assigned personnel, etc. A page tagged //site// that is also a hub page e.g. for SCPs contained within that site should also be tagged //hub//.

+++ Information pages

These pages contain information about the site or the writing process.

* **[https://scpwiki.com/system:page-tags/tag/guide guide]** -- These pages are writing guides, helpful hints, or other pages intended to assist site users. Guides are only tagged by staff, or with staff permission. See also //essay//.
* **[https://scpwiki.com/system:page-tags/tag/essay essay]** -- //essay// pages contain useful information on specific topics that may be helpful to authors writing related articles, but are different from a //guide// in that essays are subjective and reflect the author's personal opinion.
* **[https://scpwiki.com/system:page-tags/tag/news news]** -- //news// pages contain news about the SCP Foundation in the broadest sense of the word, ranging from new artwork by fans to recently posted successful articles and everything in between. May also be used for formal announcements by staff (in as far as those aren't done on the main page or in the forum).
* **[https://scpwiki.com/system:page-tags/tag/resource resource]** -- //resource// pages list various aspects of the SCP canon, optionally also adding information regarding them.

+++ User pages

Pages for site members to showcase their body of work.

* **[https://scpwiki.com/system:page-tags/tag/author author]** -- This tag should be used for author profile pages. There should only be a single author profile page for each qualifying site member.
* **[https://scpwiki.com/system:page-tags/tag/artist artist]** -- This tag should, similarly, be used for artist profile pages. If a site member wants more than one artist profile page, they must get staff permission first.
* **[https://scpwiki.com/system:page-tags/tag/artwork artwork]** -- //artwork// pages host Foundation-related artwork created by community members, whether as individual pieces or collections.

+++ Import pages

These pages are designed to be imported onto other pages.

* **[https://scpwiki.com/system:page-tags/tag/component component]** -- A page that is designed to be imported onto other pages via the {{@@[[include]]@@}} syntax in order to add new design, style or functionality.
 * //Conflicts with 'component-backend'//
 * //Superseded by 'theme', and 'more-by'//
* **[https://scpwiki.com/system:page-tags/tag/component-backend component-backend]** -- An 'internal template' page that is designed only to be imported into other //component// or //component-backend// pages, but not used directly by authors.
 * //Conflicts with 'component'//
* **[https://scpwiki.com/system:page-tags/tag/theme theme]** -- Theme pages are templates that modify the general look and feel of a page.
 * //Supersedes 'component'//
* **[https://scpwiki.com/system:page-tags/tag/fragment fragment]** -- A page that is designed to be imported onto a single page, and contains content for that page only. They should be parented to that page. Pages of this type should be in the {{fragment:}} category and are exempt from deletion as long as their parent exists on the wiki. If they are orphaned or their parent is deleted, they are eligible for summary deletion.
* **[https://scpwiki.com/system:page-tags/tag/more-by more-by]** -- A page that lists works by a single author, designed to be imported onto that author's published works on the Wiki. They should be parented to that author's author page, if they have one. Pages of this type should be in the {{more-by:}} category and are exempt from voting. EN recommends that other branches do not translate these pages.
 * //Supersedes 'component'//

+++ Internal pages

Pages created for internal use.

* **[https://scpwiki.com/system:page-tags/tag/forum forum]** -- //forum// pages are those required for internal functioning of Wikidot's forum system. They should only be created by staff.
* **[https://scpwiki.com/system:page-tags/tag/splash splash]** -- //splash// pages are used as 'cover pages' for certain articles. (see: [https://scp-wiki.wikidot.com/SCP-902 SCP-902] >> [https://scp-wiki.wikidot.com/902-warning SCP-902 Warning].)
* **[https://scpwiki.com/system:page-tags/tag/redirect redirect]** -- //redirect// pages are those which redirect the user to a different page. They should only be created by staff or with explicit staff permission.

+++ Other pages

* **[https://scpwiki.com/system:page-tags/tag/admin admin]** -- //admin// pages, as the name suggest, have some sort of official significance. Typically, they represent pages which are required to exist by Wikidot for some form of site functionality. They should only be created by staff.
* **[https://scpwiki.com/system:page-tags/tag/hub hub]** -- //hub// pages are pages with a large number of links to related pages. All of the SCP series pages are //hub// pages, as are the tale index and various other pages around the site. As it is a major page tag, hubs may not have other top-level tags (e.g. //scp// or //tale//), with the exception of //contest// pages. Tale hubs should additionally be tagged with the //_tale-hub// page.
* **[https://scpwiki.com/system:page-tags/tag/workbench workbench]** -- Workbenches are pages created by mods and admins to allow them to monitor certain pages using Wikidot's modules. While you're free to use those same monitors on your //author// page, **please do not create any workbench pages unless you're have permition from an acting team captian or admin**, or have received explicit permission from them to do so.
* **[https://scpwiki.com/system:page-tags/tag/sandbox sandbox]** -- In the very distant past, sandboxes on the main site were allowed. This was before the number of members became so big that the amount of sandboxes would create a total mess on the wiki. **Please note that personal sandboxes are no longer allowed on the main site.** The SCP Sandbox wiki at https://scp-sandbox-3.wikidot.com/ should be used for article drafts. Only staff may authorize new sandboxes on the site.

[[/tab]]
[[tab Major Page Tags]]
++ Major Page Tags

Miscellaneous major page tags that are not top-level tags.

* **[https://scpwiki.com/system:page-tags/tag/joke joke]** -- Pages which are considered 'jokes' or explicitly 'out-of-universe'. Joke pages can be parodies of any page type, and should also be tagged as such a page usually would. See [https://scp-wiki.wikidot.com/joke-scps Joke SCPs] for more information on Joke pages.
* **[https://scpwiki.com/system:page-tags/tag/poetry poetry]** -- Applicable if the page consists significantly of a form of poetry, with elements such as meter and rhyme.
* **[https://scpwiki.com/system:page-tags/tag/archived archived]** -- Pages which have been archived due to having been superseded, obsoleted, or inactivity. These pages should also be moved to the {{archived:}} category so they retain the 'archived page' notice and are locked from edits. See [https://scp-wiki.wikidot.com/archived-scps Archived Pages] for more information on archival.
* **[https://scpwiki.com/system:page-tags/tag/explained explained]** -- [https://scp-wiki.wikidot.com/scp-ex Explained] SCPs are a special sub-type of //scp//, and should be added to -EX articles as appropriate. Explained articles should also be tagged with their standard object class tag, or //esoteric-class// if the format does not specify a standard object class.
 * //Requires 'scp'//
* **[https://scpwiki.com/system:page-tags/tag/001-proposal 001-proposal]** -- This is the tag for the articles proposing a possible [https://scp-wiki.wikidot.com/scp-001 SCP-001] object. SCPs tagged with this tag should also be tagged with their standard object class tag, or //esoteric-class// if applicable.
 * //Often used with 'scp'//
* **[https://scpwiki.com/system:page-tags/tag/_canon-hub _canon-hub]** -- Used for hubs which represent a [https://scp-wiki.wikidot.com/canon-hub canon].
 * //Requires 'hub'//
 * //Supersedes '_tale-hub'//
* **[https://scpwiki.com/system:page-tags/tag/creepypasta creepypasta]** -- //creepypasta// are fiction that are unrelated to the SCP Foundation, and usually take the form of urban myths or campfire stories. Creepypasta is only appropriate for the SCP website if it's an original //creepypasta// by the posting author; we are not a repository for unattributed //creepypasta//.
 * //Requires 'tale'//
* **[https://scpwiki.com/system:page-tags/tag/collaboration collaboration]** -- //collaboration// pages are those pages that are or were open to additions from any member, with the caveat that staff and the original author reserve the right to modify or delete entries found to be subpar, or close entries entirely.
* **[https://scpwiki.com/system:page-tags/tag/co-authored co-authored]** -- //co-authored// pages are the result of two or more authors working together, but are not open to additions from other members (unless otherwise specified).
* **[https://scpwiki.com/system:page-tags/tag/contest contest]** -- //contest// pages are pages created for the purpose of community contests. This should be used in conjunction with //hub// in the case of entry listings, and should not be used on the entries themselves. These contests are only created by staff or with staff permission.
 * //Requires 'hub'//
* **[https://scpwiki.com/system:page-tags/tag/comic comic]** -- For stories that are primarily told via sequential art.
* **[https://scpwiki.com/system:page-tags/tag/required required]** -- //required// pages are guides that are part of the required reading for joining the SCP Wiki.
* **[https://scpwiki.com/system:page-tags/tag/_tale-hub _tale-hub]** -- Utilized in conjunction with the //hub// tag to designate that this hub represents a series that consists mostly or entirely of //tale// articles.
 * //Requires 'hub'//
 * //Superseded by '_canon-hub'//

+++ Supplement pages

Tags that describe the content of a //supplement// page.

* **[https://scpwiki.com/system:page-tags/tag/experiment experiment]** -- This supplement contains primarily experiment logs (see: [https://scp-wiki.wikidot.com/SCP-914 SCP-914] >> [https://scp-wiki.wikidot.com/Experiment-Log-914 Experiment Log 914]). This tag **should not** be used on //scp// pages, even if they have extensive experiment logs.
 * //Requires 'supplement'//
* **[https://scpwiki.com/system:page-tags/tag/exploration exploration]** -- This supplement contains primarily exploration logs. This tag **should not** be used on //scp// pages, even if they have extensive exploration logs.
 * //Requires 'supplement'//
* **[https://scpwiki.com/system:page-tags/tag/incident incident]** -- This supplement contains primarily incident logs or transcripts (see: [https://scp-wiki.wikidot.com/SCP-555 SCP-555] >> [https://scp-wiki.wikidot.com/Incident-Log-555-1 Incident Log 555-1]). This tag **should not** be used on //scp// pages, even if they have extensive incident logs.
 * //Requires 'supplement'//
* **[https://scpwiki.com/system:page-tags/tag/interview interview]** -- This supplement contains primarily interview transcripts (see: [https://scp-wiki.wikidot.com/SCP-277 SCP-277] >> [https://scp-wiki.wikidot.com/277interview Interview 277-A]). This tag **should not** be used on //scp// pages, even if they have extensive interview transcripts.
 * //Requires 'supplement'//

[[/tab]]
[[tab Object Classes]]
++ Object Classes

All SCP articles tagged as scp should also be tagged with the appropriate tag for their object class or esoteric-class if it does not have one, if its object class cannot be determined from the article's contents, or if it has a non-standard object class. Legacy articles that are dual-classed (such as safe/euclid) are tagged with both of their constituent classes; however, as this is no longer allowed, it is only for posterity until all such articles are updated or deleted. The only exception is that articles can be tagged as both neutralized and as the object class they were prior to being neutralized.

[[div class="blockquote"]]
The following applies to all tags in this category:

* Requires 'scp'

[[/div]]

* **[https://scpwiki.com/system:page-tags/tag/safe safe]** -- SCP is Safe.
* **[https://scpwiki.com/system:page-tags/tag/euclid euclid]** -- SCP is Euclid.
* **[https://scpwiki.com/system:page-tags/tag/keter keter]** -- SCP is Keter.
* **[https://scpwiki.com/system:page-tags/tag/thaumiel thaumiel]** -- SCP is Thaumiel.
* **[https://scpwiki.com/system:page-tags/tag/apollyon apollyon]** -- SCP is Apollyon.
* **[https://scpwiki.com/system:page-tags/tag/archon archon]** -- SCP is Archon.
* **[https://scpwiki.com/system:page-tags/tag/ticonderoga ticonderoga]** -- SCP is Ticonderoga.
* **[https://scpwiki.com/system:page-tags/tag/neutralized neutralized]** -- SCP is Neutralized.
* **[https://scpwiki.com/system:page-tags/tag/decommissioned decommissioned]** -- SCP is decommissioned.
* **[https://scpwiki.com/system:page-tags/tag/pending pending]** -- SCP is pending classification.
* **[https://scpwiki.com/system:page-tags/tag/esoteric-class esoteric-class]** -- SCP has an object class other than one of the above.

[[/tab]]
[[tab SCP Attributes]]
++ SCP Attributes

This list is intended as a guide to attribute tags, or secondary tags on SCP articles. If you would like to suggest a new tag, please do so in the most recent thread for tag proposals.

The list of tags has been divided into the following subsections: Entity, Animal, Mental, Biological, Physical, Artifact, Location, Other.

The following tags are SCP Article attribute tags, and should only be used on SCP pages, not tales.

[[div class="blockquote"]]
The following applies to all tags in this category:

* Requires 'scp'

[[/div]]

+++ Entity

Tags that apply to creatures that are **alive**, or to **autonomous** or non-living beings with similar properties.

* **[https://scpwiki.com/system:page-tags/tag/adaptive adaptive]** -- SCP adapts to stimuli in an anomalous manner.
* **[https://scpwiki.com/system:page-tags/tag/alive alive]** -- SCP is alive, meaning it exhibits the traits of metabolism, reaction, and reproduction. See the Tag [https://05command.wikidot.com/tech-hub-tag FAQ] for more information.
 * //Conflicts with 'autonomous'//
 * //Supersedes 'biological'//
* **[https://scpwiki.com/system:page-tags/tag/amorphous amorphous]** -- SCP lacks a set form or shape, constantly changes shape, or has a poorly-defined shape e.g. a blob.
 * //Conflicts with 'metamorphic'//
* **[https://scpwiki.com/system:page-tags/tag/autonomous autonomous]** -- SCP activates/operates on its own in an anomalous fashion. Only applicable to objects that normally do not activate on their own.
 * //Avoid using with 'robotic'//
 * //Conflicts with 'alive'//
* **[https://scpwiki.com/system:page-tags/tag/bacteria bacteria]** -- SCP is, resembles, or exhibits traits of a bacterial life-form.
 * //Often used with 'contagion'//
* **[https://scpwiki.com/system:page-tags/tag/clown clown]** -- SCP is, resembles, affects, or involves one or more clowns.
* **[https://scpwiki.com/system:page-tags/tag/fungus fungus]** -- SCP is or exhibits traits of fungal life-forms.
* **[https://scpwiki.com/system:page-tags/tag/ghost ghost]** -- SCP is or affects ghosts (spectral entities).
* **[https://scpwiki.com/system:page-tags/tag/hive-mind hive-mind]** -- SCP exhibits traits of an external hive-mind.
* **[https://scpwiki.com/system:page-tags/tag/hostile hostile]** -- SCP exhibits hostility towards humans or the Foundation that is not motivated by self-defence or the need for food.
 * //Conflicts with 'predatory'//
* **[https://scpwiki.com/system:page-tags/tag/humanoid humanoid]** -- SCP is humanoid or exhibits traits of humanoids.
* **[https://scpwiki.com/system:page-tags/tag/metamorphic metamorphic]** -- SCP changes its form or shape, often to mimic the form or shape of other objects or entities. Often used to describe shapeshifters or mimics.
 * //Conflicts with 'amorphous'//
* **[https://scpwiki.com/system:page-tags/tag/predatory predatory]** -- SCP exhibits predatory behavior, obtaining food or sustenance by hunting for prey.
 * //Conflicts with 'hostile'//
* **[https://scpwiki.com/system:page-tags/tag/plant plant]** -- SCP is a plant or exhibits plant-like traits.
* **[https://scpwiki.com/system:page-tags/tag/politician politician]** -- SCP is a politician or is related to a political office.
* **[https://scpwiki.com/system:page-tags/tag/sapient sapient]** -- SCP demonstrates sapience, the capacity for reason, abstract thought and complex emotional responses. Used to indicate intelligence equal to or exceeding human intelligence.
* **[https://scpwiki.com/system:page-tags/tag/species species]** -- SCP describes an entire species, rather than one or more individuals.
* **[https://scpwiki.com/system:page-tags/tag/swarm swarm]** -- SCP exhibits swarm behavior.
* **[https://scpwiki.com/system:page-tags/tag/superhero superhero]** -- SCP is related to superhero fiction or intrinsically embodies the idea of a superhero or supervillain.
* **[https://scpwiki.com/system:page-tags/tag/tree tree]** -- SCP is or exhibits traits of tree-like (arboreal) plants.
 * //Often used with 'plant'//
* **[https://scpwiki.com/system:page-tags/tag/virus virus]** -- SCP exhibits traits of viral agents.
 * //Requires either 'biological', or 'computer'//
 * //Supersedes 'contagion'//

+++ Animal

Tags that apply to animals, or to entities that resemble animals.

* **[https://scpwiki.com/system:page-tags/tag/animal animal]** -- SCP is or affects animal life.
* **[https://scpwiki.com/system:page-tags/tag/amphibian amphibian]** -- SCP is, affects or resembles amphibians, including frogs, toads and salamanders.
 * //Often used with 'animal'//
* **[https://scpwiki.com/system:page-tags/tag/arachnid arachnid]** -- SCP is, affects or resembles spider-like animals, including scorpions, mites and ticks.
 * //Often used with 'animal'//
 * //Conflicts with 'crustacean', and 'insect'//
 * //Supersedes 'invertebrate', and 'arthropod'//
* **[https://scpwiki.com/system:page-tags/tag/arthropod arthropod]** -- SCP is, affects or resembles arthropods, animals with exoskeletons, segmented bodies, and jointed appendages.
 * //Supersedes 'invertebrate'//
 * //Superseded by 'arachnid', 'crustacean', and 'insect'//
* **[https://scpwiki.com/system:page-tags/tag/bear bear]** -- SCP is, affects or resembles bears (ursine).
 * //Often used with 'animal'//
* **[https://scpwiki.com/system:page-tags/tag/bee bee]** -- SCP is, affects or resembles bees (apian).
 * //Often used with 'animal', and 'insect'//
* **[https://scpwiki.com/system:page-tags/tag/bird bird]** -- SCP is, affects or resembles birds (avian).
 * //Often used with 'animal'//
* **[https://scpwiki.com/system:page-tags/tag/bovine bovine]** -- SCP is, affects or resembles cattle-like animals, including buffalo and bison.
 * //Often used with 'animal'//
* **[https://scpwiki.com/system:page-tags/tag/butterfly butterfly]** -- SCP is, affects or resembles lepidopteran insects, including butterflies, moths, and skippers.
 * //Often used with 'animal', and 'insect'//
* **[https://scpwiki.com/system:page-tags/tag/canine canine]** -- SCP is, affects or resembles dog-like animals, including wolves, coyote and jackals.
 * //Often used with 'animal'//
* **[https://scpwiki.com/system:page-tags/tag/cephalopod cephalopod]** -- SCP is, affects or resembles cephalopods, including the cuttlefish, octopus, and squid.
 * //Often used with 'animal'//
 * //Supersedes 'invertebrate'//
* **[https://scpwiki.com/system:page-tags/tag/cetacean cetacean]** -- SCP is, affects or resembles whales, dolphins or porpoises.
 * //Often used with 'animal'//
* **[https://scpwiki.com/system:page-tags/tag/crustacean crustacean]** --  SCP is, affects or is related to crustaceans, the family of arthropods that includes crabs, lobsters, shrimp, isopods and barnacles.
 * //Often used with 'animal'//
 * //Conflicts with 'arachnid', and 'insect'//
 * //Supersedes 'invertebrate', and 'arthropod'//
* **[https://scpwiki.com/system:page-tags/tag/deer deer]** -- SCP is, affects or resembles deer, including elk and moose (cervine).
 * //Often used with 'animal'//
* **[https://scpwiki.com/system:page-tags/tag/dinosaur dinosaur]** -- SCP is, affects or resembles non-avian dinosaurs. Includes pterosaurs and extinct marine reptiles.
* **[https://scpwiki.com/system:page-tags/tag/equine equine]** -- SCP is, affects or resembles horse-like animals, including zebra and donkeys.
 * //Often used with 'animal'//
* **[https://scpwiki.com/system:page-tags/tag/feline feline]** -- SCP is, affects or resembles cat-like animals, including big cats like lions and tigers.
 * //Often used with 'animal'//
* **[https://scpwiki.com/system:page-tags/tag/fish fish]** -- SCP is, affects or resembles fish (piscine).
 * //Often used with 'animal'//
* **[https://scpwiki.com/system:page-tags/tag/insect insect]** -- SCP is, affects or resembles insects, which are six-legged arthropods. (This **does not** include spiders, which should be tagged as //arachnid//, or woodlice, which should be tagged as //crustacean//. This also does not include centipedes or millipedes).
 * //Often used with 'animal'//
 * //Conflicts with 'arachnid', and 'crustacean'//
 * //Supersedes 'invertebrate', and 'arthropod'//
* **[https://scpwiki.com/system:page-tags/tag/invertebrate invertebrate]** -- SCP is, affects or resembles invertebrates, animals lacking spinal columns.
 * //Superseded by 'arachnid', 'arthropod', 'cephalopod', 'crustacean', 'insect', and 'worm'//
* **[https://scpwiki.com/system:page-tags/tag/primate primate]** -- SCP is, affects or resembles non-human apes or monkeys (simian).
 * //Often used with 'animal'//
* **[https://scpwiki.com/system:page-tags/tag/rabbit rabbit]** -- SCP is, affects or resembles rabbits or hares (leporine).
 * //Often used with 'animal'//
* **[https://scpwiki.com/system:page-tags/tag/reptile reptile]** -- SCP is, affects or resembles reptiles.
 * //Often used with 'animal'//
* **[https://scpwiki.com/system:page-tags/tag/rodent rodent]** -- SCP is, affects or resembles rodents, including mice, rats, squirrels and beavers.
 * //Often used with 'animal'//
* **[https://scpwiki.com/system:page-tags/tag/shark shark]** -- SCP is, affects or resembles sharks, including rays and skates (selachian).
 * //Requires 'fish'//
 * //Often used with 'animal'//
* **[https://scpwiki.com/system:page-tags/tag/snake snake]** -- SCP is, affects or resembles snakes (ophidian).
 * //Often used with 'animal', and 'reptile'//
* **[https://scpwiki.com/system:page-tags/tag/worm worm]** -- SCP is, affects or resembles worms (vermian).
 * //Often used with 'animal'//
 * //Supersedes 'invertebrate'//

+++ Biological

Tags that apply to entities, objects or phenomena with biological effects or properties.

* **[https://scpwiki.com/system:page-tags/tag/biological biological]** -- SCP consists of biological molecules, tissues or organs. Please see the [https://05command.wikidot.com/tech-hub-tag FAQ] for more details.
 * //Superseded by 'alive'//
* **[https://scpwiki.com/system:page-tags/tag/biohazard biohazard]** -- SCP poses a hazard to humans or the environment as a result of biological function, or is a biological hazard.
* **[https://scpwiki.com/system:page-tags/tag/blood blood]** -- SCP is related to/anomalously affects blood.
* **[https://scpwiki.com/system:page-tags/tag/cadaver cadaver]** -- SCP is, affects, or is related to corpses, carcasses, or any dead biological matter.
 * //Often used with 'reanimation', and 'skeletal'//
* **[https://scpwiki.com/system:page-tags/tag/contagion contagion]** -- SCP is a contagious agent or exhibits contagious spread.
 * //Superseded by 'virus', and 'memetic'//
* **[https://scpwiki.com/system:page-tags/tag/dental dental]** -- SCP is or deals with teeth or the practice of dentistry.
* **[https://scpwiki.com/system:page-tags/tag/extremity extremity]** -- SCP is or affects specific extremities, regardless of species.
* **[https://scpwiki.com/system:page-tags/tag/genetic genetic]** -- SCP is related to or functions primarily via genetic encoding and decoding.
* **[https://scpwiki.com/system:page-tags/tag/medical medical]** -- SCP is used or intended for use as a medical device or otherwise has medical significance outside of pathology.
* **[https://scpwiki.com/system:page-tags/tag/nocturnal nocturnal]** -- SCP is triggered by, activated by, or otherwise is only significantly active at night.
* **[https://scpwiki.com/system:page-tags/tag/ocular ocular]** -- SCP resembles, is related to, or affects eyes.
* **[https://scpwiki.com/system:page-tags/tag/parasitic parasitic]** -- SCP exhibits traits of parasitic or parasitoid organisms.
 * //Avoid using with 'reproductive'//
* **[https://scpwiki.com/system:page-tags/tag/reanimation reanimation]** -- SCP has been restored or restores others, either whole or in part, to life from a clinically dead state.
 * //Often used with 'cadaver'//
* **[https://scpwiki.com/system:page-tags/tag/reproductive reproductive]** -- SCP anomalously affects or interferes with the normal biological reproductive processes of an organism (which may include humans), or has anomalous biological reproductive methods other than that covered by //parasitic// or //self-replicating//.
 * //Avoid using with 'parasitic', and 'self-replicating'//
* **[https://scpwiki.com/system:page-tags/tag/sexual sexual]** -- SCP includes or affects sexual organs, sexual activities, or concepts related to sex. Does not imply that the work is intended for adult audiences only.
* **[https://scpwiki.com/system:page-tags/tag/skeletal skeletal]** -- SCP is a skeleton, consists of bones or cartilage from a skeleton, or affects the skeletal tissue of an organism.
* **[https://scpwiki.com/system:page-tags/tag/toxic toxic]** -- SCP induces chemical toxicity in subjects.

+++ Mental

Tags that apply to entities, objects or phenomena that have psychological, **mind-affecting** or **sensory** effects.

* **[https://scpwiki.com/system:page-tags/tag/addictive addictive]** -- SCP causes desire or addictive behavior in affected subjects.
* **[https://scpwiki.com/system:page-tags/tag/antimemetic antimemetic]** -- SCP is or involves the use of (an) antimeme(s) to suppress knowledge and/or understanding of an idea or concept, including itself.
 * //Avoid using with 'memetic'//
* **[https://scpwiki.com/system:page-tags/tag/auditory auditory]** -- SCP is triggered by, activated by, or affects the sense of hearing.
 * //Avoid using with 'acoustic'//
* **[https://scpwiki.com/system:page-tags/tag/cognitohazard cognitohazard]** -- SCP is hazardous to subjects when observed by any of the traditional 5 senses.
 * //Often used with 'auditory', 'gustatory', 'olfactory', 'tactile', and 'visual'//
* **[https://scpwiki.com/system:page-tags/tag/compulsion compulsion]** -- SCP induces compulsive behavior in subjects or otherwise causes subjects to do things they normally would not. See Tag [https://05command.wikidot.com/tech-hub-tag FAQ] for extended clarifications.
* **[https://scpwiki.com/system:page-tags/tag/empathic empathic]** -- SCP is capable of reading or conveying emotion, feelings, or sensations.
 * //Often used with 'telepathic'//
* **[https://scpwiki.com/system:page-tags/tag/gustatory gustatory]** -- SCP is triggered by, activated by, or affects the sense of taste.
* **[https://scpwiki.com/system:page-tags/tag/hallucination hallucination]** -- SCP induces hallucinations in subjects or is a hallucination.
 * //Often used with 'auditory', and 'visual'//
* **[https://scpwiki.com/system:page-tags/tag/infohazard infohazard]** -- SCP has an effect that is triggered when it is described or referred to. See Tag [https://05command.wikidot.com/tech-hub-tag FAQ] for extended clarifications.
* **[https://scpwiki.com/system:page-tags/tag/knowledge knowledge]** -- SCP absorbs, stores, generates, grants, or possesses knowledge that is anomalous, or through an anomalous process. SCPs capable of accurate predictions should be tagged //predictive// instead.
 * //Superseded by 'predictive'//
 * //Compare with 'telepathic'//
* **[https://scpwiki.com/system:page-tags/tag/language language]** -- SCP imparts, exhibits, or is an anomalous language.
* **[https://scpwiki.com/system:page-tags/tag/memetic memetic]** -- SCP is a memetic agent or exhibits traits of [https://scp-wiki.wikidot.com/Understanding-Memetics memetic propagation]. See Tag [https://05command.wikidot.com/tech-hub-tag FAQ] for extended clarifications.
 * //Often used with 'cognitohazard'//
 * //Avoid using with 'antimemetic'//
 * //Supersedes 'contagion'//
* **[https://scpwiki.com/system:page-tags/tag/mimetic mimetic]** -- SCP exhibits anomalous mimicry.
 * //Often used with 'auditory', 'gustatory', 'olfactory', 'tactile', and 'visual'//
* **[https://scpwiki.com/system:page-tags/tag/memory-affecting memory-affecting]** -- SCP imparts, changes, or removes memories in intelligent beings such as human subjects.
 * //Compare with 'mind-affecting'//
* **[https://scpwiki.com/system:page-tags/tag/mind-affecting mind-affecting]** -- SCP affects the thinking of subjects, which can include behavior and overall intelligence. See Tag [https://05command.wikidot.com/tech-hub-tag FAQ] for extended clarifications.
 * //Compare with 'memory-affecting'//
* **[https://scpwiki.com/system:page-tags/tag/neurological neurological]** -- SCP directly or indirectly affects the neurological system of subjects. Only applicable in situations where objective neurological changes are confirmed, as opposed to a simple change of behavior in the subject.
 * //Often used with 'mind-affecting', and 'memory-affecting'//
* **[https://scpwiki.com/system:page-tags/tag/observational observational]** -- SCP has properties that are triggered or suppressed when directly or indirectly observed. These properties may or may not also be //cognitohazards//.
 * //Often used with 'cognitohazard'//
* **[https://scpwiki.com/system:page-tags/tag/olfactory olfactory]** -- SCP exhibits anomalous scent, is propagated through smell, or affects the sense of smelling.
* **[https://scpwiki.com/system:page-tags/tag/predictive predictive]** -- SCP is capable of imparting information or acting in a predictive manner.
 * //Supersedes 'knowledge'//
* **[https://scpwiki.com/system:page-tags/tag/sensory sensory]** -- SCP affects sensory perception.
 * //Often used with 'auditory', 'gustatory', 'olfactory', 'tactile', and 'visual'//
* **[https://scpwiki.com/system:page-tags/tag/sleep sleep]** -- SCP is related to sleep.
* **[https://scpwiki.com/system:page-tags/tag/tactile tactile]** -- SCP is activated by, triggered by, or affects the sense of touch. Note that this refers specifically to the sense of touch, not simply something that can activate by touching something else.
* **[https://scpwiki.com/system:page-tags/tag/telepathic telepathic]** -- SCP can transfer information via anomalous means.
* **[https://scpwiki.com/system:page-tags/tag/visual visual]** -- SCP is triggered by, activated by, or affects the sense of sight.
 * //Often used with 'cognitohazard', and 'sensory'//

+++ Physical

Tags that apply to the physical properties or effects of entities, objects or phenomena. Includes physics-related effects.

* **[https://scpwiki.com/system:page-tags/tag/acoustic acoustic]** -- SCP is composed of, affects, generates, or is propagated by sound waves.
 * //Often used with 'vibration'//
 * //Avoid using with 'auditory'//
* **[https://scpwiki.com/system:page-tags/tag/chemical chemical]** -- SCP is an anomalous chemical compound or produces chemical compounds in an anomalous way.
* **[https://scpwiki.com/system:page-tags/tag/corrosive corrosive]** -- SCP exhibits corrosive properties.
* **[https://scpwiki.com/system:page-tags/tag/ectoentropic ectoentropic]** -- SCP produces energy or matter in an unexplained way, violating the principle that entropy (the disorder of a system) must always increase.
 * //Avoid using with 'extradimensional'//
 * //Superseded by 'reality-bending'//
* **[https://scpwiki.com/system:page-tags/tag/electrical electrical]** -- SCP generates, stores, or uses electric energy.
* **[https://scpwiki.com/system:page-tags/tag/electromagnetic electromagnetic]** -- SCP generates, stores, or uses electromagnetic energy or fields.
* **[https://scpwiki.com/system:page-tags/tag/entropic entropic]** -- SCP has anomalous properties that affect or are affected by entropy, or that resemble entropic decay.
* **[https://scpwiki.com/system:page-tags/tag/fire fire]** -- SCP is composed of fire, is related to fire, or enables the process of combustion.
* **[https://scpwiki.com/system:page-tags/tag/gaseous gaseous]** -- SCP is or generates a gas.
* **[https://scpwiki.com/system:page-tags/tag/gravity gravity]** -- SCP has anomalous properties that affect or are significantly affected by gravitational force.
* **[https://scpwiki.com/system:page-tags/tag/immobile immobile]** -- SCP cannot be moved via any means known by the Foundation.
* **[https://scpwiki.com/system:page-tags/tag/indestructible indestructible]** -- SCP cannot be destroyed via any means known by the Foundation.
* **[https://scpwiki.com/system:page-tags/tag/intangible intangible]** -- SCP is intangible in a manner that precludes definition as a gas.
* **[https://scpwiki.com/system:page-tags/tag/light light]** -- SCP is triggered, activated, or propagated by or otherwise related to the presence or absence of visible light.
* **[https://scpwiki.com/system:page-tags/tag/liquid liquid]** -- SCP is or generates a liquid.
* **[https://scpwiki.com/system:page-tags/tag/magnetic magnetic]** -- SCP is magnetic or exhibits traits of magnetic charge and/or attraction.
* **[https://scpwiki.com/system:page-tags/tag/meteorological meteorological]** -- SCP is, affects, or is affected by significant weather elements.
* **[https://scpwiki.com/system:page-tags/tag/microscopic microscopic]** -- SCP is too small to be seen or otherwise meaningfully observed by the naked eye.
 * //Compare with 'miniature'//
* **[https://scpwiki.com/system:page-tags/tag/miniature miniature]** -- SCP is much smaller than objects it resembles.
 * //Compare with 'microscopic'//
* **[https://scpwiki.com/system:page-tags/tag/mobile mobile]** -- SCP is capable of movement by anomalous means. Generally only applies to objects or entities that are normally incapable of movement.
 * //Avoid using with 'teleportation'//
* **[https://scpwiki.com/system:page-tags/tag/portal portal]** -- SCP is an opening or doorway that exhibits inconsistent connectivity.
 * //Often used with 'extradimensional', and 'spatial'//
* **[https://scpwiki.com/system:page-tags/tag/paradox paradox]** -- SCP generates, exhibits, or is involved in paradoxical events or situations.
 * //Compare with 'temporal'//
* **[https://scpwiki.com/system:page-tags/tag/polyhedral polyhedral]** -- SCP is a polyhedron: a three-dimensional shape with flat faces and straight edges.
* **[https://scpwiki.com/system:page-tags/tag/radioactive radioactive]** -- SCP emits radiation or affects radioactivity.
* **[https://scpwiki.com/system:page-tags/tag/reality-bending reality-bending]** -- SCP is capable of manipulating reality through anomalous means (aka 'ontokinetic', 'reality-bending' or 'reality warping') .
 * //Avoid using with 'thaumaturgy'//
 * //Supersedes 'ectoentropic'//
* **[https://scpwiki.com/system:page-tags/tag/self-repairing self-repairing]** -- SCP exhibits an anomalous ability restore or repair itself to functional condition.
* **[https://scpwiki.com/system:page-tags/tag/self-replicating self-replicating]** -- SCP exhibits an anomalous ability to replicate other than via biological reproduction.
 * //Avoid using with 'reproductive'//
* **[https://scpwiki.com/system:page-tags/tag/shadow shadow]** -- SCP is triggered, activated, or otherwise significantly affected by shadows cast by subjects.
* **[https://scpwiki.com/system:page-tags/tag/spatial spatial]** -- SCP warps or distorts space, creating phenomena like impossible geometries or spaces that are larger or smaller than they should be.
 * //Often used with 'temporal'//
* **[https://scpwiki.com/system:page-tags/tag/sphere sphere]** -- SCP is spherical.
* **[https://scpwiki.com/system:page-tags/tag/telekinetic telekinetic]** -- SCP can manipulate objects or initiate or affect reactions through anomalous means.
* **[https://scpwiki.com/system:page-tags/tag/teleportation teleportation]** -- SCP can move without occupying intervening space or otherwise displace itself via anomalous means that preclude normal movement.
 * //Avoid using with 'mobile'//
* **[https://scpwiki.com/system:page-tags/tag/temporal temporal]** -- SCP affects or is otherwise related to the passage of time.
 * //Often used with 'spatial'//
* **[https://scpwiki.com/system:page-tags/tag/thaumaturgy thaumaturgy]** -- SCP is, performs, or is otherwise related to thaumaturgy.
 * //Avoid using with 'reality-bending'//
* **[https://scpwiki.com/system:page-tags/tag/thermal thermal]** -- SCP is activated by, triggered by, or propagates via changes in temperature. This includes both increases and decreases in temperature.
* **[https://scpwiki.com/system:page-tags/tag/thermodynamic thermodynamic]** -- SCP affects, or is otherwise significantly related to the laws of thermodynamics.
* **[https://scpwiki.com/system:page-tags/tag/transfiguration transfiguration]** -- SCP alters the shape or substance of subjects in an anomalous manner.
* **[https://scpwiki.com/system:page-tags/tag/transmission transmission]** -- SCP transmits information, typically via radio waves or other electromagnetic means.
* **[https://scpwiki.com/system:page-tags/tag/vibration vibration]** -- SCP generates anomalous vibrations or other repetitive movement.
 * //Often used with 'acoustic'//

+++ Artifact

Tags that typically apply to objects created by humans, including **artifacts** and **artistic** works.

* **[https://scpwiki.com/system:page-tags/tag/appliance appliance]** -- SCP is or resembles a household or domestic appliance.
 * //Often used with 'electrical', and 'electronic'//
 * //Supersedes 'artifact'//
 * //Superseded by 'computer'//
* **[https://scpwiki.com/system:page-tags/tag/artistic artistic]** -- SCP is a work of art, exhibits artistic properties, or has artistic significance.
 * //Supersedes 'artifact'//
 * //Superseded by 'musical', 'performance', and 'sculpture'//
* **[https://scpwiki.com/system:page-tags/tag/artificial-intelligence artificial-intelligence]** -- SCP is an artificial intelligence, possesses an AI or affects other AIs.
* **[https://scpwiki.com/system:page-tags/tag/artifact artifact]** -- SCP is or was originally created by humans.
 * //Superseded by 'appliance', 'artistic', 'clothing', 'Cinema', 'computer', 'document', 'food', 'jewelry', 'media', 'tool', 'toy', 'weapon', and 'vehicle'//
* **[https://scpwiki.com/system:page-tags/tag/clockwork clockwork]** -- SCP operates primarily via clockworks, defined as mechanical devices constructed primarily using toothed wheels and/or powered by a mainspring.
 * //Supersedes 'mechanical'//
* **[https://scpwiki.com/system:page-tags/tag/clothing clothing]** -- SCP is an artifact primarily intended to be worn for protection or comfort, including armor and protective helmets.
 * //Conflicts with 'jewelry'//
 * //Supersedes 'artifact'//
* **[https://scpwiki.com/system:page-tags/tag/Cinema Cinema]** -- SCPs that are, relate to or concern the medium of cinema, film and/or movies.
 * //Supersedes 'artifact'//
* **[https://scpwiki.com/system:page-tags/tag/computer computer]** -- SCP is a computational device or affects computational devices.
 * //Often used with 'electronic', and 'mechanical'//
 * //Supersedes 'artifact', and 'appliance'//
* **[https://scpwiki.com/system:page-tags/tag/currency currency]** -- SCP is, is related to, affects, or is activated by money or other objects primarily intended to be used as a medium of exchange.
* **[https://scpwiki.com/system:page-tags/tag/document document]** -- SCP is a textual document of some sort. Includes books.
 * //Supersedes 'artifact', and 'inscription'//
* **[https://scpwiki.com/system:page-tags/tag/electronic electronic]** -- SCP is or resembles an electronic device.
* **[https://scpwiki.com/system:page-tags/tag/food food]** -- SCP is primarily intended to be an edible object or substance.
 * //Supersedes 'artifact'//
* **[https://scpwiki.com/system:page-tags/tag/inscription inscription]** -- SCP features carvings, engravings or inscriptions of words, numbers or other designs.
 * //Superseded by 'document'//
* **[https://scpwiki.com/system:page-tags/tag/jewelry jewelry]** -- SCP is an object primarily intended to be worn in a decorative manner.
 * //Conflicts with 'clothing'//
 * //Supersedes 'artifact'//
* **[https://scpwiki.com/system:page-tags/tag/mechanical mechanical]** -- SCP operates primarily in a mechanical manner or is a mechanical device.
 * //Superseded by 'clockwork', and 'robotic'//
* **[https://scpwiki.com/system:page-tags/tag/media media]** -- SCP is or is contained on, one or more items of fixed or removable analog or digital media, such as a tape, record, disc, or drive.
 * //Supersedes 'artifact'//
* **[https://scpwiki.com/system:page-tags/tag/musical musical]** -- SCP is, generates, or is generated by musical compositions.
 * //Supersedes 'artistic'//
* **[https://scpwiki.com/system:page-tags/tag/online online]** -- SCP is available on, utilizes, or is dependent on a connection to the internet.
 * //Often used with 'computer', and 'electronic'//
* **[https://scpwiki.com/system:page-tags/tag/performance performance]** -- SCP is or is used in a performance art, such as a dance or play.
 * //Supersedes 'artistic'//
* **[https://scpwiki.com/system:page-tags/tag/photographic photographic]** -- SCP is or deals with photography or features a photograph as part of the primary anomaly.
* **[https://scpwiki.com/system:page-tags/tag/robotic robotic]** -- SCP is a device or construct designed to operate on its own. Applicable to anything that can be described as a 'robot' or 'automaton'.
 * //Avoid using with 'autonomous'//
 * //Supersedes 'mechanical'//
* **[https://scpwiki.com/system:page-tags/tag/sculpture sculpture]** -- SCP is a three-dimensional piece of artwork. To be considered a //sculpture//, the object in question must have been formed, carved, or molded.
 * //Supersedes 'artistic'//
* **[https://scpwiki.com/system:page-tags/tag/tool tool]** -- SCP is (or was intended to be) used as a tool.
 * //Supersedes 'artifact'//
* **[https://scpwiki.com/system:page-tags/tag/toy toy]** -- SCP is, or was primarily intended to be, used as a toy.
 * //Supersedes 'artifact'//
* **[https://scpwiki.com/system:page-tags/tag/weapon weapon]** -- SCP is or is intended to be used as a weapon.
 * //Supersedes 'artifact'//
* **[https://scpwiki.com/system:page-tags/tag/vehicle vehicle]** -- SCP is or is intended to be used as a vehicle.
 * //Supersedes 'artifact'//

+++ Location

Tags that describe where the SCP is, where it comes from, or that apply to SCPs that describe or affect specific locations.

* **[https://scpwiki.com/system:page-tags/tag/afterlife afterlife]** -- SCP describes or is otherwise related to what happens to consciousness after death.
* **[https://scpwiki.com/system:page-tags/tag/airborne airborne]** -- SCP lives in, moves through, or spreads through the air.
* **[https://scpwiki.com/system:page-tags/tag/aquatic aquatic]** -- SCP lives in, moves through or spreads through water.
* **[https://scpwiki.com/system:page-tags/tag/building building]** -- SCP is, is a part of, or otherwise is related to or affects a building, defined as a structure intended for human occupation.
 * //Supersedes 'structure'//
* **[https://scpwiki.com/system:page-tags/tag/city city]** -- SCP is a city, town, or other settlement intended for human occupation. Should only be used if a significant portion of the city is considered anomalous.
 * //Supersedes 'location'//
* **[https://scpwiki.com/system:page-tags/tag/extradimensional extradimensional]** -- SCP is of extradimensional origin, moves or propagates extradimensionally, and/or enables extradimensional travel.
 * //Avoid using with 'ectoentropic'//
* **[https://scpwiki.com/system:page-tags/tag/extraterrestrial extraterrestrial]** -- SCP originates or is found in outer space and/or enables or exhibits extraterrestrial travel.
* **[https://scpwiki.com/system:page-tags/tag/forest forest]** -- SCP is or affects forests, groves, orchards or other locations with high amounts of trees, manmade or otherwise.
* **[https://scpwiki.com/system:page-tags/tag/geological geological]** -- SCP is or affects natural geological formations (such as caves, cliffs, mountains, valleys, or volcanoes) or significant geological events (such as earthquakes, landslides, or sinkholes).
 * //Superseded by 'planet'//
* **[https://scpwiki.com/system:page-tags/tag/island island]** -- SCP is or affects islands, archipelagos or similar formations.
* **[https://scpwiki.com/system:page-tags/tag/library library]** -- SCP is, or is otherwise related to or affects libraries, defined as a room or building containing books for people to read or borrow.
* **[https://scpwiki.com/system:page-tags/tag/location location]** -- SCP is a unique geographical location.
 * //Superseded by 'city'//
* **[https://scpwiki.com/system:page-tags/tag/moon moon]** -- SCP is, is related to, or affects a natural satellite or moon, which may or may not be our moon.
* **[https://scpwiki.com/system:page-tags/tag/planet planet]** -- SCP is, resembles, or affects a planet, which may or may not be our planet.
 * //Supersedes 'geological'//
* **[https://scpwiki.com/system:page-tags/tag/satellite satellite]** -- SCP is a natural or artificial satellite orbiting a celestial body.
* **[https://scpwiki.com/system:page-tags/tag/school school]** -- SCP is related to or affects schools, universities, or the education system.
* **[https://scpwiki.com/system:page-tags/tag/structure structure]** -- SCP is an artificial or natural structure; if it is intended for human occupation, it should be tagged //building// instead.
 * //Superseded by 'building'//
* **[https://scpwiki.com/system:page-tags/tag/subterranean subterranean]** -- SCP is located or operates wholly or significantly underground, defined as below the surface of the Earth. Does not apply objects that are simply contained underground for safety or convenience.
* **[https://scpwiki.com/system:page-tags/tag/sun sun]** -- SCP is, is related to, or affects a sun, which may or may not be our sun.

+++ Other

Any tags that do not fit into the other sections.

* **[https://scpwiki.com/system:page-tags/tag/anomalous-event anomalous-event]** -- The SCP is a singular anomalous event that significantly changed reality in some way.
 * //Avoid using with 'phenomenon'//
* **[https://scpwiki.com/system:page-tags/tag/corporate corporate]** -- SCP affects the operations of a business or corporation.
* **[https://scpwiki.com/system:page-tags/tag/concept concept]** -- SCP is or affects a purely non-physical concept. Should not be used in conjunction with tags describing physical qualities.
* **[https://scpwiki.com/system:page-tags/tag/exchange exchange]** -- SCP involves or is triggered by some form of exchange of physical or intangible goods, including but not limited to bartering and monetary trade.
* **[https://scpwiki.com/system:page-tags/tag/foundation-made foundation-made]** -- SCP was created, intentionally or otherwise, by the SCP Foundation itself. Note that only the objects whose creation resulted directly from specific actions of the Foundation are applicable. This excludes phenomena which formed spontaneously at a Foundation site due to the area's routine exposure to a large number of contained anomalies.
* **[https://scpwiki.com/system:page-tags/tag/future future]** -- SCP is from the future or was otherwise temporally displaced from a later time frame into an earlier one.
 * //Often used with 'temporal'//
* **[https://scpwiki.com/system:page-tags/tag/game game]** -- SCP is, is used in, is activated by, or is otherwise related to one or more games, defined as a method of play or a sport -- especially a competitive one -- that can be won or lost by skill, strength, or luck.
 * //Often used with 'sport'//
* **[https://scpwiki.com/system:page-tags/tag/historical historical]** -- SCP affects or is prominent in historical events or has historical significance.
* **[https://scpwiki.com/system:page-tags/tag/k-class-scenario k-class-scenario]** -- SCP is involved in or capable of instigating one or more K-Class End of the World scenarios. Should only be used in articles that specifically name a type of K-Class scenario.
* **[https://scpwiki.com/system:page-tags/tag/legality legality]** -- SCP is, effects, or relates to law, legal proceedings, or legal scripture.
* **[https://scpwiki.com/system:page-tags/tag/loop loop]** -- SCP exhibits or is engaged in a repeating loop of activity.
* **[https://scpwiki.com/system:page-tags/tag/mathematical mathematical]** -- SCP is or affects a number, number system, mathematical equation, or otherwise has mathematical significance.
* **[https://scpwiki.com/system:page-tags/tag/military military]** -- SCP is military equipment, part or member of a military unit, or otherwise has military significance.
 * //Compare with 'weapon'//
* **[https://scpwiki.com/system:page-tags/tag/meta meta]** -- SCP affects or is affected by its documentation or requires containment procedures regarding the way it is documented. See Tag [https://05command.wikidot.com/tech-hub-tag FAQ] for extended clarifications.
* **[https://scpwiki.com/system:page-tags/tag/narrative narrative]** -- SCP is, is related to, or propagates via narrative information or documents.
* **[https://scpwiki.com/system:page-tags/tag/probability probability]** -- SCP alters or manipulates the probability of certain events or outcomes.
* **[https://scpwiki.com/system:page-tags/tag/phenomenon phenomenon]** -- The SCP is an ongoing widespread phenomenon not directly linked to a physical source.
 * //Avoid using with 'anomalous-event'//
* **[https://scpwiki.com/system:page-tags/tag/religious religious]** -- SCP is associated with or otherwise has significance to one or more organized religions.
* **[https://scpwiki.com/system:page-tags/tag/ritual ritual]** -- SCP is or is triggered or activated through ritualistic behavior.
* **[https://scpwiki.com/system:page-tags/tag/sport sport]** -- SCP is, is used in, is activated by, or is otherwise related to one or more sports, defined as an activity involving physical exertion and skill in which one or more individuals compete against other individuals or teams. Sports should also be tagged with //game//. Equipment or gear specifically or exclusively used in sporting events should also be tagged with //clothing// or //tool//, as appropriate.
 * //Compare with 'game', 'clothing', and 'tool'//
* **[https://scpwiki.com/system:page-tags/tag/uncontained uncontained]** -- SCP is neither fully nor partially contained. This should only be applied to SCPs where no instances are contained at all and does not apply if the Foundation successfully contains one or more instances.

[[/tab]]
[[tab Genre and Themes]]
++ Genre and Themes

.

[[div class="blockquote"]]
The following applies to all tags in this category:

* Requires 'tale'

[[/div]]

+++ Genre

Describes the genre of a tale.

* **[https://scpwiki.com/system:page-tags/tag/absurdist-fiction absurdist-fiction]** -- Depicts events lacking any rational explanation or meaning, for the purpose of shock or comedy.
* **[https://scpwiki.com/system:page-tags/tag/action action]** -- Focuses on exciting events and spectacular violence.
* **[https://scpwiki.com/system:page-tags/tag/adventure adventure]** -- Focuses on the exploration of unfamiliar environments.
* **[https://scpwiki.com/system:page-tags/tag/bittersweet bittersweet]** -- Intended to evoke both positive and negative emotions. For tales that mix elements of both the bleak and heartwarming tags.
* **[https://scpwiki.com/system:page-tags/tag/bleak bleak]** -- Intended to evoke negative emotions, focusing on anguish, distress and suffering.
* **[https://scpwiki.com/system:page-tags/tag/comedy comedy]** -- Intended to be funny.
* **[https://scpwiki.com/system:page-tags/tag/black-comedy black-comedy]** -- Depicts shocking or unpleasant situations for the purpose of humour.
 * //Requires 'comedy'//
* **[https://scpwiki.com/system:page-tags/tag/chase chase]** -- Focuses on pursuit or escape.
* **[https://scpwiki.com/system:page-tags/tag/crime-fiction crime-fiction]** -- Focuses on criminals and law enforcement.
* **[https://scpwiki.com/system:page-tags/tag/fantasy fantasy]** -- Depicts magic and the supernatural, inspired by mythology and folklore.
* **[https://scpwiki.com/system:page-tags/tag/heartwarming heartwarming]** -- Intended to evoke positive emotions, focusing on pleasant experiences and supportive relationships.
* **[https://scpwiki.com/system:page-tags/tag/horror horror]** -- Intended to evoke fear, shock or disgust in the reader.
* **[https://scpwiki.com/system:page-tags/tag/body-horror body-horror]** -- Focuses on physical mutilation or transformation.
 * //Requires 'horror'//
* **[https://scpwiki.com/system:page-tags/tag/cosmic-horror cosmic-horror]** -- focuses on human insignificance and irrelevance, with emphasis on the unknowable and incomprehensible.
 * //Requires 'horror'//
* **[https://scpwiki.com/system:page-tags/tag/psychological-horror psychological-horror]** -- focuses on psychological distress and emotional vulnerability.
 * //Requires 'horror'//
* **[https://scpwiki.com/system:page-tags/tag/lgbtq lgbtq]** -- Article features LGBTQ+ themes, culture or history as a major focus of the work. Possible examples include portrayal of gay and lesbian relationships, depiction of asexuality and bisexuality, and exploration of trans, queer and agender identities.
* **[https://scpwiki.com/system:page-tags/tag/military-fiction military-fiction]** -- Focuses on soldiers, field agents or mercenaries.
* **[https://scpwiki.com/system:page-tags/tag/mystery mystery]** -- Focuses on investigation of unanswered questions.
* **[https://scpwiki.com/system:page-tags/tag/mythological-fiction mythological-fiction]** -- Depicts creatures, events and practices drawn from mythology and folklore of a specific culture, outside of structured religious practice.
* **[https://scpwiki.com/system:page-tags/tag/religious-fiction religious-fiction]** -- Focuses on religion, faith and belief. Includes depictions of real-world religions, as well as worship of anomalous entities.
* **[https://scpwiki.com/system:page-tags/tag/romance romance]** -- Focuses on romantic relationships between characters.
* **[https://scpwiki.com/system:page-tags/tag/science-fiction science-fiction]** -- Depicts advanced science and technology. May feature scientific analysis of phenomena currently thought to be impossible.
* **[https://scpwiki.com/system:page-tags/tag/slice-of-life slice-of-life]** -- Offers a look into the everyday lives of characters, with a focus on the mundane.
* **[https://scpwiki.com/system:page-tags/tag/spy-fiction spy-fiction]** -- Focuses on espionage and counter-intelligence.
* **[https://scpwiki.com/system:page-tags/tag/surrealist-fiction surrealist-fiction]** -- Creates a dream-like story by juxtoposing the mundane with the impossible and irrational, with emphasis on subconscious associations between them.

+++ Setting

Describes the setting of a tale.

* **[https://scpwiki.com/system:page-tags/tag/alternate-history alternate-history]** -- Depicts historical events that diverge from how they happened in real life. Does not apply to future events, or to anomalous reinterpretations of events that did happen (e.g. the 7th Occult War).
* **[https://scpwiki.com/system:page-tags/tag/christmas christmas]** -- Article is set during of influenced by the holiday of christmas.
* **[https://scpwiki.com/system:page-tags/tag/dystopian dystopian]** -- Imagines a non-existent society or culture, portrayed as being much worse than our current one.
* **[https://scpwiki.com/system:page-tags/tag/otherworldly otherworldly]** -- Set in another world, reality or universe. Includes works that are specifically set somewhere other than Earth, as well as portal fantasy fiction featuring travel to another world..
* **[https://scpwiki.com/system:page-tags/tag/period-piece period-piece]** -- Set during a specific period in the past.
* **[https://scpwiki.com/system:page-tags/tag/post-apocalyptic post-apocalyptic]** -- Takes place after a catastrophic event.
* **[https://scpwiki.com/system:page-tags/tag/space-opera space-opera]** -- Depicts a futuristic society in outer space or on other planets, focusing on dramatic events and adventures.
* **[https://scpwiki.com/system:page-tags/tag/western western]** -- Set in the American Frontier, during the time period known as the Wild West.
* **[https://scpwiki.com/system:page-tags/tag/utopian utopian]** -- Imagines a non-existent society or culture, portrayed as being much better than our current one.

+++ Style

Describes the style of a tale.

* **[https://scpwiki.com/system:page-tags/tag/creepypasta creepypasta]** -- story in the style of short, old-school Internet horror.
* **[https://scpwiki.com/system:page-tags/tag/first-person first-person]** -- told from a first-person perspective ("I did").
* **[https://scpwiki.com/system:page-tags/tag/foundation-format foundation-format]** -- told in the form of an SCP document.
 * //Conflicts with 'scp'//
* **[https://scpwiki.com/system:page-tags/tag/journal journal]** -- told in the form of an in universe journal written while events happen.
* **[https://scpwiki.com/system:page-tags/tag/no-dialogue no-dialogue]** -- Contains no spoken dialogue.
* **[https://scpwiki.com/system:page-tags/tag/orientation orientation]** -- Styled as an orientation lecture.
* **[https://scpwiki.com/system:page-tags/tag/second-person second-person]** -- told from a second-person perspective ("you did").
* **[https://scpwiki.com/system:page-tags/tag/worldbuilding worldbuilding]** -- Focuses on conveying information about the setting, often taking the form of an in-universe document.

+++ Other

* **[https://scpwiki.com/system:page-tags/tag/_genreless _genreless]** -- No Genre, Setting or style tags apply to this tale.

[[/tab]]
[[tab Art]]
++ Art

.

[[div class="blockquote"]]
The following applies to all tags in this category:

* Requires either 'artwork', or 'artist'

[[/div]]

+++ Style

These tags describe the art style used in the piece.

* **[https://scpwiki.com/system:page-tags/tag/animated animated]** -- Artwork is animated. Generally applies to .gif files.
 * //Superseded by 'interactive', and 'video'//
* **[https://scpwiki.com/system:page-tags/tag/cel-shaded cel-shaded]** -- Artwork with outlines drawn, then shaded using solid blocks of color or gradients. The characteristic style of animation, comic books and manga.
* **[https://scpwiki.com/system:page-tags/tag/image-editing image-editing]** -- Artwork created by altering or combining existing images.
* **[https://scpwiki.com/system:page-tags/tag/painted painted]** -- Artwork created using paint or pastel, or using digital brush strokes to blend colors and mimic the appearance of paint.
* **[https://scpwiki.com/system:page-tags/tag/pixel-art pixel-art]** -- Artwork created by drawing individual pixels, or by deliberately pixelating an existing image.
* **[https://scpwiki.com/system:page-tags/tag/sketched sketched]** -- Artwork drawn with pencil, pen or crayon, or created digitally in a similar style. May be shaded, or left as a line drawing.

+++ Content

These tags refer to the content that the artwork is depicting.

* **[https://scpwiki.com/system:page-tags/tag/goi-art goi-art]** -- Artwork depicting characters, objects, or themes from a specific Group of Interest. Also applies to GoI logos.
* **[https://scpwiki.com/system:page-tags/tag/logo logo]** -- Artwork depicts one or more logos or other symbolic graphics, such as insignia, flags and coats of arms.
* **[https://scpwiki.com/system:page-tags/tag/personnel-art personnel-art]** -- Artwork depicting specific SCP Foundation employees.
* **[https://scpwiki.com/system:page-tags/tag/poster poster]** -- Artwork depicts a poster, infographic or advertisment, using a combination of images and words to convey information.
* **[https://scpwiki.com/system:page-tags/tag/scp-art scp-art]** -- Artwork depicting one or more SCP objects or entities.

[[/tab]]
[[tab Groups]]
++ Groups

The following tags are for specific Departments or Groups of Interest.

+++ Departments

These tags are used to designate pages that prominently feature a Foundation Department or Mobile Task Force.

* **[https://scpwiki.com/system:page-tags/tag/abnormalities abnormalities]** -- Of or related to the Department of Abnormalities.
* **[https://scpwiki.com/system:page-tags/tag/last-hope last-hope]** -- Of or related to MTF Alpha-9, Last Hope.
* **[https://scpwiki.com/system:page-tags/tag/angle-grinders angle-grinders]** -- Of or related to [https://scp-wiki.wikidot.com/mtf-theta-90-hub-page Mobile Task Force Theta-90] "Angle Grinders".
* **[https://scpwiki.com/system:page-tags/tag/decommissioning-dept decommissioning-dept]** -- Of or related to the [https://scp-wiki.wikidot.com/decom-dept-hub Decommissioning Department].
* **[https://scpwiki.com/system:page-tags/tag/delta-t delta-t]** -- Of or related to the Delta T, the transtemporal Foundation agency.
* **[https://scpwiki.com/system:page-tags/tag/ethics-committee ethics-committee]** -- Of or related to the Foundation's Ethics Committee.
* **[https://scpwiki.com/system:page-tags/tag/ettra ettra]** -- Of or related to the Emergent Threat Tactical Response Authority.
* **[https://scpwiki.com/system:page-tags/tag/fire-suppression-dept fire-suppression-dept]** -- Of or related to the Foundation's Fire Suppression Department.
* **[https://scpwiki.com/system:page-tags/tag/folklore-dept folklore-dept]** -- Of or related to the [https://scp-wiki.wikidot.com/department-of-mythology-and-folkloristics-hub Department of Mythology and Folkloristics].
* **[https://scpwiki.com/system:page-tags/tag/miscommunications miscommunications]** -- Of or related to the [https://scp-wiki.wikidot.com/domc-hub Department of Miscommunications].
* **[https://scpwiki.com/system:page-tags/tag/department-of-other department-of-other]** -- Of or related to the Foundation's Department of Other, responsible for -J SCPs.
* **[https://scpwiki.com/system:page-tags/tag/pataphysics-dept pataphysics-dept]** -- Of or related to the Foundation's Pataphysics Department.
* **[https://scpwiki.com/system:page-tags/tag/procurement-liquidation-dept procurement-liquidation-dept]** -- Of or related to the Foundation's Department of Procurement and Liquidation.
* **[https://scpwiki.com/system:page-tags/tag/surrealistics-dept surrealistics-dept]** -- Of or related to the Foundation's Department of Surrealistics.
* **[https://scpwiki.com/system:page-tags/tag/tactical-theology tactical-theology]** -- Of or related to the Foundation's Department of Tactical Theology.
* **[https://scpwiki.com/system:page-tags/tag/samsara samsara]** -- Of or related to Mobile Task Force Tau-5 "Samsara".
* **[https://scpwiki.com/system:page-tags/tag/telecom-office telecom-office]** -- Of or related to the Foundation's [https://scp-wiki.wikidot.com/telecommunications-monitoring-office-hub Telecommunications Monitoring Office].
* **[https://scpwiki.com/system:page-tags/tag/unreality-dept unreality-dept]** -- Of or related to the Foundation's [https://scp-wiki.wikidot.com/unreality-hub Unreality Department].

+++ Groups of Interest

These tags are used to designate pages that prominently feature a Group of Interest.

* **[https://scpwiki.com/system:page-tags/tag/accelerate-the-future accelerate-the-future]** -- Of or related to Accelerate the Future.
* **[https://scpwiki.com/system:page-tags/tag/alexylva alexylva]** -- Of or related to the [https://scp-wiki.wikidot.com/alexylva-university-hub Alexylva University] group of interest.
* **[https://scpwiki.com/system:page-tags/tag/ambrose-restaurant ambrose-restaurant]** -- Of or related to the [https://scp-wiki.wikidot.com/ambrose-restaurant-hub Ambrose Restaurant] group of interest.
* **[https://scpwiki.com/system:page-tags/tag/anderson anderson]** -- Of or related to the [https://scp-wiki.wikidot.com/anderson-robotics-hub Anderson Robotics] group of interest.
* **[https://scpwiki.com/system:page-tags/tag/arcadia arcadia]** -- Of or related to the ##purple|[https://scp-wiki.wikidot.com/arcadia-hub Arcadia]## group of interest.
* **[https://scpwiki.com/system:page-tags/tag/are-we-cool-yet are-we-cool-yet]** -- Of or related to the [https://scp-wiki.wikidot.com/are-we-cool-yet-hub Are We Cool Yet?] (AWCY) group of interest.
* **[https://scpwiki.com/system:page-tags/tag/asci asci]** -- Of or related to the American Secure Containment Initiative.
* **[https://scpwiki.com/system:page-tags/tag/avelar avelar]** -- Of or related to the Avelar Professional Products group of interest.
* **[https://scpwiki.com/system:page-tags/tag/black-queen black-queen]** -- Of or related to the [https://scp-wiki.wikidot.com/black-queen-hub Black Queen] person or group of interest.
* **[https://scpwiki.com/system:page-tags/tag/british-occult-service british-occult-service]** -- Of or related to the British Occult Service (MI666) group of interest.
* **[https://scpwiki.com/system:page-tags/tag/broken-god broken-god]** -- Of or related to Mekhane, or the [https://scp-wiki.wikidot.com/church-of-the-broken-god-hub Church of the Broken God] (CotBG) group of interest.
* **[https://scpwiki.com/system:page-tags/tag/brothers-of-death brothers-of-death]** -- Of or related to the Brothers of Death canon or characters.
* **[https://scpwiki.com/system:page-tags/tag/chaos-insurgency chaos-insurgency]** -- Of or related to the [https://scp-wiki.wikidot.com/chaos-insurgency-hub Chaos Insurgency] (CI) group of interest.
* **[https://scpwiki.com/system:page-tags/tag/chicago-spirit chicago-spirit]** -- Of or related to the [https://scp-wiki.wikidot.com/chicago-spirit Chicago Spirit] group of interest.
* **[https://scpwiki.com/system:page-tags/tag/children-of-the-night children-of-the-night]** -- Of or related to the Children of the Night, outlined in [https://scp-wiki.wikidot.com/scp-1000 SCP-1000].
* **[https://scpwiki.com/system:page-tags/tag/children-of-the-torch children-of-the-torch]** -- SCP is of or related to the Children of the Torch group of interest.
* **[https://scpwiki.com/system:page-tags/tag/class-of-76 class-of-76]** -- Of or related to the [https://scp-wiki.wikidot.com/remembrance Class of '76] SCPs and stories.
* **[https://scpwiki.com/system:page-tags/tag/cogwork-orthodoxy cogwork-orthodoxy]** -- Of or related to the Cogwork Orthodox Church faction of the Church of the Broken God group of interest.
* **[https://scpwiki.com/system:page-tags/tag/daevite daevite]** -- Of or related to [https://scp-wiki.wikidot.com/daevite-hub the Daevites].
* **[https://scpwiki.com/system:page-tags/tag/deer-college deer-college]** -- Of or related to the [https://scp-wiki.wikidot.com/deer-college-hub Deer College] group of interest.
* **[https://scpwiki.com/system:page-tags/tag/dr-wondertainment dr-wondertainment]** -- Of or related to the [https://scp-wiki.wikidot.com/dr-wondertainment-hub Dr. Wondertainment] person or group of interest.
* **[https://scpwiki.com/system:page-tags/tag/factory factory]** -- Of or related to [https://scp-wiki.wikidot.com/factory-hub The Factory] group of interest.
* **[https://scpwiki.com/system:page-tags/tag/fifthist fifthist]** -- Of or related to [https://scp-wiki.wikidot.com/fifthist-hub The Fifth Church] group of interest.
* **[https://scpwiki.com/system:page-tags/tag/gamers-against-weed gamers-against-weed]** -- Of or related to the [https://scp-wiki.wikidot.com/gamers-against-weed-hub Gamers Against Weed] (GAW) group of interest.
* **[https://scpwiki.com/system:page-tags/tag/giftschreiber giftschreiber]** -- Of or related to the Giftschreiber (Poison Writers) group of interest.
* **[https://scpwiki.com/system:page-tags/tag/global-occult-coalition global-occult-coalition]** -- Of or related to the [https://scp-wiki.wikidot.com/goc-hub-page Global Occult Coalition (GOC)] group of interest.
* **[https://scpwiki.com/system:page-tags/tag/goldbaker-reinz goldbaker-reinz]** -- Of or related to the [https://scp-wiki.wikidot.com/goldbaker-reinz-hub Goldbaker-Reinz Ltd] group of interest.
* **[https://scpwiki.com/system:page-tags/tag/golden-horde golden-horde]** -- Of or related to the Golden Horde group of interest.
* **[https://scpwiki.com/system:page-tags/tag/greazeburger greazeburger]** -- Of or related to the [https://scp-wiki.wikidot.com/greazeburger-incorporated-hub Greazeburger Incorporated] group of interest.
* **[https://scpwiki.com/system:page-tags/tag/gru-division-p gru-division-p]** -- Of or related to the [https://scp-wiki.wikidot.com/gru-p-hub GRU Division P] group of interest.
* **[https://scpwiki.com/system:page-tags/tag/herman-fuller herman-fuller]** -- Of or related to the [https://scp-wiki.wikidot.com/herman-fuller-hub Herman Fuller's Circus of the Disquieting] group of interest.
* **[https://scpwiki.com/system:page-tags/tag/hmfscp hmfscp]** -- Of or related to His/Her Majesty's Foundation For The Study of Curiosities and Phantasmagoria.
* **[https://scpwiki.com/system:page-tags/tag/homo-sapiens-sidhe homo-sapiens-sidhe]** -- Of or related to the Fae/Homo sapiens sidhe, as outlined in [https://scp-wiki.wikidot.com/from-120-s-archives-hub From 120's Archives].
* **[https://scpwiki.com/system:page-tags/tag/horizon-initiative horizon-initiative]** -- Of or related to [https://scp-wiki.wikidot.com/horizon-initiative-hub The Horizon Initiative] group of interest.
* **[https://scpwiki.com/system:page-tags/tag/icsut icsut]** -- Of or related to the International Center for the Study of Unified Thaumatology, member of the GOC's Council of 108.
* **[https://scpwiki.com/system:page-tags/tag/ijamea ijamea]** -- Of or related to the [https://scp-wiki.wikidot.com/ijamea-hub Imperial Japanese Anomalous Matters Examination Agency] group of interest.
* **[https://scpwiki.com/system:page-tags/tag/just-girly-things just-girly-things]** -- Of or related to the Just Girly Things group of interest.
* **[https://scpwiki.com/system:page-tags/tag/madao madao]** -- Of or related to the Italian [https://scp-wiki.wikidot.com/hub-madao Medicean Academy of Occult Art] (Medicea Accademia Dell'Arte Occulta) group of interest.
* **[https://scpwiki.com/system:page-tags/tag/mages-academy mages-academy]** -- Of or related to the German [https://scp-wiki.wikidot.com/magierakademie-hub Mages Academy] group of interest.
* **[https://scpwiki.com/system:page-tags/tag/manna-charitable-foundation manna-charitable-foundation]** -- Of or related to the [https://scp-wiki.wikidot.com/manna-charitable-foundation-hub Manna Charitable Foundation] group of interest.
* **[https://scpwiki.com/system:page-tags/tag/marshall-carter-and-dark marshall-carter-and-dark]** -- Of or related to the [https://scp-wiki.wikidot.com/marshall-carter-and-dark-hub Marshall, Carter, and Dark Ltd.] (MC&D) group of interest.
* **[https://scpwiki.com/system:page-tags/tag/maxwellism maxwellism]** -- Of or related to the Church of Maxwellism faction of the Church of the Broken God group of interest.
* **[https://scpwiki.com/system:page-tags/tag/miracle-liberation-front miracle-liberation-front]** -- Of or related to the Miracle Liberation Front. A para-terrorist organization staffed by sapient anomalous entities dedicated to overthrowing the Veil.
* **[https://scpwiki.com/system:page-tags/tag/nameless nameless]** -- Of or related to the Nameless, or the Fae, outlined in [https://scp-wiki.wikidot.com/scp-4000 SCP-4000].
* **[https://scpwiki.com/system:page-tags/tag/nobody nobody]** -- Of or related to the "[https://scp-wiki.wikidot.com/nobody-hub Nobody]" person or group of interest.
* **[https://scpwiki.com/system:page-tags/tag/obearwatch obearwatch]** -- Of or related to the Obearwatch group of interest.
* **[https://scpwiki.com/system:page-tags/tag/obskura obskura]** -- Of or related to the Obskura Corps group of interest.
* **[https://scpwiki.com/system:page-tags/tag/oneiroi oneiroi]** -- Of or related to the [https://scp-wiki.wikidot.com/oneiroi Oneiroi Collective] group of interest.
* **[https://scpwiki.com/system:page-tags/tag/oria oria]** -- Of or related to the [https://scp-wiki.wikidot.com/oria-hub Office For The Reclamation of Islamic Artifacts (ORIA)] group of interest.
* **[https://scpwiki.com/system:page-tags/tag/parawatch parawatch]** -- Of or related to the [https://scp-wiki.wikidot.com/parawatch-hub Parawatch Wiki] group of interest.
* **[https://scpwiki.com/system:page-tags/tag/pattern-screamer pattern-screamer]** -- Of or related to pattern screamers.
* **[https://scpwiki.com/system:page-tags/tag/pentagram pentagram]** -- Of or related to Pentagram group of interest.
* **[https://scpwiki.com/system:page-tags/tag/prometheus prometheus]** -- Of or related to the [https://scp-wiki.wikidot.com/prometheus-labs-hub Prometheus Labs] group of interest.
* **[https://scpwiki.com/system:page-tags/tag/sapphire sapphire]** -- Of or related to the French [https://scp-wiki.wikidot.com/saphir-centre SAPPHIRE] group of interest.
* **[https://scpwiki.com/system:page-tags/tag/sarkic sarkic]** -- Of or related to the [https://scp-wiki.wikidot.com/sarkicism-hub Sarkic Cults] group of interest.
* **[https://scpwiki.com/system:page-tags/tag/scarlet-king scarlet-king]** -- Of or related to the The Scarlet King, or the [https://scp-wiki.wikidot.com/cotsk-hub Children of the Scarlet King] group of interest.
* **[https://scpwiki.com/system:page-tags/tag/second-hytoth second-hytoth]** -- Of or related to the [https://scp-wiki.wikidot.com/second-hytoth-hub Church of the Second Hytoth] group of Interest.
* **[https://scpwiki.com/system:page-tags/tag/serpents-hand serpents-hand]** -- Of or related to [https://scp-wiki.wikidot.com/serpent-s-hand-hub The Serpent's Hand] group of interest.
* **[https://scpwiki.com/system:page-tags/tag/shark-punching-center shark-punching-center]** -- Of or related to the [https://scp-wiki.wikidot.com/spc-hub Shark Punching Center] group of interest.
* **[https://scpwiki.com/system:page-tags/tag/silicon-nornir silicon-nornir]** -- Of or related to the Servants of the Silicon Nornir religion, a member of the GOC's Council of 108.
* **[https://scpwiki.com/system:page-tags/tag/sugarcomb-confectionery sugarcomb-confectionery]** -- Of or related to the Sugarcomb Confectionery group of interest.
* **[https://scpwiki.com/system:page-tags/tag/three-moons-initiative three-moons-initiative]** -- Of or related to [https://scp-wiki.wikidot.com/three-moons-initiative-hub The Three Moons Initiative] group of interest.
* **[https://scpwiki.com/system:page-tags/tag/totleighsoft totleighsoft]** -- Of or related to the anomalous software development corporation TotleighSoft.
* **[https://scpwiki.com/system:page-tags/tag/unusual-cargo unusual-cargo]** -- Of or related to the Commission on Unusual Cargo.
* **[https://scpwiki.com/system:page-tags/tag/unusual-incidents-unit unusual-incidents-unit]** -- Of or related to the Federal Bureau of Investigation [https://scp-wiki.wikidot.com/unusual-incidents-unit-hub Unusual Incidents Unit (UIU)] group of interest.
* **[https://scpwiki.com/system:page-tags/tag/valravn valravn]** -- Of or related to the [https://scp-wiki.wikidot.com/valravn-corporation-hub Valravn Corporation] group of interest.
* **[https://scpwiki.com/system:page-tags/tag/vikander-kneed vikander-kneed]** -- Of or related to the [https://scp-wiki.wikidot.com/vikander-kneed-technical-media-hub Vikander-Kneed Technical Media] group of interest.
* **[https://scpwiki.com/system:page-tags/tag/wandsmen wandsmen]** -- Of or related to [https://scp-wiki.wikidot.com/wandsmen-hub The Wandsmen] group of interest.
* **[https://scpwiki.com/system:page-tags/tag/westhead-media westhead-media]** -- Of or related to the Westhead Media group of interest.
* **[https://scpwiki.com/system:page-tags/tag/wilsons-wildlife wilsons-wildlife]** -- Of or related to the [https://scp-wiki.wikidot.com/wilson-s-wildlife-solutions-hub Wilson's Wildlife Solutions] group of interest.
* **[https://scpwiki.com/system:page-tags/tag/xia-dynasty xia-dynasty]** -- Of or related to the Xia Dynasty.

[[/tab]]
[[tab GoI Formats]]
++ GoI Formats

These are tags for GoI formats that describe which GoI the page is formatted for. There should be one tag for each GoI; however, only GoIs for which GoI Format articles exist are listed here. If there is a GoI Format article in the format of a GoI that does not have a tag, it should be tagged //_other//. Additionally, if the corresponding tag for a GoI format does not exist but there is an article that should have it, please contact staff to request it.

[[div class="blockquote"]]
The following applies to all tags in this category:

* Requires 'goi-format'

[[/div]]

* **[https://scpwiki.com/system:page-tags/tag/_alexylva _alexylva]** -- An article following the Alexylva Universiy format.
 * //Requires 'alexylva'//
* **[https://scpwiki.com/system:page-tags/tag/_ambrose-restaurant _ambrose-restaurant]** -- An article following the Ambrose Restaurants format.
 * //Requires 'ambrose-restaurant'//
* **[https://scpwiki.com/system:page-tags/tag/_anderson _anderson]** -- An article following the Anderson Robotics format.
 * //Requires 'anderson'//
* **[https://scpwiki.com/system:page-tags/tag/_arcadia _arcadia]** -- An article following the Arcadia format.
 * //Requires 'arcadia'//
* **[https://scpwiki.com/system:page-tags/tag/_are-we-cool-yet _are-we-cool-yet]** -- An article following the Are We Cool Yet? format.
 * //Requires 'are-we-cool-yet'//
* **[https://scpwiki.com/system:page-tags/tag/_black-queen _black-queen]** -- An article following the Black Queen format.
 * //Requires 'black-queen'//
* **[https://scpwiki.com/system:page-tags/tag/_broken-god _broken-god]** -- An article following the Church of the Broken God format.
 * //Requires 'broken-god'//
* **[https://scpwiki.com/system:page-tags/tag/_chaos-insurgency _chaos-insurgency]** -- An article following the Chaos Insurgency format.
 * //Requires 'chaos-insurgency'//
* **[https://scpwiki.com/system:page-tags/tag/_chicago-spirit _chicago-spirit]** -- An article following the Chicago Spirit format.
 * //Requires 'chicago-spirit'//
* **[https://scpwiki.com/system:page-tags/tag/_deer-college _deer-college]** -- An article following the Deer College format.
 * //Requires 'deer-college'//
* **[https://scpwiki.com/system:page-tags/tag/_eric _eric]** -- An article following the Eric format.
 * //Requires 'eric'//
* **[https://scpwiki.com/system:page-tags/tag/_factory _factory]** -- An article following the Factory format.
 * //Requires 'factory'//
* **[https://scpwiki.com/system:page-tags/tag/_fifthist _fifthist]** -- An article following the Fifthist format.
 * //Requires 'fifthist'//
* **[https://scpwiki.com/system:page-tags/tag/_global-occult-coalition _global-occult-coalition]** -- An article following the Global Occult Coalition format.
 * //Requires 'global-occult-coalition'//
* **[https://scpwiki.com/system:page-tags/tag/_gru-division-p _gru-division-p]** -- An article following the GRU Division P format.
 * //Requires 'gru-division-p'//
* **[https://scpwiki.com/system:page-tags/tag/_herman-fuller _herman-fuller]** -- An article following the Herman Fuller format.
 * //Requires 'herman-fuller'//
* **[https://scpwiki.com/system:page-tags/tag/_horizon-initiative _horizon-initiative]** -- An article following the Horizon Initiative format.
 * //Requires 'horizon-initiative'//
* **[https://scpwiki.com/system:page-tags/tag/_icsut _icsut]** -- An article following the International Center for the Study of Unified Thaumatology.
 * //Requires 'icsut'//
* **[https://scpwiki.com/system:page-tags/tag/_ijamea _ijamea]** -- An article following the IJAMEA format.
 * //Requires 'ijamea'//
* **[https://scpwiki.com/system:page-tags/tag/_just-girly-things _just-girly-things]** -- An article following the Just Girly Things format.
 * //Requires 'just-girly-things'//
* **[https://scpwiki.com/system:page-tags/tag/_la-rue-macabre _la-rue-macabre]** -- An article following the La Rue Macabre format.
 * //Requires 'la-rue-macabre'//
* **[https://scpwiki.com/system:page-tags/tag/_madao _madao]** -- An article following the Medicea Accademia format.
 * //Requires 'madao'//
* **[https://scpwiki.com/system:page-tags/tag/_manna-charitable-foundation _manna-charitable-foundation]** -- An article following the Manna Charitable Foundation format.
 * //Requires 'manna-charitable-foundation'//
* **[https://scpwiki.com/system:page-tags/tag/_marshall-carter-and-dark _marshall-carter-and-dark]** -- An article following the Marshall, Carter and Dark format.
 * //Requires 'marshall-carter-and-dark'//
* **[https://scpwiki.com/system:page-tags/tag/_nobody _nobody]** -- An article following the Nobody format.
 * //Requires 'nobody'//
* **[https://scpwiki.com/system:page-tags/tag/_oneiroi _oneiroi]** -- An article following the Oneiroi format.
 * //Requires 'oneiroi'//
* **[https://scpwiki.com/system:page-tags/tag/_oria _oria]** -- An article following the ORIA format.
 * //Requires 'oria'//
* **[https://scpwiki.com/system:page-tags/tag/_other _other]** -- A GoI Format following a format not associated with a tagged Group of Interest.
* **[https://scpwiki.com/system:page-tags/tag/_parawatch _parawatch]** -- An article following the Parawatch format.
 * //Requires 'parawatch'//
* **[https://scpwiki.com/system:page-tags/tag/_prometheus _prometheus]** -- An article following the Prometheus format.
 * //Requires 'prometheus'//
* **[https://scpwiki.com/system:page-tags/tag/_sapphire _sapphire]** -- An article following the SAPPHIRE format.
 * //Requires 'sapphire'//
* **[https://scpwiki.com/system:page-tags/tag/_sarkic _sarkic]** -- An article following the Sarkic format.
 * //Requires 'sarkic'//
* **[https://scpwiki.com/system:page-tags/tag/_second-hytoth _second-hytoth]** -- An article following the Second Hytoth format.
 * //Requires 'second-hytoth'//
* **[https://scpwiki.com/system:page-tags/tag/_serpents-hand _serpents-hand]** -- An article following the Serpents' Hand format.
 * //Requires 'serpents-hand'//
* **[https://scpwiki.com/system:page-tags/tag/_shark-punching-center _shark-punching-center]** -- An article following the Shark Punching Center format.
 * //Requires 'shark-punching-center'//
* **[https://scpwiki.com/system:page-tags/tag/_three-moons-initiative _three-moons-initiative]** -- An article following the Three Moons Initiative format.
 * //Requires 'three-moons-initiative'//
* **[https://scpwiki.com/system:page-tags/tag/_unusual-cargo _unusual-cargo]** -- An article following the Unusual Cargo format.
 * //Requires 'unusual-cargo'//
* **[https://scpwiki.com/system:page-tags/tag/_unusual-incidents-unit _unusual-incidents-unit]** -- An article following the Unusual Incidents Unit format.
 * //Requires 'unusual-incidents-unit'//
* **[https://scpwiki.com/system:page-tags/tag/_valravn _valravn]** -- An article following the Valravn corporation format.
 * //Requires 'valravn'//
* **[https://scpwiki.com/system:page-tags/tag/_wandsmen _wandsmen]** -- An article following the Wandsmen format.
 * //Requires 'wandsmen'//
* **[https://scpwiki.com/system:page-tags/tag/_wilsons-wildlife _wilsons-wildlife]** -- An article following the Wilsons' Wildlife format.
 * //Requires 'wilsons-wildlife'//

[[/tab]]
[[tab Canons]]
++ Canons

Tags for canons from the Canon Hub and the articles that take place in their setting.

* **[https://scpwiki.com/system:page-tags/tag/aces-and-eights aces-and-eights]** -- Of or related to the [https://scp-wiki.wikidot.com/aces-and-eights Aces and Eights] canon.
* **[https://scpwiki.com/system:page-tags/tag/aiad aiad]** -- Of or related to the [https://scp-wiki.wikidot.com/aiad-homescreen AIAD] canon.
* **[https://scpwiki.com/system:page-tags/tag/ad-astra ad-astra]** -- Of or related to the [https://scp-wiki.wikidot.com/ad-astra-per-aspera-hub Ad Astra Per Aspera] canon.
* **[https://scpwiki.com/system:page-tags/tag/alchemy-department alchemy-department]** -- Of or related to [https://scp-wiki.wikidot.com/the-alchemy-department-hub The Alchemy Department] canon.
* **[https://scpwiki.com/system:page-tags/tag/antarctic-exchange antarctic-exchange]** -- Of or related to the [https://scp-wiki.wikidot.com/antarctic-exchange-hub Antarctic Exchange] canon.
* **[https://scpwiki.com/system:page-tags/tag/apotheosis apotheosis]** -- Of or related to the [https://scp-wiki.wikidot.com/antarctic-exchange-hub Apotheosis] canon.
* **[https://scpwiki.com/system:page-tags/tag/bellerverse bellerverse]** -- Of or related to the [https://scp-wiki.wikidot.com/bellerverse Bellerverse] canon.
* **[https://scpwiki.com/system:page-tags/tag/broken-masquerade broken-masquerade]** -- Of or related to the [https://scp-wiki.wikidot.com/broken-masquerade-hub Broken Masquerade] canon.
* **[https://scpwiki.com/system:page-tags/tag/competitive-eschatology competitive-eschatology]** -- Of or related to the [https://scp-wiki.wikidot.com/Competitive-Eschatology-Hub Competitive Eschatology] canon.
* **[https://scpwiki.com/system:page-tags/tag/cool-war-2 cool-war-2]** -- Of or related to the [https://scp-wiki.wikidot.com/cool-war-2-hub Cool War 2: Ruiz From Your Grave] canon.
* **[https://scpwiki.com/system:page-tags/tag/daybreak daybreak]** -- Of or related to the [https://scp-wiki.wikidot.com/daybreak Daybreak] canon.
* **[https://scpwiki.com/system:page-tags/tag/deepwell-catalog deepwell-catalog]** -- Of or related to the [https://scp-wiki.wikidot.com/site-17-hub Site-17 Deepwell] canon.
* **[https://scpwiki.com/system:page-tags/tag/doctors-of-the-church doctors-of-the-church]** -- Of or related to the [https://scp-wiki.wikidot.com/doctors-of-the-church-hub Doctors of the Church] canon.
* **[https://scpwiki.com/system:page-tags/tag/dread&circuses dread&circuses]** -- Of or related to the [https://scp-wiki.wikidot.com/dread-circuses-hub Dread and Circuses] canon.
* **[https://scpwiki.com/system:page-tags/tag/end-of-death end-of-death]** -- Of or related to the [https://scp-wiki.wikidot.com/end-of-death-hub End of Death] canon.
* **[https://scpwiki.com/system:page-tags/tag/from-120s-archives from-120s-archives]** -- Of or related to the [https://scp-wiki.wikidot.com/from-120-s-archives-hub From 120's Archives] canon.
* **[https://scpwiki.com/system:page-tags/tag/green-king green-king]** -- Of or related to the [https://scp-wiki.wikidot.com/codename-green-king-hub Codename: Green King hub].
* **[https://scpwiki.com/system:page-tags/tag/heimdall heimdall]** -- Of or related to [https://scp-wiki.wikidot.com/Project-Heimdall Project Heimdall].
* **[https://scpwiki.com/system:page-tags/tag/insect-hell insect-hell]** -- Of or related to the [https://scp-wiki.wikidot.com/arbh-class-hub Insect Hell] canon.
* **[https://scpwiki.com/system:page-tags/tag/Lampeter Lampeter]** -- Of or related to the [https://scp-wiki.wikidot.com/lampeter-hub Lampeter] canon.
* **[https://scpwiki.com/system:page-tags/tag/lolfoundation lolfoundation]** -- Of or related to the [https://scp-wiki.wikidot.com/lolfoundation-hub-page lolFoundation] canon.
* **[https://scpwiki.com/system:page-tags/tag/man-who-wasnt-there man-who-wasnt-there]** -- Of or relating to [https://scp-wiki.wikidot.com/the-man-who-wasnt-there-hub The Man Who Wasn't There] canon.
* **[https://scpwiki.com/system:page-tags/tag/memoria-adytum memoria-adytum]** -- Of or related to the [https://scp-wiki.wikidot.com/memoria-adytum In Memoria, Adytum] canon.
* **[https://scpwiki.com/system:page-tags/tag/nightfall nightfall]** -- Of or related to the [https://scp-wiki.wikidot.com/nightfall-hub Nightfall] canon.
* **[https://scpwiki.com/system:page-tags/tag/Ninth-World Ninth-World]** -- Of or related to the [https://scp-wiki.wikidot.com/the-ninth-world-hub Ninth World] canon.
* **[https://scpwiki.com/system:page-tags/tag/no-return no-return]** -- Of or related to the [https://scp-wiki.wikidot.com/no-return-hub No Return] canon.
* **[https://scpwiki.com/system:page-tags/tag/old-man-in-the-sea old-man-in-the-sea]** -- Of or related to the [https://scp-wiki.wikidot.com/old-man-in-the-sea-hub Old Man in the Sea] canon.
* **[https://scpwiki.com/system:page-tags/tag/on-guard-43 on-guard-43]** -- Of or related to the [https://scp-wiki.wikidot.com/on-guard-43-hub On Guard 43] canon.
* **[https://scpwiki.com/system:page-tags/tag/on-mount-golgotha on-mount-golgotha]** -- Of or related to the [https://scp-wiki.wikidot.com/on-mount-golgotha-hub On Mount Golgotha] canon.
* **[https://scpwiki.com/system:page-tags/tag/only-game-in-town only-game-in-town]** -- Of or related to the [https://scp-wiki.wikidot.com/only-game-in-town-hub Only Game in Town] canon.
* **[https://scpwiki.com/system:page-tags/tag/orcadia orcadia]** -- Of or related to the Seas of Orcadia canon.
* **[https://scpwiki.com/system:page-tags/tag/pitch-haven pitch-haven]** -- Of or related to the [https://scp-wiki.wikidot.com/pitch-haven-hub Pitch Haven] canon.
* **[https://scpwiki.com/system:page-tags/tag/rats-nest rats-nest]** -- Of or related to the [https://scp-wiki.wikidot.com/rat-s-nest-hub Rat's Nest] canon.
* **[https://scpwiki.com/system:page-tags/tag/resurrection resurrection]** -- Of or related to the [https://scp-wiki.wikidot.com/resurrection Resurrection] project.
* **[https://scpwiki.com/system:page-tags/tag/s&c-plastics s&c-plastics]** -- Of or related to the [https://scp-wiki.wikidot.com/the-s-c-plastics-hub S & C Plastics] canon.
* **[https://scpwiki.com/system:page-tags/tag/ship-in-a-bottle ship-in-a-bottle]** -- Of or related to the [https://scp-wiki.wikidot.com/siabhub Ship In A Bottle] canon.
* **[https://scpwiki.com/system:page-tags/tag/simulacrum simulacrum]** -- Of or related to the [https://scp-wiki.wikidot.com/simulacrum-project-hub simulacrum] canon.
* **[https://scpwiki.com/system:page-tags/tag/sotm sotm]** -- Of or related to the [https://scp-wiki.wikidot.com/sotmhub Straight On Till Morning] canon.
* **[https://scpwiki.com/system:page-tags/tag/the-coldest-war the-coldest-war]** -- Of or related to the [https://scp-wiki.wikidot.com/the-coldest-war-hub Coldest War] canon.
* **[https://scpwiki.com/system:page-tags/tag/the-gulf the-gulf]** -- Of or related to [https://scp-wiki.wikidot.com/The-Gulf The Gulf] canon.
* **[https://scpwiki.com/system:page-tags/tag/the-trashfire the-trashfire]** -- Of or relating to [https://scp-wiki.wikidot.com/the-trashfire The Trashfire] canon.
* **[https://scpwiki.com/system:page-tags/tag/third-law third-law]** -- Of or pertaining to the [https://scp-wiki.wikidot.com/third-law-hub Third Law] canon.
* **[https://scpwiki.com/system:page-tags/tag/twisted-pines twisted-pines]** -- Of or related to the [https://scp-wiki.wikidot.com/those-twisted-pines-hub Those Twisted Pines] canon.
* **[https://scpwiki.com/system:page-tags/tag/unfounded unfounded]** -- Of or related to the [https://scp-wiki.wikidot.com/unfounded-hub Unfounded] canon.
* **[https://scpwiki.com/system:page-tags/tag/unhuman unhuman]** -- Of or related to the [https://scp-wiki.wikidot.com/unhuman-hub UnHuman] canon.
* **[https://scpwiki.com/system:page-tags/tag/war-on-all-fronts war-on-all-fronts]** -- Of or related to the [https://scp-wiki.wikidot.com/war-on-all-fronts-hub War On All Fronts] canon.
* **[https://scpwiki.com/system:page-tags/tag/wonderful-world wonderful-world]** -- Of or related to the [https://scp-wiki.wikidot.com/wonder-world What a Wonderful World] canon.

[[/tab]]
[[tab Series]]
++ Series

Tags for tale and SCP series, that may or may not have a Hub.

* **[https://scpwiki.com/system:page-tags/tag/8000-dead-rats 8000-dead-rats]** -- Part of the  [https://scp-wiki.wikidot.com/8000-dead-rats-hub 8000 dead rats series].
* **[https://scpwiki.com/system:page-tags/tag/abcs-of-death abcs-of-death]** -- Part of the ABC's of Death [https://scp-wiki.wikidot.com/scp-anthology-hub anthology].
* **[https://scpwiki.com/system:page-tags/tag/admonition admonition]** -- Of or related to [https://scp-wiki.wikidot.com/admonition the Admonition] series.
* **[https://scpwiki.com/system:page-tags/tag/anabasis anabasis]** -- Of or related to the [https://scp-wiki.wikidot.com/anabasis-hub Anabasis] stories.
* **[https://scpwiki.com/system:page-tags/tag/ao-tale ao-tale]** -- Of or related to the [https://scp-wiki.wikidot.com/ao-hub Tales of Anomalous Items] stories.
* **[https://scpwiki.com/system:page-tags/tag/appliance-war appliance-war]** -- Of or related to [https://scp-wiki.wikidot.com/the-appliance-war-hub The Appliance War] series.
* **[https://scpwiki.com/system:page-tags/tag/black-rabbit-company black-rabbit-company]** -- Of or related to the [https://scp-wiki.wikidot.com/stealingsolidarityhub Stealing Solidarity] series.
* **[https://scpwiki.com/system:page-tags/tag/bury-the-survivors bury-the-survivors]** -- Of or related to the [https://scp-wiki.wikidot.com/bury-the-survivors-hub Bury the Survivors] series.
* **[https://scpwiki.com/system:page-tags/tag/but-a-dream but-a-dream]** -- Of or related to the but a dream series.
* **[https://scpwiki.com/system:page-tags/tag/cack-hard cack-hard]** -- Of or related to the [https://scp-wiki.wikidot.com/cack-hub cack-hard] stories.
* **[https://scpwiki.com/system:page-tags/tag/classical-revival classical-revival]** -- Of or related to the [https://scp-wiki.wikidot.com/classicalrevivalindex Classical Revival] stories.
* **[https://scpwiki.com/system:page-tags/tag/collector-tale collector-tale]** -- Of or related to the Tales of Mr. Collector. (See also: //[https://scp-wiki.wikidot.com/system:page-tags/tag/mister mister]//).
* **[https://scpwiki.com/system:page-tags/tag/etdp etdp]** -- Of or related to the [https://scp-wiki.wikidot.com/etdp-hub-page Et Tam Deum Petivi] series.
* **[https://scpwiki.com/system:page-tags/tag/eternal-mxtape eternal-mxtape]** -- Of or related to the [https://scp-wiki.wikidot.com/the-eternal-mxtape Eternal MxTape] series.
* **[https://scpwiki.com/system:page-tags/tag/goc-casefiles goc-casefiles]** -- Of or related to the [https://scp-wiki.wikidot.com/goc-hub-page#toc111 Global Occult Coalition Casefiles] stories.
* **[https://scpwiki.com/system:page-tags/tag/harbinger harbinger]** -- Of or related to the Of or related to the HARBINGER stories.
* **[https://scpwiki.com/system:page-tags/tag/hecatoncheires-cycle hecatoncheires-cycle]** -- Of or related to the [https://scp-wiki.wikidot.com/hecatoncheires-cycle-hub Hecatoncheires Cycle] series.
* **[https://scpwiki.com/system:page-tags/tag/integration-program integration-program]** -- Of or related to the [https://scp-wiki.wikidot.com/integration-program-hub Integration Program] series.
* **[https://scpwiki.com/system:page-tags/tag/kiryu-labs kiryu-labs]** -- Of or related to the [https://scp-wiki.wikidot.com/kiryu-labs-hub Kiryu Labs] series.
* **[https://scpwiki.com/system:page-tags/tag/mister mister]** -- Of or related to the "Little Misters" series of anomalous individuals.
* **[https://scpwiki.com/system:page-tags/tag/mundus-Liberari mundus-Liberari]** -- Of or related to the [https://scp-wiki.wikidot.com/mundus-liberari Mundus, Liberari] series.
* **[https://scpwiki.com/system:page-tags/tag/new-faces new-faces]** -- Of or related to the [https://scp-wiki.wikidot.com/resurrection-new-faces-hub Resurrection: New Faces] series.
* **[https://scpwiki.com/system:page-tags/tag/old-foes old-foes]** -- Of or related to the [resurrection-old-foes-hub Resurrection: Old Foes] series.
* **[https://scpwiki.com/system:page-tags/tag/olympia olympia]** -- Of or related to the [https://scp-wiki.wikidot.com/Olympia-Project Olympia Project].
* **[https://scpwiki.com/system:page-tags/tag/palisade palisade]** -- Of the [https://scp-wiki.wikidot.com/project-palisade Project Palisade] series.
* **[https://scpwiki.com/system:page-tags/tag/project-crossover project-crossover]** -- Of or related to [https://scp-wiki.wikidot.com/crossoverprojectindex Project Crossover].
* **[https://scpwiki.com/system:page-tags/tag/project-thaumiel project-thaumiel]** -- Of or related to [https://scp-wiki.wikidot.com/thaumiel Project Thaumiel].
* **[https://scpwiki.com/system:page-tags/tag/team-bird team-bird]** -- Of or related to [https://scp-wiki.wikidot.com/bird Team Bird].
* **[https://scpwiki.com/system:page-tags/tag/time-after-time-password time-after-time-password]** -- Of or related to the [https://scp-wiki.wikidot.com/the-time-after-time-password-hub Time After Time Password] series.
* **[https://scpwiki.com/system:page-tags/tag/the-twin-sites the-twin-sites]** -- Of or related to the Twin Sites series.
* **[https://scpwiki.com/system:page-tags/tag/untitled-series untitled-series]** -- Error description cannot be blank [https://scp-wiki.wikidot.com/https://scp-wiki.wikidot.com/unreality-hub or linked to the click to add text] series.
* **[https://scpwiki.com/system:page-tags/tag/we-meet-again we-meet-again]** -- Of or related to the [https://scp-wiki.wikidot.com/and-every-time-we-meet-again-hub And Every Time We Meet Again] series.
* **[https://scpwiki.com/system:page-tags/tag/whore-of-blood whore-of-blood]** -- Of or related to the [https://scp-wiki.wikidot.com/whore-of-blood-hub Whore of Blood] series.
* **[https://scpwiki.com/system:page-tags/tag/w-i-t-c-h w-i-t-c-h]** -- Of or relating to the Weaving Imperceptible Threads Continuity.
* **[https://scpwiki.com/system:page-tags/tag/wrong-tomorrow wrong-tomorrow]** -- Of or related to the [https://scp-wiki.wikidot.com/wrong-tomorrow-hub Wrong Tomorrow] series.
* **[https://scpwiki.com/system:page-tags/tag/yggdrasil-s-surveyor yggdrasil-s-surveyor]** -- Of or related to the cross-canon series [https://scp-wiki.wikidot.com/yggdrasils-surveyor Yggdrasil's Surveyor].

[[/tab]]
[[tab Characters]]
++ Characters

Tags indicating that a specific character has a significant presence within the article. Divided into Foundation Employees, SCP Objects, and Persons of Interest.

+++ Foundation Employees

Employees of the Foundation.

* **[https://scpwiki.com/system:page-tags/tag/8-ball 8-ball]** -- 8-ball, aka 8B-A1, an artificial intelligence.
* **[https://scpwiki.com/system:page-tags/tag/aaron-siegel aaron-siegel]** -- Aaron Siegel, O5-1.
* **[https://scpwiki.com/system:page-tags/tag/agent-adams agent-adams]** -- Agent Andrea Adams.
* **[https://scpwiki.com/system:page-tags/tag/agent-calendar agent-calendar]** -- Site-666 Director's Adjutant, Wrath demoness, and all-around badass.
* **[https://scpwiki.com/system:page-tags/tag/agent-green agent-green]** -- Agent Green.
* **[https://scpwiki.com/system:page-tags/tag/agent-kazmarek agent-kazmarek]** -- Agent Travis Kazmarek.
* **[https://scpwiki.com/system:page-tags/tag/agent-laferrier agent-laferrier]** -- Agent V.A. LaFerrier.
* **[https://scpwiki.com/system:page-tags/tag/agent-lament agent-lament]** -- Agent Troy Lament.
* **[https://scpwiki.com/system:page-tags/tag/agent-lurk agent-lurk]** -- Agent Dietrich M. Lurk.
* **[https://scpwiki.com/system:page-tags/tag/agent-merlo agent-merlo]** -- Agent Sasha Merlo.
* **[https://scpwiki.com/system:page-tags/tag/agent-navarro agent-navarro]** -- Agent Daniel Navarro.
* **[https://scpwiki.com/system:page-tags/tag/agent-popescu agent-popescu]** -- Agent Lucretia Popescu.
* **[https://scpwiki.com/system:page-tags/tag/agent-rodney agent-rodney]** -- Agent Rodney, a seasoned agent who is primarily concerned with cases related to the Miracle Liberation Front..
* **[https://scpwiki.com/system:page-tags/tag/agent-strelnikov agent-strelnikov]** -- Agent Dmitri Strelnikov.
* **[https://scpwiki.com/system:page-tags/tag/agent-trauss agent-trauss]** -- Agent Trauss, aka C-51174.
* **[https://scpwiki.com/system:page-tags/tag/agent-yoric agent-yoric]** -- Agent Yoric Elroy, aka Jack "Poor Yoric" Dawkins.
* **[https://scpwiki.com/system:page-tags/tag/alexandra alexandra]** -- Alexandra, an artificial intelligence.
* **[https://scpwiki.com/system:page-tags/tag/alex-thorley alex-thorley]** -- Alex Thorley of the Department of Unreality.
* **[https://scpwiki.com/system:page-tags/tag/chief-ibanez chief-ibanez]** -- Diminutive leader of Site-43's Mobile Task Forces. Tough as nails, takes zero shit, leads by example and does not delegate.
* **[https://scpwiki.com/system:page-tags/tag/bailey-brothers bailey-brothers]** -- Tristan, Thomas and Trevor Bailey.
* **[https://scpwiki.com/system:page-tags/tag/captain-adrian captain-adrian]** -- Adrian, AKA SCP-6159-2: Familiar, Boat Captain, Paralegal, Emotional Support Animal.
* **[https://scpwiki.com/system:page-tags/tag/d-7294 d-7294]** -- D-7294.
* **[https://scpwiki.com/system:page-tags/tag/d-11424 d-11424]** -- D-11424.
* **[https://scpwiki.com/system:page-tags/tag/director-aktus director-aktus]** -- Director Aktus.
* **[https://scpwiki.com/system:page-tags/tag/director-bold director-bold]** -- Director Cal Bold of the Decommissioning Department.
* **[https://scpwiki.com/system:page-tags/tag/director-bohart director-bohart]** -- Vincent Bohart, the Director of Site-333, who does not have a PhD.
* **[https://scpwiki.com/system:page-tags/tag/director-diaghilev director-diaghilev]** -- Director Ruslav Diaghilev of the Alchemy Department.
* **[https://scpwiki.com/system:page-tags/tag/director-gillespie director-gillespie]** -- Director Gillespie.
* **[https://scpwiki.com/system:page-tags/tag/director-mcinnis director-mcinnis]** -- Dr. Allan J. McInnis, Director of Site-43.
* **[https://scpwiki.com/system:page-tags/tag/director-mctiriss director-mctiriss]** -- Director Kate McTiriss.
* **[https://scpwiki.com/system:page-tags/tag/director-moose director-moose]** -- Director Moose.
* **[https://scpwiki.com/system:page-tags/tag/director-richter director-richter]** -- Director of Site-78 Leah Richter.
* **[https://scpwiki.com/system:page-tags/tag/director-scout director-scout]** -- Vivian L. Scout, late Site-43 co-director.
* **[https://scpwiki.com/system:page-tags/tag/director-lague director-lague]** -- Director Paul Lague, of the Integration Program and Site-322.
* **[https://scpwiki.com/system:page-tags/tag/django-bridge django-bridge]** -- Django Bridge.
* **[https://scpwiki.com/system:page-tags/tag/doctor-asheworth doctor-asheworth]** -- Dr. Daniel Asheworth.
* **[https://scpwiki.com/system:page-tags/tag/doctor-blank doctor-blank]** -- Dr. Harold R. Blank.
* **[https://scpwiki.com/system:page-tags/tag/doctor-bright doctor-bright]** -- Dr. Bright.
* **[https://scpwiki.com/system:page-tags/tag/doctor-cimmerian doctor-cimmerian]** -- Dr. Cimmerian.
* **[https://scpwiki.com/system:page-tags/tag/doctor-clef doctor-clef]** -- Dr. Alto Clef.
* **[https://scpwiki.com/system:page-tags/tag/doctor-dan doctor-dan]** -- Dr. Dan ███████, of SCP-096.
* **[https://scpwiki.com/system:page-tags/tag/doctor-edison doctor-edison]** -- Dr. Michael Edison.
* **[https://scpwiki.com/system:page-tags/tag/doctor-elliott doctor-elliott]** -- Dr. Chelsea Elliott.
* **[https://scpwiki.com/system:page-tags/tag/doctor-elstrom doctor-elstrom]** -- Site-43's chief administrative officer Doctor Elstrom.
* **[https://scpwiki.com/system:page-tags/tag/doctor-everwood doctor-everwood]** -- Dr. Everwood, GOI specialist.
* **[https://scpwiki.com/system:page-tags/tag/doctor-fynegan doctor-fynegan]** -- Dr. Fynegan.
* **[https://scpwiki.com/system:page-tags/tag/doctor-gears doctor-gears]** -- Dr. Gears.
* **[https://scpwiki.com/system:page-tags/tag/doctor-gerald doctor-gerald]** -- Dr. Gerald.
* **[https://scpwiki.com/system:page-tags/tag/doctor-glass doctor-glass]** -- Dr. Simon Glass.
* **[https://scpwiki.com/system:page-tags/tag/doctor-heiden doctor-heiden]** -- Dr. Frederick Heiden.
* **[https://scpwiki.com/system:page-tags/tag/doctor-hoygull doctor-hoygull]** -- Dr. Hoygull, Avian Division.
* **[https://scpwiki.com/system:page-tags/tag/doctor-iceberg doctor-iceberg]** -- Dr. Iceberg.
* **[https://scpwiki.com/system:page-tags/tag/doctor-king doctor-king]** -- Dr. King.
* **[https://scpwiki.com/system:page-tags/tag/doctor-kondraki doctor-kondraki]** -- Dr. Kondraki.
* **[https://scpwiki.com/system:page-tags/tag/doctor-light doctor-light]** -- Dr. Sophia N. Light.
* **[https://scpwiki.com/system:page-tags/tag/doctor-lillihammer doctor-lillihammer]** -- Dr. Lillian S. Lillihammer.
* **[https://scpwiki.com/system:page-tags/tag/doctor-mann doctor-mann]** -- Dr. Everett Mann.
* **[https://scpwiki.com/system:page-tags/tag/doctor-mcdoctorate doctor-mcdoctorate]** -- Dr. Placeholder McDoctorate, previously known as Director Nathan Valis.
* **[https://scpwiki.com/system:page-tags/tag/doctor-reynders doctor-reynders]** -- Dr. Ilse Reynders.
* **[https://scpwiki.com/system:page-tags/tag/doctor-rights doctor-rights]** -- Dr. Rights.
* **[https://scpwiki.com/system:page-tags/tag/doctor-rivera doctor-rivera]** -- Dr. Jessie Rivera.
* **[https://scpwiki.com/system:page-tags/tag/doctor-roget doctor-roget]** -- Dr. Ralph Roget.
* **[https://scpwiki.com/system:page-tags/tag/doctor-scranton doctor-scranton]** -- Dr. Robert Scranon, inventor of the scranton reality anchor, see SCP-3001.
* **[https://scpwiki.com/system:page-tags/tag/doctor-shaw doctor-shaw]** -- Dr. Elias Blake Shaw AKA SCP-963.
* **[https://scpwiki.com/system:page-tags/tag/doctor-sinclair doctor-sinclair]** -- Dr. Katherine Sinclair.
* **[https://scpwiki.com/system:page-tags/tag/doctor-sokolsky doctor-sokolsky]** -- Dr. Daniil Sokolsky.
* **[https://scpwiki.com/system:page-tags/tag/doctor-sorts doctor-sorts]** -- Dr. Johannes Sorts.
* **[https://scpwiki.com/system:page-tags/tag/doctor-thereven doctor-thereven]** -- Doctor Cole Thereven.
* **[https://scpwiki.com/system:page-tags/tag/doctor-vang doctor-vang]** -- Dr. S. Vang.
* **[https://scpwiki.com/system:page-tags/tag/doctor-wettle doctor-wettle]** -- Dr. William Wallace Wettle.
* **[https://scpwiki.com/system:page-tags/tag/draven-kondraki draven-kondraki]** -- Dr./Director Draven Kondraki.
* **[https://scpwiki.com/system:page-tags/tag/general-bowe general-bowe]** -- General Bowe.
* **[https://scpwiki.com/system:page-tags/tag/glacon glacon]** -- Glacon.aic, an artificial intelligence.
* **[https://scpwiki.com/system:page-tags/tag/greg-chudley greg-chudley]** -- Researcher Greg Chudley of Site-78.
* **[https://scpwiki.com/system:page-tags/tag/james-harkness james-harkness]** -- James Harkness, a disgruntled network admin with an abnormally high Cognitive Resistance Value.
* **[https://scpwiki.com/system:page-tags/tag/judith-low judith-low]** -- Dr. Judith Low, Department of History.
* **[https://scpwiki.com/system:page-tags/tag/kain-pathos-crow kain-pathos-crow]** -- Professor Kain Pathos Crow.
* **[https://scpwiki.com/system:page-tags/tag/lombardi lombardi]** -- [https://scp-wiki.wikidot.com/the-lombardi-tales Agent Lombardi].
* **[https://scpwiki.com/system:page-tags/tag/maria-jones maria-jones]** -- Maria Jones, of RAISA.
* **[https://scpwiki.com/system:page-tags/tag/maria-johnston maria-johnston]** -- Researcher Maria Johnston of Site-78.
* **[https://scpwiki.com/system:page-tags/tag/marie-surratt marie-surratt]** -- Marie Surratt, an ex-Foundation agent and a paranormal gangster.
* **[https://scpwiki.com/system:page-tags/tag/marion-wheeler marion-wheeler]** -- Marion Wheeler, of the Antimemetics Division.
* **[https://scpwiki.com/system:page-tags/tag/mark-kiryu mark-kiryu]** -- Mark Kiryu of Kiryu Labs.
* **[https://scpwiki.com/system:page-tags/tag/odongo-tejani odongo-tejani]** -- Odongo Tejani, chairman of the Ethics Committee.
* **[https://scpwiki.com/system:page-tags/tag/philip-deering philip-deering]** -- Philip E. Deering, formerly [https://scp-wiki.wikidot.com/scp-5056 SCP-5056-B].
* **[https://scpwiki.com/system:page-tags/tag/primrose-esquire primrose-esquire]** -- Primrose Fatish Von Trevil, AKA SCP-6159-1: Lawyer, archdemon, Whore of Blood, Matchmaker.
* **[https://scpwiki.com/system:page-tags/tag/professor-bjornsen professor-bjornsen]** -- Professor Anders Bjornsen.
* **[https://scpwiki.com/system:page-tags/tag/researcher-conwell researcher-conwell]** -- Researcher Jacob Conwell.
* **[https://scpwiki.com/system:page-tags/tag/researcher-james researcher-james]** -- Junior Researcher James, best foundation researcher ever! (Age 5).
* **[https://scpwiki.com/system:page-tags/tag/researcher-labelle researcher-labelle]** -- Researcher Rose Labelle.
* **[https://scpwiki.com/system:page-tags/tag/researcher-lloyd researcher-lloyd]** -- Researcher Lloyd, Destroyer of Worlds.
* **[https://scpwiki.com/system:page-tags/tag/researcher-rosen researcher-rosen]** -- Researcher David Rosen.
* **[https://scpwiki.com/system:page-tags/tag/researcher-rex researcher-rex]** -- Doctor Everwood's assistant and Junior Researcher, Rex Alces.
* **[https://scpwiki.com/system:page-tags/tag/researcher-smalls researcher-smalls]** -- Researcher Adamo Smalls.
* **[https://scpwiki.com/system:page-tags/tag/researcher-talloran researcher-talloran]** -- Researcher Talloran.
* **[https://scpwiki.com/system:page-tags/tag/riven-mercer riven-mercer]** -- Riven Mercer of Kiryu Labs.
* **[https://scpwiki.com/system:page-tags/tag/sheldon-katz sheldon-katz]** -- Sheldon Katz, of the Legal Department.
* **[https://scpwiki.com/system:page-tags/tag/samara-maclear samara-maclear]** -- Samara Maclear, Foundation Psionics Specialist.
* **[https://scpwiki.com/system:page-tags/tag/simon-pietrykau simon-pietrykau]** -- Simon Pietrykau, of the Department of Analytics.
* **[https://scpwiki.com/system:page-tags/tag/thad-xyank thad-xyank]** -- Dr. Thaddeus "Thad" Xyank, of the Department of Temporal Anomalies.
* **[https://scpwiki.com/system:page-tags/tag/the-administrator the-administrator]** -- The Administrator (as a separate entity from the O5 Council).
* **[https://scpwiki.com/system:page-tags/tag/yossarian-leiner yossarian-leiner]** -- Yossarian Leiner, Director of the Department of Tactical Theology..
* **[https://scpwiki.com/system:page-tags/tag/zyn-kiryu zyn-kiryu]** -- Researcher Zyn Kiryu.

+++ SCP Objects

SCP Objects with their own character tags.

* **[https://scpwiki.com/system:page-tags/tag/able able]** -- Able, aka [https://scp-wiki.wikidot.com/scp-076 SCP-076-2].
* **[https://scpwiki.com/system:page-tags/tag/alexei-belitrov alexei-belitrov]** -- Alexei Belitrov, aka [https://scp-wiki.wikidot.com/scp-2273 SCP-2273].
* **[https://scpwiki.com/system:page-tags/tag/alleged-god alleged-god]** -- "God", aka [https://scp-wiki.wikidot.com/scp-343 SCP-343].
* **[https://scpwiki.com/system:page-tags/tag/blackwood blackwood]** -- [https://scp-wiki.wikidot.com/new Lord Blackwood, Explorer and Gentleman], aka [https://scp-wiki.wikidot.com/scp-1867 SCP-1867].
* **[https://scpwiki.com/system:page-tags/tag/bobble-the-clown bobble-the-clown]** -- Bobble The Clown, aka [https://scp-wiki.wikidot.com/scp-993 SCP-993].
* **[https://scpwiki.com/system:page-tags/tag/bones bones]** -- Bones, aka [https://scp-wiki.wikidot.com/scp-2721 SCP-2721-LORD] or Eli.
* **[https://scpwiki.com/system:page-tags/tag/cain cain]** -- Cain, aka [https://scp-wiki.wikidot.com/scp-073 SCP-073].
* **[https://scpwiki.com/system:page-tags/tag/Blue-blooded-alien Blue-blooded-alien]** -- Blue Blooded, aka [https://scp-wiki.wikidot.com/scp-6118 SCP-6118].
* **[https://scpwiki.com/system:page-tags/tag/cousin-johnny cousin-johnny]** -- Cousin Johnny, aka [https://scp-wiki.wikidot.com/scp-2852 SCP-2852].
* **[https://scpwiki.com/system:page-tags/tag/doctor-spanko doctor-spanko]** -- [https://scp-wiki.wikidot.com/doctor-spanko-hub Dr. Spanko], aka [https://scp-wiki.wikidot.com/scp-2337 SCP-2337].
* **[https://scpwiki.com/system:page-tags/tag/donkman donkman]** -- Ulysses B. Donkman, aka [https://scp-wiki.wikidot.com/scp-4768 SCP-4768].
* **[https://scpwiki.com/system:page-tags/tag/fred fred]** -- Fred, aka [https://scp-wiki.wikidot.com/scp-423 SCP-423].
* **[https://scpwiki.com/system:page-tags/tag/grabnok grabnok]** -- Grabnok the Destroyer, the Reluctant Dimension Hopper, aka [https://scp-wiki.wikidot.com/scp-507 SCP-507].
* **[https://scpwiki.com/system:page-tags/tag/geoffrey-quincy-harrison geoffrey-quincy-harrison]** -- Geoffrey Quincy Harrison III, a sassy gumball machine stationed in Site-322’s accounting department, aka [https://scp-wiki.wikidot.com/scp-5595 SCP-5595].
* **[https://scpwiki.com/system:page-tags/tag/hard-to-destroy-reptile hard-to-destroy-reptile]** -- The "Hard-To-Destroy Reptile", aka [https://scp-wiki.wikidot.com/scp-682 SCP-682].
* **[https://scpwiki.com/system:page-tags/tag/half-cat-josie half-cat-josie]** -- Josie the half cat, aka [https://scp-wiki.wikidot.com/scp-529 SCP-529].
* **[https://scpwiki.com/system:page-tags/tag/heather-mason heather-mason]** -- Heather Mason, aka "Ms. Mad About Video Games" or [https://scp-wiki.wikidot.com/scp-3090 SCP-3090].
* **[https://scpwiki.com/system:page-tags/tag/hogslice hogslice]** -- Hogslice, aka [https://scp-wiki.wikidot.com/scp-6599 SCP-6599].
* **[https://scpwiki.com/system:page-tags/tag/iris-thompson iris-thompson]** -- Iris Thompson, aka [https://scp-wiki.wikidot.com/scp-105 SCP-105].
* **[https://scpwiki.com/system:page-tags/tag/leslie leslie]** -- Leslie, instance of [https://scp-wiki.wikidot.com/scp-3774 SCP-3774].
* **[https://scpwiki.com/system:page-tags/tag/moon-champion moon-champion]** -- Moon Champion, aka Champion of the Moon or [https://scp-wiki.wikidot.com/scp-1233 SCP-1233].
* **[https://scpwiki.com/system:page-tags/tag/mr-fish mr-fish]** -- Mr. Fish, Little Mister from Dr. Wondertainment, aka [https://scp-wiki.wikidot.com/scp-527 SCP-527].
* **[https://scpwiki.com/system:page-tags/tag/murphy-law murphy-law]** -- Pataphysical noir detective character Murphy Law aka, [https://scp-wiki.wikidot.com/scp-3143 SCP-3143].
* **[https://scpwiki.com/system:page-tags/tag/old-ai old-ai]** -- "Old AI", aka [https://scp-wiki.wikidot.com/scp-079 SCP-079].
* **[https://scpwiki.com/system:page-tags/tag/plague-doctor plague-doctor]** -- The Plague Doctor, aka [https://scp-wiki.wikidot.com/scp-049 SCP-049].
* **[https://scpwiki.com/system:page-tags/tag/possessive-mask possessive-mask]** -- The Possessive Mask, aka [https://scp-wiki.wikidot.com/scp-035 SCP-035].
* **[https://scpwiki.com/system:page-tags/tag/rainer-miller rainer-miller]** -- Rainer Miller, aka [https://scp-wiki.wikidot.com/scp-4051 SCP-4051].
* **[https://scpwiki.com/system:page-tags/tag/sauelsuesor sauelsuesor]** -- Sauelsuesor, aka [https://scp-wiki.wikidot.com/scp-179 SCP-179].
* **[https://scpwiki.com/system:page-tags/tag/shy-guy shy-guy]** -- The Shy Guy, aka [https://scp-wiki.wikidot.com/scp-096 SCP-096].
* **[https://scpwiki.com/system:page-tags/tag/sigurros sigurros]** -- Sigurrós Stefánsdóttir, aka [https://scp-wiki.wikidot.com/scp-239 SCP-239].
* **[https://scpwiki.com/system:page-tags/tag/teenage-gaea teenage-gaea]** -- Meri, aka [https://scp-wiki.wikidot.com/scp-166 SCP-166] (post rewrite).
* **[https://scpwiki.com/system:page-tags/tag/ten-dots ten-dots]** -- [https://scp-wiki.wikidot.com/scp-2521 SCP-2521].
* **[https://scpwiki.com/system:page-tags/tag/the-old-man the-old-man]** -- The Old Man, aka [https://scp-wiki.wikidot.com/scp-106 SCP-106].
* **[https://scpwiki.com/system:page-tags/tag/tickle-monster tickle-monster]** -- The Tickle Monster, aka [https://scp-wiki.wikidot.com/scp-999 SCP-999].
* **[https://scpwiki.com/system:page-tags/tag/the-sculpture the-sculpture]** -- The Sculpture, aka [https://scp-wiki.wikidot.com/scp-173 SCP-173].
* **[https://scpwiki.com/system:page-tags/tag/the-specter the-specter]** -- The Specter, aka [https://scp-wiki.wikidot.com/scp-4944 SCP-4944].

+++ Persons of Interest

Other individuals involved in the anomalous.

* **[https://scpwiki.com/system:page-tags/tag/aldon aldon]** -- Aldon, an anartist.
* **[https://scpwiki.com/system:page-tags/tag/big-cheese-horace big-cheese-horace]** -- Big Cheese Horace of the Fifthists
* **[https://scpwiki.com/system:page-tags/tag/brainy-brian brainy-brian]** -- Brainy Brian of Wondertainment/MC&D, also known as "Doctor Neurosis".
* **[https://scpwiki.com/system:page-tags/tag/chaz-ambrose chaz-ambrose]** -- Chaz Ambrose, founder of Ambrose Restaurants.
* **[https://scpwiki.com/system:page-tags/tag/dado dado]** -- [https://scp-wiki.wikidot.com/dado-hub dado] is taking care of u in dis one. u no worry.
* **[https://scpwiki.com/system:page-tags/tag/damien-nowak damien-nowak]** -- Damien Nowak, cult leader.
* **[https://scpwiki.com/system:page-tags/tag/dc-al-fine dc-al-fine]** -- D.C. al Fine, Undersecretary-General of the Global Occult Coalition.
* **[https://scpwiki.com/system:page-tags/tag/eric eric]** -- Eric, a mysterious creator of anomalies.
* **[https://scpwiki.com/system:page-tags/tag/esther-kogan esther-kogan]** -- Esther Kogan, aka lesbian_gengar of Gamers Against Weed.
* **[https://scpwiki.com/system:page-tags/tag/faeowynn-wilson faeowynn-wilson]** -- Faeowynn "Fae" Wilson, of Wilson's Wildlife Solutions.
* **[https://scpwiki.com/system:page-tags/tag/finnegan finnegan]** -- Finnegan, anartist.
* **[https://scpwiki.com/system:page-tags/tag/grand-karcist-ion grand-karcist-ion]** -- Grand Karcist Ion, founder of Sarkicism.
* **[https://scpwiki.com/system:page-tags/tag/halyna-ieva halyna-ieva]** -- Karcist Halyna Ieva, aka [https://scp-wiki.wikidot.com/mother-who-demands-ones-toes The Mother Who Demands One's Toes].
* **[https://scpwiki.com/system:page-tags/tag/hanged-king hanged-king]** -- The Hanged King of Alagadda.
* **[https://scpwiki.com/system:page-tags/tag/holly-light holly-light]** -- Holly Light, of Dr Wondertainment.
* **[https://scpwiki.com/system:page-tags/tag/icky icky]** -- Veronica Mason, aka [https://scp-wiki.wikidot.com/icky-the-magic-clown Icky the Magic Clown] of Herman Fuller's Circus of the Disquieting.
* **[https://scpwiki.com/system:page-tags/tag/iris-dark iris-dark]** -- Iris Dark, of Marshall, Carter & Dark Ltd.
* **[https://scpwiki.com/system:page-tags/tag/isabel-v isabel-v]** -- Isabel Helga Anastasia Parvati Wondertainment V.
* **[https://scpwiki.com/system:page-tags/tag/jockjamsvol6 jockjamsvol6]** -- JJ, aka jockjamsvol6 of Gamers Against Weed.
* **[https://scpwiki.com/system:page-tags/tag/jude-kriyot jude-kriyot]** -- Jude Kriyot, aka bluntfiend of Gamers Against Weed.
* **[https://scpwiki.com/system:page-tags/tag/judy-papill judy-papill]** -- Judy Papill, aka Judy the Tongue of Doctor Wondertainment.
* **[https://scpwiki.com/system:page-tags/tag/kenneth-spencer kenneth-spencer]** -- Kenneth Spencer, of the FBI Unusual Investigations Unit.
* **[https://scpwiki.com/system:page-tags/tag/kindness kindness]** -- A kind man.
* **[https://scpwiki.com/system:page-tags/tag/legate-trunnion legate-trunnion]** -- Legate Trunnion, prophet of the Cogwork Orthodoxy.
* **[https://scpwiki.com/system:page-tags/tag/lewitt-zairi-family lewitt-zairi-family]** -- The Lewitt Zairi Family, of the Horizon Initiative.
* **[https://scpwiki.com/system:page-tags/tag/lovataar lovataar]** -- Lovataar, the ex-daeva princess who became one of the Klavigars.
* **[https://scpwiki.com/system:page-tags/tag/manny manny]** -- Manny, aka The Man With the Upside Down Face of Herman Fuller's Circus of the Disquieting.
* **[https://scpwiki.com/system:page-tags/tag/mari-macphaerson mari-macphaerson]** -- Mari MacPhaerson, the VP of Public Relations from Vikander-Kneed Technical Studies.
* **[https://scpwiki.com/system:page-tags/tag/nadox nadox]** -- Nadox, one of the four Klavigars of Sarkicism.
* **[https://scpwiki.com/system:page-tags/tag/olivie-gwyneth olivie-gwyneth]** -- olivie-gwyneth, Head archivist of the Sidhe Lounge.
* **[https://scpwiki.com/system:page-tags/tag/orok orok]** -- Orok, one of the four Klavigars of Sarkicism.
* **[https://scpwiki.com/system:page-tags/tag/pangloss pangloss]** -- Pangloss, mythical figure and leaver of notes.
* **[https://scpwiki.com/system:page-tags/tag/percival-darke percival-darke]** -- Percival Darke, founder of Marshall, Carter and Dark AKA the Deathless Merchant of London.
* **[https://scpwiki.com/system:page-tags/tag/polaricecraps polaricecraps]** -- Polaricecraps, of Gamers Against Weed.
* **[https://scpwiki.com/system:page-tags/tag/queen-mab queen-mab]** -- Queen Mab, a Fae tyrant and goddess.
* **[https://scpwiki.com/system:page-tags/tag/professor-aw professor-aw]** -- Professor A.W., inventor and creator of curiosities.
* **[https://scpwiki.com/system:page-tags/tag/richard-chappell richard-chappell]** -- Richard Davis Chappell, founder of the Chicago Spirit.
* **[https://scpwiki.com/system:page-tags/tag/robert-bumaro robert-bumaro]** -- Robert Bumaro, prophet of Mekhane.
* **[https://scpwiki.com/system:page-tags/tag/robin-thorne robin-thorne]** -- Robin Thorne, of the FBI Unusual Investigations Unit.
* **[https://scpwiki.com/system:page-tags/tag/ruiz-duchamp ruiz-duchamp]** -- Ruiz Duchamp, an anartist.
* **[https://scpwiki.com/system:page-tags/tag/saint-hedwig saint-hedwig]** -- Saint Hedwig, a prophet of Maxwellism.
* **[https://scpwiki.com/system:page-tags/tag/saarn saarn]** -- Saarn, one of the four Klavigars of Sarkicism.
* **[https://scpwiki.com/system:page-tags/tag/saturn-deer saturn-deer]** -- Saturn Deer, serial reincarnator and false prophet.
* **[https://scpwiki.com/system:page-tags/tag/the-engineer the-engineer]** -- The Engineer, of the Chaos Insurgency.
* **[https://scpwiki.com/system:page-tags/tag/the-critic the-critic]** -- The Critic, of Are We Cool Yet.
* **[https://scpwiki.com/system:page-tags/tag/thilo-zwist thilo-zwist]** -- Thilo Zwist, memeticist.
* **[https://scpwiki.com/system:page-tags/tag/tim-wilson tim-wilson]** -- Tim Wilson, of Wilson's Wildlife Solutions.
* **[https://scpwiki.com/system:page-tags/tag/veronica-fitzroy veronica-fitzroy]** -- Veronica Katherine Fitzroy, anartist/D-class.
* **[https://scpwiki.com/system:page-tags/tag/vincent-anderson vincent-anderson]** -- Vincent Anderson, of Anderson Robotics.

[[/tab]]
[[tab Locations]]
++ Locations

Tags indicating that a tale or SCP article takes place in a specific time/location that isn't a Foundation Site or installation.

* **[https://scpwiki.com/system:page-tags/tag/7th-occult-war 7th-occult-war]** -- The Seventh Occult War between the Allied Occult Initiative and the Obskuracorps.
* **[https://scpwiki.com/system:page-tags/tag/alagadda alagadda]** -- The kingdom of Alagadda.
* **[https://scpwiki.com/system:page-tags/tag/backdoor-soho backdoor-soho]** -- The city of Backdoor Soho.
* **[https://scpwiki.com/system:page-tags/tag/deus-ex-machina deus-ex-machina]** -- Related to the Foundation's world rebooting machine SCP-2000.
* **[https://scpwiki.com/system:page-tags/tag/esterberg esterberg]** -- The Free Port known as Esterberg.
* **[https://scpwiki.com/system:page-tags/tag/eurtec eurtec]** -- The metropolis of Eurtec.
* **[https://scpwiki.com/system:page-tags/tag/hy-brasil hy-brasil]** -- The island of Hy-Brasil.
* **[https://scpwiki.com/system:page-tags/tag/la-rue-macabre la-rue-macabre]** -- The free port of La Rue Macabre.
* **[https://scpwiki.com/system:page-tags/tag/three-portlands three-portlands]** -- The city of Three Portlands.
* **[https://scpwiki.com/system:page-tags/tag/undervegas undervegas]** -- The demonic city of Undervegas.
* **[https://scpwiki.com/system:page-tags/tag/wanderers-library wanderers-library]** -- The Wanderer's Library.

[[/tab]]
[[tab Content Markers]]
++ Content Markers

Tags for noting specific content.

* **[https://scpwiki.com/system:page-tags/tag/_adult _adult]** -- Denotes mature content, view at your own discretion.
* **[https://scpwiki.com/system:page-tags/tag/audio audio]** -- //audio// pages are pages with one or more audio files attached.
* **[https://scpwiki.com/system:page-tags/tag/interactive interactive]** -- The article contains elements that require user input or interaction, e.g. making a decision (making the user click a single link or open a collapsible does not count).
 * //Supersedes 'animated'//
* **[https://scpwiki.com/system:page-tags/tag/video video]** -- //video// pages are pages with one or more video files attached.
 * //Supersedes 'animated'//
* **[https://scpwiki.com/system:page-tags/tag/_listpages _listpages]** -- A tag to denote that this page is an LPT article. LPT (ListPages Presented Text) means that the article presents its content through offsets served via ListPages.

[[/tab]]
[[tab Staff Process]]
++ Staff Process

These tags are added only used by SCP Wiki staff, and are intended to designate articles under staff process.

* **[https://scpwiki.com/system:page-tags/tag/in-rewrite in-rewrite]** -- This is a temporary tag that may be placed on an article //by members of the Rewrite Team// only. It indicates the article is currently being rewritten and should be removed when said rewrite is posted. It should only be placed on articles where for reasons of site history, the original article will not be deleted before the rewrite is posted.
* **[https://scpwiki.com/system:page-tags/tag/rewritable rewritable]** -- This is a temporary tag that may be be placed on an article //by members of the Rewrite Team// only. It indicates that the article is eligible to be rewritten due to circumstances falling outside the usual case of low rating and old age.
* **[https://scpwiki.com/system:page-tags/tag/rewrite rewrite]** -- This tag indicates that the article in question is a rewrite of another article.
* **[https://scpwiki.com/system:page-tags/tag/deletion-range deletion-range]** -- This is a temporary tag that indicates the article is currently being voted on for deletion. It should only be placed on articles where a deletion vote has been started. Other tags should be removed when this tag is added to a page. Remove if deletion is permanently cancelled for whatever reason.
* **[https://scpwiki.com/system:page-tags/tag/deletable deletable]** -- This is a temporary tag that indicates the article has been voted on for deletion. It should only be placed on articles where a deletion vote has been concluded. Other tags should be removed when this tag is added to a page. Remove if deletion is permanently cancelled for whatever reason.
* **[https://scpwiki.com/system:page-tags/tag/featured featured]** -- Designates [https://scp-wiki.wikidot.com/featured-scp-archive Featured Articles] and [https://scp-wiki.wikidot.com/featured-tale-archive Featured Tales].
* **[https://scpwiki.com/system:page-tags/tag/prize-feature prize-feature]** -- Designates articles featured by the winner of a site contest.
* **[https://scpwiki.com/system:page-tags/tag/reviewers-spotlight reviewers-spotlight]** -- Designates articles featured by a [https://scp-wiki.wikidot.com/reviewers-spotlight-archive forum reviewer].
* **[https://scpwiki.com/system:page-tags/tag/event-featured event-featured]** -- Designates articles featured on special event days such as International Talk Like a Pirate Day.
* **[https://scpwiki.com/system:page-tags/tag/metadata metadata]** -- Designates pages with meta information about articles.
* **[https://scpwiki.com/system:page-tags/tag/unlisted unlisted]** -- Article has been unlisted from the SCP wiki.
* **[https://scpwiki.com/system:page-tags/tag/_cc _cc]** -- This tag indicates that all images on the page in question have been demonstrated to be fully compliant with current licensing policy. __This tag should **only** be added by a member of the Licensing team__. This tag conflicts with _image.
 * //Conflicts with '_image'//
 * //Supersedes '_image'//
* **[https://scpwiki.com/system:page-tags/tag/_cc4 _cc4]** -- This tag indicates that the page includes an image licensed under CC4. __This tag should **only** be added by a member of the Licensing team__. This tag conflicts with _image.
* **[https://scpwiki.com/system:page-tags/tag/_image _image]** -- This is a temporary tag that the tagging team applies to new articles that include one or more images, irrespective of whatever licensing information is provided by the author. This tag acts as an indicator to the Licensing team that there are images whose license status need to be confirmed and/or verified. Licensing will remove the _image tag and replace it with the _cc tag (or, if images are removed, no tag at all) when appropriate.
 * //Conflicts with '_cc'//
 * //Superseded by '_cc'//
* **[https://scpwiki.com/system:page-tags/tag/_licensebox _licensebox]** -- A tag for designating that an article has a standard license info block that is tracked on the [https://scp-wiki.wikidot.com/licensing-master-list Licensing Master List].
* **[https://scpwiki.com/system:page-tags/tag/_theme-temp _theme-temp]** -- Temporary tag used for marking old theme locations while they were moved from the {{component:}} category to the {{theme:}} category.
* **[https://scpwiki.com/system:page-tags/tag/crosslink crosslink]** -- This is a temporary tag that indicates the Wikiwalk Subteam of MAST is currently proposing revisions on the page, which should be seen in the comments.

[[/tab]]
[[tab Events]]
++ Events

Tags for all events on the wiki, including contests.

* **[https://scpwiki.com/system:page-tags/tag/173fest 173fest]** -- An entry to the [https://scp-wiki.wikidot.com/173-festival 173 Festival].
* **[https://scpwiki.com/system:page-tags/tag/art-exchange art-exchange]** -- Of or related to the [https://scp-wiki.wikidot.com/art-exchange-hub Annual Holiday Art Exchange].
* **[https://scpwiki.com/system:page-tags/tag/af2014 af2014]** -- Of or related to the [https://scp-wiki.wikidot.com/april-fools-2014 Super Cute Pets!] 2014 April Fool's prank.
* **[https://scpwiki.com/system:page-tags/tag/game-day game-day]** -- Of or related to the [https://scp-wiki.wikidot.com/gamedayindex Game Day] project.
* **[https://scpwiki.com/system:page-tags/tag/nightmarefest nightmarefest]** -- An entry to the unofficial [https://scp-wiki.wikidot.com/nightmarefest NIGHTMAREFEST].
* **[https://scpwiki.com/system:page-tags/tag/_townhouse _townhouse]** -- An entry to the 'Townhouse' category of the unofficial NIGHTMAREFEST.
 * //Requires 'nightmarefest'//
* **[https://scpwiki.com/system:page-tags/tag/_the-bureaucrat _the-bureaucrat]** -- An entry to the 'The Bureaucrat' category of the unofficial NIGHTMAREFEST.
 * //Requires 'nightmarefest'//
* **[https://scpwiki.com/system:page-tags/tag/_graveyard-shift _graveyard-shift]** -- An entry to the 'Graveyard Shift' category of the unofficial NIGHTMAREFEST.
 * //Requires 'nightmarefest'//

+++ Contests

Tags for contests and the articles submitted to them.

* **[https://scpwiki.com/system:page-tags/tag/1000 1000]** -- An entry to the [https://scp-wiki.wikidot.com/forum/t-376556 SCP-1000 Contest].
* **[https://scpwiki.com/system:page-tags/tag/2000 2000]** -- An entry to the [https://scp-wiki.wikidot.com/scp2000contesthub SCP-2000 Contest].
* **[https://scpwiki.com/system:page-tags/tag/3000 3000]** -- An entry to the [https://scp-wiki.wikidot.com/scp3000contesthub SCP-3000 Contest].
* **[https://scpwiki.com/system:page-tags/tag/4000 4000]** -- An entry to the [https://scp-wiki.wikidot.com/scp4000contesthub SCP-4000 Contest].
* **[https://scpwiki.com/system:page-tags/tag/5000 5000]** -- An entry to the [https://scp-wiki.wikidot.com/scp5000contesthub SCP-5000 Contest].
* **[https://scpwiki.com/system:page-tags/tag/6000 6000]** -- An entry to the [https://scp-wiki.wikidot.com/scp6000contesthub SCP-6000 Contest].
* **[https://scpwiki.com/system:page-tags/tag/7000 7000]** -- An entry to the [https://scp-wiki.wikidot.com/scp7000contesthub SCP-7000 Contest].
* **[https://scpwiki.com/system:page-tags/tag/8000 8000]** -- An entry to the [https://scp-wiki.wikidot.com/scp7000contesthub SCP-8000 Contest].
* **[https://scpwiki.com/system:page-tags/tag/af2016 af2016]** -- An entry to the [https://scp-wiki.wikidot.com/an-incredibly-important-announcement Crack Fiction Contest] 2016 April Fool's prank.
* **[https://scpwiki.com/system:page-tags/tag/art2017 art2017]** -- An entry to the [https://scp-wiki.wikidot.com/social-media-art-contest 2017 Art Contest].
* **[https://scpwiki.com/system:page-tags/tag/canon2020 canon2020]** -- An entry to the [https://scp-wiki.wikidot.com/canon-renaissance-contest 2020 Canon Renaissance Contest].
* **[https://scpwiki.com/system:page-tags/tag/cliche2019 cliche2019]** -- An entry to [https://scp-wiki.wikidot.com/cliche-con-2019 Cliche-Con 2019].
* **[https://scpwiki.com/system:page-tags/tag/coldpostcon coldpostcon]** -- An entry to [https://scp-wiki.wikidot.com/coldpostcon ColdpostCon].
* **[https://scpwiki.com/system:page-tags/tag/collab-con2019 collab-con2019]** -- An entry to [https://scp-wiki.wikidot.com/collaboration-contest Collab-Con 2019].
* **[https://scpwiki.com/system:page-tags/tag/cupid2021 cupid2021]** -- An entry to [https://scp-wiki.wikidot.com/cupid-contest-2021 Cupid Contest 2021].
* **[https://scpwiki.com/system:page-tags/tag/d-con2016 d-con2016]** -- An entry to the [https://scp-wiki.wikidot.com/d-class-contest 2016 D-Class Contest].
* **[https://scpwiki.com/system:page-tags/tag/dc2014 dc2014]** -- An entry to the [https://scp-wiki.wikidot.com/Dystopia-Contest 2014 Dystopia Contest].
* **[https://scpwiki.com/system:page-tags/tag/departmentcon2022 departmentcon2022]** -- An entry to the [https://scp-wiki.wikidot.com/department-contest 2022 Department Contest].
* **[https://scpwiki.com/system:page-tags/tag/doomsday2018 doomsday2018]** -- An entry to the [https://scp-wiki.wikidot.com/doomsday-contest 2018 Doomsday Contest].
* **[https://scpwiki.com/system:page-tags/tag/exquisite-corpse2020 exquisite-corpse2020]** -- An entry to the [https://scp-wiki.wikidot.com/exquisite-corpse-contest 2020 Exquisite Corpse Contest].
* **[https://scpwiki.com/system:page-tags/tag/five-questions five-questions]** -- An entry to the [https://scp-wiki.wikidot.com/five-questions Five Questions Contest].
* **[https://scpwiki.com/system:page-tags/tag/gbc09 gbc09]** -- An entry to [https://scp-wiki.wikidot.com/gears-birthday-contest-2009 2009 Gears' Birthday Contest].
* **[https://scpwiki.com/system:page-tags/tag/talecon10 talecon10]** -- An entry to [https://scp-wiki.wikidot.com/the-great-short-story-contest-archives The Great Short Story Contest].
* **[https://scpwiki.com/system:page-tags/tag/goblincon2023 goblincon2023]** -- An entry to the [https://scp-wiki.wikidot.com/goblincon 2023 GoblinCon].
* **[https://scpwiki.com/system:page-tags/tag/_goblin-76 _goblin-76]** -- An entry to the 'Class of '76' category of the 2023 GoblinCon.
 * //Requires 'goblincon2023'//
* **[https://scpwiki.com/system:page-tags/tag/_goblin-glitch _goblin-glitch]** -- An entry to the 'Glitch' category of the 2023 GoblinCon.
 * //Requires 'goblincon2023'//
* **[https://scpwiki.com/system:page-tags/tag/_goblin-goblin _goblin-goblin]** -- An entry to the 'Fantasy Goblin' category of the 2023 GoblinCon.
 * //Requires 'goblincon2023'//
* **[https://scpwiki.com/system:page-tags/tag/_goblin-royale _goblin-royale]** -- An entry to the 'Battle Royale' category of the 2023 GoblinCon.
 * //Requires 'goblincon2023'//
* **[https://scpwiki.com/system:page-tags/tag/_goblin-deletions _goblin-deletions]** -- An entry to the 'Deletions' category of the 2023 GoblinCon.
 * //Requires 'goblincon2023'//
* **[https://scpwiki.com/system:page-tags/tag/goi2014 goi2014]** -- An entry to the [https://scp-wiki.wikidot.com/goi-contest-2014 2014 Groups of Interest Contest].
* **[https://scpwiki.com/system:page-tags/tag/goi2019 goi2019]** -- An entry to the [http://scp-int.wikidot.com/international-goi-contest-2019 International Groups of Interest Contest 2019].
* **[https://scpwiki.com/system:page-tags/tag/halloween2018 halloween2018]** -- An entry to the [https://scp-wiki.wikidot.com/halloween-contest-2018 2018 Halloween Contest].
* **[https://scpwiki.com/system:page-tags/tag/halloweencon2022 halloweencon2022]** -- An entry to the [https://scp-wiki.wikidot.com/halloween-con-2022 2022 Halloweencon].
* **[https://scpwiki.com/system:page-tags/tag/hc2012 hc2012]** -- An entry to the [https://scp-wiki.wikidot.com/halloween-contest 2012 Halloween Contest].
* **[https://scpwiki.com/system:page-tags/tag/hiscon2017 hiscon2017]** -- An entry to the [https://scp-wiki.wikidot.com/history-contest 2017 History Contest].
* **[https://scpwiki.com/system:page-tags/tag/jam-con2018 jam-con2018]** -- An entry to the [https://scp-wiki.wikidot.com/72-hour-jam-contest 2018 72 Hour Jam Contest].
* **[https://scpwiki.com/system:page-tags/tag/_dark-and-stormy _dark-and-stormy]** -- An entry to the 'Dark and Stormy' category of the 2018 72 Hour Jam Contest.
 * //Requires 'jam-con2018'//
* **[https://scpwiki.com/system:page-tags/tag/_murder-mystery _murder-mystery]** -- An entry to the 'Murder Mystery' category of the 2018 72 Hour Jam Contest.
 * //Requires 'jam-con2018'//
* **[https://scpwiki.com/system:page-tags/tag/_tropical _tropical]** -- An entry to the 'Tropical' category of the 2018 72 Hour Jam Contest.
 * //Requires 'jam-con2018'//
* **[https://scpwiki.com/system:page-tags/tag/jam-con2019 jam-con2019]** -- An entry to the [https://scp-wiki.wikidot.com/144-hour-jam-contest 2019 144-Hour Jam Contest].
* **[https://scpwiki.com/system:page-tags/tag/_shaggy-dog _shaggy-dog]** -- An entry to the 'Shaggy Dog' category of the 2019 144 Hour Jam Contest.
 * //Requires 'jam-con2019'//
* **[https://scpwiki.com/system:page-tags/tag/_pulp-fiction _pulp-fiction]** -- An entry to the 'Pulp Fiction' category of the 2019 144 Hour Jam Contest.
 * //Requires 'jam-con2019'//
* **[https://scpwiki.com/system:page-tags/tag/_all-a-dream _all-a-dream]** -- An entry to the 'All a Dream' category of the 2019 144 Hour Jam Contest.
 * //Requires 'jam-con2019'//
* **[https://scpwiki.com/system:page-tags/tag/jam-con2020 jam-con2020]** -- An entry to the [https://scp-wiki.wikidot.com/144-hour-jam-contest-two 2020 144-Hour Jam Contest].
* **[https://scpwiki.com/system:page-tags/tag/_explosions _explosions]** -- An entry to the 'Explosions' category of the 2020 144 Hour Jam Contest.
 * //Requires 'jam-con2020'//
* **[https://scpwiki.com/system:page-tags/tag/_delicious _delicious]** -- An entry to the 'Delicious' category of the 2020 144 Hour Jam Contest.
 * //Requires 'jam-con2020'//
* **[https://scpwiki.com/system:page-tags/tag/_meets-the-eye _meets-the-eye]** -- An entry to the 'Meets the Eye' category of the 2020 144 Hour Jam Contest.
 * //Requires 'jam-con2020'//
* **[https://scpwiki.com/system:page-tags/tag/jam-con2021 jam-con2021]** -- An entry to [http://scp-wiki.wikidot.com/jam-con-2021 JamCon 2021].
* **[https://scpwiki.com/system:page-tags/tag/_marine _marine]** -- An entry to the 'Marine' category of JamCon 2021.
 * //Requires 'jam-con2021'//
* **[https://scpwiki.com/system:page-tags/tag/_corruption _corruption]** -- An entry to the 'Corruption' category of JamCon 2021.
 * //Requires 'jam-con2021'//
* **[https://scpwiki.com/system:page-tags/tag/_famouslastwords _famouslastwords]** -- An entry to the '"What could possibly go wrong?"' category of JamCon 2021.
 * //Requires 'jam-con2021'//
* **[https://scpwiki.com/system:page-tags/tag/lorecon2023 lorecon2023]** -- An entry to the [http://scp-int.wikidot.com/lorecon2023 International 2023 Lore and Aesthetics Contest].
* **[https://scpwiki.com/system:page-tags/tag/mtf2016 mtf2016]** -- An entry to the [https://scp-wiki.wikidot.com/mobile-task-force-contest 2016 Mobile Task Force Contest].
* **[https://scpwiki.com/system:page-tags/tag/nyc2013 nyc2013]** -- An entry to the [https://scp-wiki.wikidot.com/new-years-contest 2013 New Year's Canon Contest].
* **[https://scpwiki.com/system:page-tags/tag/rei2015 rei2015]** -- An entry to the [https://scp-wiki.wikidot.com/reimagining-contest 2015 Reimagining Contest].
* **[https://scpwiki.com/system:page-tags/tag/remixcon2023 remixcon2023]** -- An entry to the [https://scp-wiki.wikidot.com/remixcon2023 2023 Remix Contest].
* **[https://scpwiki.com/system:page-tags/tag/spring-cleaning24 spring-cleaning24]** -- An entry to the [https://scp-wiki.wikidot.com/deer-college-spring-cleaning-event 2024 Spring Cleaning Event].
* **[https://scpwiki.com/system:page-tags/tag/sc2015 sc2015]** -- An entry to the [https://scp-wiki.wikidot.com/short-works-contest 2015 Short Works Contest].
* **[https://scpwiki.com/system:page-tags/tag/tc2013 tc2013]** -- An entry to the [https://scp-wiki.wikidot.com/time-contest 2013 Time Contest].
* **[https://scpwiki.com/system:page-tags/tag/uac2014 uac2014]** -- An entry to the [https://scp-wiki.wikidot.com/under-appreciated-contest 2014 Under-Appreciated SCPs Contest].
* **[https://scpwiki.com/system:page-tags/tag/visual-archives2024 visual-archives2024]** -- An entry to the [https://scp-wiki.wikidot.com/visual-archives-art-contest 2024 Visual Archives Art Contest].
* **[https://scpwiki.com/system:page-tags/tag/memecon2021-unofficial memecon2021-unofficial]** -- An entry to the unofficial [https://scp-wiki.wikidot.com/memecon-unofficial 2021 MEMECON].
* **[https://scpwiki.com/system:page-tags/tag/romcon2023-unofficial romcon2023-unofficial]** -- An entry to the unofficial [https://scp-wiki.wikidot.com/romcon 2023 RomCon]: an SCP OCT.

[[/tab]]
[[tab Translation]]
++ Translation

These tags indicate that the article in question has been translated to SCP-EN from one of the official SCP translation sites.

* **[https://scpwiki.com/system:page-tags/tag/international international]** -- Applicable if the tale or SCP article was translated from one of the recognized translation sites. Don't add this tag if the article //was// translated to another language.

+++ Language Codes

* **[https://scpwiki.com/system:page-tags/tag/_int _int]** -- Translated from the [http://scp-int.wikidot.com/ International Site].
* **[https://scpwiki.com/system:page-tags/tag/_ru _ru]** -- Translated from the [http://scpfoundation.net/ Russian Site].
* **[https://scpwiki.com/system:page-tags/tag/_ko _ko]** -- Translated from the [http://scpko.wikidot.com/ Korean Site].
* **[https://scpwiki.com/system:page-tags/tag/_cn _cn]** -- Translated from the [http://scp-wiki-cn.wikidot.com/ Chinese Site].
* **[https://scpwiki.com/system:page-tags/tag/_fr _fr]** -- Translated from the [http://fondationscp.wikidot.com/ French Site].
* **[https://scpwiki.com/system:page-tags/tag/_pl _pl]** -- Translated from the [http://scp-wiki.net.pl/ Polish Site].
* **[https://scpwiki.com/system:page-tags/tag/_es _es]** -- Translated from the [http://lafundacionscp.wikidot.com/ Spanish Site].
* **[https://scpwiki.com/system:page-tags/tag/_th _th]** -- Translated from the [http://scp-th.wikidot.com/main Thai Site].
* **[https://scpwiki.com/system:page-tags/tag/_jp _jp]** -- Translated from the [http://scp-jp.wikidot.com/ Japanese Site].
* **[https://scpwiki.com/system:page-tags/tag/_de _de]** -- Translated from the [http://scp-wiki-de.wikidot.com/ German Site].
* **[https://scpwiki.com/system:page-tags/tag/_it _it]** -- Translated from the [http://fondazionescp.wikidot.com/ Italian Site].
* **[https://scpwiki.com/system:page-tags/tag/_ua _ua]** -- Translated from the [http://scp-ukrainian.wikidot.com/ Ukrainian Site].
* **[https://scpwiki.com/system:page-tags/tag/_pt _pt]** -- Translated from the [http://scp-pt-br.wikidot.com/ Portuguese Site].
* **[https://scpwiki.com/system:page-tags/tag/_zh _zh]** -- Translated from the [http://scp-zh-tr.wikidot.com/ Traditional Chinese Site].
* **[https://scpwiki.com/system:page-tags/tag/_vn _vn]** -- Translated from the [http://scp-vn.wikidot.com/ Vietnamese Site].
* **[https://scpwiki.com/system:page-tags/tag/_el _el]** -- Translated from the [http://scp-el.wikidot.com/ Greek Site].

[[/tab]]

[[/tabview]]
