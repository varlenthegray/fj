<template>
  <nav class="breadcrumb" aria-label="breadcrumbs">
    <ul>
      <li><router-link to="/">Home</router-link></li>
      <li><span class="mx-3 has-text-weight-light">Writings</span></li>
      <li><span class="mx-3 has-text-weight-light">Create</span></li>
      <li class="is-active"><router-link to="/writings/create/character" aria-current="page">Character</router-link></li>
    </ul>
  </nav>

  <div class="box">
    <h1 class="title">What is this?</h1>

    <p>This is a list of your characters in your writing. The questions below are designed to enhance your understanding
      of your character and determine if your character is a "main" character or a background character.</p>
  </div>

  <div class="field is-grouped">
    <label class="checkbox"><input type="checkbox" v-model="recurring"> Recurring Character</label>
    <label class="checkbox mx-3"><input type="checkbox" v-model="important"> Important</label>
    <label class="checkbox mx-3"><input type="checkbox" v-model="hasPast"> Has a Past</label>
    <label class="checkbox mx-3"><input type="checkbox" v-model="hasFuture"> Will Have a Future</label>
    <label class="checkbox mx-3"><input type="checkbox" v-model="hasRelationships"> Has Relationships</label>
  </div>

  <div class="field">
    <label class="label">Family/Last Name</label>
    <div class="control"><input class="input" type="text" placeholder="e.g. Smith"></div>
  </div>

  <div v-if="recurring || important">
    <div class="my-3 has-text-centered">
      <n-upload>
        <n-upload-dragger>
          <div style="margin-bottom: 12px"><n-icon size="48" :depth="3"><archive-outline /></n-icon></div>

          <n-text style="font-size: 16px">Click or drag an image for your Character Portrait.</n-text>

          <n-p depth="3" style="margin: 8px 0 0 0">Do not upload sensitive information.</n-p>
        </n-upload-dragger>
      </n-upload>

      Need inspiration? <a href="https://www.artbreeder.com/browse" onclick="preventDefault();" target="_blank">Try Artbreeder!</a>
    </div>

    <div class="field is-grouped">
      <label class="checkbox"><input type="checkbox" v-model="fantasy"> Fantasy Fields</label>
      <label class="checkbox mx-3"><input type="checkbox" v-model="detailed"> Detailed Fields</label>
    </div>

    <div class="columns">
      <div class="column">
        <div class="field">
          <label class="label">First Name</label>
          <div class="control"><input class="input" type="text" placeholder="e.g. John"></div>
        </div>

        <div class="field">
          <label class="label">Age (years)</label>
          <div class="control"><input class="input" min="0" type="number" placeholder="e.g. 18"></div>
        </div>

        <div class="field" v-if="fantasy">
          <label class="label">Species</label>
          <div class="control"><input class="input" type="text" placeholder="e.g. Human"></div>
        </div>

        <div class="field" v-if="detailed">
          <label class="label">Eye Color</label>
          <div class="control"><input class="input" type="text" placeholder="e.g. Blue"></div>
        </div>

        <div class="field" v-if="detailed">
          <label class="label">Hair Color</label>
          <div class="control"><input class="input" type="text" placeholder="e.g. Red"></div>
        </div>

        <div class="field" v-if="detailed">
          <label class="label">Life Expectancy</label>
          <div class="control"><input class="input" type="text" placeholder="e.g. 400 yrs"></div>
        </div>

        <div class="field" v-if="detailed">
          <label class="label">Languages</label>
          <div class="control"><input class="input" type="text" placeholder="e.g. English, Latin, etc."></div>
        </div>

        <div class="field">
          <label class="label">Unique Abilities</label>
          <div class="control"><input class="input" type="text" placeholder="e.g. Extremely Strong"></div>
        </div>

        <div class="field">
          <label class="label">Goals</label>
          <div class="control"><input class="input" type="text" placeholder="e.g. Live Forever"></div>
        </div>
      </div>

      <div class="column">
        <div class="field" v-if="detailed">
          <label class="label">Gender</label>
          <div class="control"><input class="input" type="text" placeholder="e.g. Male/Female"></div>
        </div>

        <div class="field" v-if="detailed">
          <label class="label">Height</label>
          <div class="control"><input class="input" type="text" placeholder="e.g. 3 ft"></div>
        </div>

        <div class="field" v-if="detailed">
          <label class="label">Skin Color</label>
          <div class="control"><input class="input" type="text" placeholder="e.g. Dark/Blue"></div>
        </div>

        <div class="field" v-if="detailed">
          <label class="label">Defining Features</label>
          <div class="control"><input class="input" type="text" placeholder="e.g. Scars, Glasses, Facial Hair, Tattoos, Piercings, etc"></div>
        </div>

        <div class="field">
          <label class="label">Archetype</label>
          <div class="control"><input class="input" type="text" placeholder="e.g. Good, Evil, Chaotic Neutral"></div>
        </div>

        <div class="field" v-if="detailed">
          <label class="label">Hobbies</label>
          <div class="control"><input class="input" type="text" placeholder="e.g. Learning"></div>
        </div>

        <div class="field" v-if="detailed">
          <label class="label">Home</label>
          <div class="control"><input class="input" type="text" placeholder="e.g. London, Gnome House, Bar, etc"></div>
        </div>

        <div class="field" v-if="detailed">
          <label class="label">Job</label>
          <div class="control"><input class="input" type="text" placeholder="e.g. Bartender, Hero, Fighter"></div>
        </div>

        <div class="field" v-if="detailed">
          <label class="label">Traits</label>
          <div class="control">
            <n-select v-model:value="traits" :render-tag="renderTag" multiple filterable :options="traitOptions" />
          </div>
        </div>
      </div>
    </div>
  </div>

  <div v-if="hasRelationships" class="my-3">
    <div class="field">
      <label class="label">What Are Their Relations?</label>
      <div class="control"><QuillEditor theme="snow" toolbar="minimum" style="overflow: auto; max-height: 200px;" /></div>
    </div>

    <!-- todo: add in books dropdown or reference to writings -->
  </div>

  <div v-if="important" class="my-3">
    <div class="field">
      <label class="label">What Makes them Important?</label>
      <div class="control"><QuillEditor theme="snow" toolbar="minimum" style="overflow: auto; max-height: 200px;" /></div>
    </div>

    <!-- todo: add in books dropdown or reference to writings -->
  </div>

  <div v-if="hasPast" class="my-3">
    <div class="field">
      <label class="label">Past Information</label>
      <div class="control"><QuillEditor theme="snow" toolbar="minimum" style="overflow: auto; max-height: 200px;" /></div>
    </div>

    <!-- todo: add in books dropdown or reference to writings -->
  </div>

  <div v-if="hasFuture" class="my-3">
    <div class="field">
      <label class="label">Future Information</label>
      <div class="control"><QuillEditor theme="snow" toolbar="minimum" style="overflow: auto; max-height: 200px;" /></div>
    </div>

    <!-- todo: add in books dropdown or reference to writings -->
  </div>
</template>

<script>
import { QuillEditor } from '@vueup/vue-quill';
import '@vueup/vue-quill/dist/vue-quill.snow.css';
import {h} from "vue";
import {NTag} from "naive-ui";
import { ArchiveOutline } from "@vicons/ionicons5";

function trait(name, type = '') {
  let ucName = name.charAt(0).toUpperCase() + name.slice(1);

  switch(type) {
    case 'g':
      type = 'success';
      break;

    case 'n':
      type = 'info';
      break;

    case 'b':
      type = 'error';
      break;

    default:
      type = '';
      break;
  }

  return { label:  ucName, value: name, type: type }
}

export default {
  name: "Character",
  components: { QuillEditor, ArchiveOutline },
  setup() {
    const renderTag = ({ option, handleClose }) => {
      return h(NTag, {
        type: option.type,
        closable: true,
        onClose: (e) => {
          e.stopPropagation();
          handleClose();
        }
      }, { default: () => option.label });
    };

    let traitOptions = [
      { type: 'group', label: 'Nice', key: 'nice',
        children: [
          trait('helpful', 'g'), trait('friendly', 'g'), trait('kindhearted', 'g'),
          trait('compassionate', 'g'), trait('pleasant', 'g'), trait('thoughtful', 'g'),
          trait('agreeable', 'g'), trait('courteous', 'g'),
        ]
      },
      { type: 'group', label: 'Mean', key: 'mean',
        children: [
          trait('wicked', 'b'), trait('rude', 'b'), trait('thoughtless', 'b'), trait('impolite', 'b'),
          trait('cruel', 'b'), trait('hateful', 'b'), trait('unfriendly', 'b'), trait('unkind', 'b'),
        ]
      },
      { type: 'group', label: 'Happy', key: 'happy',
        children: [
          trait('cheerful', 'g'), trait('joyful', 'g'), trait('excited', 'g'), trait('satisfied', 'g'),
          trait('content', 'g'), trait('delighted', 'g'), trait('pleased', 'g'), trait('glad', 'g'),
        ]
      },
      { type: 'group', label: 'Sad', key: 'sad',
        children: [
          trait('depressed', 'b'), trait('serious', 'n'), trait('gloomy', 'b'), trait('miserable', 'b'),
          trait('unhappy', 'b'), trait('discouraged', 'b'), trait('sorrowful', 'b'), trait('mournful', 'b'),
        ]
      },
      { type: 'group', label: 'Scared', key: 'scared',
        children: [
          trait('terrified', 'b'), trait('panicked', 'b'), trait('nervous', 'b'), trait('afraid', 'b'),
          trait('alarmed', 'b'), trait('frightened', 'b'), trait('fearful', 'b'), trait('petrified', 'b'),
        ]
      },
      { type: 'group', label: 'Mad', key: 'mad',
        children: [
          trait('exasperated', 'b'), trait('annoyed', 'b'), trait('outraged', 'b'), trait('furious', 'b'),
          trait('frustrated', 'b'), trait('angry', 'b'), trait('displeased', 'b'), trait('irritated', 'b'),
        ]
      },
      { type: 'group', label: 'Smart', key: 'smart',
        children: [
          trait('intelligent', 'g'), trait('brilliant', 'g'), trait('clever', 'g'), trait('bright', 'g'),
          trait('skillful', 'g'), trait('wise', 'g'), trait('brainy', 'g'),
        ]
      },
      { type: 'group', label: 'Brave', key: 'brave',
        children: [
          trait('daring', 'g'), trait('courageous', 'g'), trait('adventurous', 'g'), trait('fearless', 'g'),
          trait('heroic', 'g'),
        ]
      },
      { type: 'group', label: 'Tricky', key: 'tricky',
        children: [
          trait('dishonest', 'b'), trait('deceitful', 'b'), trait('sneaky', 'b'), trait('secretive', 'b'),
          trait('sly', 'b'), trait('untrustworthy', 'b'),
        ]
      },
      { type: 'group', label: 'Funny', key: 'funny',
        children: [
          trait('amusing', 'g'), trait('hysterical', 'g'), trait('humorous', 'g'), trait('comical', 'g'),
          trait('hilarious', 'g'), trait('silly', 'g'),
        ]
      },
      { type: 'group', label: 'Thankful', key: 'thankful',
        children: [
          trait('appreciative', 'g'), trait('grateful', 'g'),
        ]
      },
      { type: 'group', label: 'Active', key: 'active',
        children: [
          trait('athletic', 'g'), trait('energetic', 'g'),
        ]
      },
      { type: 'group', label: 'Talkative', key: 'talkative',
        children: [
          trait('chatty', 'n'), trait('communicative', 'n'),
        ]
      },
      { type: 'group', label: 'Shy', key: 'shy',
        children: [
          trait('bashful', 'n'), trait('quiet','n'),
        ]
      },
      { type: 'group', label: 'Positive Traits', key: 'positive-traits',
        children: [
          trait('active ', 'g'), trait('Active ', 'g'), trait('Admirable ', 'g'), trait('Adventurous ', 'g'),
          trait('Agreeable ', 'g'), trait('Amiable ', 'g'), trait('Amusing ', 'g'), trait('Appreciative ', 'g'),
          trait('Athletic ', 'g'), trait('Authentic ', 'g'), trait('Benevolent ', 'g'), trait('Brave  ', 'g'),
          trait('Bright ', 'g'), trait('Brilliant ', 'g'), trait('Calm   ', 'g'), trait('Capable ', 'g'),
          trait('Caring ', 'g'), trait('Charming ', 'g'), trait('Cheerful ', 'g'), trait('Clean  ', 'g'),
          trait('Clear - headed ', 'g'), trait('Clever ', 'g'), trait('Compassionate ', 'g'), trait('Confident ', 'g'),
          trait('Considerate ', 'g'), trait('Cooperative ', 'g'), trait('Courageous ', 'g'), trait('Courteous ', 'g'),
          trait('Creative ', 'g'), trait('Curious ', 'g'), trait('Dedicated ', 'g'), trait('Easygoing ', 'g'),
          trait('Educated ', 'g'), trait('Enthusiastic ', 'g'), trait('Ethical ', 'g'), trait('Exciting ', 'g'),
          trait('Extraordinary ', 'g'), trait('Fair ', 'g'), trait('Firm ', 'g'), trait('Focused ', 'g'), trait('Forgiving ', 'g'),
          trait('Friendly ', 'g'), trait('Generous ', 'g'), trait('Gentle ', 'g'), trait('Good-natured ', 'g'), trait('Grateful ', 'g'),
          trait('Happy ', 'g'), trait('Hardworking ', 'g'), trait('Helpful ', 'g'), trait('Heroic ', 'g'), trait('Honest ', 'g'),
          trait('Hopeful ', 'g'), trait('Humble ', 'g'), trait('Innocent ', 'g'), trait('Intelligent ', 'g'), trait('Inventive ', 'g'),
          trait('Joyful ', 'g'), trait('Kind ', 'g'), trait('Lively ', 'g'), trait('Loving ', 'g'), trait('Loyal ', 'g'),
          trait('Neat ', 'g'), trait('Nice ', 'g'), trait('Optimistic ', 'g'), trait('Organized ', 'g'), trait('Passionate ', 'g'),
          trait('Patient ', 'g'), trait('Peaceful ', 'g'), trait('Playful ', 'g'), trait('Polite ', 'g'), trait('Principled ', 'g'),
          trait('Reliable ', 'g'), trait('Respectful ', 'g'), trait('Responsible ', 'g'), trait('Self-disciplined ', 'g'),
          trait('Selfless ', 'g'), trait('Sincere ', 'g'), trait('Skillful ', 'g'), trait('Strong ', 'g'), trait('Sweet ', 'g'),
          trait('Thoughtful ', 'g'), trait('Trustworthy ', 'g'), trait('Understanding ', 'g'), trait('Unselfish ', 'g'), trait('Wise ', 'g')
        ]
      },
      { type: 'group', label: 'Negative Traits', key: 'negative-traits',
        children: [
          trait('Aggressive ', 'b'), trait('Angry ', 'b'), trait('Anxious ', 'b'), trait('Argumentative ', 'b'),
          trait('Arrogant ', 'b'), trait('Bored ', 'b'), trait('Bossy ', 'b'), trait('Brutal ', 'b'), trait('Careless ', 'b'),
          trait('Charmless ', 'b'), trait('Clumsy ', 'b'), trait('Conceited ', 'b'), trait('Cowardly ', 'b'), trait('Critical ', 'b'),
          trait('Cruel ', 'b'), trait('Dangerous ', 'b'), trait('Deceitful ', 'b'), trait('Destructive ', 'b'), trait('Devious ', 'b'),
          trait('Difficult ', 'b'), trait('Discouraging ', 'b'), trait('Discourteous ', 'b'), trait('Dishonest ', 'b'),
          trait('Disloyal ', 'b'), trait('Disobedient ', 'b'), trait('Disorganized ', 'b'), trait('Disrespectful ', 'b'),
          trait('Disruptive ', 'b'), trait('Envious ', 'b'), trait('Fearful ', 'b'), trait('Foolish ', 'b'), trait('Forgetful ', 'b'),
          trait('Frightening ', 'b'), trait('Gloomy ', 'b'), trait('Greedy ', 'b'), trait('Grim ', 'b'), trait('Hateful ', 'b'),
          trait('Haughty ', 'b'), trait('Hostile ', 'b'), trait('Ignorant ', 'b'), trait('Impatient ', 'b'), trait('Impractical ', 'b'),
          trait('Inconsiderate ', 'b'), trait('Insincere ', 'b'), trait('Insulting ', 'b'), trait('Intolerant ', 'b'),
          trait('Irresponsible ', 'b'), trait('Irritable ', 'b'), trait('Jealous ', 'b'), trait('Lazy ', 'b'), trait('Liar ', 'b'),
          trait('Mean ', 'b'), trait('Meddlesome ', 'b'), trait('Messy ', 'b'), trait('Miserable ', 'b'), trait('Monstrous ', 'b'),
          trait('Moody ', 'b'), trait('Negative ', 'b'), trait('Neglectful ', 'b'), trait('Obnoxious ', 'b'), trait('Petty ', 'b'),
          trait('Possessive ', 'b'), trait('Power-hungry ', 'b'), trait('Prejudiced ', 'b'), trait('Resentful ', 'b'),
          trait('Rude ', 'b'), trait('Scornful ', 'b'), trait('Selfish ', 'b'), trait('Shallow ', 'b'), trait('Sloppy ', 'b'),
          trait('Sneaky ', 'b'), trait('Snobbish ', 'b'), trait('Thoughtless ', 'b'), trait('Unappreciative ', 'b'),
          trait('Uncaring ', 'b'), trait('Uncooperative ', 'b'), trait('Unforgiving ', 'b'), trait('Unfriendly ', 'b'),
          trait('Ungrateful ', 'b'), trait('Unhealthy ', 'b'), trait('Unreliable ', 'b'), trait('Violent ', 'b'),
          trait('Weak ', 'b'), trait('Wicked ', 'b')
        ]
      },
      { type: 'group', label: 'Neutral Traits', key: 'neutral-traits',
        children: [
          trait('Abrupt ', 'n'), trait('Active ', 'n'), trait('Alluring ', 'n'), trait('Aloof ', 'n'), trait('Ambitious ', 'n'),
          trait('Astonishing ', 'n'), trait('Average ', 'n'), trait('Bold ', 'n'), trait('Businesslike ', 'n'), trait('Carefree ', 'n'),
          trait('Casual ', 'n'), trait('Cautious ', 'n'), trait('Childlike ', 'n'), trait('Commonplace ', 'n'), trait('Competitive ', 'n'),
          trait('Confident ', 'n'), trait('Conventional ', 'n'), trait('Decisive ', 'n'), trait('Discreet ', 'n'), trait('Distracted ', 'n'),
          trait('Dramatic ', 'n'), trait('Emotional ', 'n'), trait('Enigmatic ', 'n'), trait('Experimental ', 'n'), trait('Extroverted ', 'n'),
          trait('Fidgety ', 'n'), trait('Firm ', 'n'), trait('Formal ', 'n'), trait('Frugal ', 'n'), trait('Guarded ', 'n'),
          trait('High-spirited ', 'n'), trait('Imaginative ', 'n'), trait('Impressionable ', 'n'), trait('Impulsive ', 'n'),
          trait('Inactive ', 'n'), trait('Inflexible ', 'n'), trait('Intense ', 'n'), trait('Introverted ', 'n'), trait('Lively ', 'n'),
          trait('Loud ', 'n'), trait('Mature ', 'n'), trait('Meek ', 'n'), trait('Mellow ', 'n'), trait('Memorable ', 'n'),
          trait('Methodical ', 'n'), trait('Mysterious ', 'n'), trait('Normal ', 'n'), trait('Objective ', 'n'), trait('Old-fashioned ', 'n'),
          trait('Opinionated ', 'n'), trait('Ordinary ', 'n'), trait('Outgoing ', 'n'), trait('Outspoken ', 'n'), trait('Persuadable ', 'n'),
          trait('Persuasive ', 'n'), trait('Playful ', 'n'), trait('Practical ', 'n'), trait('Predictable ', 'n'), trait('Preoccupied ', 'n'),
          trait('Prim ', 'n'), trait('Private ', 'n'), trait('Proud ', 'n'), trait('Questioning ', 'n'), trait('Quiet ', 'n'),
          trait('Quirky ', 'n'), trait('Realistic ', 'n'), trait('Reserved ', 'n'), trait('Restless ', 'n'), trait('Restrained ', 'n'),
          trait('Sensational ', 'n'), trait('Sensitive ', 'n'), trait('Sentimental ', 'n'), trait('Shameless ', 'n'), trait('Shrewd ', 'n'),
          trait('Shy ', 'n'), trait('Silent ', 'n'), trait('Solemn ', 'n'), trait('Solitary ', 'n'), trait('Sorrowful ', 'n'),
          trait('Spontaneous ', 'n'), trait('Subtle ', 'n'), trait('Talkative ', 'n'), trait('Traditional ', 'n'), trait('Trendy ', 'n'),
          trait('Unbending ', 'n'), trait('Uncertain ', 'n'), trait('Unchanging ', 'n'), trait('Unemotional ', 'n'), trait('Unhurried ', 'n'),
          trait('Uninhibited ', 'n'), trait('Uninterested ', 'n'), trait('Unopinionated ', 'n'), trait('Unpredictable ', 'n'), trait('Unusual ', 'n'),
          trait('Verbose ', 'n'), trait('Youthful ', 'n')
        ]
      },
    ];

    return { traitOptions, renderTag };
  },
  data() {
    return {
      recurring: false,
      important: false,
      hasPast: false,
      hasFuture: false,
      fantasy: true,
      detailed: true,
      hasRelationships: false,
      traits: [],
    }
  }
}
</script>

<style>
.n-base-select-menu .n-base-select-group-header {
  background-color: #000;
  color: #FFF;
  font-weight: bold;
}
</style>