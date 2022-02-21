<template>
  <div class="box">
    <!--    fixme: need to update the value of this when you navigate outside of menu -->
    <n-menu :options="menuOptions" :default-expanded-keys="defaultExpandedKeys" :indent="16" />
  </div>
</template>

<script>
import { h } from 'vue';
import { RouterLink } from 'vue-router'
import { NIcon } from 'naive-ui';
import VideogameAssetFilled from '@vicons/material/VideogameAssetFilled';
import LaptopMacTwotone from '@vicons/material/LaptopMacTwotone';
import SellTwotone from '@vicons/material/SellTwotone';
import AreaChartOutlined from '@vicons/material/AreaChartOutlined';
import SignpostTwotone from '@vicons/material/SignpostTwotone';
import MenuBookOutlined from '@vicons/material/MenuBookOutlined';
import MenuBookTwotone from '@vicons/material/MenuBookTwotone';
import LibraryBooksOutlined from '@vicons/material/LibraryBooksOutlined';
import CollectionsBookmarkTwotone from '@vicons/material/CollectionsBookmarkTwotone';
import { WritingSign, Books, ChartArrowsVertical } from '@vicons/tabler';
import { Blog, BoxSmall, BoxMedium, BoxLarge } from '@vicons/carbon';
import { Shower, Bath, Signature, Book } from '@vicons/fa';
import { IosLaptop } from '@vicons/ionicons4';
import {
  Book24Filled, DocumentOnePage24Filled, DrawImage24Filled, FoodPizza24Filled,
  ReadingModeMobile24Filled, Bed24Filled, BookCompass24Filled, Box24Filled,
  Money24Filled, CalligraphyPen24Filled, Keyboard12324Filled, DesktopToolbox24Regular,
  DesktopMac24Regular, BuildingRetailMoney24Filled, MoneyCalculator24Filled, Globe24Regular,
  BookOpenGlobe24Filled, BookContacts24Regular, BookPulse24Regular, BookStar24Regular,
  BookTheta24Regular, BookAdd24Regular, NotebookAdd24Regular, BookmarkMultiple24Regular,
  NotebookLightning24Regular, BookDatabase24Regular
} from '@vicons/fluent';

function renderIcon (icon) {
  return () => h(NIcon, null, { default: () => h(icon) });
}

function renderLabel(to, labelName) {
  return () => h(RouterLink, {to: to}, { default: () => labelName })
}

const menuOptions = [
  {
    label: 'Game',
    key: 'game',
    icon: renderIcon(VideogameAssetFilled),
    children: [
      {
        label: 'Write',
        key: 'write',
        icon: renderIcon(WritingSign),
        children: [
          {label: 'Book', key: 'write-book', icon: renderIcon(Book24Filled)},
          {label: 'Short Story', key: 'write-short-story', icon: renderIcon(DocumentOnePage24Filled)},
          {label: 'Comic', key: 'write-comic', icon: renderIcon(DrawImage24Filled)},
          {label: 'Blog', key: 'write-blog', icon: renderIcon(Blog)},
          {label: 'Novel', key: 'write-novel', icon: renderIcon(Books)},
        ]
      },
      {
        label: 'Needs',
        key: 'needs',
        icon: renderIcon(Shower),
        children: [
          {label: 'Hygiene', key: 'need-hygiene', icon: renderIcon(Bath)},
          {label: 'Eat', key: 'need-eat', icon: renderIcon(FoodPizza24Filled)},
          {label: 'Read', key: 'need-read', icon: renderIcon(ReadingModeMobile24Filled)},
          {label: 'Sleep', key: 'need-sleep', icon: renderIcon(Bed24Filled)},
          {label: 'Research', key: 'need-research', icon: renderIcon(BookCompass24Filled)},
        ]
      },
      {
        label: 'Items',
        key: 'items',
        icon: renderIcon(Box24Filled),
        children: [
          {
            label: 'Buy',
            key: 'item-buy',
            icon: renderIcon(Money24Filled),
            children: [
              {label: 'Pen & Paper', key: 'buy-pen-paper', icon: renderIcon(CalligraphyPen24Filled)},
              {label: 'Typewriter', key: 'buy-typewriter', icon: renderIcon(Keyboard12324Filled)},
              {label: 'Used Desktop', key: 'buy-used-desktop', icon: renderIcon(DesktopToolbox24Regular)},
              {label: 'New Desktop', key: 'buy-new-desktop', icon: renderIcon(DesktopMac24Regular)},
              {label: 'Used Laptop', key: 'buy-used-laptop', icon: renderIcon(LaptopMacTwotone)},
              {label: 'New Laptop', key: 'buy-new-laptop', icon: renderIcon(IosLaptop)},
            ]
          },
          {label: 'Sell', key: 'item-sell', icon: renderIcon(SellTwotone)},
          {label: 'Upgrade', key: 'item-upgrade', icon: renderIcon(BuildingRetailMoney24Filled)},
        ]
      },
      {
        label: 'Marketing',
        key: 'marketing',
        icon: renderIcon(AreaChartOutlined),
        children: [
          {label: 'Market Writings', key: 'marketing-market', icon: renderIcon(ChartArrowsVertical)},
          {label: 'Attend Conference', key: 'marketing-conference', icon: renderIcon(SignpostTwotone)},
          {label: 'Book Signing', key: 'marketing-book-signing', icon: renderIcon(Signature)},
        ]
      },
      {
        label: 'Contracted Writings',
        key: 'contracted-writings',
        icon: renderIcon(MoneyCalculator24Filled),
        children: [
          {
            label: 'Website Article',
            key: 'contract-web',
            icon: renderIcon(Globe24Regular),
            children: [
              {label: 'Small Article', key: 'small-web', icon: renderIcon(BoxSmall)},
              {label: 'Medium Article', key: 'medium-web', icon: renderIcon(BoxMedium)},
              {label: 'Large Article', key: 'large-web', icon: renderIcon(BoxLarge)},
            ]
          },
        ]
      },
      {
        label: 'Hire Publisher',
        key: 'hire-publisher',
        icon: renderIcon(BookOpenGlobe24Filled),
        children: [
          {label: 'One Man Show', key: 'pub-one-man', icon: renderIcon(BookContacts24Regular)},
          {label: 'Local Firm', key: 'pub-local-firm', icon: renderIcon(BookTheta24Regular)},
          {label: 'National Firm', key: 'pub-national-firm', icon: renderIcon(BookPulse24Regular)},
          {label: 'International Firm', key: 'pub-international-firm', icon: renderIcon(BookStar24Regular)},
        ]
      },
    ]
  },
  {
    label: 'Writings',
    key: 'writings',
    icon: renderIcon(Book),
    children: [
      {
        label: 'Create',
        key: 'writing-create',
        icon: renderIcon(MenuBookOutlined),
        children: [
          {label: renderLabel('/writing/create', 'Chapter'), key: 'create-chapter', icon: renderIcon(NotebookAdd24Regular)},
          {label: renderLabel('/writing/create/comic', 'Comic'), key: 'create-comic', icon: renderIcon(MenuBookTwotone)},
          {label: renderLabel('/writing/create/scrap', 'Scrap'), key: 'create-scrap', icon: renderIcon(LibraryBooksOutlined)},
          {label: renderLabel('/writing/create/book', 'Book'), key: 'create-book', icon: renderIcon(BookAdd24Regular)},
        ]
      },
      {
        label: 'Manage',
        key: 'writing-manage',
        icon: renderIcon(NotebookLightning24Regular),
        children: [
          {label: 'Books', key: 'manage-books', icon: renderIcon(BookmarkMultiple24Regular)},
          {label: 'Permissions', key: 'manage-permissions', icon: renderIcon(BookDatabase24Regular)},
          {label: 'Collection', key: 'manage-collection', icon: renderIcon(CollectionsBookmarkTwotone)},
        ]
      },
    ]
  }
]

export default {
  name: "Actions",
  setup() {
    return {
      menuOptions,
      defaultExpandedKeys: ['game', 'writings'],
    }
  },
}
</script>

<style scoped>

</style>