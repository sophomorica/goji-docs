# Science — quiz blueprints (K–4 content batch)

Format per [`../../QUIZZES.md`](../../QUIZZES.md) §4. For interactive lesson packages the check is **built into the package** and its score is posted via `lesson.check` / `lesson.complete` (see [`../../LESSON_PACKAGES.md`](../../LESSON_PACKAGES.md) §4). Until the player ships, deliver the same items as a **parent quiz**.


## `quiz.science.k2.living.01` — Living or not living?

```yaml
quiz.science.k2.living.01:
  objectives: [obj.science.k2.living.01]
  skill: "classify living vs nonliving; name the sign of life used"
  tools: lesson-package (built-in check) | parent-quiz (bridge)
  item_type: multiple_choice   # picture + read-aloud text; 2–3 choices at K
  n_items: 5
  pass_rule: ">= 4/5"
  difficulty: intro
  constraints:
    must_include: [one moving nonliving thing, one still living thing, one once-alive object, one "which sign?" item]
    distractors: movement-as-life, stillness-as-nonlife, once-alive-as-alive
```

**Gold items (v1):** (each distractor names its misconception)

1. A **wolf** runs through the woods. Living or not living? → **living** / not living *(baseline)*
2. A **river** rushes downhill all day. Living or not living? → living *(movement-as-life)* / **not living**
3. An **oak tree** stands still all winter. Living or not living? → **living** / not living *(stillness-as-nonlife)*
4. A **log** on the ground. Living or not living? → living *(once-alive-as-alive)* / **not living**
5. A **fox** has three kits in spring. Which sign of life is that? → grows / needs food / **makes more of its kind** / moves

Retakes swap the animal for the current fable animal (ant, crow, lion, hare…) — the misconceptions stay fixed.

## `quiz.science.35.adapt.01` — Why the mongoose wins

```yaml
quiz.science.35.adapt.01:
  objectives: [obj.science.35.adapt.01]
  skill: "classify physical vs behavioral adaptations; populations change over generations; fossils as evidence of past environments"
  tools: lesson-package (built-in check) | parent-quiz (bridge)
  item_type: multiple_choice   # picture + read-aloud text; 2–3 choices at grade 3
  n_items: 5
  pass_rule: ">= 4/5"
  difficulty: intro
  anchor: jungle-book   # Rikki-Tikki-Tavi week; specimens are the anchor's own animals
  constraints:
    must_include: [one physical item, one behavioral item, one population-change item, one fossil-inference item, one anchor-case item]
    distractors: physical-behavioral-mixup, adapt-on-purpose, adapt-quickly, fossils-no-story
```

**Gold items (v1):** (each distractor names its misconception)

1. The **tiger's stripes** hide it in tall grass. What kind of adaptation? → **physical — a body pattern it was born with** / behavioral — a thing it decides to do *(physical-behavioral-mixup)*
2. **Wolves hunt in a pack.** What kind of adaptation? → physical — pack-hunting is in their paws *(physical-behavioral-mixup)* / **behavioral — hunting together is a thing they DO**
3. One year, only big hard seeds are left. How does the **bird population** end up with bigger beaks? → each bird decides to grow a bigger beak *(adapt-on-purpose)* / **over many generations, big-beaked birds survive and have chicks** / beaks stretch bigger in a week or two *(adapt-quickly)*
4. High on a mountain you find a **fish fossil**. What does it tell you? → nothing — it is just an old rock *(fossils-no-story)* / **this place was once under water** / fish used to climb mountains *(misread evidence — evidence still tells a story, but you must ask where fish LIVE)*
5. Why does **Rikki-tikki the mongoose** beat the cobra? → pure luck, every time *(no-mechanism)* / **adaptations: speed, thick fur, and a tough body** / he wants to win more than the cobra does *(adapt-on-purpose: wanting doesn't build bodies)*

Retakes swap the specimens for other anchor animals (Shere Khan's stripes → leopard spots, wolf pack → elephant herd, hare → desert fox); the misconceptions stay fixed.

## `quiz.science.35.conservation.01` — The caretakers

```yaml
quiz.science.35.conservation.01:
  objectives: [obj.science.35.conservation.01]
  skill: "natural + human effects on ecosystems; erosion on bare land; conservation counter-moves; kid agency"
  tools: lesson-package (built-in check) | parent-quiz (bridge)
  item_type: multiple_choice   # picture + read-aloud text; 2–3 choices at grade 3
  n_items: 5
  pass_rule: ">= 4/5"
  difficulty: intro
  constraints:
    must_include: [one fire-nuance item, one erosion item, one counter-move item, one kid-agency item, one downstream-harm item]
    distractors: all-fire-always-bad, erosion-only-in-deserts, soil-made-quickly, nothing-a-kid-can-do, out-of-sight-no-harm
```

**Gold items (v1):** (each distractor names its misconception)

1. Is every **forest fire** always bad for every forest? → yes — all fire ruins every forest forever *(all-fire-always-bad)* / **no — some fires clear old brush and make room for new growth**
2. Heavy rain falls on a **bare hill** with no plants. What happens to the topsoil? → **it washes into the stream — that is erosion** / nothing — erosion only happens in deserts *(erosion-only-in-deserts)* / it grows back by tomorrow *(soil-made-quickly — ties to `quiz.science.35.soil.01`)*
3. What is the best **counter-move** for bare, washing-away soil? → **plant a cover of grass or crops** / pave it with concrete *(quick-fix that kills the soil)* / hope for less rain *(wait-and-hope)*
4. Can a **kid** really help an ecosystem? → no — there is nothing a kid can do *(nothing-a-kid-can-do)* / **yes — save water, pick up litter, help plant cover**
5. **Litter** floats down the stream and out of sight. Who does it hurt? → nobody — the stream carried it away *(out-of-sight-no-harm)* / **the fish and animals downstream that use the water** / only the person who dropped it *(harm-stays-local)*

Retakes swap the scenarios (flooded meadow for the fire item, windy bare field for the rain-erosion item, leaky hose for the shower); the misconceptions stay fixed.

## `quiz.science.35.ecosystems.01` — The jungle is a team

```yaml
quiz.science.35.ecosystems.01:
  objectives: [obj.science.35.ecosystems.01]
  skill: "ecosystem = living + nonliving components; different ecosystems, different residents; relationships eat/help/compete"
  tools: lesson-package (built-in check) | parent-quiz (bridge)
  item_type: multiple_choice   # picture + read-aloud text; 2–3 choices at grade 3
  n_items: 5
  pass_rule: ">= 4/5"
  difficulty: intro
  constraints:
    must_include: [one definition item, one nonliving-component item, one help-relationship item, one compete item, one big-vs-small predator item]
    distractors: only-animals, nonliving-not-part, all-relationships-are-eating, big-eats-small, help-confused-with-compete
```

**Gold items (v1):** (each distractor names its misconception)

1. What is an **ecosystem**? → only the animals in a place *(only-animals)* / **all the living things in a place PLUS the nonliving things they use** / only the plants in a place *(only-animals variant: "only the living stuff I noticed")*
2. Is the **river's water** part of the jungle ecosystem? → no — water is not alive, so it is not part of it *(nonliving-not-part)* / **yes — the living things drink it and live in it**
3. A **bee** visits a flower: bee gets food, flower gets its pollen carried. What is this? → eating — the bee is hurting the flower *(all-relationships-are-eating)* / **helping — both of them win** / competing — they fight over the pollen *(help-confused-with-compete)*
4. A **tiger and a python** both hunt the same deer. They are…? → helping each other hunt *(help-confused-with-compete)* / **competing for the same food** / the tiger eats the python *(big-eats-small)*
5. A huge **elephant** and a tiny squirrel share the jungle. Does the elephant eat the squirrel? → yes — big animals eat every smaller animal *(big-eats-small)* / **no — elephants eat plants; big does not mean it eats everything**

Retakes swap the jungle for the river or grassland (e.g. "is the sunlight part of the pond ecosystem?"; "two herons and one fish — eat, help, or compete?"); the misconceptions stay fixed.

## `quiz.science.35.foodwebs.01` — The jungle food web

```yaml
quiz.science.35.foodwebs.01:
  objectives: [obj.science.35.foodwebs.01]
  skill: "energy flow sun→producers→consumers→decomposers; arrow direction = energy to the eater; ripple effects; P/C/D classification; population/community/ecosystem"
  tools: lesson-package (built-in check) | parent-quiz (bridge)
  item_type: multiple_choice   # picture + read-aloud text; 2–3 choices at grade 4
  n_items: 5
  pass_rule: ">= 4/5"
  difficulty: intro
  constraints:
    must_include: [one where-does-energy-start item, one arrow-direction item, one remove-a-population ripple item, one decomposer item, one population/community/ecosystem item]
    distractors: energy-starts-with-lion, arrow-at-food, top-needs-nothing, decomposers-useless, level-confusion
```

**Gold items (v1):** (each distractor names its misconception)

1. Where does the energy in the jungle food web START? → with the tiger — the strongest hunter *(energy-starts-with-lion)* / **at the sun** / in the soil *(soil-as-energy)*
2. Which arrow is drawn correctly between the deer and the tiger? → **deer → tiger, because energy flows TO the eater** / tiger → deer, because the arrow points at the tiger's food *(arrow-at-food)*
3. Every deer leaves the jungle. What happens to the tiger and the wolves? → nothing — top hunters don't need anyone *(top-needs-nothing)* / they can start eating sunlight *(only producers use sunlight)* / **they lose a food source and go hungry**
4. What do the mushrooms and beetles on the jungle floor do? → **they return dead material to the soil — the web needs them** / nothing — they are gross and useless *(decomposers-useless)* / they make food from sunlight *(P/C/D role confusion)*
5. ALL the deer in the jungle, counted together, are called… → a community *(level-confusion)* / an ecosystem *(level-confusion — adds nonliving parts)* / **a population**

Retakes swap the removed population (deer → monkeys: then Kaa and the eagle go hungry) and the classified organism (mushroom ↔ dung beetle ↔ termite); the misconceptions stay fixed.

## `quiz.science.35.machines.01` — Net force and the force-tricks

```yaml
quiz.science.35.machines.01:
  objectives: [obj.science.35.machines.01]
  skill: "net force decides motion when multiple forces act; simple machines trade a longer path for a smaller push; match machine to job; spot machines in a compound tool"
  tools: lesson-package (built-in check) | parent-quiz (bridge)
  item_type: multiple_choice   # picture + read-aloud text; 3 choices at grade 3
  n_items: 5
  pass_rule: ">= 4/5"
  difficulty: intro
  constraints:
    must_include: [one where-does-the-help-come-from item, one steady-motion multiple-forces item, one net-force totals item, one machine-for-job item, one compound-machine item]
    distractors: free-force, one-force-only, teams-always-balance, wrong-machine-for-job
```

**Gold items (v1):** (each distractor names its misconception)

1. A **ramp** helps you push the piano into the truck. Where does the help come from? → the ramp adds free force of its own *(free-force)* / **you push with LESS force over a LONGER path** / the ramp does the work while you rest *(free-force, stated as "machines do the work for you")*
2. A **sled** slides along at a steady speed. How many forces act on it? → just one — the pull moving it *(one-force-only: "if it's moving, only one force acts")* / **more than one — the pull forward AND friction rubbing back** / zero — it moves all on its own *(moves-by-itself, K–2 prereq regression flag)*
3. **Tug-of-war**: left team total pull 5, right team total pull 8. What happens to the rope? → **it moves toward the RIGHT team** / it stands still — two teams always balance *(teams-always-balance: only equal totals cancel)* / it moves toward the LEFT team *(fails to compare totals — net-force blind)*
4. Lift the **flag** to the top of the pole. Which machine fits? → **pulley** / wedge *(wrong-machine-for-job: a wedge splits)* / screw *(wrong-machine-for-job: a screw holds)*
5. **Scissors** cut paper. Which two simple machines make scissors? → **lever + wedge** / pulley + ramp *(wrong parts — no wheel or slope in scissors)* / no machines — scissors cut for free *(free-force)*

Retakes swap the surface objects (piano→couch, sled→wagon, flag→bucket-in-a-well, scissors→hand-can-opener); the misconceptions stay fixed.

## `quiz.science.35.mixtures.01` — The dissolve-or-not lab

```yaml
quiz.science.35.mixtures.01:
  objectives: [obj.science.35.mixtures.01]
  skill: "predict dissolving; dissolved material persists (and how to prove it); liquids can refuse to mix; hot water dissolves faster"
  tools: lesson-package (built-in check) | parent-quiz (bridge)
  item_type: multiple_choice   # picture + read-aloud text; 3 choices at grade 3
  n_items: 5
  pass_rule: ">= 4/5"
  difficulty: intro
  constraints:
    must_include: [one where-did-it-go item, one stir-hard item, one hot-vs-cold item, one prove-it item, one liquid-mixing item]
    distractors: dissolved-is-destroyed, stir-hard-enough, hot-cold-same, settles-like-sand
```

**Gold items (v1):** (each distractor names its misconception)

1. The **salt** dissolved and vanished from sight. Where is it? → gone forever — the stirring destroyed it *(dissolved-is-destroyed)* / **still there — in pieces too small to see** / it turned into water *(dissolved-is-destroyed, transformation variant)*
2. You stir **sand** in water as hard as you can, for ten whole minutes. What happens? → it finally dissolves — hard stirring dissolves anything *(stir-hard-enough)* / **it still settles to the bottom — sand never dissolves** / it floats on top like oil *(confuses settling with floating)*
3. Which water dissolves a **sugar cube** faster? → **hot water** / cold water *(hot-cold reversed)* / neither — temperature makes no difference *(hot-cold-same)*
4. How could you PROVE the dissolved salt is still in the water? → **let the water dry up — the salt is left behind** / you can't — dissolved things are destroyed *(dissolved-is-destroyed)* / wait for the salt to settle out like sand *(settles-like-sand: confuses dissolving with a suspension)*
5. You pour **oil** into a glass of water. What happens? → **it floats on top in its own layer** / it dissolves like salt *(everything-mixes)* / it sinks and settles like sand *(settles-like-sand)*

Retakes swap the surface materials (salt→sugar, sand→gravel, oil→syrup-contrast); the misconceptions stay fixed. The flour/cloudy trick stays a practice-only item at v1 (hardest discrimination) — promote it to the check in a retake variant.

## `quiz.science.35.moon.01` — Our closest neighbor

```yaml
quiz.science.35.moon.01:
  objectives: [obj.science.35.moon.01]
  skill: "Earth–moon–sun motions; tilt (not distance) causes seasons; moonlight = reflected sunlight; four phases as viewing angle; moon's pull causes tides"
  tools: lesson-package (built-in check) | parent-quiz (bridge)
  item_type: multiple_choice   # picture + read-aloud text; 2–3 choices at grade 4
  n_items: 5
  pass_rule: ">= 4/5"
  difficulty: intro
  constraints:
    must_include: [one tilt-vs-distance item, one moonlight-source item, one phase-cause item, one phase-order item, one tides item]
    distractors: closer-in-summer, sun-changes, moon-glows, phases-are-shadow, shape-change, phase-order-skip, wind-tides, heat-tides
```

**Gold items (v1):** (each distractor names its misconception)

1. Why is it summer where you live? → **your half of Earth tilts toward the sun** / Earth moves closer to the sun in summer *(closer-in-summer — THE target)* / the sun grows bigger in summer *(sun-changes)*
2. Why does the moon shine at night? → **it reflects sunlight, like a mirror** / it makes its own light, like a lamp *(moon-glows)*
3. What makes the moon's phases? → **we see different amounts of its lit half as it circles Earth** / Earth's shadow covers part of the moon *(phases-are-shadow)* / the moon really changes shape *(shape-change)*
4. The new moon starts to grow. Which phase comes NEXT? → **first quarter** / full moon *(phase-order-skip)* / last quarter *(phase-order — backwards)*
5. What makes the sea rise and fall twice a day? → **the moon's pull** / the wind *(wind-tides — waves-vs-tides confusion)* / the sun heating the water *(heat-tides)*

Retake variants rotate the phase-order probe (after full? after first quarter?), swap the hemisphere in item 1 (why is it WINTER in July in Australia?), and probe the farther-in-summer fun fact directly; the misconceptions stay fixed.

## `quiz.science.35.ocean.01` — Down to the deep

```yaml
quiz.science.35.ocean.01:
  objectives: [obj.science.35.ocean.01]
  skill: "ocean floor shape; properties of ocean water by depth; what moves the water (waves/tides/currents); life in every zone; plankton as food-web base"
  tools: lesson-package (built-in check) | parent-quiz (bridge)
  item_type: multiple_choice   # picture + read-aloud text; 2–3 choices at grade 4
  n_items: 5
  pass_rule: ">= 4/5"
  difficulty: intro
  constraints:
    must_include: [one floor-shape item, one depth-properties item, one water-movement item, one deep-life item, one plankton item]
    distractors: flat-floor, unmapped-floor, sunny-deep, fresh-not-salty, still-water, empty-deep, zone-mixup, literal-grass, plankton-unimportant
```

**Gold items (v1):** (each distractor names its misconception)

1. What is the deep ocean floor like? → **it has shape — slopes, plains, ridges, and deep trenches** / flat sand, smooth all the way across *(flat-floor)* / nobody has ever mapped it *(unmapped-floor)*
2. Deep down, ocean water is… → **cold, pitch dark — and still salty** / warm and sunny, like at the beach *(sunny-deep)* / fresh, like river water *(fresh-not-salty)*
3. "Only the waves on top move — the rest of the ocean stands still." True? → **no — currents flow through it like rivers in the sea** / yes — under the waves the water never moves *(still-water)*
4. What lives in the pitch-dark midnight zone? → **specialists like the glowing anglerfish** / nothing — it is too dark and cold to live there *(empty-deep)* / coral reefs *(zone-mixup)*
5. Why is plankton called the ocean's grass? → **almost every ocean food web starts with it** / it is lawn grass that washed into the sea *(literal-grass)* / it is not important to ocean animals *(plankton-unimportant)*

Retake variants rotate the movement cause probed (waves → wind; tides → moon; Gulf Stream → warm current), swap the deep resident, and probe the dive order directly ("what comes after the slope?"); the misconceptions stay fixed.

## `quiz.science.35.soil.01` — Dig deeper

```yaml
quiz.science.35.soil.01:
  objectives: [obj.science.35.soil.01]
  skill: "soil components (rock bits, humus, water, air); slow formation; layers; support + nutrients for plants; soil animals help"
  tools: lesson-package (built-in check) | parent-quiz (bridge)
  item_type: multiple_choice   # picture + read-aloud text; 2–3 choices at grade 3
  n_items: 5
  pass_rule: ">= 4/5"
  difficulty: intro
  constraints:
    must_include: [one components item, one made-slowly item, one layers item, one worms-help item, one support+nutrients item]
    distractors: soil-is-one-thing, soil-made-quickly, worms-wreck-soil, strongest-layer-best, support-only
```

**Gold items (v1):** (each distractor names its misconception)

1. What is **soil** made of? → just one thing — dirt *(soil-is-one-thing)* / **a mix: rock bits, humus, water and air** / only dead leaves *(soil-is-one-thing variant: single ingredient)*
2. How long does nature take to **make new soil**? → about one rainy week *(soil-made-quickly)* / **a very long time — rock crumbles and leaves rot slowly**
3. Which **layer** is the richest for plants? → **the dark topsoil on top** / the solid rock at the bottom — it is the strongest *(strongest-layer-best)* / the lighter subsoil *(layer confusion)*
4. You find **worms** all over the garden bed. What should you do? → pull them out — worms wreck the soil *(worms-wreck-soil)* / **leave them — their tunnels bring air in and mix the soil**
5. What does soil **do for a plant**? → only holds it up straight *(support-only)* / **holds it up AND feeds it water and nutrients** / nothing — plants only need sunshine *(plants-need-nothing-from-soil)*

Retakes swap the pictures (compost bin for humus, anthill for the digger, flowerpot for the plant); the misconceptions stay fixed.

## `quiz.science.35.solar.01` — Our solar system

```yaml
quiz.science.35.solar.01:
  objectives: [obj.science.35.solar.01]
  skill: "rotate (day/night) vs revolve (year); eight planets in order; rocky vs gas; relative size of sun vs planets; real spacing"
  tools: lesson-package (built-in check) | parent-quiz (bridge)
  item_type: multiple_choice   # picture + read-aloud text; 2–3 choices at grade 4
  n_items: 5
  pass_rule: ">= 4/5"
  difficulty: intro
  constraints:
    must_include: [one rotate-vs-revolve item, one year-cause item, one sun-nature/size item, one planet-order item, one real-spacing item]
    distractors: rotate-revolve-same, sun-moves, sun-is-planet, sun-small, order-scramble, poster-spacing
```

**Gold items (v1):** (each distractor names its misconception)

1. Earth spins around once every day. What is that motion, and what does it make? → **rotate — it makes day and night** / revolve — it makes day and night *(rotate-revolve-same — right effect, wrong word)* / rotate — it makes a whole year *(rotate-revolve-same — right word, wrong effect)*
2. What gives us a whole YEAR? → **Earth revolves — one full trip around the sun** / Earth rotates — one full spin *(rotate-revolve-same)* / the sun travels around Earth *(sun-moves)*
3. The sun is… → **a star, far bigger than every planet** / a planet, like Earth *(sun-is-planet)* / a star about the same size as Earth *(sun-small)*
4. Which shows the first four planets, in order from the sun? → **Mercury, Venus, Earth, Mars** / Venus, Mercury, Mars, Earth *(order-scramble)* / Earth, Mercury, Venus, Mars *(order-scramble — home-first bias)*
5. In real space, how are the planets spaced? → **far, far apart — mostly empty space** / close together, like on a poster *(poster-spacing)*

Retake variants swap which order segment is asked (middle four; outer four), which planet's hook fact is probed ("which planet is tipped on its side?"), and the size comparison object (beach ball → basketball); the misconceptions stay fixed.

## `quiz.science.35.structures.01` — Built to survive

```yaml
quiz.science.35.structures.01:
  objectives: [obj.science.35.structures.01]
  skill: "photosynthesis word equation (leaf makes food; soil is not food); structures serve energy, survival, offspring"
  tools: lesson-package (built-in check) | parent-quiz (bridge)
  item_type: multiple_choice   # picture + read-aloud text; 3 choices at grade 4
  n_items: 5
  pass_rule: ">= 4/5"
  difficulty: intro
  constraints:
    must_include: [one where-does-plant-food-come-from item, one factory-inputs item, one why-oxygen item, one teeth-tell-the-diet item, one offspring-structure item]
    distractors: soil-as-food, oxygen-for-us, structure-as-decoration, teeth-diet
```

**Gold items (v1):** (each distractor names its misconception)

1. Where does the meadow grass get its food? → **it makes food in its leaves** / it sucks food up from the soil *(soil-as-food)* / Black Beauty shares his oats *(soil-as-food — food must come from outside)*
2. What goes INTO the leaf factory? → soil and sunlight *(soil-as-food)* / **sunlight, carbon dioxide, and water** / only water *(incomplete-recipe)*
3. Why does the leaf let oxygen out? → it makes oxygen on purpose, as a gift for people *(oxygen-for-us)* / oxygen feeds the roots *(recipe-confusion)* / **oxygen is the leftover from making sugar**
4. A horse's big flat back teeth tell you… → **it grinds tough grass all day** / they are just decoration *(structure-as-decoration)* / it slices meat like a fox *(teeth-diet)*
5. What is the apple's job for the tree? → it is made just for people to eat *(oxygen-for-us family: made-for-us)* / **it carries and protects the seeds** / nothing — it is decoration *(structure-as-decoration)*

Retakes swap the plant (meadow grass ↔ oak ↔ clover) and the structure pairs (mane/tail ↔ hooves; apple ↔ rose hip); the misconceptions stay fixed.

## `quiz.science.35.va-resources.01` — Our Virginia

```yaml
quiz.science.35.va-resources.01:
  objectives: [obj.science.35.va-resources.01]
  skill: "watershed definition + Virginia's three drainage systems; resource kinds (forest/soil, mineral, water, wildlife); wise use and protecting the Bay"
  tools: lesson-package (built-in check) | parent-quiz (bridge)
  item_type: multiple_choice   # picture + read-aloud text; 2–3 choices at grade 4
  n_items: 5
  pass_rule: ">= 4/5"
  difficulty: intro
  constraints:
    must_include: [one watershed-definition item, one raindrop-path item, one land-cover item, one resource-kind item, one protect-the-Bay item]
    distractors: watershed-building, wrong-watershed, river-endpoint, city-cover, resource-category, stays-in-street, disappears
```

**Gold items (v1):** (each distractor names its misconception)

1. What is a watershed? → **all the land that drains to one river or bay** / a building that sheds water off its roof *(watershed-building)* / a kind of boat *(watershed-building — word-guess variant)*
2. Rain near Richmond flows into the James River. Where does the James carry it? → **to the Chesapeake Bay** / to the Gulf of Mexico *(wrong-watershed)* / nowhere — it stays in the river forever *(river-endpoint)*
3. Most of Virginia's land is covered by… → **forests** / cities and roads *(city-cover)* / bare sand *(city-cover — land-cover blindness)*
4. Which of these is one of Virginia's MINERAL resources? → **coal** / oysters *(resource-category — wildlife)* / oak trees *(resource-category — forest)*
5. Motor oil is poured into a street drain. What happens to it? → **it washes into a creek and can reach the Bay** / it stays in the street forever *(stays-in-street)* / it vanishes into nothing *(disappears)*

Retake variants swap the raindrop start (southwest coalfields → Gulf of Mexico; south-central → NC sounds), the mineral probed (granite, limestone), and the Bay species named; the misconceptions stay fixed.

## `quiz.science.35.watercycle.01` — One drop's endless journey

```yaml
quiz.science.35.watercycle.01:
  objectives: [obj.science.35.watercycle.01]
  skill: "water cycle processes (evaporation, condensation, precipitation); sun as engine; reservoirs; water is recycled, never new"
  tools: lesson-package (built-in check) | parent-quiz (bridge)
  item_type: multiple_choice   # picture + read-aloud text; 2–3 choices at grade 3
  n_items: 5
  pass_rule: ">= 4/5"
  difficulty: intro
  constraints:
    must_include: [one vanished-puddle item, one clouds item, one sun-engine item, one process-naming item, one recycled-water item]
    distractors: water-is-destroyed, clouds-are-smoke, clouds-are-cotton, rain-is-new-water, process-mixup
```

**Gold items (v1):** (each distractor names its misconception)

1. The morning **puddle** is gone by noon. Where did the water go? → it was destroyed — gone forever *(water-is-destroyed)* / **it evaporated — rose into the air as an invisible gas** / it turned into dust *(water-is-destroyed variant)*
2. What are **clouds** made of? → smoke from fires *(clouds-are-smoke)* / soft cotton *(clouds-are-cotton)* / **billions of tiny water droplets**
3. What is the **engine** that keeps the water cycle turning? → **the sun's heat** / the clouds make new water themselves *(rain-is-new-water)* / the rivers push the water up *(water-flows-uphill, ties to `quiz.science.k2.water.01`)*
4. High in the cold sky, water gas turns into tiny cloud droplets. What is that process called? → evaporation *(process-mixup: direction reversed)* / **condensation** / precipitation *(process-mixup)*
5. Is the rain that falls today **brand-new water**? → yes — clouds make new water every day *(rain-is-new-water)* / **no — it is the same water, recycled forever; a dinosaur may have drunk it!**

Retakes swap the scenario pictures (drying towel for the puddle, foggy mirror for the cloud-droplet item, snowfall for rain); the misconceptions stay fixed.

## `quiz.science.35.weather.01` — Reading the sky

```yaml
quiz.science.35.weather.01:
  objectives: [obj.science.35.weather.01]
  skill: "weather tools and their measurements; records → patterns → evidence-based forecasts; extreme events; weather vs climate"
  tools: lesson-package (built-in check) | parent-quiz (bridge)
  item_type: multiple_choice   # picture + read-aloud text; 3 choices at grade 4
  n_items: 5
  pass_rule: ">= 4/5"
  difficulty: intro
  constraints:
    must_include: [one tool→measurement item, one read-the-record forecast item, one what-is-a-forecast item, one weather-vs-climate item, one cold-week trap item]
    distractors: forecasts-are-guesses, forecast-as-promise, weather-equals-climate, cold-week-changes-climate, tool-mixup
```

**Gold items (v1):** (each distractor names its misconception)

1. Which tool measures air pressure? → **the barometer** / the anemometer *(tool-mixup — wind speed)* / the thermometer *(tool-mixup — temperature)*
2. The record shows the pressure falling for two days. Tomorrow will most likely be… → **stormy — falling pressure hints a storm** / impossible to say — forecasts are just guesses *(forecasts-are-guesses)* / exactly like today, guaranteed *(forecast-as-promise)*
3. What IS a forecast? → a magic guess about the sky *(forecasts-are-guesses)* / **a prediction built on measured records — evidence** / a promise that is always right *(forecast-as-promise)*
4. "Kansas prairie summers are usually hot and dry." That sentence describes… → weather — same thing as climate *(weather-equals-climate)* / a forecast for tomorrow *(record-vs-prediction confusion)* / **climate — the pattern over many years**
5. One freezing cold week arrives in May. What does it mean? → the climate has changed *(cold-week-changes-climate)* / **it is weather — day-to-day change; the climate pattern needs many years** / winter has restarted for the year *(weather-equals-season, K–2 holdover)*

Retakes swap the tool asked (barometer ↔ anemometer ↔ rain gauge), flip the record (rising/steady pressure → fair likely), and swap the trap week (a hot week in October); the misconceptions stay fixed.

## `quiz.science.k2.animals.01` — The fox's parts have jobs

```yaml
quiz.science.k2.animals.01:
  objectives: [obj.science.k2.animals.01]
  skill: "match animal parts to their jobs; same needs across different parts; classify by body covering"
  tools: lesson-package (built-in check) | parent-quiz (bridge)
  item_type: multiple_choice   # picture + read-aloud text; 2–3 choices at grade 1
  n_items: 5
  pass_rule: ">= 4/5"
  difficulty: intro
  constraints:
    must_include: [one part↔job item, one born-with-parts (why) item, one same-needs item, one covering item, one anchor-fable item]
    distractors: job-swap, chose-parts, people-needs, animals-like-people, covering-swap
```

**Gold items (v1):** (each distractor names its misconception)

1. Which part does the **hearing** job for the fox? → **big ears** / bushy tail *(job-swap)* / it just chooses to hear *(chose-parts)*
2. **Why** does the fox have sharp teeth? → **born with them — they fit eating meat** / it grew them on purpose because it wanted them *(chose-parts)* / to chew grass like a cow *(part-job-mismatch)*
3. The fox and the crow **both** need… → **food, water, and air** / toys and cooked dinner *(people-needs)* / nothing — animals need nothing *(needs-blind)*
4. What **covers** a bird's body? → **feathers** / fur *(covering-swap)* / scales *(covering-swap)*
5. In the fable, the crow held the cheese with its… → **beak** / hands *(animals-like-people)* / ears *(job-swap)*

Retake variants swap the specimen for the current fable animal (wolf ears, ant legs, lion teeth…) — the part→job logic and the misconceptions stay fixed.

## `quiz.science.k2.change.01` — Before and after

```yaml
quiz.science.k2.change.01:
  objectives: [obj.science.k2.change.01]
  skill: "pair before→after; sort changes fast vs slow; living grows, nonliving gets changed"
  tools: lesson-package (built-in check) | parent-quiz (bridge)
  item_type: multiple_choice   # picture + read-aloud text; 2 choices at K
  n_items: 5
  pass_rule: ">= 4/5"
  difficulty: intro
  constraints:
    must_include: [one slow-but-still-changing item, one nonliving-thing-changes item, one fast-vs-slow pick each way, one how-does-growth-happen item]
    distractors: invisible-change-denial, living-only, all-at-once, speed-swap
```

**Gold items (v1):** (each distractor names its misconception)

1. A **seed** becomes a tall tree. Is the seed changing? → **yes — slowly, even when we can't see it move** / no — it isn't moving, so it isn't changing *(invisible-change-denial)*
2. Which change is **FAST**? → **ice cream melting in the sun** / a puppy growing into a dog *(speed-swap)*
3. Waves wash the **sandcastle** flat. Can a nonliving sandcastle change? → **yes — the waves change it** / no — only living things change *(living-only)*
4. How does a **puppy** become a dog? → **it grows a little every day** / it changes all at once, in one night *(all-at-once)*
5. Which change is **SLOW**? → **a seed growing into a tree** / a leaf falling from the branch *(speed-swap)*

Retakes swap the specimens (bean plant, kitten→cat, snowman melting, worn shoes) — the misconceptions stay fixed.

## `quiz.science.k2.change.02` — The land changes too

```yaml
quiz.science.k2.change.02:
  objectives: [obj.science.k2.change.02]
  skill: "living things respond to weather/seasons; wind and water change the land; fast vs slow change"
  tools: lesson-package (built-in check) | parent-quiz (bridge)
  item_type: multiple_choice   # picture + read-aloud text; 2–3 choices at grade 2
  n_items: 5
  pass_rule: ">= 4/5"
  difficulty: intro
  constraints:
    must_include: [one who-made-the-canyon item, one rocks-change item, one fast-vs-slow item, one only-storms item, one living-things-respond item]
    distractors: someone-dug-it, land-never-changes, only-storms, seasons-dont-affect-living-things
```

**Gold items (v1):** (each distractor names its misconception)

1. Who made the **deep canyon**? → **the river — carving little by little for a very long time** / someone dug it with machines *(someone-dug-it)* / no one — canyons were always there and never change *(land-never-changes)*
2. Do **mountains and rocks** ever change? → **yes — wind and water change them, very slowly** / never — mountains are forever *(land-never-changes)*
3. Which one is a **FAST** change? → **a storm knocks a branch down** / a river carves a canyon *(speed-swap)* / waves turn rock into sand *(speed-swap)*
4. Is a **storm** the only thing that changes the land? → **no — wind and water change it a little every single day** / yes — only storms change the land *(only-storms)*
5. Autumn turns cold. Why do the **geese fly south**? → **living things answer the changing seasons** / weather never affects living things *(seasons-dont-affect-living-things)*

Retake variants swap the specimens (dune for canyon, worn stone step for rusty swing, robin for geese) — the misconceptions stay fixed.

## `quiz.science.k2.cycles.01` — Round and round: life cycles

```yaml
quiz.science.k2.cycles.01:
  objectives: [obj.science.k2.cycles.01]
  skill: "order life-cycle stages as a repeating circle; match offspring to parents; similar but not identical"
  tools: lesson-package (built-in check) | parent-quiz (bridge)
  item_type: multiple_choice   # picture + read-aloud text; 3 choices at K
  n_items: 5
  pass_rule: ">= 4/5"
  difficulty: intro
  constraints:
    must_include: [one stage-order item, one same-animal item, one cycle-keeps-going item, one non-obvious parent match, one similar-not-identical item]
    distractors: different-animal, identical-copies, cycle-ends-at-adult, cycle-backwards, tiny-adult-hatches, cross-cycle-mixup
```

**Gold items (v1):** (each distractor names its misconception)

1. What comes out of the butterfly's **egg**? → **a caterpillar** / a tiny butterfly *(tiny-adult-hatches / identical-copies)* / a tadpole *(cross-cycle-mixup)*
2. The caterpillar and the butterfly are… → **the same animal, growing and changing** / two different animals *(different-animal)* / just friends *(different-animal, softened)*
3. What happens **after** the butterfly is grown? → **she lays eggs — the circle starts again** / the cycle is over *(cycle-ends-at-adult)* / she turns back into a caterpillar *(cycle-backwards)*
4. Which baby grows up to be a **frog**? → **the tadpole** / the caterpillar *(cross-cycle-mixup)* / the puppy *(wrong kind)*
5. A mother dog has five puppies. The puppies look… → **like her, but not exactly the same** / exactly the same as her, like copies *(identical-copies)* / nothing like her at all *(resemblance denied)*

Retake variants swap the featured cycle (frog first, chicken egg→chick→hen) and the litter (kittens for puppies) — the misconceptions stay fixed.

## `quiz.science.k2.cycles.02` — Two life stories: frog and bean

```yaml
quiz.science.k2.cycles.02:
  objectives: [obj.science.k2.cycles.02]
  skill: "animal AND plant life cycles as orderly circles; stage order; seeds/eggs as living beginnings"
  tools: lesson-package (built-in check) | parent-quiz (bridge)
  item_type: multiple_choice   # picture + read-aloud text; 2–3 choices at grade 2
  n_items: 5
  pass_rule: ">= 4/5"
  difficulty: intro
  constraints:
    must_include: [one first-stage item, one what-comes-next item, one plant-makes-new-seeds item, one any-order item, one seed-is-alive item]
    distractors: any-order, cycle-backwards-or-skipped, plants-just-sit, seed-not-alive
```

**Gold items (v1):** (each distractor names its misconception)

1. What comes FIRST in a **frog's** life? → **egg** / tadpole *(skipped start — cycle order)* / frog *(cycle-backwards: starting at the adult)*
2. Which comes right after the **sprout**? → **the young plant** / the flower *(skipped stage — any-order)* / new seeds *(any-order: jumping to the end)*
3. Which bean stage makes the **new seeds**? → **the flower** / the sprout *(any-order)* / none — plants just sit, they don't make new plants *(plants-just-sit)*
4. Can life-cycle stages happen in **any order**? → **no — always the same order** / yes — any order *(any-order, stated)*
5. Is a **bean seed** alive? → **yes — give it water and it grows** / no — it is like a little rock *(seed-not-alive; ties back to `quiz.science.k2.living.01`'s seed card)*

Retakes swap the animal ring for the current fable animal with a distinct cycle (butterfly: egg → caterpillar → chrysalis → butterfly; hen: egg → chick → hen) and the bean for a sunflower; the misconceptions stay fixed.

## `quiz.science.k2.forces.01` — Pushes and pulls

```yaml
quiz.science.k2.forces.01:
  objectives: [obj.science.k2.forces.01]
  skill: "pushes and pulls cause motion and change direction; strength changes how far"
  tools: lesson-package (built-in check) | parent-quiz (bridge)
  item_type: multiple_choice   # picture + read-aloud text; 2–3 choices at K
  n_items: 5
  pass_rule: ">= 4/5"
  difficulty: intro
  constraints:
    must_include: [one pull-causes-motion item, one strength item, one starts-by-itself item, one push-vs-pull direction item]
    distractors: only-pushes-cause-motion, strength-does-not-matter, moves-by-itself, push-pull-direction-mixup
```

**Gold items (v1):** (each distractor names its misconception)

1. The **wagon** is across the yard. To bring it TO you, what do you do? → push it *(only-pushes-cause-motion / direction: a push sends it away)* / **pull it** / wait — it will come by itself *(moves-by-itself)*
2. Which kick sends the **ball** farther? → a gentle tap *(strength-does-not-matter)* / **a strong kick** / both the same — strength does not matter *(strength-does-not-matter, stated)*
3. A **ball** sits still on the grass. What can start it moving? → it starts all by itself *(moves-by-itself)* / **a push or a pull**
4. A gentle push did not move the **stuck wagon**. What should you try? → **a stronger push** / the same gentle push again *(strength-does-not-matter)* / just wait for it to move *(moves-by-itself)*
5. To send the **swing** AWAY from you, what do you do? → pull it *(push-pull-direction-mixup: pulls bring things toward you)* / **push it** / it swings by itself *(moves-by-itself)*

Retakes swap the objects (door, drawer, sled, toy car — never a self-moving animal); the misconceptions stay fixed.

## `quiz.science.k2.forces.02` — Invisible forces: gravity and magnets

```yaml
quiz.science.k2.forces.02:
  objectives: [obj.science.k2.forces.02]
  skill: "contact vs at-a-distance forces; gravity pulls down; what magnets do and don't attract; magnet ends"
  tools: lesson-package (built-in check) | parent-quiz (bridge)
  item_type: multiple_choice   # picture + read-aloud text; 2–3 choices at grade 2
  n_items: 5
  pass_rule: ">= 4/5"
  difficulty: intro
  constraints:
    must_include: [one no-touch gravity item, one feather-falls item, one magnets-not-everything item, one through-paper item, one same-ends item]
    distractors: must-touch-to-move, heavy-falls-light-floats, magnets-grab-everything, same-ends-snap
```

**Gold items (v1):** (each distractor names its misconception)

1. Nothing touches the **apple**, but it falls. What pulls it down? → **gravity — a pull with no touch** / something must be touching it *(must-touch-to-move)* / the wind blew it *(must-touch, displaced agent)*
2. You drop a **feather** and a rock. What does the feather do? → **falls down too — just slowly** / floats away — only heavy things fall *(heavy-falls-light-floats)*
3. Will the magnet grab the wax **crayon**? → yes — magnets grab everything *(magnets-grab-everything)* / **no — magnets grab only some metals**
4. A steel **paperclip** is under a sheet of paper. Can the magnet move it? → **yes — its pull goes through paper** / no — the magnet must touch it *(must-touch-to-move)*
5. Two magnets face **N to N** — the same ends. What happens? → **they push apart** / they snap together *(same-ends-snap)*

Retakes swap the objects (spoon vs plastic fork, key under a napkin, a dropped leaf vs a pinecone); the misconceptions stay fixed. An aluminum-can variant of item 3 keeps the sharper "not ALL metal" edge.

## `quiz.science.k2.habitats.01` — Home sweet habitat

```yaml
quiz.science.k2.habitats.01:
  objectives: [obj.science.k2.habitats.01]
  skill: "habitat = needs met by a place; living + nonliving parts interdepend; habitats change"
  tools: lesson-package (built-in check) | parent-quiz (bridge)
  item_type: multiple_choice   # picture + read-aloud text; 2–3 choices at grade 2
  n_items: 5
  pass_rule: ">= 4/5"
  difficulty: intro
  constraints:
    must_include: [one what-is-a-habitat item, one wrong-habitat item, one nonliving-parts-matter item, one habitats-change item, one which-need item]
    distractors: any-animal-anywhere, nonliving-doesnt-matter, habitats-never-change
```

**Gold items (v1):** (each distractor names its misconception)

1. What is a **habitat**? → **a home where an animal's needs are met** / any place at all — animals can live anywhere *(any-animal-anywhere)* / a word for the animal itself *(habitat-equals-animal)*
2. Could the **hare** live in the hot **desert**? → **no — no grass, burrow, or stream there** / yes — any animal can live anywhere *(any-animal-anywhere)*
3. The **sun** is not living. Does it still matter to the hare? → **yes — sunshine makes the grass grow that the hare eats** / no — nonliving things don't matter to animals *(nonliving-doesnt-matter)*
4. A hot summer **shrinks the pond**. What does that show? → **habitats can change over time** / habitats never change *(habitats-never-change)*
5. What does the **burrow** give the hare? → **shelter — a safe place to hide** / food to eat / water to drink *(need-mix-up baseline)*

Retake variants swap the specimen for the current fable animal and its habitat (tortoise/pond edge, ant/soil nest, crow/tall trees…) — the misconceptions stay fixed.

## `quiz.science.k2.materials.01` — The material tester

```yaml
quiz.science.k2.materials.01:
  objectives: [obj.science.k2.materials.01]
  skill: "name an object's material; size change keeps the material; predict light pass-through (all/some/none)"
  tools: lesson-package (built-in check) | parent-quiz (bridge)
  item_type: multiple_choice   # picture + read-aloud text; 2–3 choices at grade 1
  n_items: 5
  pass_rule: ">= 4/5"
  difficulty: intro
  constraints:
    must_include: [one object-vs-material item, one cut-in-half item, one all-light item, one thin-but-opaque item]
    distractors: cutting-changes-material, thin-equals-see-through, object-material-confusion
```

**Gold items (v1):** (each distractor names its misconception)

1. A chair is made of wood. Which word is the MATERIAL? → chair *(object-material-confusion: that's the object)* / **wood** / big *(property word, not a material)*
2. We cut a sheet of paper into little pieces. What are the little pieces? → **still paper** / not paper any more *(cutting-changes-material)* / wood *(cutting can't turn one material into another)*
3. We cut a wax candle in half. Is each half still wax? → **yes — smaller, but still wax** / no — cutting changed it *(cutting-changes-material)*
4. A flashlight shines at WINDOW GLASS. How much light gets through? → **all of it — you can see right through** / some *(glass is the clear one)* / none *(glass is not a blocker)*
5. A flashlight shines at a THIN sheet of cardboard. How much light gets through? → all — it is thin *(thin-equals-see-through)* / **none — thin does not mean see-through** / it makes its own light *(materials don't make light)*

Retakes swap the objects (metal vs wooden spoon, cut string/cloth, glass jar, wax paper as the "some" case, thin wooden ruler as the thin-but-opaque case); the misconceptions stay fixed — always one cut-in-half item and one thin-but-opaque item.

## `quiz.science.k2.matter.01` — Property detective

```yaml
quiz.science.k2.matter.01:
  objectives: [obj.science.k2.matter.01]
  skill: "describe objects by color/shape/texture/relative size-weight; sort by one named property"
  tools: lesson-package (built-in check) | parent-quiz (bridge)
  item_type: multiple_choice   # picture + read-aloud text; 2–3 choices at K
  n_items: 5
  pass_rule: ">= 4/5"
  difficulty: intro
  constraints:
    must_include: [one color item, one texture item, one big-vs-heavy item, one sort-rule-change item]
    distractors: property-word-confusion, big-equals-heavy, sort-rule-mixing
```

**Gold items (v1):** (each distractor names its misconception)

1. Which word tells the **ball's** COLOR? → round *(property-word-confusion: shape)* / **red** / smooth *(property-word-confusion: texture)*
2. Which word tells how the **sock** FEELS? → **soft** / blue *(property-word-confusion: color)* / little *(property-word-confusion: size)*
3. We are sorting by SHAPE. Where does the **ball** go? → with the red things *(sort-rule-mixing: color is not the rule)* / **with the round things** / with the big things *(sort-rule-mixing: size is not the rule)*
4. A **big balloon** and a **little rock** — which one is heavier? → the big balloon *(big-equals-heavy)* / **the little rock**
5. We sorted by color. Now the rule is SIZE. Where does the **little red button** go now? → with the red things — it always stays there *(sort-rule-mixing: the old rule is gone)* / **with the small things**

Retakes swap the objects (cup, leaf, blanket, coin, feather vs stone…); the misconceptions stay fixed — always one big-but-light vs small-but-heavy pair.

## `quiz.science.k2.matter.02` — Shape-shifter: solid, liquid, gas

```yaml
quiz.science.k2.matter.02:
  objectives: [obj.science.k2.matter.02]
  skill: "solid/liquid/gas properties; heating and cooling change phase but not the stuff"
  tools: lesson-package (built-in check) | parent-quiz (bridge)
  item_type: multiple_choice   # picture + read-aloud text; 2–3 choices at grade 2
  n_items: 5
  pass_rule: ">= 4/5"
  difficulty: intro
  constraints:
    must_include: [one liquid-takes-shape item, one sand item, one gas-is-real item, one same-stuff melting item, one cooling-freezes item]
    distractors: pours-means-liquid, gas-is-nothing, melting-makes-new-stuff, solid-keeps-shape-confusion
```

**Gold items (v1):** (each distractor names its misconception)

1. You pour the same **juice** into a tall thin glass. What shape is the juice now? → **tall and thin — the glass's shape** / it keeps its old shape *(solid-keeps-shape applied to a liquid)*
2. **Sand** pours out of a bucket. What is sand? → a liquid — because it pours *(pours-means-liquid)* / **many tiny solids**
3. The **balloon** is puffed up with air. What is inside? → nothing — air is nothing *(gas-is-nothing)* / **a gas that fills all the space**
4. Heat melts the **chocolate bar** into a puddle. What is the puddle? → **still chocolate — now liquid** / a new, different stuff *(melting-makes-new-stuff)*
5. What turns water into **ice**? → **cooling it down** / heating it up *(phase-direction mixup)* / pouring it fast *(pours-means-liquid adjacent — motion, not temperature, credited with the change)*

Retakes swap the materials (butter for chocolate, flour for sand, a beach ball for the balloon, milk for juice); the misconceptions stay fixed.

## `quiz.science.k2.motion.01` — The motion museum

```yaml
quiz.science.k2.motion.01:
  objectives: [obj.science.k2.motion.01]
  skill: "name a motion type (straight / circular / spinning / back-and-forth); explain sound as vibration"
  tools: lesson-package (built-in check) | parent-quiz (bridge)
  item_type: multiple_choice   # picture + read-aloud text; 2–3 choices at grade 1
  n_items: 5
  pass_rule: ">= 4/5"
  difficulty: intro
  constraints:
    must_include: [one spinning-vs-circular contrast pair (top AND merry-go-round), one back-and-forth item, one sound-source item]
    distractors: spinning-circular-swap, sound-just-happens, motion-word-swap
```

**Gold items (v1):** (each distractor names its misconception)

1. A ball rolls across the floor in one line. How does it move? → **straight** / in a circle *(motion-word-swap)* / back and forth *(motion-word-swap: one trip is not a repeat)*
2. A top turns fast in ONE spot. How does it move? → in a circle around a path *(spinning-circular-swap)* / **spinning** / straight
3. A horse on a merry-go-round travels around and around a path. How does it move? → spinning in one spot *(spinning-circular-swap, other direction)* / **circular — around a path** / back and forth
4. A swing goes forward, then back, then forward again. How does it move? → **back and forth** / straight *(motion-word-swap: the repeat is the clue)* / spinning
5. You hear a drum boom. What made the sound? → **the drum skin vibrates — it moves back and forth very fast** / sound just happens — nothing has to move *(sound-just-happens)* / the drum gets bigger *(nothing grows; something moves)*

Retakes swap the objects (rolling marble, spinning coin, ferris-wheel car, rocking chair, plucked guitar string / rubber band); the misconceptions stay fixed — always one top-vs-carousel contrast pair and one what-made-the-sound item.

## `quiz.science.k2.needs.01` — What does the lion need?

```yaml
quiz.science.k2.needs.01:
  objectives: [obj.science.k2.needs.01]
  skill: "name the five basic needs; distinguish needs from wants; same needs, different forms across animals"
  tools: lesson-package (built-in check) | parent-quiz (bridge)
  item_type: multiple_choice   # picture + read-aloud text; 3 choices at K
  n_items: 5
  pass_rule: ">= 4/5"
  difficulty: intro
  constraints:
    must_include: [one "which is NOT a basic need?" item, one shelter item, one air/space item, one two-animals same-need item]
    distractors: people-fun-as-need, shelter-equals-house, only-people-need-air, candy-as-food, small-animals-need-nothing
```

**Gold items (v1):** (each distractor names its misconception)

1. Which of these does the **lion** need to live? → **water** / a toy ball *(people-fun-as-need)* / a TV *(people-fun-as-need)*
2. What is the lion's **shelter**? → **shady rocks and tall grass** / a house with walls and a door *(shelter-equals-house)* / lions don't need shelter *(invisible-need skipped)*
3. Which one is **NOT** a basic need? → food / **candy** *(candy-as-food — a people-treat, not a need)* / air
4. Who needs **air and space**? → **every animal** / only people *(only-people-need-air)* / only big animals *(small-animals-need-nothing)*
5. A **mouse** and a **lion** both need food. What is different? → **the kind and the amount** / the mouse needs no food *(small-animals-need-nothing)* / they eat exactly the same things *(same-need-same-form)*

Retake variants swap the specimen for the current fable animal (wolf, ant, crow…) — the five needs and the misconceptions stay fixed.

## `quiz.science.k2.plants.01` — Grow a plant

```yaml
quiz.science.k2.plants.01:
  objectives: [obj.science.k2.plants.01]
  skill: "match plant parts to their jobs; pick what a plant needs vs does not"
  tools: lesson-package (built-in check) | parent-quiz (bridge)
  item_type: multiple_choice   # picture + read-aloud text; 2–3 choices at grade 1
  n_items: 5
  pass_rule: ">= 4/5"
  difficulty: intro
  constraints:
    must_include: [one which-part-drinks item, one which-part-makes-food item, one flower-job item, one does-it-need-air item]
    distractors: leaves-eat-dirt, plants-eat-soil, flower-decoration, no-air-needed, people-treats
```

**Gold items (v1):** (each distractor names its misconception)

1. Which part DRINKS water from the soil? → **the roots** / the leaves — they eat the dirt *(leaves-eat-dirt)* / the flower *(wrong part; flowers make seeds)*
2. Which part MAKES FOOD for the plant? → **the leaves — from light and air** / the roots — plants eat soil *(plants-eat-soil)* / the stem *(the stem carries; it doesn't make)*
3. What is the flower's JOB? → **it makes seeds, so new plants can grow** / it is just for pretty *(flower-decoration)* / it drinks the water *(wrong part; roots drink)*
4. Does a plant need AIR? → **yes — the leaves use air to make food** / no — plants do not breathe *(no-air-needed)*
5. Your plant is droopy. What will help it? → **water and light** / candy *(people-treats — carried over from the animal-needs quiz)* / a toy to play with *(people-treats)*

Retakes swap the framing plant (bean, sunflower, the child's own seed cup) and reorder the parts; the misconceptions stay fixed — always one leaves-eat-dirt distractor, one flower-decoration distractor, and one does-it-need-air item.

## `quiz.science.k2.plants.02` — Thank a plant

```yaml
quiz.science.k2.plants.02:
  objectives: [obj.science.k2.plants.02]
  skill: "plant products vs non-plant look-alikes; plants give air/homes/food; roots hold soil"
  tools: lesson-package (built-in check) | parent-quiz (bridge)
  item_type: multiple_choice   # picture (incl. the two-hills scene) + read-aloud text; 2–3 choices at grade 2
  n_items: 5
  pass_rule: ">= 4/5"
  difficulty: intro
  constraints:
    must_include: [one processed-plant-product item (bread or paper), one wool trap, one plants-give-animals item, one cut-all-trees item, the two-hills erosion prediction]
    distractors: soft-means-plant, processed-loses-plant-origin, cutting-harmless
```

**Gold items (v1):** (each distractor names its misconception)

1. Is **bread** from a plant? → **yes — it's baked from wheat** / no — bread isn't from a plant *(processed-loses-plant-origin)*
2. Is a **wool sweater** from a plant? → **no — wool comes from sheep** / yes — everything soft is from plants *(soft-means-plant)*
3. What do plants give **animals**? → **fresh air, homes, and food** / nothing — animals don't use plants *(cutting-harmless family: plants-don't-matter)*
4. What if we cut down **ALL the trees** and planted nothing? → **animals lose homes and food, and rain washes the soil away** / nothing bad — cutting all trees hurts nothing *(cutting-harmless)*
5. *(two-hills scene shown)* Rain falls on both hills. Which hill **keeps its soil**? → **the planted hill — roots hold the soil** / the bare hill *(plants-do-nothing)* / both exactly the same *(plants-do-nothing)*

Retake variants swap the traced products (paper for bread, chocolate/cacao for wheat; glass or a metal spoon for the wool trap) — the misconceptions stay fixed. The parent-quiz bridge may run item 1 against a product found in the child's own home hunt.

## `quiz.science.k2.resources.01` — Earth helpers

```yaml
quiz.science.k2.resources.01:
  objectives: [obj.science.k2.resources.01]
  skill: "resources come from the Earth; trash/reuse/recycle sorted and distinguished; choices affect air, water, land, living things"
  tools: lesson-package (built-in check) | parent-quiz (bridge)
  item_type: multiple_choice   # picture + read-aloud text; 2 choices at K
  n_items: 5
  pass_rule: ">= 4/5"
  difficulty: intro
  constraints:
    must_include: [one where-does-trash-go item, one reuse-definition item, one recycle-definition item, one my-choice-matters item, one comes-from-the-Earth item]
    distractors: trash-disappears, reuse-equals-recycle, one-person, store-origin
```

**Gold items (v1):** (each distractor names its misconception)

1. The trash truck drives away. Where does the trash go? → **to a landfill — a big pile on the land** / it disappears forever *(trash-disappears)*
2. What does **REUSE** mean? → **use the same thing again** / melt it down into something new — same as recycling *(reuse-equals-recycle)*
3. Paper goes in the **recycle** bin. What happens to it? → **it is made into NEW paper** / it is used again as the very same sheet *(reuse-equals-recycle, flipped)*
4. One kid picks up one wrapper by the stream. Does it help? → **yes — every choice helps the water and the animals** / no — one person can't change anything *(one-person)*
5. Where does the wood in your chair come from? → **trees that grew on the Earth** / the store makes it out of nothing *(store-origin)*

Retakes swap the resource in q5 (water in your cup → rain and rivers; the apple → a tree) and the item in q2/q3 (jar/bottle); the misconceptions stay fixed.

## `quiz.science.k2.resources.02` — Only so much

```yaml
quiz.science.k2.resources.02:
  objectives: [obj.science.k2.resources.02]
  skill: "resources are limited and slow to renew; actions affect availability; reduce vs reuse vs recycle as three distinct helps"
  tools: lesson-package (built-in check) | parent-quiz (bridge)
  item_type: multiple_choice   # picture + read-aloud text; 3 choices at grade 1
  n_items: 5
  pass_rule: ">= 4/5"
  difficulty: intro
  constraints:
    must_include: [one limited/slow-renewal item, one reduce scenario, one reuse-vs-recycle discriminator, one recycle-definition item, one wildlife/habitat choice]
    distractors: instant-refill, three-Rs-one-word, unlimited-resource, choices-dont-matter, bin-confusion
```

**Gold items (v1):** (each distractor names its misconception)

1. We cut down **every tree** today. When will tall trees be back? → **after many, many years — trees grow slowly** / tomorrow — nature refills instantly *(instant-refill)* / never — so it doesn't matter what we do *(choices-dont-matter)*
2. The **faucet runs** while you brush. Which help fits? → **reduce — turn it off, use less** / recycle — put the water in the recycle bin *(three-Rs-one-word)* / no help — water never runs out *(unlimited-resource)*
3. You draw on the **back** of used paper. Which help is that? → **reuse** / recycle *(three-Rs-one-word — nothing is made into a new thing)* / reduce *(three-Rs-one-word)*
4. What does **recycle** mean? → **an old thing is made into a NEW thing** / any kind of helping — all three words mean the same *(three-Rs-one-word)* / throwing things in any bin *(bin-confusion)*
5. A **berry bush** in the woods. The kind choice is… → **take some, leave some for the wildlife** / take them all — more grow by morning *(instant-refill)* / berries don't matter to animals *(wildlife-blind)*

Retake variants swap the scenarios (bath water, glass jar, cardboard box, forest firewood) — the three-help logic and the misconceptions stay fixed.

## `quiz.science.k2.senses.01` — Which sense told you?

```yaml
quiz.science.k2.senses.01:
  objectives: [obj.science.k2.senses.01]
  skill: "pair each sense with its body part; pick the sense(s) that give the clue in a scene"
  tools: lesson-package (built-in check) | parent-quiz (bridge)
  item_type: multiple_choice   # picture + read-aloud text; 3 choices at K
  n_items: 5
  pass_rule: ">= 4/5"
  difficulty: intro
  constraints:
    must_include: [one taste item, one sound-only "can't see it" item, one smell item, one touch item, one multi-sense item]
    distractors: organ-mixup, must-see-it, seeing-for-touch, mouth-as-smell
```

**Gold items (v1):** (each distractor names its misconception)

1. You bite a **cookie**. It is sweet! Which body part told you? → **tongue** / ears *(organ-mixup: hearing for taste)* / hands *(organ-mixup: feeling for taste)*
2. A **bird** sings high in a tree — you cannot see it. How do you know it is there? → **I hear it with my ears** / I see it with my eyes *(must-see-it)* / I smell it with my nose *(organ-mixup)*
3. **Bread** is baking in the oven. Which body part smells it? → **nose** / mouth *(mouth-as-smell — taste/smell conflation, kept simple at K)* / ears *(organ-mixup)*
4. The **kitten** is soft and fluffy. Which sense tells you? → **feel — my hands** / see — my eyes *(seeing-for-touch: "it looks soft")* / taste — my tongue *(organ-mixup)*
5. **Popcorn** pops under a lid — you cannot see it. Which senses can tell you? → **my ears AND my nose** / only my eyes *(must-see-it; also misses that senses team up)* / my hands *(organ-mixup)*

Retake variants swap the scenes (drum→ears, flowers→nose, ice cube→hands, lemon→tongue, sizzling pancakes→ears+nose) — the misconceptions stay fixed.

## `quiz.science.k2.sun.01` — Sun and shadows

```yaml
quiz.science.k2.sun.01:
  objectives: [obj.science.k2.sun.01]
  skill: "sun warms land/air/water; shadow = blocked light, falls away from the sun; shade is cooler"
  tools: lesson-package (built-in check) | parent-quiz (bridge)
  item_type: multiple_choice   # picture + read-aloud text; 2–3 choices at K
  n_items: 5
  pass_rule: ">= 4/5"
  difficulty: intro
  constraints:
    must_include: [one what-makes-a-shadow item, two shadow-side predict items (sun left AND sun moving right), one cooler-spot item, one what-does-the-sun-warm item]
    distractors: shadow-as-substance, sun-side-shadow, same-temp, only-warms-land
```

**Gold items (v1):** (each distractor names its misconception)

1. What makes the toy dinosaur's **shadow**? → **the toy BLOCKS the sun's light** / dark stuff leaks out of the toy *(shadow-as-substance)*
2. The sun is on the **LEFT**. Where is the toy's shadow? → **on the RIGHT — away from the sun** / on the LEFT — next to the sun *(sun-side-shadow)*
3. Which spot feels **COOLER**? → **the shade under the tree** / the sunny open spot *(warmth-reversal — child flips which side the sun heats)* / they feel the same *(same-temp)*
4. What does the sun warm? → **the land, the air, AND the water** / only the land *(only-warms-land)*
5. The sun moves to the **RIGHT**. What does the shadow do? → **it moves to the LEFT — away from the sun** / it stays next to the sun *(sun-side-shadow)*

Retakes swap the toy (dinosaur → block tower → watering can) and flip left/right; the misconceptions stay fixed.

## `quiz.science.k2.sun.02` — The sun's day trip

```yaml
quiz.science.k2.sun.02:
  objectives: [obj.science.k2.sun.02]
  skill: "sun position through the day; shadow length follows sun height; sun warms land, air, water; night = other side of the turning Earth"
  tools: lesson-package (built-in check) | parent-quiz (bridge)
  item_type: multiple_choice   # picture + read-aloud text; 3 choices at grade 1
  n_items: 5
  pass_rule: ">= 4/5"
  difficulty: intro
  constraints:
    must_include: [one where-is-the-sun (time) item, one shortest-shadow item, one night item, one why-does-it-seem-to-move item, one what-does-it-warm item]
    distractors: sun-alive, sun-disappears, same-shadow, land-only, static-sun
```

**Gold items (v1):** (each distractor names its misconception)

1. It's **morning**. Where is the sun? → **low, on the side where it rises** / straight overhead *(noon-swap)* / nowhere — it went away *(sun-disappears)*
2. When is the tree's shadow **shortest**? → **at noon** / in the morning *(time-swap — low sun makes LONG shadows)* / shadows stay the same all day *(same-shadow)*
3. At **night**, the sun… → **shines on the other side of the Earth** / turns off and disappears *(sun-disappears)* / comes down to sleep *(sun-alive)*
4. **Why** does the sun seem to move across the sky? → **the Earth slowly turns** / the sun is alive and follows you *(sun-alive)* / it doesn't move — it stays in one spot *(static-sun)*
5. What does the sun **warm**? → **the land, the air, AND the water** / only the land *(land-only)* / nothing — it only gives light *(no-warmth)*

Retake variants swap the scene object (tree → flagpole → the child) — sun positions, shadow logic and misconceptions stay fixed.

## `quiz.science.k2.water.01` — The water journey

```yaml
quiz.science.k2.water.01:
  objectives: [obj.science.k2.water.01]
  skill: "water's uses, places found, three forms (same water), flows downhill"
  tools: lesson-package (built-in check) | parent-quiz (bridge)
  item_type: multiple_choice   # picture + read-aloud text; 2–3 choices at K
  n_items: 5
  pass_rule: ">= 4/5"
  difficulty: intro
  constraints:
    must_include: [one ice-is-water item, one steam item, one flow-direction item, one needs-water item]
    distractors: ice-not-water, steam-is-air, steam-is-smoke, water-flows-uphill, water-does-not-flow, nonliving-needs-water
```

**Gold items (v1):** (each distractor names its misconception)

1. What is an **ice cube**? → **frozen water** / not water — its own cold thing *(ice-not-water)*
2. What is the **steam** above hot soup? → just air *(steam-is-air)* / **water floating up as a gas** / smoke from a fire *(steam-is-smoke)*
3. Rain lands on top of a **hill**. Which way does it flow? → up the hill *(water-flows-uphill)* / **down the hill** / it stays on top forever *(water-does-not-flow)*
4. Which one needs water to **grow**? → **a bean plant** / a plastic flower *(nonliving-needs-water: looks alive, isn't — ties to `quiz.science.k2.living.01`)* / a rock *(nonliving-needs-water)*
5. Can water flow UP a hill all by itself? → yes — if the hill is small *(water-flows-uphill)* / **no — water always finds the low path**

Retakes swap the pictures (snowman for ice, kettle for steam, slide/gutter for the slope); the misconceptions stay fixed.

## `quiz.science.k2.weather.01` — Patterns in the sky

```yaml
quiz.science.k2.weather.01:
  objectives: [obj.science.k2.weather.01]
  skill: "day/night cycle repeats; seasons in fixed order; weather recorded daily reveals patterns; weather ≠ season"
  tools: lesson-package (built-in check) | parent-quiz (bridge)
  item_type: multiple_choice   # picture + read-aloud text; 2–3 choices at K
  n_items: 5
  pass_rule: ">= 4/5"
  difficulty: intro
  constraints:
    must_include: [one day/night-cycle item, two season-order items, one weather-vs-season item, one why-record-weather item]
    distractors: sun-gone-forever, seasons-random-order, weather-equals-season, nothing-to-record
```

**Gold items (v1):** (each distractor names its misconception)

1. The sun goes down at night. What happens in the morning? → **the sun comes up again** / the sun is gone forever *(sun-gone-forever)*
2. What season comes after **SUMMER**? → **fall** / winter *(seasons-random-order — skips a season)* / spring *(seasons-random-order — runs backwards)*
3. What season comes after **WINTER**? → **spring** / summer *(seasons-random-order)*
4. One hot, sunny day comes in spring. Did spring turn into summer? → **no — weather changes day to day; the season stays** / yes — a hot day means it is summer now *(weather-equals-season)*
5. How can we find the weather pattern? → **write the weather down every day** / we can't — weather is just random *(nothing-to-record)*

Retakes rotate which season pair is asked (after fall? after spring?) and swap the q4 weather (a cold day in summer); the misconceptions stay fixed.

## `quiz.science.k2.weather.02` — One meadow, four seasons

```yaml
quiz.science.k2.weather.02:
  objectives: [obj.science.k2.weather.02]
  skill: "season effects on plants, animals, people; daily weather varies inside a season; why we record weather"
  tools: lesson-package (built-in check) | parent-quiz (bridge)
  item_type: multiple_choice   # picture + read-aloud text; 3 choices at grade 1
  n_items: 5
  pass_rule: ">= 4/5"
  difficulty: intro
  constraints:
    must_include: [one weather-vs-season trap, one animal-effect item, one plant-effect item, one people-effect item, one why-record item]
    distractors: one-day-season, animals-feel-nothing, tree-static, records-pointless, animals-like-people
```

**Gold items (v1):** (each distractor names its misconception)

1. One **HOT** day comes in spring. Is it summer now? → **no — one day is not a season** / yes — hot means summer *(one-day-season)* / spring can never have hot days *(weather-rigid)*
2. What does the **fox** do for winter? → **grows a thick warm coat** / nothing — animals don't feel winter *(animals-feel-nothing)* / puts on a scarf from the store *(animals-like-people)*
3. The **tree** is bare. Which season, most likely? → **winter** / summer *(season-swap)* / trees are bare in every season *(tree-static)*
4. Why do we **record** the weather every day? → **to find the pattern of the season** / no reason — weather is random *(records-pointless)* / writing it down changes the weather *(record-magic)*
5. It's **fall** and getting cooler. What do people do? → **put on warmer clothes** / keep summer clothes — seasons don't change us *(seasons-dont-affect-people)* / stop going outside forever *(overreaction)*

Retake variants swap the animal (fox → squirrel storing nuts → goose flying south) and the strip's counts — the season logic and misconceptions stay fixed.

## `quiz.science.k2.weather.03` — Junior forecaster

```yaml
quiz.science.k2.weather.03:
  objectives: [obj.science.k2.weather.03]
  skill: "tools measure weather; record → pictograph → pattern; predict and prepare for storms"
  tools: lesson-package (built-in check) | parent-quiz (bridge)
  item_type: multiple_choice   # picture (incl. one in-quiz pictograph) + read-aloud text; 2–3 choices at grade 2
  n_items: 5
  pass_rule: ">= 4/5"
  difficulty: intro
  constraints:
    must_include: [one tool-identification item, one tool-only-measures item, one pictograph-reading item, one why-record item, one storm-prep item]
    distractors: tool-makes-weather, cant-know-tomorrow, pictograph-as-decoration
```

**Gold items (v1):** (each distractor names its misconception)

1. Which tool tells you **how warm** it is? → **thermometer** / rain gauge *(tool-job mix-up)* / windsock *(tool-job mix-up)*
2. The thermometer shows a hot day. Did the thermometer **make** it hot? → **no — it only measures the heat** / yes — the tool makes the weather *(tool-makes-weather)*
3. *(pictograph shown: 4 suns, 2 raindrops, 1 cloud; each picture = one day)* How many **sunny days** were in the week? → **4** / 2 *(row mix-up / miscount)* / you can't tell — the pictures are just decoration *(pictograph-as-decoration)*
4. Why record the weather **every single day**? → **the record shows patterns that help you predict** / no reason — nobody can know anything about tomorrow *(cant-know-tomorrow)*
5. The pattern says a **storm** is coming tonight. What do you do? → **charge the flashlight and stay inside** / nothing — tomorrow is a total mystery *(cant-know-tomorrow)* / ask the thermometer to make it sunny *(tool-makes-weather)*

Retake variants re-deal the pictograph counts (e.g. 5/1/2) and swap which tool is asked — the misconceptions stay fixed. When the child's own paper pictograph exists, the parent-quiz bridge may ask items 3–4 against *that* chart.
