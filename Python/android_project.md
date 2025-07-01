# 🧠 Project Full Summary

- Root Dir: `C:\Users\Purve\AndroidStudioProjects\doc_tools`

## 📁 Folder Structure

```
doc_tools/
├── .cursor
│   └── rules
├── .gitignore
├── .kotlin
│   ├── errors
│   │   ├── errors-1749485197658.log
│   │   └── errors-1751107010660.log
│   └── sessions
├── CHANGELOG.md
├── README.md
├── app
│   ├── .gitignore
│   ├── build.gradle.kts
│   ├── proguard-rules.pro
│   └── src
│       ├── androidTest
│       │   └── java
│       │       └── com
│       │           └── example
│       │               └── doc_tools
│       │                   └── ExampleInstrumentedTest.kt
│       ├── main
│       │   ├── AndroidManifest.xml
│       │   ├── java
│       │   │   └── com
│       │   │       └── example
│       │   │           └── doc_tools
│       │   │               ├── MainActivity.kt
│       │   │               ├── config
│       │   │               │   └── FeatureFlags.kt
│       │   │               ├── core
│       │   │               │   ├── common
│       │   │               │   │   ├── constants
│       │   │               │   │   │   └── AppDestinations.kt
│       │   │               │   │   ├── model
│       │   │               │   │   │   └── FileDetails.kt
│       │   │               │   │   └── utils
│       │   │               │   ├── domain
│       │   │               │   │   ├── model
│       │   │               │   │   │   ├── SaveMode.kt
│       │   │               │   │   │   └── ToolCategory.kt
│       │   │               │   │   ├── repository
│       │   │               │   │   └── usecase
│       │   │               │   ├── navigation
│       │   │               │   │   └── AppNavigation.kt
│       │   │               │   ├── presentation
│       │   │               │   │   ├── eventbus
│       │   │               │   │   │   └── UiMessageBus.kt
│       │   │               │   │   ├── state
│       │   │               │   │   │   ├── DisplayMethod.kt
│       │   │               │   │   │   ├── MessageType.kt
│       │   │               │   │   │   ├── ProcessingStateManager.kt
│       │   │               │   │   │   ├── ToolItem.kt
│       │   │               │   │   │   └── UiMessageData.kt
│       │   │               │   │   └── viewmodel
│       │   │               │   ├── ui
│       │   │               │   │   ├── components
│       │   │               │   │   │   ├── button
│       │   │               │   │   │   │   ├── ChipButton.kt
│       │   │               │   │   │   │   └── ProgressToolButton.kt
│       │   │               │   │   │   ├── card
│       │   │               │   │   │   │   ├── FileInfoActionCard.kt
│       │   │               │   │   │   │   └── ToolCard.kt
│       │   │               │   │   │   ├── feedback
│       │   │               │   │   │   │   └── WarningBanner.kt
│       │   │               │   │   │   ├── file
│       │   │               │   │   │   │   ├── ChangeSaveLocation.kt
│       │   │               │   │   │   │   ├── FileBottomSheet.kt
│       │   │               │   │   │   │   └── FilePickerHandler.kt
│       │   │               │   │   │   ├── layout
│       │   │               │   │   │   │   ├── AppTopBar.kt
│       │   │               │   │   │   │   └── BaseToolScreen.kt
│       │   │               │   │   │   ├── overlay
│       │   │               │   │   │   │   └── ProcessingAwareComponent.kt
│       │   │               │   │   │   └── tool_layout
│       │   │               │   │   │       └── HeaderSection.kt
│       │   │               │   │   └── theme
│       │   │               │   │       ├── Color.kt
│       │   │               │   │       ├── Shape.kt
│       │   │               │   │       ├── Theme.kt
│       │   │               │   │       └── Type.kt
│       │   │               │   └── utils
│       │   │               │       ├── file
│       │   │               │       │   ├── FileActionsUtils.kt
│       │   │               │       │   ├── FileBottomSheetUtils.kt
│       │   │               │       │   ├── FileIconUtils.kt
│       │   │               │       │   ├── FileInfoUtils.kt
│       │   │               │       │   ├── FileIoUtils.kt
│       │   │               │       │   ├── SaveLocationUtils.kt
│       │   │               │       │   └── UriUtils.kt
│       │   │               │       ├── image
│       │   │               │       │   ├── ImageFormat.kt
│       │   │               │       │   └── ImageUtils.kt
│       │   │               │       ├── pdf
│       │   │               │       │   └── PdfUtils.kt
│       │   │               │       └── state
│       │   │               └── features
│       │   │                   ├── home
│       │   │                   │   ├── domain
│       │   │                   │   │   ├── model
│       │   │                   │   │   └── usecase
│       │   │                   │   └── presentation
│       │   │                   │       ├── state
│       │   │                   │       ├── ui
│       │   │                   │       │   ├── HomeScreen.kt
│       │   │                   │       │   └── components
│       │   │                   │       │       └── FixedToolGrid.kt
│       │   │                   │       └── viewmodel
│       │   │                   ├── image
│       │   │                   │   ├── compressimages
│       │   │                   │   │   ├── domain
│       │   │                   │   │   │   ├── model
│       │   │                   │   │   │   └── usecase
│       │   │                   │   │   └── presentation
│       │   │                   │   │       ├── state
│       │   │                   │   │       │   └── CompressImagesUiState.kt
│       │   │                   │   │       ├── ui
│       │   │                   │   │       │   ├── CompressImagesScreen.kt
│       │   │                   │   │       │   └── components
│       │   │                   │   │       │       ├── CompressionSettingSection.kt
│       │   │                   │   │       │       └── FileSelectionSection.kt
│       │   │                   │   │       └── viewmodel
│       │   │                   │   │           └── CompressImagesViewModel.kt
│       │   │                   │   └── convertimages
│       │   │                   │       ├── domain
│       │   │                   │       │   ├── model
│       │   │                   │       │   └── usecase
│       │   │                   │       └── presentation
│       │   │                   │           ├── state
│       │   │                   │           │   └── ConvertImagesUiState.kt
│       │   │                   │           ├── ui
│       │   │                   │           │   ├── ConvertImagesScreen.kt
│       │   │                   │           │   └── components
│       │   │                   │           │       ├── ConversionSettingSection.kt
│       │   │                   │           │       └── FileSelectionSection.kt
│       │   │                   │           └── viewmodel
│       │   │                   │               └── ConvertImagesViewModel.kt
│       │   │                   ├── pdf
│       │   │                   │   ├── compresspdf
│       │   │                   │   │   ├── domain
│       │   │                   │   │   │   ├── model
│       │   │                   │   │   │   │   └── CompressionMode.kt
│       │   │                   │   │   │   └── usecase
│       │   │                   │   │   └── presentation
│       │   │                   │   │       ├── state
│       │   │                   │   │       │   └── CompressPdfUiState.kt
│       │   │                   │   │       ├── ui
│       │   │                   │   │       │   ├── CompressPdfScreen.kt
│       │   │                   │   │       │   └── components
│       │   │                   │   │       │       ├── CompressionQualitySection.kt
│       │   │                   │   │       │       └── FileSelectionSection.kt
│       │   │                   │   │       └── viewmodel
│       │   │                   │   │           └── CompressPdfViewModel.kt
│       │   │                   │   ├── imagestopdf
│       │   │                   │   │   ├── domain
│       │   │                   │   │   │   ├── model
│       │   │                   │   │   │   └── usecase
│       │   │                   │   │   └── presentation
│       │   │                   │   │       ├── state
│       │   │                   │   │       │   └── ImagesToPdfUiState.kt
│       │   │                   │   │       ├── ui
│       │   │                   │   │       │   ├── ImagesToPdfScreen.kt
│       │   │                   │   │       │   └── components
│       │   │                   │   │       │       ├── FileSelectionSection.kt
│       │   │                   │   │       │       └── PdfSettingSection.kt
│       │   │                   │   │       └── viewmodel
│       │   │                   │   │           └── ImagesToPdfViewModel.kt
│       │   │                   │   ├── mergepdf
│       │   │                   │   │   ├── domain
│       │   │                   │   │   │   ├── model
│       │   │                   │   │   │   │   └── MergeResult.kt
│       │   │                   │   │   │   └── usecase
│       │   │                   │   │   └── presentation
│       │   │                   │   │       ├── state
│       │   │                   │   │       │   └── MergePdfUiState.kt
│       │   │                   │   │       ├── ui
│       │   │                   │   │       │   ├── MergePdfScreen.kt
│       │   │                   │   │       │   └── components
│       │   │                   │   │       │       └── FileSelectionSection.kt
│       │   │                   │   │       └── viewmodel
│       │   │                   │   │           └── MergePdfViewModel.kt
│       │   │                   │   ├── pdftoimages
│       │   │                   │   │   ├── PdfConversionNotificationHelper.kt
│       │   │                   │   │   ├── domain
│       │   │                   │   │   │   ├── model
│       │   │                   │   │   │   └── usecase
│       │   │                   │   │   └── presentation
│       │   │                   │   │       ├── state
│       │   │                   │   │       │   └── PdfToImagesUiState.kt
│       │   │                   │   │       ├── ui
│       │   │                   │   │       │   ├── PdfToImagesScreen.kt
│       │   │                   │   │       │   └── components
│       │   │                   │   │       │       ├── DpiSelectionSection.kt
│       │   │                   │   │       │       ├── FileSelectionSection.kt
│       │   │                   │   │       │       └── ImageFormatSection.kt
│       │   │                   │   │       └── viewmodel
│       │   │                   │   │           └── PdfToImagesViewModel.kt
│       │   │                   │   └── splitpdf
│       │   │                   │       ├── domain
│       │   │                   │       │   ├── model
│       │   │                   │       │   └── usecase
│       │   │                   │       └── presentation
│       │   │                   │           ├── state
│       │   │                   │           │   └── SplitPdfUiState.kt
│       │   │                   │           ├── ui
│       │   │                   │           │   ├── SplitPdfScreen.kt
│       │   │                   │           │   └── components
│       │   │                   │           │       ├── FileSelectionSection.kt
│       │   │                   │           │       └── PageRangeSection.kt
│       │   │                   │           └── viewmodel
│       │   │                   │               └── SplitPdfViewModel.kt
│       │   │                   └── settings
│       │   │                       ├── domain
│       │   │                       │   ├── model
│       │   │                       │   └── usecase
│       │   │                       └── presentation
│       │   │                           ├── state
│       │   │                           ├── ui
│       │   │                           │   ├── SettingsScreen.kt
│       │   │                           │   └── components
│       │   │                           │       ├── SettingItem.kt
│       │   │                           │       ├── SettingsSection.kt
│       │   │                           │       └── ThemeOption.kt
│       │   │                           └── viewmodel
│       │   │                               └── SettingsViewModel.kt
│       │   └── res
│       │       ├── drawable
│       │       │   ├── ic_compress_images.xml
│       │       │   └── ic_default_foreground.xml
│       │       ├── mipmap-anydpi-v26
│       │       │   ├── ic_doc_tools.xml
│       │       │   └── ic_doc_tools_round.xml
│       │       ├── mipmap-hdpi
│       │       │   ├── ic_doc_tools.webp
│       │       │   └── ic_doc_tools_round.webp
│       │       ├── mipmap-mdpi
│       │       │   ├── ic_doc_tools.webp
│       │       │   └── ic_doc_tools_round.webp
│       │       ├── mipmap-xhdpi
│       │       │   ├── ic_doc_tools.webp
│       │       │   └── ic_doc_tools_round.webp
│       │       ├── mipmap-xxhdpi
│       │       │   ├── ic_doc_tools.webp
│       │       │   └── ic_doc_tools_round.webp
│       │       ├── mipmap-xxxhdpi
│       │       │   ├── ic_doc_tools.webp
│       │       │   └── ic_doc_tools_round.webp
│       │       ├── values
│       │       │   ├── colors.xml
│       │       │   ├── ic_default_background.xml
│       │       │   ├── strings.xml
│       │       │   └── themes.xml
│       │       └── xml
│       │           ├── backup_rules.xml
│       │           ├── data_extraction_rules.xml
│       │           └── file_paths.xml
│       └── test
│           └── java
│               └── com
│                   └── example
│                       └── doc_tools
│                           └── ExampleUnitTest.kt
├── build.gradle.kts
├── build.ps1
├── gradle
│   ├── libs.versions.toml
│   └── wrapper
│       ├── gradle-wrapper.jar
│       └── gradle-wrapper.properties
├── gradle.properties
├── gradlew
├── gradlew.bat
├── local.properties
└── settings.gradle.kts
```

## 🧩 Symbol Index

| Symbol           | Type           | Location                       |
|------------------|----------------|--------------------------------|
| AppContent       | function       | app\src\main\java\com\example\doc_tools\MainActivity.kt |
| AppContextProvider | class          | app\src\main\java\com\example\doc_tools\features\pdf\pdftoimages\presentation\viewmodel\PdfToImagesViewModel.kt |
| AppDestinations  | class          | app\src\main\java\com\example\doc_tools\core\common\constants\AppDestinations.kt |
| AppDestinations  | class          | app\src\main\java\com\example\doc_tools\core\navigation\AppNavigation.kt |
| AppNavigation    | function       | app\src\main\java\com\example\doc_tools\core\navigation\AppNavigation.kt |
| AppTopBar        | function       | app\src\main\java\com\example\doc_tools\core\ui\components\layout\AppTopBar.kt |
| BaseToolScreen   | function       | app\src\main\java\com\example\doc_tools\core\ui\components\layout\BaseToolScreen.kt |
| ChangeSaveLocation | function       | app\src\main\java\com\example\doc_tools\core\ui\components\file\ChangeSaveLocation.kt |
| ChipButton       | function       | app\src\main\java\com\example\doc_tools\core\ui\components\button\ChipButton.kt |
| ClearAll         | class          | app\src\main\java\com\example\doc_tools\core\presentation\eventbus\UiMessageBus.kt |
| ClearScope       | class          | app\src\main\java\com\example\doc_tools\core\presentation\eventbus\UiMessageBus.kt |
| CompactDetailRow | function       | app\src\main\java\com\example\doc_tools\core\ui\components\card\FileInfoActionCard.kt |
| CompressImagesScreen | function       | app\src\main\java\com\example\doc_tools\features\image\compressimages\presentation\ui\CompressImagesScreen.kt |
| CompressImagesUiState | class          | app\src\main\java\com\example\doc_tools\features\image\compressimages\presentation\state\CompressImagesUiState.kt |
| CompressImagesViewModel | class          | app\src\main\java\com\example\doc_tools\features\image\compressimages\presentation\viewmodel\CompressImagesViewModel.kt |
| CompressPdfScreen | function       | app\src\main\java\com\example\doc_tools\features\pdf\compresspdf\presentation\ui\CompressPdfScreen.kt |
| CompressPdfUiState | class          | app\src\main\java\com\example\doc_tools\features\pdf\compresspdf\presentation\state\CompressPdfUiState.kt |
| CompressPdfViewModel | class          | app\src\main\java\com\example\doc_tools\features\pdf\compresspdf\presentation\viewmodel\CompressPdfViewModel.kt |
| CompressionQualitySection | function       | app\src\main\java\com\example\doc_tools\features\pdf\compresspdf\presentation\ui\components\CompressionQualitySection.kt |
| CompressionSettingsSection | function       | app\src\main\java\com\example\doc_tools\features\image\compressimages\presentation\ui\components\CompressionSettingSection.kt |
| ConversionSettingsSection | function       | app\src\main\java\com\example\doc_tools\features\image\convertimages\presentation\ui\components\ConversionSettingSection.kt |
| ConvertImagesScreen | function       | app\src\main\java\com\example\doc_tools\features\image\convertimages\presentation\ui\ConvertImagesScreen.kt |
| ConvertImagesUiState | class          | app\src\main\java\com\example\doc_tools\features\image\convertimages\presentation\state\ConvertImagesUiState.kt |
| ConvertImagesViewModel | class          | app\src\main\java\com\example\doc_tools\features\image\convertimages\presentation\viewmodel\ConvertImagesViewModel.kt |
| Dismiss          | class          | app\src\main\java\com\example\doc_tools\core\presentation\eventbus\UiMessageBus.kt |
| DpiSelectionSection | function       | app\src\main\java\com\example\doc_tools\features\pdf\pdftoimages\presentation\ui\components\DpiSelectionSection.kt |
| ExampleInstrumentedTest | class          | app\src\androidTest\java\com\example\doc_tools\ExampleInstrumentedTest.kt |
| ExampleUnitTest  | class          | app\src\test\java\com\example\doc_tools\ExampleUnitTest.kt |
| FeatureFlags     | class          | app\src\main\java\com\example\doc_tools\config\FeatureFlags.kt |
| FileActionsUtils | class          | app\src\main\java\com\example\doc_tools\core\utils\file\FileActionsUtils.kt |
| FileBottomSheet  | function       | app\src\main\java\com\example\doc_tools\core\ui\components\file\FileBottomSheet.kt |
| FileBottomSheetUtils | class          | app\src\main\java\com\example\doc_tools\core\utils\file\FileBottomSheetUtils.kt |
| FileDetails      | class          | app\src\main\java\com\example\doc_tools\core\common\model\FileDetails.kt |
| FileIconUtils    | class          | app\src\main\java\com\example\doc_tools\core\utils\file\FileIconUtils.kt |
| FileInfoActionCard | function       | app\src\main\java\com\example\doc_tools\core\ui\components\card\FileInfoActionCard.kt |
| FileInfoUtils    | class          | app\src\main\java\com\example\doc_tools\core\utils\file\FileInfoUtils.kt |
| FileIoUtils      | class          | app\src\main\java\com\example\doc_tools\core\utils\file\FileIoUtils.kt |
| FileListContent  | function       | app\src\main\java\com\example\doc_tools\core\ui\components\file\FileBottomSheet.kt |
| FileListItem     | function       | app\src\main\java\com\example\doc_tools\core\ui\components\file\FileBottomSheet.kt |
| FilePickerHandler | function       | app\src\main\java\com\example\doc_tools\core\ui\components\file\FilePickerHandler.kt |
| FileSelectionSection | function       | app\src\main\java\com\example\doc_tools\features\image\compressimages\presentation\ui\components\FileSelectionSection.kt |
| FileSelectionSection | function       | app\src\main\java\com\example\doc_tools\features\image\convertimages\presentation\ui\components\FileSelectionSection.kt |
| FileSelectionSection | function       | app\src\main\java\com\example\doc_tools\features\pdf\compresspdf\presentation\ui\components\FileSelectionSection.kt |
| FileSelectionSection | function       | app\src\main\java\com\example\doc_tools\features\pdf\imagestopdf\presentation\ui\components\FileSelectionSection.kt |
| FileSelectionSection | function       | app\src\main\java\com\example\doc_tools\features\pdf\mergepdf\presentation\ui\components\FileSelectionSection.kt |
| FileSelectionSection | function       | app\src\main\java\com\example\doc_tools\features\pdf\pdftoimages\presentation\ui\components\FileSelectionSection.kt |
| FileSelectionSection | function       | app\src\main\java\com\example\doc_tools\features\pdf\splitpdf\presentation\ui\components\FileSelectionSection.kt |
| FixedToolsGrid   | function       | app\src\main\java\com\example\doc_tools\features\home\presentation\ui\components\FixedToolGrid.kt |
| HeaderSection    | function       | app\src\main\java\com\example\doc_tools\core\ui\components\tool_layout\HeaderSection.kt |
| HomeScreen       | function       | app\src\main\java\com\example\doc_tools\features\home\presentation\ui\HomeScreen.kt |
| ImageFormatSection | function       | app\src\main\java\com\example\doc_tools\features\pdf\pdftoimages\presentation\ui\components\ImageFormatSection.kt |
| ImageUtils       | class          | app\src\main\java\com\example\doc_tools\core\utils\image\ImageUtils.kt |
| ImagesToPdfScreen | function       | app\src\main\java\com\example\doc_tools\features\pdf\imagestopdf\presentation\ui\ImagesToPdfScreen.kt |
| ImagesToPdfUiState | class          | app\src\main\java\com\example\doc_tools\features\pdf\imagestopdf\presentation\state\ImagesToPdfUiState.kt |
| ImagesToPdfViewModel | class          | app\src\main\java\com\example\doc_tools\features\pdf\imagestopdf\presentation\viewmodel\ImagesToPdfViewModel.kt |
| MainActivity     | class          | app\src\main\java\com\example\doc_tools\MainActivity.kt |
| MergePdfScreen   | function       | app\src\main\java\com\example\doc_tools\features\pdf\mergepdf\presentation\ui\MergePdfScreen.kt |
| MergePdfUiState  | class          | app\src\main\java\com\example\doc_tools\features\pdf\mergepdf\presentation\state\MergePdfUiState.kt |
| MergePdfViewModel | class          | app\src\main\java\com\example\doc_tools\features\pdf\mergepdf\presentation\viewmodel\MergePdfViewModel.kt |
| MergeResult      | class          | app\src\main\java\com\example\doc_tools\features\pdf\mergepdf\domain\model\MergeResult.kt |
| MessageEvent     | class          | app\src\main\java\com\example\doc_tools\core\presentation\eventbus\UiMessageBus.kt |
| PageRangeSection | function       | app\src\main\java\com\example\doc_tools\features\pdf\splitpdf\presentation\ui\components\PageRangeSection.kt |
| PdfConversionNotificationHelper | class          | app\src\main\java\com\example\doc_tools\features\pdf\pdftoimages\PdfConversionNotificationHelper.kt |
| PdfSettingsSection | function       | app\src\main\java\com\example\doc_tools\features\pdf\imagestopdf\presentation\ui\components\PdfSettingSection.kt |
| PdfToImagesScreen | function       | app\src\main\java\com\example\doc_tools\features\pdf\pdftoimages\presentation\ui\PdfToImagesScreen.kt |
| PdfToImagesUiState | class          | app\src\main\java\com\example\doc_tools\features\pdf\pdftoimages\presentation\state\PdfToImagesUiState.kt |
| PdfToImagesViewModel | class          | app\src\main\java\com\example\doc_tools\features\pdf\pdftoimages\presentation\viewmodel\PdfToImagesViewModel.kt |
| PdfUtils         | class          | app\src\main\java\com\example\doc_tools\core\utils\pdf\PdfUtils.kt |
| Pdf_img_tools_appTheme | function       | app\src\main\java\com\example\doc_tools\core\ui\theme\Theme.kt |
| ProcessingAware  | function       | app\src\main\java\com\example\doc_tools\core\ui\components\overlay\ProcessingAwareComponent.kt |
| ProcessingStateManager | class          | app\src\main\java\com\example\doc_tools\core\presentation\state\ProcessingStateManager.kt |
| ProgressToolButton | function       | app\src\main\java\com\example\doc_tools\core\ui\components\button\ProgressToolButton.kt |
| SaveLocationDialog | function       | app\src\main\java\com\example\doc_tools\core\ui\components\file\ChangeSaveLocation.kt |
| SaveLocationUtils | class          | app\src\main\java\com\example\doc_tools\core\utils\file\SaveLocationUtils.kt |
| SelectedFilesSection | function       | app\src\main\java\com\example\doc_tools\features\pdf\mergepdf\presentation\ui\MergePdfScreen.kt |
| SettingItem      | function       | app\src\main\java\com\example\doc_tools\features\settings\presentation\ui\components\SettingItem.kt |
| SettingsScreen   | function       | app\src\main\java\com\example\doc_tools\features\settings\presentation\ui\SettingsScreen.kt |
| SettingsSection  | function       | app\src\main\java\com\example\doc_tools\features\settings\presentation\ui\components\SettingsSection.kt |
| SettingsUiState  | class          | app\src\main\java\com\example\doc_tools\features\settings\presentation\viewmodel\SettingsViewModel.kt |
| SettingsViewModel | class          | app\src\main\java\com\example\doc_tools\features\settings\presentation\viewmodel\SettingsViewModel.kt |
| Show             | class          | app\src\main\java\com\example\doc_tools\core\presentation\eventbus\UiMessageBus.kt |
| SingleImagePreviewContent | function       | app\src\main\java\com\example\doc_tools\core\ui\components\file\FileBottomSheet.kt |
| SplitPdfScreen   | function       | app\src\main\java\com\example\doc_tools\features\pdf\splitpdf\presentation\ui\SplitPdfScreen.kt |
| SplitPdfUiState  | class          | app\src\main\java\com\example\doc_tools\features\pdf\splitpdf\presentation\state\SplitPdfUiState.kt |
| SplitPdfViewModel | class          | app\src\main\java\com\example\doc_tools\features\pdf\splitpdf\presentation\viewmodel\SplitPdfViewModel.kt |
| Theme.Pdf_img_tools_app | resource:style | app\src\main\res\values\themes.xml |
| ThemeOption      | function       | app\src\main\java\com\example\doc_tools\features\settings\presentation\ui\components\ThemeOption.kt |
| ToolCard         | function       | app\src\main\java\com\example\doc_tools\core\ui\components\card\ToolCard.kt |
| ToolItem         | class          | app\src\main\java\com\example\doc_tools\core\presentation\state\ToolItem.kt |
| UiMessageBus     | class          | app\src\main\java\com\example\doc_tools\core\presentation\eventbus\UiMessageBus.kt |
| UiMessageData    | class          | app\src\main\java\com\example\doc_tools\core\presentation\state\UiMessageData.kt |
| UriUtils         | class          | app\src\main\java\com\example\doc_tools\core\utils\file\UriUtils.kt |
| WarningBanner    | function       | app\src\main\java\com\example\doc_tools\core\ui\components\feedback\WarningBanner.kt |
| addImages        | function       | app\src\main\java\com\example\doc_tools\features\image\compressimages\presentation\viewmodel\CompressImagesViewModel.kt |
| addImages        | function       | app\src\main\java\com\example\doc_tools\features\pdf\imagestopdf\presentation\viewmodel\ImagesToPdfViewModel.kt |
| addPdfFiles      | function       | app\src\main\java\com\example\doc_tools\features\pdf\mergepdf\presentation\viewmodel\MergePdfViewModel.kt |
| addition_isCorrect | function       | app\src\test\java\com\example\doc_tools\ExampleUnitTest.kt |
| app_name         | resource:string | app\src\main\res\values\strings.xml |
| black            | resource:color | app\src\main\res\values\colors.xml |
| calculateTotalPageCount | function       | app\src\main\java\com\example\doc_tools\features\pdf\mergepdf\presentation\viewmodel\MergePdfViewModel.kt |
| cancelAllOperations | function       | app\src\main\java\com\example\doc_tools\core\utils\file\FileBottomSheetUtils.kt |
| cancelCompression | function       | app\src\main\java\com\example\doc_tools\features\image\compressimages\presentation\viewmodel\CompressImagesViewModel.kt |
| cancelCompression | function       | app\src\main\java\com\example\doc_tools\features\pdf\compresspdf\presentation\viewmodel\CompressPdfViewModel.kt |
| cancelMerge      | function       | app\src\main\java\com\example\doc_tools\features\pdf\mergepdf\presentation\viewmodel\MergePdfViewModel.kt |
| cancelNotification | function       | app\src\main\java\com\example\doc_tools\features\pdf\pdftoimages\PdfConversionNotificationHelper.kt |
| cancelOperation  | function       | app\src\main\java\com\example\doc_tools\features\pdf\splitpdf\presentation\viewmodel\SplitPdfViewModel.kt |
| cancelProcessing | function       | app\src\main\java\com\example\doc_tools\features\image\convertimages\presentation\viewmodel\ConvertImagesViewModel.kt |
| cancelProcessing | function       | app\src\main\java\com\example\doc_tools\features\pdf\imagestopdf\presentation\viewmodel\ImagesToPdfViewModel.kt |
| cancelProcessing | function       | app\src\main\java\com\example\doc_tools\features\pdf\pdftoimages\presentation\viewmodel\PdfToImagesViewModel.kt |
| centralizes      | class          | app\src\main\java\com\example\doc_tools\core\common\constants\AppDestinations.kt |
| changeSaveMode   | function       | app\src\main\java\com\example\doc_tools\features\pdf\compresspdf\presentation\viewmodel\CompressPdfViewModel.kt |
| changeSaveMode   | function       | app\src\main\java\com\example\doc_tools\features\pdf\mergepdf\presentation\viewmodel\MergePdfViewModel.kt |
| class            | class          | app\src\main\java\com\example\doc_tools\core\domain\model\SaveMode.kt |
| class            | class          | app\src\main\java\com\example\doc_tools\core\domain\model\ToolCategory.kt |
| class            | class          | app\src\main\java\com\example\doc_tools\core\presentation\state\DisplayMethod.kt |
| class            | class          | app\src\main\java\com\example\doc_tools\core\presentation\state\MessageType.kt |
| class            | class          | app\src\main\java\com\example\doc_tools\core\ui\theme\Theme.kt |
| class            | class          | app\src\main\java\com\example\doc_tools\core\utils\image\ImageFormat.kt |
| class            | class          | app\src\main\java\com\example\doc_tools\core\utils\image\ImageFormat.kt |
| class            | class          | app\src\main\java\com\example\doc_tools\features\pdf\compresspdf\domain\model\CompressionMode.kt |
| class            | class          | app\src\main\java\com\example\doc_tools\features\settings\presentation\viewmodel\SettingsViewModel.kt |
| clearAll         | function       | app\src\main\java\com\example\doc_tools\core\ui\components\file\FileBottomSheet.kt |
| clearAllFiles    | function       | app\src\main\java\com\example\doc_tools\core\utils\file\FileBottomSheetUtils.kt |
| clearAllImages   | function       | app\src\main\java\com\example\doc_tools\features\image\compressimages\presentation\viewmodel\CompressImagesViewModel.kt |
| clearAllImages   | function       | app\src\main\java\com\example\doc_tools\features\pdf\imagestopdf\presentation\viewmodel\ImagesToPdfViewModel.kt |
| clearAllImages   | function       | app\src\main\java\com\example\doc_tools\features\pdf\pdftoimages\presentation\viewmodel\PdfToImagesViewModel.kt |
| clearAllMessages | function       | app\src\main\java\com\example\doc_tools\core\presentation\eventbus\UiMessageBus.kt |
| clearAllPdfs     | function       | app\src\main\java\com\example\doc_tools\features\pdf\mergepdf\presentation\viewmodel\MergePdfViewModel.kt |
| clearMessages    | function       | app\src\main\java\com\example\doc_tools\core\presentation\eventbus\UiMessageBus.kt |
| clearOutputDetails | function       | app\src\main\java\com\example\doc_tools\features\image\compressimages\presentation\viewmodel\CompressImagesViewModel.kt |
| clearOutputDetails | function       | app\src\main\java\com\example\doc_tools\features\image\convertimages\presentation\viewmodel\ConvertImagesViewModel.kt |
| clearOutputDetails | function       | app\src\main\java\com\example\doc_tools\features\pdf\compresspdf\presentation\viewmodel\CompressPdfViewModel.kt |
| clearOutputDetails | function       | app\src\main\java\com\example\doc_tools\features\pdf\imagestopdf\presentation\viewmodel\ImagesToPdfViewModel.kt |
| clearOutputDetails | function       | app\src\main\java\com\example\doc_tools\features\pdf\mergepdf\presentation\viewmodel\MergePdfViewModel.kt |
| clearPdfFile     | function       | app\src\main\java\com\example\doc_tools\features\pdf\pdftoimages\presentation\viewmodel\PdfToImagesViewModel.kt |
| clearPdfFile     | function       | app\src\main\java\com\example\doc_tools\features\pdf\splitpdf\presentation\viewmodel\SplitPdfViewModel.kt |
| clearScope       | function       | app\src\main\java\com\example\doc_tools\core\presentation\eventbus\UiMessageBus.kt |
| clearSelectedFile | function       | app\src\main\java\com\example\doc_tools\features\pdf\compresspdf\presentation\viewmodel\CompressPdfViewModel.kt |
| clearSelectedImage | function       | app\src\main\java\com\example\doc_tools\features\image\convertimages\presentation\viewmodel\ConvertImagesViewModel.kt |
| compressImages   | function       | app\src\main\java\com\example\doc_tools\features\image\compressimages\presentation\viewmodel\CompressImagesViewModel.kt |
| constant         | class          | app\src\main\java\com\example\doc_tools\core\ui\theme\Theme.kt |
| contactDeveloper | function       | app\src\main\java\com\example\doc_tools\features\settings\presentation\viewmodel\SettingsViewModel.kt |
| containing       | class          | app\src\main\java\com\example\doc_tools\core\ui\components\card\FileInfoActionCard.kt |
| contains         | class          | app\src\main\java\com\example\doc_tools\core\navigation\AppNavigation.kt |
| convertImage     | function       | app\src\main\java\com\example\doc_tools\features\image\convertimages\presentation\viewmodel\ConvertImagesViewModel.kt |
| convertImagesToPdf | function       | app\src\main\java\com\example\doc_tools\features\pdf\imagestopdf\presentation\viewmodel\ImagesToPdfViewModel.kt |
| convertPdfToImages | function       | app\src\main\java\com\example\doc_tools\features\pdf\pdftoimages\presentation\viewmodel\PdfToImagesViewModel.kt |
| createNotificationChannel | function       | app\src\main\java\com\example\doc_tools\features\pdf\pdftoimages\PdfConversionNotificationHelper.kt |
| createOutputFile | function       | app\src\main\java\com\example\doc_tools\core\utils\file\FileIoUtils.kt |
| createOutputFileInAppDir | function       | app\src\main\java\com\example\doc_tools\core\utils\file\FileIoUtils.kt |
| createTempFile   | function       | app\src\main\java\com\example\doc_tools\core\utils\file\FileIoUtils.kt |
| createZipArchive | function       | app\src\main\java\com\example\doc_tools\core\utils\file\FileIoUtils.kt |
| defines          | class          | app\src\main\java\com\example\doc_tools\core\domain\model\SaveMode.kt |
| defines          | class          | app\src\main\java\com\example\doc_tools\core\presentation\state\DisplayMethod.kt |
| deleteFiles      | function       | app\src\main\java\com\example\doc_tools\core\ui\components\file\FileBottomSheet.kt |
| dismissLargeFileWarning | function       | app\src\main\java\com\example\doc_tools\features\pdf\compresspdf\presentation\viewmodel\CompressPdfViewModel.kt |
| dismissMessage   | function       | app\src\main\java\com\example\doc_tools\core\presentation\eventbus\UiMessageBus.kt |
| endProcess       | function       | app\src\main\java\com\example\doc_tools\core\presentation\state\ProcessingStateManager.kt |
| error            | function       | app\src\main\java\com\example\doc_tools\core\presentation\state\UiMessageData.kt |
| finishProcessing | function       | app\src\main\java\com\example\doc_tools\features\pdf\pdftoimages\presentation\viewmodel\PdfToImagesViewModel.kt |
| for              | class          | app\src\main\java\com\example\doc_tools\core\utils\file\FileActionsUtils.kt |
| for              | class          | app\src\main\java\com\example\doc_tools\core\utils\file\FileBottomSheetUtils.kt |
| for              | class          | app\src\main\java\com\example\doc_tools\features\pdf\mergepdf\domain\model\MergeResult.kt |
| for              | class          | app\src\main\java\com\example\doc_tools\features\pdf\pdftoimages\PdfConversionNotificationHelper.kt |
| for              | class          | app\src\main\java\com\example\doc_tools\features\pdf\splitpdf\presentation\viewmodel\SplitPdfViewModel.kt |
| forceEndProcess  | function       | app\src\main\java\com\example\doc_tools\core\presentation\state\ProcessingStateManager.kt |
| formatTimeRemaining | function       | app\src\main\java\com\example\doc_tools\features\pdf\compresspdf\presentation\viewmodel\CompressPdfViewModel.kt |
| fromDisplayName  | function       | app\src\main\java\com\example\doc_tools\core\utils\image\ImageFormat.kt |
| fromMimeType     | function       | app\src\main\java\com\example\doc_tools\core\utils\image\ImageFormat.kt |
| getColorScheme   | function       | app\src\main\java\com\example\doc_tools\core\ui\theme\Theme.kt |
| getContentUri    | function       | app\src\main\java\com\example\doc_tools\core\utils\file\FileActionsUtils.kt |
| getDirectoryName | function       | app\src\main\java\com\example\doc_tools\core\utils\file\UriUtils.kt |
| getElapsedTime   | function       | app\src\main\java\com\example\doc_tools\core\presentation\state\ProcessingStateManager.kt |
| getFileDetails   | function       | app\src\main\java\com\example\doc_tools\core\utils\file\FileInfoUtils.kt |
| getFileName      | function       | app\src\main\java\com\example\doc_tools\core\utils\file\FileInfoUtils.kt |
| getFilePath      | function       | app\src\main\java\com\example\doc_tools\core\utils\file\UriUtils.kt |
| getFileSize      | function       | app\src\main\java\com\example\doc_tools\core\utils\file\FileInfoUtils.kt |
| getFormatByName  | function       | app\src\main\java\com\example\doc_tools\features\image\convertimages\presentation\state\ConvertImagesUiState.kt |
| getFormatNames   | function       | app\src\main\java\com\example\doc_tools\core\utils\image\ImageFormat.kt |
| getFormattedFileSize | function       | app\src\main\java\com\example\doc_tools\core\utils\file\FileInfoUtils.kt |
| getIconForMimeType | function       | app\src\main\java\com\example\doc_tools\core\utils\file\FileIconUtils.kt |
| getImageDimensions | function       | app\src\main\java\com\example\doc_tools\core\utils\image\ImageUtils.kt |
| getMimeType      | function       | app\src\main\java\com\example\doc_tools\core\utils\file\FileInfoUtils.kt |
| getPageCount     | function       | app\src\main\java\com\example\doc_tools\core\utils\pdf\PdfUtils.kt |
| getSaveLocationUri | function       | app\src\main\java\com\example\doc_tools\core\utils\file\SaveLocationUtils.kt |
| handleConversionSuccess | function       | app\src\main\java\com\example\doc_tools\features\pdf\pdftoimages\presentation\viewmodel\PdfToImagesViewModel.kt |
| handles          | class          | app\src\main\java\com\example\doc_tools\core\utils\file\SaveLocationUtils.kt |
| ic_default_background | resource:color | app\src\main\res\values\ic_default_background.xml |
| info             | function       | app\src\main\java\com\example\doc_tools\core\presentation\state\UiMessageData.kt |
| isWebpTypeSupported | function       | app\src\main\java\com\example\doc_tools\core\utils\image\ImageFormat.kt |
| loadAppVersion   | function       | app\src\main\java\com\example\doc_tools\features\settings\presentation\viewmodel\SettingsViewModel.kt |
| mergePdfFiles    | function       | app\src\main\java\com\example\doc_tools\features\pdf\mergepdf\presentation\viewmodel\MergePdfViewModel.kt |
| onCreate         | function       | app\src\main\java\com\example\doc_tools\MainActivity.kt |
| onEndPageChanged | function       | app\src\main\java\com\example\doc_tools\features\pdf\splitpdf\presentation\viewmodel\SplitPdfViewModel.kt |
| onFilePicked     | function       | app\src\main\java\com\example\doc_tools\features\pdf\compresspdf\presentation\viewmodel\CompressPdfViewModel.kt |
| onFilePicked     | function       | app\src\main\java\com\example\doc_tools\features\pdf\splitpdf\presentation\viewmodel\SplitPdfViewModel.kt |
| onStartPageChanged | function       | app\src\main\java\com\example\doc_tools\features\pdf\splitpdf\presentation\viewmodel\SplitPdfViewModel.kt |
| provides         | class          | app\src\main\java\com\example\doc_tools\core\ui\theme\Shape.kt |
| provides         | class          | app\src\main\java\com\example\doc_tools\core\utils\file\FileActionsUtils.kt |
| provides         | class          | app\src\main\java\com\example\doc_tools\core\utils\file\SaveLocationUtils.kt |
| purple_200       | resource:color | app\src\main\res\values\colors.xml |
| purple_500       | resource:color | app\src\main\res\values\colors.xml |
| purple_700       | resource:color | app\src\main\res\values\colors.xml |
| removeFile       | function       | app\src\main\java\com\example\doc_tools\core\utils\file\FileBottomSheetUtils.kt |
| removeFiles      | function       | app\src\main\java\com\example\doc_tools\core\utils\file\FileBottomSheetUtils.kt |
| removeImage      | function       | app\src\main\java\com\example\doc_tools\features\image\compressimages\presentation\viewmodel\CompressImagesViewModel.kt |
| removeImage      | function       | app\src\main\java\com\example\doc_tools\features\pdf\imagestopdf\presentation\viewmodel\ImagesToPdfViewModel.kt |
| removeImage      | function       | app\src\main\java\com\example\doc_tools\features\pdf\pdftoimages\presentation\viewmodel\PdfToImagesViewModel.kt |
| removePdf        | function       | app\src\main\java\com\example\doc_tools\features\pdf\mergepdf\presentation\viewmodel\MergePdfViewModel.kt |
| removeSelectedPdfs | function       | app\src\main\java\com\example\doc_tools\features\pdf\mergepdf\presentation\viewmodel\MergePdfViewModel.kt |
| representing     | class          | app\src\main\java\com\example\doc_tools\core\presentation\eventbus\UiMessageBus.kt |
| representing     | class          | app\src\main\java\com\example\doc_tools\core\presentation\state\UiMessageData.kt |
| representing     | class          | app\src\main\java\com\example\doc_tools\features\image\compressimages\presentation\state\CompressImagesUiState.kt |
| representing     | class          | app\src\main\java\com\example\doc_tools\features\pdf\compresspdf\presentation\state\CompressPdfUiState.kt |
| representing     | class          | app\src\main\java\com\example\doc_tools\features\pdf\imagestopdf\presentation\state\ImagesToPdfUiState.kt |
| representing     | class          | app\src\main\java\com\example\doc_tools\features\pdf\mergepdf\presentation\state\MergePdfUiState.kt |
| representing     | class          | app\src\main\java\com\example\doc_tools\features\pdf\pdftoimages\presentation\state\PdfToImagesUiState.kt |
| representing     | class          | app\src\main\java\com\example\doc_tools\features\settings\presentation\viewmodel\SettingsViewModel.kt |
| resetOutput      | function       | app\src\main\java\com\example\doc_tools\features\pdf\splitpdf\presentation\viewmodel\SplitPdfViewModel.kt |
| resetSelection   | function       | app\src\main\java\com\example\doc_tools\core\ui\components\file\FileBottomSheet.kt |
| saveFileToDirectory | function       | app\src\main\java\com\example\doc_tools\core\utils\file\FileIoUtils.kt |
| saveFileToDownloads | function       | app\src\main\java\com\example\doc_tools\core\utils\file\FileIoUtils.kt |
| saveToLocation   | function       | app\src\main\java\com\example\doc_tools\core\utils\file\SaveLocationUtils.kt |
| selectImage      | function       | app\src\main\java\com\example\doc_tools\features\image\convertimages\presentation\viewmodel\ConvertImagesViewModel.kt |
| setPdfFile       | function       | app\src\main\java\com\example\doc_tools\features\pdf\pdftoimages\presentation\viewmodel\PdfToImagesViewModel.kt |
| setPrivacyDialogVisible | function       | app\src\main\java\com\example\doc_tools\features\settings\presentation\viewmodel\SettingsViewModel.kt |
| shareFile        | function       | app\src\main\java\com\example\doc_tools\core\utils\file\FileActionsUtils.kt |
| showCompletedNotification | function       | app\src\main\java\com\example\doc_tools\features\pdf\pdftoimages\PdfConversionNotificationHelper.kt |
| showDialog       | function       | app\src\main\java\com\example\doc_tools\core\presentation\eventbus\UiMessageBus.kt |
| showError        | function       | app\src\main\java\com\example\doc_tools\core\presentation\eventbus\UiMessageBus.kt |
| showInfo         | function       | app\src\main\java\com\example\doc_tools\core\presentation\eventbus\UiMessageBus.kt |
| showMessage      | function       | app\src\main\java\com\example\doc_tools\core\presentation\eventbus\UiMessageBus.kt |
| showMessage      | function       | app\src\main\java\com\example\doc_tools\core\presentation\eventbus\UiMessageBus.kt |
| showProgressNotification | function       | app\src\main\java\com\example\doc_tools\features\pdf\pdftoimages\PdfConversionNotificationHelper.kt |
| showSnackbar     | function       | app\src\main\java\com\example\doc_tools\core\presentation\eventbus\UiMessageBus.kt |
| showSuccess      | function       | app\src\main\java\com\example\doc_tools\core\presentation\eventbus\UiMessageBus.kt |
| showToast        | function       | app\src\main\java\com\example\doc_tools\core\presentation\eventbus\UiMessageBus.kt |
| showWarning      | function       | app\src\main\java\com\example\doc_tools\core\presentation\eventbus\UiMessageBus.kt |
| smartFileView    | function       | app\src\main\java\com\example\doc_tools\core\utils\file\FileActionsUtils.kt |
| splitPdf         | function       | app\src\main\java\com\example\doc_tools\features\pdf\splitpdf\presentation\viewmodel\SplitPdfViewModel.kt |
| startCompression | function       | app\src\main\java\com\example\doc_tools\features\pdf\compresspdf\presentation\viewmodel\CompressPdfViewModel.kt |
| startProcess     | function       | app\src\main\java\com\example\doc_tools\core\presentation\state\ProcessingStateManager.kt |
| success          | function       | app\src\main\java\com\example\doc_tools\core\presentation\state\UiMessageData.kt |
| teal_200         | resource:color | app\src\main\res\values\colors.xml |
| teal_700         | resource:color | app\src\main\res\values\colors.xml |
| that             | class          | app\src\main\java\com\example\doc_tools\config\FeatureFlags.kt |
| to               | class          | app\src\main\java\com\example\doc_tools\core\ui\theme\Theme.kt |
| toggleAllImagesBottomSheet | function       | app\src\main\java\com\example\doc_tools\features\image\compressimages\presentation\viewmodel\CompressImagesViewModel.kt |
| toggleBottomSheet | function       | app\src\main\java\com\example\doc_tools\features\pdf\pdftoimages\presentation\viewmodel\PdfToImagesViewModel.kt |
| toggleConfirmMergeDialog | function       | app\src\main\java\com\example\doc_tools\features\pdf\mergepdf\presentation\viewmodel\MergePdfViewModel.kt |
| toggleFormatMenu | function       | app\src\main\java\com\example\doc_tools\features\image\convertimages\presentation\viewmodel\ConvertImagesViewModel.kt |
| toggleImageSelection | function       | app\src\main\java\com\example\doc_tools\features\pdf\pdftoimages\presentation\viewmodel\PdfToImagesViewModel.kt |
| toggleImagesBottomSheet | function       | app\src\main\java\com\example\doc_tools\features\pdf\imagestopdf\presentation\viewmodel\ImagesToPdfViewModel.kt |
| toggleItemSelection | function       | app\src\main\java\com\example\doc_tools\features\pdf\mergepdf\presentation\viewmodel\MergePdfViewModel.kt |
| toggleOutputFileSheet | function       | app\src\main\java\com\example\doc_tools\features\pdf\mergepdf\presentation\viewmodel\MergePdfViewModel.kt |
| toggleSaveLocationSelector | function       | app\src\main\java\com\example\doc_tools\features\pdf\splitpdf\presentation\viewmodel\SplitPdfViewModel.kt |
| toggleSelectedFilesSheet | function       | app\src\main\java\com\example\doc_tools\features\pdf\mergepdf\presentation\viewmodel\MergePdfViewModel.kt |
| toggleSelectedImagesBottomSheet | function       | app\src\main\java\com\example\doc_tools\features\image\compressimages\presentation\viewmodel\CompressImagesViewModel.kt |
| updateCompressionFormat | function       | app\src\main\java\com\example\doc_tools\features\image\compressimages\presentation\viewmodel\CompressImagesViewModel.kt |
| updateCompressionQuality | function       | app\src\main\java\com\example\doc_tools\features\image\compressimages\presentation\viewmodel\CompressImagesViewModel.kt |
| updateDpi        | function       | app\src\main\java\com\example\doc_tools\features\pdf\pdftoimages\presentation\viewmodel\PdfToImagesViewModel.kt |
| updateImageAlignment | function       | app\src\main\java\com\example\doc_tools\features\pdf\imagestopdf\presentation\viewmodel\ImagesToPdfViewModel.kt |
| updateImageDetails | function       | app\src\main\java\com\example\doc_tools\features\image\compressimages\presentation\viewmodel\CompressImagesViewModel.kt |
| updateImageDetails | function       | app\src\main\java\com\example\doc_tools\features\pdf\imagestopdf\presentation\viewmodel\ImagesToPdfViewModel.kt |
| updateImages     | function       | app\src\main\java\com\example\doc_tools\features\pdf\imagestopdf\presentation\viewmodel\ImagesToPdfViewModel.kt |
| updateImagesList | function       | app\src\main\java\com\example\doc_tools\core\utils\file\FileBottomSheetUtils.kt |
| updateImagesList | function       | app\src\main\java\com\example\doc_tools\features\image\compressimages\presentation\viewmodel\CompressImagesViewModel.kt |
| updateImagesList | function       | app\src\main\java\com\example\doc_tools\features\pdf\imagestopdf\presentation\viewmodel\ImagesToPdfViewModel.kt |
| updateMessage    | function       | app\src\main\java\com\example\doc_tools\core\presentation\eventbus\UiMessageBus.kt |
| updateOutputFormat | function       | app\src\main\java\com\example\doc_tools\features\pdf\pdftoimages\presentation\viewmodel\PdfToImagesViewModel.kt |
| updateOutputImages | function       | app\src\main\java\com\example\doc_tools\features\pdf\pdftoimages\presentation\viewmodel\PdfToImagesViewModel.kt |
| updatePaperSize  | function       | app\src\main\java\com\example\doc_tools\features\pdf\imagestopdf\presentation\viewmodel\ImagesToPdfViewModel.kt |
| updatePdfFiles   | function       | app\src\main\java\com\example\doc_tools\features\pdf\mergepdf\presentation\viewmodel\MergePdfViewModel.kt |
| updateProgress   | function       | app\src\main\java\com\example\doc_tools\core\presentation\state\ProcessingStateManager.kt |
| updateProgressNotification | function       | app\src\main\java\com\example\doc_tools\features\pdf\pdftoimages\PdfConversionNotificationHelper.kt |
| updateQuality    | function       | app\src\main\java\com\example\doc_tools\features\image\convertimages\presentation\viewmodel\ConvertImagesViewModel.kt |
| updateQuality    | function       | app\src\main\java\com\example\doc_tools\features\pdf\compresspdf\presentation\viewmodel\CompressPdfViewModel.kt |
| updateSaveLocation | function       | app\src\main\java\com\example\doc_tools\features\pdf\splitpdf\presentation\viewmodel\SplitPdfViewModel.kt |
| updateSaveMode   | function       | app\src\main\java\com\example\doc_tools\features\image\compressimages\presentation\viewmodel\CompressImagesViewModel.kt |
| updateSaveMode   | function       | app\src\main\java\com\example\doc_tools\features\image\convertimages\presentation\viewmodel\ConvertImagesViewModel.kt |
| updateSaveMode   | function       | app\src\main\java\com\example\doc_tools\features\pdf\imagestopdf\presentation\viewmodel\ImagesToPdfViewModel.kt |
| updateSaveMode   | function       | app\src\main\java\com\example\doc_tools\features\pdf\pdftoimages\presentation\viewmodel\PdfToImagesViewModel.kt |
| updateSaveMode   | function       | app\src\main\java\com\example\doc_tools\features\pdf\splitpdf\presentation\viewmodel\SplitPdfViewModel.kt |
| updateSavePath   | function       | app\src\main\java\com\example\doc_tools\features\image\compressimages\presentation\viewmodel\CompressImagesViewModel.kt |
| updateSavePath   | function       | app\src\main\java\com\example\doc_tools\features\image\convertimages\presentation\viewmodel\ConvertImagesViewModel.kt |
| updateSavePath   | function       | app\src\main\java\com\example\doc_tools\features\pdf\compresspdf\presentation\viewmodel\CompressPdfViewModel.kt |
| updateSavePath   | function       | app\src\main\java\com\example\doc_tools\features\pdf\imagestopdf\presentation\viewmodel\ImagesToPdfViewModel.kt |
| updateSavePath   | function       | app\src\main\java\com\example\doc_tools\features\pdf\mergepdf\presentation\viewmodel\MergePdfViewModel.kt |
| updateSavePath   | function       | app\src\main\java\com\example\doc_tools\features\pdf\pdftoimages\presentation\viewmodel\PdfToImagesViewModel.kt |
| updateSelectedFormat | function       | app\src\main\java\com\example\doc_tools\features\image\convertimages\presentation\viewmodel\ConvertImagesViewModel.kt |
| updateThemeMode  | function       | app\src\main\java\com\example\doc_tools\features\settings\presentation\viewmodel\SettingsViewModel.kt |
| useAppContext    | function       | app\src\androidTest\java\com\example\doc_tools\ExampleInstrumentedTest.kt |
| validatePageInputs | function       | app\src\main\java\com\example\doc_tools\features\pdf\splitpdf\presentation\viewmodel\SplitPdfViewModel.kt |
| validateSaveLocation | function       | app\src\main\java\com\example\doc_tools\core\utils\file\SaveLocationUtils.kt |
| viewArchive      | function       | app\src\main\java\com\example\doc_tools\core\utils\file\FileActionsUtils.kt |
| viewFile         | function       | app\src\main\java\com\example\doc_tools\core\utils\file\FileActionsUtils.kt |
| viewImage        | function       | app\src\main\java\com\example\doc_tools\core\utils\file\FileActionsUtils.kt |
| viewPdf          | function       | app\src\main\java\com\example\doc_tools\core\utils\file\FileActionsUtils.kt |
| warning          | function       | app\src\main\java\com\example\doc_tools\core\presentation\state\UiMessageData.kt |
| white            | resource:color | app\src\main\res\values\colors.xml |
| with             | class          | app\src\main\java\com\example\doc_tools\core\utils\image\ImageFormat.kt |

## 📄 Included Files (Full Content)

### `CHANGELOG.md`

```md
# Changelog

## v1.0.0 - 2025-06-22
🎉 First official release of **DocTools** — All-in-one document utility app!

### 🧰 Included Tools:

## Pdf Tools:
- Compress pdf tool
- merge pdf tool
- split pdf tool
- images to pdf
- pdf to images

## Image Tools:
- compress images
- convert image format
```

### `gradle.properties`

```properties
# Project-wide Gradle settings.
# IDE (e.g. Android Studio) users:
# Gradle settings configured through the IDE *will override*
# any settings specified in this file.
# For more details on how to configure your build environment visit
# http://www.gradle.org/docs/current/userguide/build_environment.html
# Specifies the JVM arguments used for the daemon process.
# The setting is particularly useful for tweaking memory settings.
org.gradle.jvmargs=-Xmx2048m -Dfile.encoding=UTF-8
# When configured, Gradle will run in incubating parallel mode.
# This option should only be used with decoupled projects. For more details, visit
# https://developer.android.com/r/tools/gradle-multi-project-decoupled-projects
# org.gradle.parallel=true
# AndroidX package structure to make it clearer which packages are bundled with the
# Android operating system, and which are packaged with your app's APK
# https://developer.android.com/topic/libraries/support-library/androidx-rn
android.useAndroidX=true
# Kotlin code style for this project: "official" or "obsolete":
kotlin.code.style=official
# Enables namespacing of each library's R class so that its R class includes only the
# resources declared in the library itself and none from the library's dependencies,
# thereby reducing the size of the R class for that library
android.nonTransitiveRClass=true```

### `local.properties`

```properties
## This file must *NOT* be checked into Version Control Systems,
# as it contains information specific to your local configuration.
#
# Location of the SDK. This is only used by Gradle.
# For customization when using a Version Control System, please read the
# header note.
#Fri May 23 14:47:08 IST 2025
sdk.dir=C\:\\Users\\Purve\\AppData\\Local\\Android\\Sdk
```

### `README.md`

```md
# PDF & Image Tools App 📄 🖼️

## Overview 🎯

PDF & Image Tools App is a comprehensive Android application that provides a powerful suite of tools for working with PDF documents and image files. Transform, modify, and manage your documents and images with ease using our intuitive interface.

## Features ⚡

### PDF Tools 📑

#### 🗜️ Compress PDF
- Reduce PDF file size while preserving quality
- Adjustable compression quality (10-100%)
- Original file metadata preservation
- Downloads folder output with original filename preservation

#### 🔄 Merge PDFs
- Support for multiple PDF selection
- Drag-and-drop reordering
- Preview capability for selected PDFs
- Page count display for output file

#### ✂️ Split PDF
- Custom page range selection
- Page count validation
- Original file size and details display
- Preview capability for input PDF

#### 🖼️ PDF to Images
- Configurable DPI settings
- Format selection (JPG/PNG)
- Multiple page extraction
- Batch processing support

#### 📸 Images to PDF
- Support for various image formats (JPG, PNG, WebP)
- Multiple image selection
- Image preview and management
- Automatic page sizing

### Image Tools 🎨

#### 🗜️ Compress Images
- Batch compression support
- Quality slider (10-100%)
- Original format preservation
- Size comparison display

#### 📏 Resize Images
- Width/height adjustment
- Aspect ratio preservation option
- Custom save location support
- Original dimensions display

#### 🔄 Convert Format
- Support for JPG, PNG, and WebP
- Quality adjustment for lossy formats
- Format-specific optimization
- Size comparison after conversion

## Technical Details 🛠️

### Development Environment
- 💻 **IDE:** Android Studio
- 🏗️ **Build System:** Gradle (Kotlin DSL)
- 📱 **Minimum SDK:** 24
- 🎯 **Target SDK:** 35
- ⚙️ **Compile SDK:** 35

### Core Dependencies 📚
- 📑 **PDF Processing:** PdfBox-Android v2.0.27.0
- 🖼️ **Image Loading:** 
  - Coil v2.5.0
  - Glide Compose v1.0.0-beta01
- 🎨 **Image Processing:** Compressor v3.0.1
- 🎯 **UI Framework:** 
  - Jetpack Compose (Material 3)
  - Navigation Compose v2.7.7
- 🏗️ **Architecture Components:**
  - ViewModel Compose
  - WorkManager
  - Accompanist Permissions

### Architecture 🏛️
- **UI Pattern:** MVVM with Compose
- **Navigation:** Single-activity with Compose Navigation
- **Services:** 
  - PdfService: PDF operations handling
  - ImageService: Image processing operations
- **Storage:** 
  - MediaStore API for Android 10+
  - SAF (Storage Access Framework) for custom locations
  - Downloads directory for output files

## Installation 🚀

1. Clone the repository
2. Open project in Android Studio
3. Sync Gradle files
4. Build and run on device/emulator (API 24+)

## Project Structure 📁

```
app/
├── src/
│   └── main/
│       ├── java/com/example/pdf_img_tools_app/
│       │   ├── data/          # Data repositories
│       │   ├── model/         # Data models
│       │   ├── navigation/    # Navigation components
│       │   ├── service/       # PDF and Image services
│       │   ├── ui/           
│       │   │   ├── components/# Reusable UI components
│       │   │   ├── screens/   # Feature screens
│       │   │   └── theme/     # App theming
│       │   └── utils/         # Utility classes
│       └── res/              # Android resources
└── build.gradle.kts         # App-level build config
```

## Performance Optimizations ⚡

- 🧠 Memory management for large PDFs
- ♻️ Bitmap recycling for image operations
- ⚡ Background processing for intensive tasks
- 📊 Efficient file handling with streams
- 🗑️ Cache management for temporary files

## Error Handling 🛡️

- 📝 Comprehensive error messages
- 🔄 Graceful failure handling
- 👥 User-friendly error displays
- 🧹 Automatic cleanup of temporary files
- 🔒 Permission handling for storage access

## Future Enhancements 🚀

- 🔐 PDF encryption/decryption
- 📦 Batch PDF operations
- 💧 Image watermarking
- 📑 PDF page reordering
- ✨ Advanced PDF editing features

---
**Note:** This project is under active development. Features and implementations may change. 🔄```

### `app\src\androidTest\java\com\example\doc_tools\ExampleInstrumentedTest.kt`

```kt
package com.example.doc_tools

import androidx.test.platform.app.InstrumentationRegistry
import androidx.test.ext.junit.runners.AndroidJUnit4

import org.junit.Test
import org.junit.runner.RunWith

import org.junit.Assert.*

/**
 * Instrumented test, which will execute on an Android device.
 *
 * See [testing documentation](http://d.android.com/tools/testing).
 */
@RunWith(AndroidJUnit4::class)
class ExampleInstrumentedTest {
    @Test
    fun useAppContext() {
        // Context of the app under test.
        val appContext = InstrumentationRegistry.getInstrumentation().targetContext
        assertEquals("com.example.doc_tools", appContext.packageName)
    }
}```

### `app\src\main\AndroidManifest.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools">

    <!-- Storage permissions -->
    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" 
        android:maxSdkVersion="32" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" 
        android:maxSdkVersion="28" />
    <!-- For Android 13+ -->
    <uses-permission android:name="android.permission.READ_MEDIA_IMAGES" />
    <uses-permission android:name="android.permission.READ_MEDIA_VIDEO" />
    <uses-permission android:name="android.permission.READ_MEDIA_AUDIO" />
    <!-- For notifications -->
    <uses-permission android:name="android.permission.POST_NOTIFICATIONS" />

    <application
        android:allowBackup="true"
        android:dataExtractionRules="@xml/data_extraction_rules"
        android:fullBackupContent="@xml/backup_rules"
        android:icon="@drawable/ic_compress_images"
        android:label="@string/app_name"
        android:roundIcon="@drawable/ic_default_foreground"
        android:supportsRtl="true"
        android:theme="@style/Theme.Pdf_img_tools_app"
        android:requestLegacyExternalStorage="true"
        android:enableOnBackInvokedCallback="true"
        tools:targetApi="33">
        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:label="@string/app_name"
            android:theme="@style/Theme.Pdf_img_tools_app">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
        
        <!-- File provider for sharing files with other apps -->
        <provider
            android:name="androidx.core.content.FileProvider"
            android:authorities="${applicationId}.fileprovider"
            android:exported="false"
            android:grantUriPermissions="true">
            <meta-data
                android:name="android.support.FILE_PROVIDER_PATHS"
                android:resource="@xml/file_paths" />
        </provider>
        
        <!-- WorkManager for background processing -->
        <provider
            android:name="androidx.startup.InitializationProvider"
            android:authorities="${applicationId}.androidx-startup"
            android:exported="false"
            tools:node="merge">
            <meta-data
                android:name="androidx.work.WorkManagerInitializer"
                android:value="androidx.startup"
                tools:node="remove" />
        </provider>
    </application>

</manifest>

```

### `app\src\main\java\com\example\doc_tools\MainActivity.kt`

```kt
package com.example.doc_tools

import android.os.Bundle
import androidx.compose.runtime.Composable
import androidx.compose.runtime.CompositionLocalProvider
import androidx.compose.runtime.staticCompositionLocalOf
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.runtime.setValue
import androidx.navigation.compose.rememberNavController
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.ui.Modifier
import com.example.doc_tools.core.navigation.AppNavigation
import com.example.doc_tools.core.ui.theme.Pdf_img_tools_appTheme
import com.example.doc_tools.features.pdf.pdftoimages.presentation.viewmodel.AppContextProvider
import com.tom_roush.pdfbox.android.PDFBoxResourceLoader

// Local composition provider for dark theme state
val LocalDarkTheme = staticCompositionLocalOf { false }

class MainActivity : ComponentActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // Initialize AppContextProvider for WorkManager access
        AppContextProvider.appContext = applicationContext
        // Initialize PDFBox - handle potential exceptions
        try {
            PDFBoxResourceLoader.init(applicationContext)
        }
        catch(_: Exception) {
            // Just log the error and continue - don't let this crash the app
        }
        // Enable edge-to-edge display
        enableEdgeToEdge()
        setContent { AppContent() }
    }
}

@Composable
fun AppContent() {

    // Get system theme once at startup and make it saveable
    val initialDarkTheme = isSystemInDarkTheme()
    var isDarkTheme by rememberSaveable { mutableStateOf(initialDarkTheme) }
    
    // Use the theme value
    Pdf_img_tools_appTheme(darkTheme = isDarkTheme) {
        // Use a fixed size surface with a single color to prevent layout loops
        Surface(
            modifier = Modifier.fillMaxSize(),
            color = MaterialTheme.colorScheme.background,
        ){
            CompositionLocalProvider(LocalDarkTheme provides isDarkTheme) {
                val navController = rememberNavController()
                AppNavigation(
                    navController = navController,
                    isDarkTheme = isDarkTheme,
                    onThemeToggle = { isDarkTheme = !isDarkTheme }
                )
            }
        }
    }
}```

### `app\src\main\java\com\example\doc_tools\config\FeatureFlags.kt`

```kt
package com.example.doc_tools.config

/**
 * `FeatureFlags` is an object that defines constants for enabling or disabling
 * specific features within the PDF & Image Tools application.
 *
 * This centralized configuration allows for easy toggling of functionalities,
 * which is particularly useful during development, testing, or for phased rollouts.
 *
 * Each constant represents a specific tool or enhancement. Setting a constant
 * to `true` enables the feature, while `false` disables it.
 *
 * **PDF Tools:**
 * - `ENABLE_COMPRESS_PDF`: Enables PDF compression functionality.
 * - `ENABLE_MERGE_PDFS`: Enables merging multiple PDF files.
 * - `ENABLE_SPLIT_PDF`: Enables splitting a PDF file into multiple parts.
 * - `ENABLE_PDF_TO_IMAGES`: Enables converting PDF pages to images.
 * - `ENABLE_IMAGES_TO_PDF`: Enables creating a PDF from multiple images.
 *
 * **Image Tools:**
 * - `ENABLE_COMPRESS_IMAGES`: Enables image compression functionality.
 * - `ENABLE_RESIZE_IMAGES`: Enables resizing images.
 * - `ENABLE_CONVERT_IMAGES`: Enables converting images between different formats.
 * - `ENABLE_IMAGE_RESIZER`: A specific image resizing tool (currently disabled for v1).
 *
 * **Future Enhancements:**
 * These are placeholders for features planned for future releases.
 * - `ENABLE_BATCH_PDF_OPERATIONS`: Enables performing operations on multiple PDF files in batch.
 * - `ENABLE_WATERMARKING`: Enables adding watermarks to PDFs or images.
 */

object FeatureFlags {
    // PDF Tools
    const val ENABLE_COMPRESS_PDF = true
    const val ENABLE_MERGE_PDFS = true
    const val ENABLE_SPLIT_PDF = true
    const val ENABLE_PDF_TO_IMAGES = true
    const val ENABLE_IMAGES_TO_PDF = true

    // Image Tools
    const val ENABLE_COMPRESS_IMAGES = true
    const val ENABLE_CONVERT_IMAGES = true

}```

### `app\src\main\java\com\example\doc_tools\core\common\constants\AppDestinations.kt`

```kt
package com.example.doc_tools.core.common.constants

/**
 * Represents the various navigation destinations within the application.
 * This object centralizes all route constants, making them easily accessible
 * and maintainable for navigation purposes.
 *
 * Each constant string defines a unique route that can be used with the
 * navigation component to navigate to different screens or features.
 */

object AppDestinations {
    // Home screen
    const val HOME = "home"

    // PDF operations
    const val MERGE_PDF = "merge_pdf"
    const val SPLIT_PDF = "split_pdf"
    const val COMPRESS_PDF = "compress_pdf"
    const val PDF_TO_IMAGES = "pdf_to_images"
    const val IMAGES_TO_PDF = "images_to_pdf"

    // Image operations
    const val RESIZE_IMAGES = "resize_images"
    const val COMPRESS_IMAGES = "compress_images"
    const val CONVERT_IMAGES = "convert_images"
    const val IMAGE_RESIZER = "image_resizer"
}```

### `app\src\main\java\com\example\doc_tools\core\common\model\FileDetails.kt`

```kt
package com.example.doc_tools.core.common.model

import android.net.Uri

data class FileDetails(
    val uri: Uri,
    val name: String,
    val size: Long, // Size in bytes
    val mimeType: String,
    val path: String? = null,
    val dimensions: Pair<Int, Int>? = null,// Width, Height for images
    val pageCount: Int? = null,

    )```

### `app\src\main\java\com\example\doc_tools\core\domain\model\SaveMode.kt`

```kt
package com.example.doc_tools.core.domain.model

/**
 * Enum representing different save modes for PDF and image operations.
 *
 * This enum defines various ways in which the output of PDF or image
 * processing tasks can be saved.
 */

enum class SaveMode {
    SINGLE_FILE,     // Save as a single file
    MULTIPLE_FILES,  // Save as multiple files
    ZIP_ARCHIVE,     // Save as a zip archive
    FOLDER,          // Save to folder structure
    SEPARATELY,      // Save files separately
    AS_ARCHIVE       // Save as a single archive
}```

### `app\src\main\java\com\example\doc_tools\core\domain\model\ToolCategory.kt`

```kt
package com.example.doc_tools.core.domain.model

/**
 * Categories of tools in the app
 */
enum class ToolCategory {
    PDF,
    IMAGE
}```

### `app\src\main\java\com\example\doc_tools\core\navigation\AppNavigation.kt`

```kt
package com.example.doc_tools.core.navigation

import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.navigation.NavHostController
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import com.example.doc_tools.features.home.presentation.ui.HomeScreen
import com.example.doc_tools.features.image.compressimages.presentation.ui.CompressImagesScreen
import com.example.doc_tools.features.image.convertimages.presentation.ui.ConvertImagesScreen
import com.example.doc_tools.features.pdf.compresspdf.presentation.ui.CompressPdfScreen
import com.example.doc_tools.features.pdf.mergepdf.presentation.ui.MergePdfScreen
import com.example.doc_tools.features.pdf.splitpdf.presentation.ui.SplitPdfScreen
import com.example.doc_tools.features.pdf.pdftoimages.presentation.ui.PdfToImagesScreen
import com.example.doc_tools.features.pdf.imagestopdf.presentation.ui.ImagesToPdfScreen
import com.example.doc_tools.features.settings.presentation.ui.SettingsScreen

/**
 * Defines the navigation routes for the app.
 *
 * This object contains constants representing all the possible navigation destinations within the application.
 * These constants are used to configure the navigation graph and to navigate between screens.
 */

object AppDestinations {

    const val HOME = "home"

    // PDF Tools
    const val COMPRESS_PDF = "compress_pdf"
    const val MERGE_PDF = "merge_pdf"
    const val SPLIT_PDF = "split_pdf"
    const val PDF_TO_IMAGES = "pdf_to_images"
    const val IMAGES_TO_PDF = "images_to_pdf"

    // Image Tools
    const val COMPRESS_IMAGES = "compress_images"
    const val RESIZE_IMAGES = "resize_images"
    const val CONVERT_IMAGES = "convert_images"
    const val IMAGE_RESIZER = "image_resizer"
    
    // App Settings
    const val SETTINGS = "settings"
}

/**
 * Composable function that defines the navigation graph for the application.
 *
 * This function uses a [NavHost] to define the different screens (destinations)
 * and how to navigate between them. It also passes necessary parameters like
 * the [navController], [isDarkTheme] status, and [onThemeToggle] callback to each screen.
 *
 * @param navController The [NavHostController] used for navigation.
 * @param isDarkTheme A boolean indicating whether the dark theme is currently active.
 * @param onThemeToggle A lambda function to be invoked when the theme toggle is pressed.
 * @param modifier Optional [Modifier] to be applied to the NavHost.
 */

@Composable
fun AppNavigation(
    navController: NavHostController,
    isDarkTheme: Boolean,
    onThemeToggle: () -> Unit,
    modifier: Modifier = Modifier
) {
    NavHost(
        navController = navController,
        startDestination = AppDestinations.HOME,
        modifier = modifier
    ) {
        composable(AppDestinations.HOME) {
            HomeScreen(
                navController = navController,
                isDarkTheme = isDarkTheme,
                onThemeToggle = onThemeToggle
            )
        }
        
        // Settings Screen
        composable(AppDestinations.SETTINGS) {
            SettingsScreen(
                navController = navController,
                isDarkTheme = isDarkTheme,
                onThemeToggle = onThemeToggle
            )
        }

        // PDF Tool Screens
        composable(AppDestinations.COMPRESS_PDF) {
            CompressPdfScreen(
                navController = navController,
                isDarkTheme = isDarkTheme,
                onThemeToggle = onThemeToggle
            )
        }
        composable(AppDestinations.MERGE_PDF) {
            MergePdfScreen(
                navController = navController,
                isDarkTheme = isDarkTheme,
                onThemeToggle = onThemeToggle
            )
        }
        composable(AppDestinations.SPLIT_PDF) {
            SplitPdfScreen(
                navController = navController,
                isDarkTheme = isDarkTheme,
                onThemeToggle = onThemeToggle
            )
        }
        composable(AppDestinations.PDF_TO_IMAGES) {
            PdfToImagesScreen(
                navController = navController,
                isDarkTheme = isDarkTheme,
                onThemeToggle = onThemeToggle
            )
        }
        composable(AppDestinations.IMAGES_TO_PDF) {
            ImagesToPdfScreen(
                navController = navController,
                isDarkTheme = isDarkTheme,
                onThemeToggle = onThemeToggle
            )
        }

        // Image Tool Screens
        composable(AppDestinations.COMPRESS_IMAGES) {
            CompressImagesScreen(
                navController = navController,
                isDarkTheme = isDarkTheme,
                onThemeToggle = onThemeToggle
            )
        }

        composable(AppDestinations.CONVERT_IMAGES) {
            ConvertImagesScreen(
                navController = navController,
                isDarkTheme = isDarkTheme,
                onThemeToggle = onThemeToggle
            )
        }

    }
}```

### `app\src\main\java\com\example\doc_tools\core\presentation\eventbus\UiMessageBus.kt`

```kt
package com.example.doc_tools.core.presentation.eventbus

import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch
import kotlinx.coroutines.flow.MutableSharedFlow
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.SharedFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asSharedFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.update

import com.example.doc_tools.core.presentation.state.MessageType
import com.example.doc_tools.core.presentation.state.UiMessageData
import com.example.doc_tools.core.presentation.state.DisplayMethod

/**
 * Centralized bus for managing UI messages across the application.
 * This singleton provides methods to show, update and dismiss messages,
 * as well as observe messages for specific scopes.
 */

object UiMessageBus {

    private val coroutineScope = CoroutineScope(Dispatchers.Main)
    // Holds all active messages
    private val _messages = MutableStateFlow<List<UiMessageData>>(emptyList())
    val messages: StateFlow<List<UiMessageData>> = _messages.asStateFlow() // Event flow for message actions
    private val _messageEvents = MutableSharedFlow<MessageEvent>()
    val messageEvents: SharedFlow<MessageEvent> = _messageEvents.asSharedFlow()
    
    /**
     * Show a new message
     * @param message The message to show
     * @param preferredDisplayMethod Optional preferred display method (toast, snackbar, dialog, inline)
     */

    fun showMessage(
        message: UiMessageData, 
        preferredDisplayMethod: DisplayMethod? = null
    ) {
        val messageWithDisplayMethod = if (preferredDisplayMethod != null) {
            message.copy(metadata = mapOf("displayMethod" to preferredDisplayMethod.name))
        } else {
            message
        }
        
        _messages.update { currentMessages ->
            val newList = currentMessages.toMutableList()
            newList.add(messageWithDisplayMethod)
            newList
        }
        
        coroutineScope.launch {
            _messageEvents.emit(MessageEvent.Show(messageWithDisplayMethod))
            
            // Auto-dismiss after timeout if specified
            messageWithDisplayMethod.timeout?.let { timeout ->
                delay(timeout)
                dismissMessage(messageWithDisplayMethod.id)
            }
        }
    }
    
    /**
     * Show a message with the specified type, text and optional scope
     */
    fun showMessage(
        text: String,
        type: MessageType = MessageType.INFO,
        scope: String? = null,
        dismissible: Boolean = true,
        timeout: Long? = UiMessageData.DEFAULT_TIMEOUT,
        preferredDisplayMethod: DisplayMethod? = null
    ) {
        val message = UiMessageData(
            text = text,
            type = type,
            scope = scope,
            dismissible = dismissible,
            timeout = timeout
        )
        showMessage(message, preferredDisplayMethod)
    }
    
    /**
     * Shorthand methods for different message types
     */
    fun showInfo(
        text: String, 
        scope: String? = null, 
        timeout: Long? = UiMessageData.DEFAULT_TIMEOUT,
        preferredDisplayMethod: DisplayMethod? = DisplayMethod.TOAST
    ) {
        showMessage(
            UiMessageData.info(text, scope, timeout = timeout),
            preferredDisplayMethod
        )
    }
    
    fun showSuccess(
        text: String, 
        scope: String? = null, 
        timeout: Long? = UiMessageData.DEFAULT_TIMEOUT,
        preferredDisplayMethod: DisplayMethod? = DisplayMethod.SNACKBAR
    ) {
        showMessage(
            UiMessageData.success(text, scope, timeout = timeout),
            preferredDisplayMethod
        )
    }
    
    fun showWarning(
        text: String, 
        scope: String? = null, 
        timeout: Long? = UiMessageData.DEFAULT_TIMEOUT,
        preferredDisplayMethod: DisplayMethod? = DisplayMethod.SNACKBAR
    ) {
        showMessage(
            UiMessageData.warning(text, scope, timeout = timeout),
            preferredDisplayMethod
        )
    }
    
    fun showError(
        text: String, 
        scope: String? = null, 
        timeout: Long? = null,
        preferredDisplayMethod: DisplayMethod? = null
    ) {
        // based on content length and severity
        showMessage(
            UiMessageData.error(text, scope, timeout = timeout),
            preferredDisplayMethod
        )
    }
    
    // Toast-specific methods for convenience

    fun showToast(text: String, scope: String? = null, isLongDuration: Boolean = false) {
        showInfo(
            text = text,
            scope = scope,
            timeout = if (isLongDuration) 3500L else 2000L,
            preferredDisplayMethod = DisplayMethod.TOAST
        )
    }
    
    // Snackbar-specific methods for convenience

    fun showSnackbar(text: String, scope: String? = null, type: MessageType = MessageType.INFO) {
        showMessage(
            text = text,
            type = type,
            scope = scope,
            preferredDisplayMethod = DisplayMethod.SNACKBAR
        )
    }
    
    // Dialog-specific methods for convenience

    fun showDialog(text: String, scope: String? = null, type: MessageType = MessageType.ERROR) {
        showMessage(
            text = text,
            type = type,
            scope = scope,
            preferredDisplayMethod = DisplayMethod.DIALOG
        )
    }
    
    /**
     * Dismiss a specific message by its ID
     * @param messageId The ID of the message to dismiss
     */

    fun dismissMessage(messageId: String) {
        _messages.update { currentMessages ->
            currentMessages.filter { it.id != messageId }
        }
        
        coroutineScope.launch {
            _messageEvents.emit(MessageEvent.Dismiss(messageId))
        }
    }
    
    /**
     * Clear all messages
     */

    fun clearAllMessages() {
        _messages.update { emptyList() }
        
        coroutineScope.launch {
            _messageEvents.emit(MessageEvent.ClearAll)
        }
    }
    
    /**
     * Clear all messages for a specific scope
     * @param scope The scope to clear messages for
     */

    fun clearScope(scope: String) {
        val messagesToRemove = _messages.value.filter { it.scope == scope }
        
        _messages.update { currentMessages ->
            currentMessages.filter { it.scope != scope }
        }
        
        coroutineScope.launch {
            _messageEvents.emit(MessageEvent.ClearScope(scope))
        }
    }
    
    /**
     * Alias for clearScope method for more intuitive API
     * @param scope The scope to clear messages for
     */

    fun clearMessages(scope: String) {
        clearScope(scope)
    }
    
    /**
     * Update an existing message
     * @param messageId The ID of the message to update
     * @param update A lambda that receives the old message and returns an updated one
     */

    fun updateMessage(messageId: String, update: (UiMessageData) -> UiMessageData) {
        _messages.update { currentMessages ->
            currentMessages.map { 
                if (it.id == messageId) update(it) else it 
            }
        }
    }
}

/**
 * Sealed class representing different message events
 */

sealed class MessageEvent {
    data class Show(val message: UiMessageData) : MessageEvent()
    data class Dismiss(val messageId: String) : MessageEvent()
    data class ClearScope(val scope: String) : MessageEvent()
    object ClearAll : MessageEvent()
}
```

### `app\src\main\java\com\example\doc_tools\core\presentation\state\DisplayMethod.kt`

```kt
package com.example.doc_tools.core.presentation.state

/**
 * Enum representing different methods for displaying messages.
 *
 * This enum defines the various ways a message can be presented to the user
 * within the application. Each method offers a different user experience and
 * level of intrusiveness.
 */

enum class DisplayMethod {
    TOAST,      // Short-lived message shown at the bottom of the screen
    SNACKBAR,   // Message with possible actions, shown at bottom of the screen
    DIALOG,     // Modal dialog requiring user acknowledgment
    INLINE      // Inline message within the UI (fallback to original implementation)
}```

### `app\src\main\java\com\example\doc_tools\core\presentation\state\MessageType.kt`

```kt
package com.example.doc_tools.core.presentation.state

/**
 * Enum representing the type of UI message.
 * This determines the visual styling and potentially the behavior of the message.
 *
 * - `INFO`: For general informational messages.
 * - `SUCCESS`: For messages indicating a successful operation.
 * - `WARNING`: For messages warning the user about a potential issue.
 * - `ERROR`: For messages indicating an error or failure.
 */
enum class MessageType {
    INFO,
    SUCCESS,
    WARNING,
    ERROR
}```

### `app\src\main\java\com\example\doc_tools\core\presentation\state\ProcessingStateManager.kt`

```kt
package com.example.doc_tools.core.presentation.state

import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow

/**
 * Singleton manager that handles the global processing state across the app.
 *
 * This ensures that only one tool can be processing at a time, preventing users
 * from starting multiple resource-intensive operations simultaneously.
 */
object ProcessingStateManager {
    // Internal state
    private val _isProcessing = MutableStateFlow(false)
    private val _currentProcess = MutableStateFlow<String?>(null)
    private val _processingStartTime = MutableStateFlow<Long>(0)
    private val _currentProgress = MutableStateFlow(-1f)

    // Exposed states
    val isProcessing: StateFlow<Boolean> = _isProcessing.asStateFlow()
    val currentProcess: StateFlow<String?> = _currentProcess.asStateFlow()
    val currentProgress: StateFlow<Float> = _currentProgress.asStateFlow()

    /**
     * Start a new processing operation.
     *
     * @param processName The name of the process (e.g., "pdf_compression", "image_conversion")
     * @return True if the process was successfully started, false if another process is already running
     */
    fun startProcess(processName: String): Boolean {
        // If already processing, don't allow starting a new process
        if (_isProcessing.value) {
            return false
        }

        _isProcessing.value = true
        _currentProcess.value = processName
        _processingStartTime.value = System.currentTimeMillis()
        _currentProgress.value = -1f
        return true
    }

    /**
     * Update the progress of the current process.
     *
     * @param progress The progress value from 0.0 to 1.0
     * @param processName Optional process name for verification
     * @return True if progress was updated, false if no process is running or wrong process name
     */
    fun updateProgress(progress: Float, processName: String? = null): Boolean {
        if (!_isProcessing.value) return false

        // If process name is provided, verify it matches the current process
        if (processName != null && _currentProcess.value != processName) return false

        _currentProgress.value = progress.coerceIn(0f, 1f)
        return true
    }

    /**
     * End the currently running process.
     *
     * @param processName The name of the process to end (must match the current process)
     * @return True if the process was successfully ended, false if no matching process was running
     */
    fun endProcess(processName: String): Boolean {
        // Only end if this is the currently running process
        if (_isProcessing.value && _currentProcess.value == processName) {
            _isProcessing.value = false
            _currentProcess.value = null
            _currentProgress.value = -1f
            return true
        }
        return false
    }

    /**
     * Force end any running process.
     * This should be used carefully, typically in error handling scenarios.
     */
    fun forceEndProcess() {
        _isProcessing.value = false
        _currentProcess.value = null
        _currentProgress.value = -1f
    }

    /**
     * Get the elapsed time of the current process in milliseconds.
     *
     * @return Elapsed time in milliseconds, or 0 if no process is running
     */
    fun getElapsedTime(): Long {
        if (!_isProcessing.value) return 0
        return System.currentTimeMillis() - _processingStartTime.value
    }
}```

### `app\src\main\java\com\example\doc_tools\core\presentation\state\ToolItem.kt`

```kt
package com.example.doc_tools.core.presentation.state

import androidx.compose.ui.graphics.vector.ImageVector
import com.example.doc_tools.core.domain.model.ToolCategory

/**
 * Represents a tool in the app.
 *
 * @property id Unique identifier for the tool.
 * @property name Display name of the tool.
 * @property description A brief description of what the tool does.
 * @property icon The icon representing the tool, as an [androidx.compose.ui.graphics.vector.ImageVector].
 * @property route The navigation route associated with this tool.
 * @property category The category the tool belongs to, see [com.example.doc_tools.core.domain.model.ToolCategory].
 */

data class ToolItem(
    val id: String,
    val name: String,
    val description: String,
    val icon: ImageVector,
    val route: String,
    val category: ToolCategory
)```

### `app\src\main\java\com\example\doc_tools\core\presentation\state\UiMessageData.kt`

```kt
package com.example.doc_tools.core.presentation.state

import java.util.UUID

/**
 * Data class representing a UI message to be displayed in the application
 * @param id Unique identifier for the message
 * @param text The message content to display
 * @param type The type of message (info, success, warning, error)
 * @param scope Optional scope identifier for the message (e.g., "compress_pdf", "merge_pdf")
 * @param dismissible Whether the message can be dismissed by the user
 * @param timeout Optional timeout in milliseconds after which the message will auto-dismiss (null means no auto-dismiss)
 * @param metadata Additional key-value pairs for custom handling of messages
 */
data class UiMessageData(
    val id: String = UUID.randomUUID().toString(),
    val text: String,
    val type: MessageType = MessageType.INFO,
    val scope: String? = null,
    val dismissible: Boolean = true,
    val timeout: Long? = DEFAULT_TIMEOUT,
    val timestamp: Long = System.currentTimeMillis(),
    val metadata: Map<String, String> = emptyMap()
) {
    companion object {
        const val DEFAULT_TIMEOUT: Long = 5000 // 5 seconds

        // Factory methods for common message types
        fun info(
            text: String,
            scope: String? = null,
            dismissible: Boolean = true,
            timeout: Long? = DEFAULT_TIMEOUT,
            metadata: Map<String, String> = emptyMap()
        ) = UiMessageData(
            text = text,
            type = MessageType.INFO,
            scope = scope,
            dismissible = dismissible,
            timeout = timeout,
            metadata = metadata
        )

        fun success(
            text: String,
            scope: String? = null,
            dismissible: Boolean = true,
            timeout: Long? = DEFAULT_TIMEOUT,
            metadata: Map<String, String> = emptyMap()
        ) = UiMessageData(
            text = text,
            type = MessageType.SUCCESS,
            scope = scope,
            dismissible = dismissible,
            timeout = timeout,
            metadata = metadata
        )

        fun warning(
            text: String,
            scope: String? = null,
            dismissible: Boolean = true,
            timeout: Long? = DEFAULT_TIMEOUT,
            metadata: Map<String, String> = emptyMap()
        ) = UiMessageData(
            text = text,
            type = MessageType.WARNING,
            scope = scope,
            dismissible = dismissible,
            timeout = timeout,
            metadata = metadata
        )

        fun error(
            text: String,
            scope: String? = null,
            dismissible: Boolean = true,
            timeout: Long? = null, // Errors don't auto-dismiss by default
            metadata: Map<String, String> = emptyMap()
        ) = UiMessageData(
            text = text,
            type = MessageType.ERROR,
            scope = scope,
            dismissible = dismissible,
            timeout = timeout,
            metadata = metadata
        )
    }
}```

### `app\src\main\java\com\example\doc_tools\core\ui\components\button\ChipButton.kt`

```kt
package com.example.doc_tools.core.ui.components.button

import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.unit.dp

/**
 * A reusable chip-like button with icon and label, supporting selection state.
 */
@Composable
fun ChipButton(
    label: String,
    icon: ImageVector?,
    selected: Boolean,
    onClick: () -> Unit,
    modifier: Modifier = Modifier.padding(horizontal = 14.dp, vertical = 12.dp),
    enabled: Boolean = true
) {
//    val backgroundColor = if (selected) MaterialTheme.colorScheme.tertiaryContainer else MaterialTheme.colorScheme.surfaceVariant
    val contentColor = if (selected) MaterialTheme.colorScheme.onTertiaryContainer else MaterialTheme.colorScheme.onSurfaceVariant
    val border = if (selected) BorderStroke(1.dp, MaterialTheme.colorScheme.tertiary) else null

    Surface(
        modifier = Modifier.clickable(enabled = enabled, onClick = onClick),
        shape = RoundedCornerShape(8.dp),
        color = MaterialTheme.colorScheme.surfaceVariant,
        contentColor = contentColor,
        border = border,
//        shadowElevation = if (selected) 2.dp else 0.dp,
    ) {
        Row(
            verticalAlignment = Alignment.CenterVertically,
//          verticalArrangement = Arrangement.Center,
//          horizontalAlignment = Alignment.CenterHorizontally,
            modifier = modifier
        ) {
            if (icon != null) {
                Icon(imageVector = icon, contentDescription = null, modifier = Modifier.size(16.dp))
                Spacer(modifier = Modifier.size(8.dp))
            }
            Text(
                text = label,
                style = MaterialTheme.typography.labelSmall
            )
        }
    }
} ```

### `app\src\main\java\com\example\doc_tools\core\ui\components\button\ProgressToolButton.kt`

```kt
package com.example.doc_tools.core.ui.components.button

import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.material3.Button
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import kotlin.math.roundToInt

/**
 * A composable function that displays a button with a progress indicator.
 *
 * This Progress button can be used to indicate that a tool is in progress.
 * It can also display an error message if the process fails.
 * Shows percentage progress when a valid progress value is provided.
 * When processing, shows the status text in the center with the circular
 * progress indicator on the right side.
 *
 * @param text The text to display on the button when not processing.
 * @param onClick The callback to be invoked when the button is clicked.
 * @param modifier The modifier to be applied to the button.
 * @param isProcessing Whether the process is currently in progress.
 * @param progress The progress of the process, from 0.0 to 1.0.
 * @param icon The icon to display on the button.
 * @param errorMessage The error message to display if the process fails.
 * @param onCancel The callback to be invoked when the cancel button is clicked.
 * @param enabled Whether the button is enabled.
 * @param processingText The text to show during processing (e.g., "Compressing", "Merging").
 */

@Composable
fun ProgressToolButton(
    text: String,
    onClick: () -> Unit,
    modifier: Modifier = Modifier,
    isProcessing: Boolean = false,
    progress: Float = -1f,
    icon: ImageVector? = null,
    errorMessage: String? = null,
    onCancel: (() -> Unit)? = null,
    enabled: Boolean = true,
    processingText: String = "Processing"
) {
    Button(onClick = onClick, modifier = modifier.fillMaxWidth(), enabled = enabled && !isProcessing) {
        Row(verticalAlignment = Alignment.CenterVertically, modifier = Modifier.padding(vertical = 12.dp).fillMaxWidth()) {
            if (!isProcessing) {
                Text(text = text, modifier = Modifier.weight(1f), textAlign = TextAlign.Center)
            }
            else { // Processing state with centered status text and percentage
                if (progress >= 0f) { // With progress percentage
                    Text(text = "$processingText...  ${(progress * 100).roundToInt()}%", color = MaterialTheme.colorScheme.primary, textAlign = TextAlign.Center, modifier = Modifier.weight(1f))
                } else { // Without progress percentage (indeterminate)
                    Text(text = processingText, color = MaterialTheme.colorScheme.primary, textAlign = TextAlign.Center, modifier = Modifier.weight(1f))
                } // Progress indicator on the right
                CircularProgressIndicator(modifier = Modifier.size(24.dp), color = MaterialTheme.colorScheme.primary, strokeWidth = 2.dp, progress = if (progress >= 0f) progress else 1f)
            }
        }
    }
}
```

### `app\src\main\java\com\example\doc_tools\core\ui\components\card\FileInfoActionCard.kt`

```kt
package com.example.doc_tools.core.ui.components.card

import androidx.compose.animation.AnimatedVisibility
import androidx.compose.animation.core.Spring
import androidx.compose.animation.core.spring
import androidx.compose.animation.expandVertically
import androidx.compose.animation.fadeIn
import androidx.compose.foundation.background
import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.outlined.*
import androidx.compose.material.icons.automirrored.outlined.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.example.doc_tools.core.common.model.FileDetails
import com.example.doc_tools.core.utils.file.FileInfoUtils
import androidx.compose.material3.HorizontalDivider
import com.example.doc_tools.core.utils.file.FileIconUtils

/**
 * Composable function to display a modern file information card with configurable details and actions.
 *
 * This card presents file details in a compact and visually appealing manner,
 * using Material Design 3 components. It allows customization of which
 * details are shown (name, size, format, dimensions, compression, path, page count)
 * and provides optional action buttons (open, share, delete).
 *
 * @param file The [FileDetails] object containing information about the file.
 * @param showName Boolean flag to control visibility of the file name. Defaults to true.
 * @param showSize Boolean flag to control visibility of the file size. Defaults to true.
 * @param showFormat Boolean flag to control visibility of the file format (MIME type). Defaults to false.
 * @param showDimensions Boolean flag to control visibility of image dimensions (width x height). Defaults to false.
 * @param showCompression Boolean flag to control visibility of compression information. Defaults to false.
 * @param showPath Boolean flag to control visibility of the file path. Defaults to false.
 * @param showPages Boolean flag to control visibility of the page count for PDF files. Defaults to false.
 * @param compressionInfo A [Pair] of Long values representing (originalSize, compressedSize) in bytes. Used when `showCompression` is true. Defaults to null.
 * @param labelOverrides A [Map] to override default labels for displayed details. Keys are detail types (e.g., "size", "format"), values are custom labels. Defaults to an empty map.
 * @param onOpen Optional lambda function to be invoked when the "Open" or "View" action is triggered. If null, the button is not shown. Defaults to null.
 * @param onShare Optional lambda function to be invoked when the "Share" action is triggered. If null, the button is not shown. Defaults to null.
 * @param onDelete Optional lambda function to be invoked when the "Delete" or "Remove" action is triggered. If null, the button is not shown. Defaults to null.
 * @param isDarkTheme Boolean indicating if the dark theme is active. Defaults to the system setting.
 * @param modifier [Modifier] for this composable. Defaults to [Modifier].
 */

@OptIn(ExperimentalLayoutApi::class)
@Composable
fun FileInfoActionCard(
    file: FileDetails,
    showName: Boolean = true,
    showSize: Boolean = true,
    showFormat: Boolean = false,
    showDimensions: Boolean = false,
    showCompression: Boolean = false,
    showPath: Boolean = false,
    showPages: Boolean = false,
    compressionInfo: Pair<Long, Long>? = null, // Pair of (originalSize, compressedSize) in bytes
    labelOverrides: Map<String, String> = emptyMap(),
    onOpen: (() -> Unit)? = null,
    onShare: (() -> Unit)? = null,
    onDelete: (() -> Unit)? = null,
    isDarkTheme: Boolean = isSystemInDarkTheme(),
    modifier: Modifier = Modifier,
    enabled: Boolean = true  // Add enabled parameter with default value true
) {
    val context = LocalContext.current

    AnimatedVisibility(visible = true, enter = fadeIn(animationSpec = spring(stiffness = Spring.StiffnessLow)) + expandVertically(animationSpec = spring(stiffness = Spring.StiffnessLow))) {
        Card(modifier = modifier.fillMaxWidth(), colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surfaceVariant), shape = RoundedCornerShape(14.dp)
        ) {
            Column(modifier = Modifier.fillMaxWidth()) {

                if (showName) {
                    Row(verticalAlignment = Alignment.CenterVertically, modifier = Modifier.fillMaxWidth().padding(8.dp)) {
                        // File type icon with circular background
                        Box(contentAlignment = Alignment.Center, modifier = Modifier.size(36.dp).clip(RoundedCornerShape(8.dp)).background(MaterialTheme.colorScheme.secondaryContainer)) {
                            Icon(imageVector = FileIconUtils.getIconForMimeType(file.mimeType), contentDescription = null, tint = MaterialTheme.colorScheme.onSurfaceVariant, modifier = Modifier.size(24.dp))
                        }
                        Spacer(modifier = Modifier.width(14.dp))
                        // File name and type
                        Column(modifier = Modifier.weight(1f)) {
                            Text(text = file.name, style = MaterialTheme.typography.bodyMedium, fontWeight = FontWeight.SemiBold, maxLines = 1, overflow = TextOverflow.Ellipsis, color = MaterialTheme.colorScheme.onSurfaceVariant)
                            Spacer(modifier = Modifier.height(2.dp))
                            if (showFormat) {
                                val formatLabel = labelOverrides["format"] ?: "Type"
                                Text(text = file.mimeType ?: "Unknown type", style = MaterialTheme.typography.bodySmall, color = MaterialTheme.colorScheme.onSurfaceVariant, maxLines = 1, overflow = TextOverflow.Ellipsis,)
                            }
                        }
                    }
                }

                HorizontalDivider(color = MaterialTheme.colorScheme.outline)

                // Details - single column layout for better readability
                Column(modifier = Modifier.fillMaxWidth().padding(0.dp)) {
                    // File details and metadata
                    FlowRow(modifier = Modifier.padding(start = 50.dp)) {
                        // File size
                        if (showSize) {
                            val sizeLabel = labelOverrides["size"] ?: "Size"
                            CompactDetailRow(icon = Icons.Outlined.Storage, label = sizeLabel, value = FileInfoUtils.getFormattedFileSize(file.size))
                        }

                        // File format/type
                        if (showFormat) {
                            val formatLabel = labelOverrides["format"] ?: "Type"
                            CompactDetailRow(icon = Icons.Outlined.Description, label = formatLabel, value = file.mimeType)
                        }

                        // Path info if available
                        if (showPath && file.path != null) {
                            val pathLabel = labelOverrides["path"] ?: "Path"
                            CompactDetailRow(icon = Icons.Outlined.Folder, label = pathLabel, value = file.path)
                        }

                        // Dimensions if available (for images)
                        if (showDimensions && file.dimensions != null) {
                            val dimensionsLabel = labelOverrides["dimensions"] ?: "Dimensions"
                            val (width, height) = file.dimensions
                            CompactDetailRow(icon = Icons.Outlined.Fullscreen, label = dimensionsLabel, value = "${width}×${height}")
                        }

                        // Page count for PDFs
                        if (showPages && file.mimeType == "application/pdf") {
                            val pagesLabel = labelOverrides["pages"] ?: "Pages"
                            CompactDetailRow(icon = Icons.AutoMirrored.Outlined.Article, label = pagesLabel, value = file.pageCount?.toString() ?: "Unknown")
                        }

                        // Compression info if original size is available
                        if (showCompression && compressionInfo != null) {
                            val savingsField = "compression"
                            val savingsLabel = labelOverrides[savingsField] ?: "Compression"
                            if (compressionInfo.first > 0 && compressionInfo.second > 0) {
                                val originalSize = compressionInfo.first
                                val compressedSize = compressionInfo.second
                                // Calculate compression percentage
                                val difference = originalSize - compressedSize
                                val percentSaved = ((difference.toFloat() / originalSize) * 100).toInt()
                                // Original size row
                                CompactDetailRow(icon = Icons.Outlined.FilePresent, label = "Original Size", value = FileInfoUtils.getFormattedFileSize(originalSize))
                                // Compressed size row
                                CompactDetailRow(icon = Icons.Outlined.FileDownload, label = "Compressed Size", value = FileInfoUtils.getFormattedFileSize(compressedSize))
                                // Savings percentage row
                                CompactDetailRow(icon = Icons.AutoMirrored.Outlined.TrendingDown, label = savingsLabel,
                                    value = if (percentSaved >= 0) "$percentSaved% smaller" else "${-percentSaved}% larger"
                                )
                            }
                        }
                    }
                }

                // Action buttons
                Row(horizontalArrangement = Arrangement.End, modifier = Modifier.fillMaxWidth().padding(horizontal = 8.dp, vertical = 12.dp)) {
                    // Open button
                    if (onOpen != null) {
                        FilledTonalIconButton(
                            onClick = { if (enabled) onOpen() },  // Only call if enabled
                            modifier = Modifier.size(width = 80.dp, height = 32.dp),
                            colors = IconButtonDefaults.filledTonalIconButtonColors(containerColor = MaterialTheme.colorScheme.primaryContainer, contentColor = MaterialTheme.colorScheme.onPrimaryContainer),
                            enabled = enabled  // Pass enabled parameter
                        ) {
                            Row(verticalAlignment = Alignment.CenterVertically) {
                                Icon(imageVector = Icons.Outlined.Visibility, contentDescription = "Open", modifier = Modifier.size(16.dp))
                                Spacer(Modifier.width(6.dp))
                                Text(text = "View", style = MaterialTheme.typography.labelMedium, fontSize = 12.sp)
                            }
                        }
                    }

                    // Share button
                    if (onShare != null) {
                        Spacer(modifier = Modifier.width(8.dp))
                        FilledTonalIconButton(
                            onClick = { if (enabled) onShare() },  // Only call if enabled
                            modifier = Modifier.size(width = 80.dp, height = 32.dp) ,
                            colors = IconButtonDefaults.filledTonalIconButtonColors(containerColor = MaterialTheme.colorScheme.secondaryContainer, contentColor = MaterialTheme.colorScheme.onSecondaryContainer),
                            enabled = enabled  // Pass enabled parameter
                        ) {
                            Row(verticalAlignment = Alignment.CenterVertically) {
                                Icon(imageVector = Icons.Outlined.Share, contentDescription = "Share", modifier = Modifier.size(16.dp))
                                Spacer(modifier = Modifier.width(4.dp))
                                Text(text = "Share", style = MaterialTheme.typography.labelMedium, fontSize = 12.sp)
                            }
                        }
                    }

                    Spacer(modifier = Modifier.width(8.dp))
                    // Delete button
                    if (onDelete != null) {
                        FilledTonalIconButton(
                            onClick = { if (enabled) onDelete() },  // Only call if enabled
                            modifier = Modifier.size(width = 80.dp, height = 32.dp),
                            colors = IconButtonDefaults.filledTonalIconButtonColors(containerColor = MaterialTheme.colorScheme.secondaryContainer, contentColor = MaterialTheme.colorScheme.onSecondaryContainer),
                            enabled = enabled  // Pass enabled parameter
                        ) {
                            Row(verticalAlignment = Alignment.CenterVertically) {
                                Icon(imageVector = Icons.Outlined.Delete, contentDescription = "Delete", modifier = Modifier.size(16.dp))
                                Spacer(modifier = Modifier.width(4.dp))
                                Text(text = "Remove", style = MaterialTheme.typography.labelMedium, fontSize = 12.sp)
                            }
                        }
                    }
                }
            }
        }
    }
}

/**
 * A more compact version of DetailRow for the modernized UI
 */
@Composable
private fun CompactDetailRow(icon: ImageVector, label: String, value: String, modifier: Modifier = Modifier) {
    Row(modifier = Modifier.padding(top = 8.dp, start = 8.dp, end = 8.dp)) {
        Icon(imageVector = icon, contentDescription = null, tint = MaterialTheme.colorScheme.onSurfaceVariant, modifier = Modifier.size(14.dp))
        Spacer(modifier = Modifier.width(4.dp))
        Column {
            Text(text = label, style = MaterialTheme.typography.labelSmall, color = MaterialTheme.colorScheme.onSurfaceVariant, fontSize = 12.sp)
            Spacer(modifier = Modifier.height(2.dp))
            Text(text = value, style = MaterialTheme.typography.bodyMedium, fontSize = 10.sp, maxLines = 1, overflow = TextOverflow.Ellipsis)
        }
    }
}
```

### `app\src\main\java\com\example\doc_tools\core\ui\components\card\ToolCard.kt`

```kt
package com.example.doc_tools.core.ui.components.card

import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import com.example.doc_tools.core.domain.model.ToolCategory
import com.example.doc_tools.core.presentation.state.ToolItem

/**
 * Card component for displaying a tool item
 */
@Composable
fun ToolCard(
    toolItem: ToolItem,
    onClick: () -> Unit,
    modifier: Modifier = Modifier,
    isDarkTheme: Boolean = false
) {
    val accentColor = when (toolItem.category) {
        ToolCategory.PDF -> MaterialTheme.colorScheme.primary
        ToolCategory.IMAGE -> MaterialTheme.colorScheme.secondary
    }
    
    Card(
        modifier = modifier.fillMaxWidth().height(160.dp).clickable(onClick = onClick),
        elevation = CardDefaults.cardElevation(defaultElevation = 0.dp),
        colors = CardDefaults.cardColors(
            containerColor = MaterialTheme.colorScheme.surfaceVariant,
            contentColor = MaterialTheme.colorScheme.onSurfaceVariant
        ),
        shape = RoundedCornerShape(14.dp),
        border = null
    ){
        Column(modifier = Modifier.padding(14.dp).fillMaxWidth(), verticalArrangement = Arrangement.spacedBy(16.dp), horizontalAlignment = Alignment.CenterHorizontally) {

            Icon(
                imageVector = toolItem.icon,
                contentDescription = toolItem.name,
                modifier = Modifier.size(32.dp),
            )

            Text(
                text = toolItem.name,
                style = MaterialTheme.typography.titleMedium,
            )

            Text(
                text = toolItem.description,
                style = MaterialTheme.typography.bodySmall,
                textAlign = TextAlign.Center,
                maxLines = 2,
            )
        }
    }
}
```

### `app\src\main\java\com\example\doc_tools\core\ui\components\feedback\WarningBanner.kt`

```kt
package com.example.doc_tools.core.ui.components.feedback

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Warning
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

@Composable
fun WarningBanner(
    text: String,
    modifier: Modifier = Modifier,
    icon: @Composable (() -> Unit)? = {
        Icon(
            imageVector = Icons.Default.Warning,
            contentDescription = "Warning",
            modifier = Modifier.size(16.dp),
            tint = Color(0xFFFFA000),
        )
    }
) {
    Row(
        modifier = modifier
            .fillMaxWidth()
            .background(MaterialTheme.colorScheme.surface)
            .padding(8.dp),
        verticalAlignment = Alignment.CenterVertically
    ) {
        icon?.invoke()
        Spacer(modifier = Modifier.width(8.dp))
        Text(
            text = text,
            fontSize = 12.sp,
            style = MaterialTheme.typography.bodySmall,
            modifier = Modifier.weight(1f)
        )
    }
}
```

### `app\src\main\java\com\example\doc_tools\core\ui\components\file\ChangeSaveLocation.kt`

```kt
package com.example.doc_tools.core.ui.components.file

import android.net.Uri
import android.content.Context
import android.content.Intent
import android.util.Log
import android.widget.Toast
import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Folder
import androidx.compose.material.icons.filled.Save
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.window.Dialog
import com.example.doc_tools.core.domain.model.SaveMode
import com.example.doc_tools.core.utils.file.UriUtils

/**
 * A reusable save location selector component that allows users to choose a directory
 * and optionally a save mode (e.g., save files separately or as an archive).
 * This component becomes visible only after the user has selected files to process.
 *
 * It handles requesting directory access permissions and stores the selected
 * location's URI in SharedPreferences for persistence. If permission is denied
 * or an error occurs, it displays an appropriate message.
 *
 * @param visible Controls the visibility of the component.
 * @param defaultSaveLocation The initial path to display as the save location.
 * @param onSaveLocationChanged A callback function invoked when the save location is changed by the user. It receives the new save path as a [String].
 * @param saveModeEnabled A boolean indicating whether the save mode selection (e.g., separately or as archive) should be enabled. Defaults to `true`.
 * @param initialSaveMode The [SaveMode] to be selected by default when the component is first displayed. Defaults to [SaveMode.SEPARATELY].
 * @param onSaveModeChanged A callback function invoked when the save mode is changed. It receives the new [SaveMode]. Defaults to an empty lambda.
 * @param modifier The [Modifier] to be applied to the root Composable of this component.
 */

@Composable
fun ChangeSaveLocation(
    visible: Boolean,
    defaultSaveLocation: String,
    onSaveLocationChanged: (String) -> Unit,
    saveModeEnabled: Boolean = true,
    initialSaveMode: SaveMode = SaveMode.SEPARATELY,
    onSaveModeChanged: (SaveMode) -> Unit = {},
    modifier: Modifier = Modifier
) {
    if (!visible) return
    
    val context = LocalContext.current
    // State for tracking selected save location
    var selectedSavePath by remember { mutableStateOf(defaultSaveLocation) }
    var showSaveLocationDialog by remember { mutableStateOf(false) }
    var saveMode by remember { mutableStateOf(initialSaveMode) }
    var hasPermissionError by remember { mutableStateOf(false) }
    var selectedSaveUri by remember { mutableStateOf("") }
    
    // Directory picker launcher
    val dirPickerLauncher = rememberLauncherForActivityResult(contract = ActivityResultContracts.OpenDocumentTree()){

        uri: Uri? -> uri?.let {
            try { // Log the selected URI for debugging
                Log.d("ReusableSaveLocationSelector", "Selected URI: $it") // Get permission to write to this location
                val takeFlags = Intent.FLAG_GRANT_READ_URI_PERMISSION or Intent.FLAG_GRANT_WRITE_URI_PERMISSION
                try { // Take persistable URI permission to maintain access across app restarts
                    context.contentResolver.takePersistableUriPermission(it, takeFlags)
                }
                catch (e: SecurityException) {
                    Log.w("ReusableSaveLocationSelector", "Could not take persistable permission: ${e.message}") // Continue anyway, might be a permissions issue that we can work around
                }
                
                // Get folder name and path for display
                val directoryName = UriUtils.getDirectoryName(context, it)
                if (directoryName != null) {
                    selectedSavePath = directoryName
                    onSaveLocationChanged(directoryName)
                    hasPermissionError = false
                    // Store the actual URI in a tag for future use
                    selectedSaveUri = it.toString()
                    // Save this URI to SharedPreferences for the SaveLocationUtils to use
                    val sharedPrefs = context.getSharedPreferences("save_locations", Context.MODE_PRIVATE)
                    sharedPrefs.edit().apply {
                        putString(directoryName, it.toString())
                        apply()
                    }
                    Log.d("ReusableSaveLocationSelector", "Directory selected: $directoryName, URI: $it")
                }
                else {
                    // If we couldn't get the name, try to extract something useful from the URI
                    val fallbackName = it.lastPathSegment ?: it.toString()
                    selectedSavePath = "Selected: $fallbackName"
                    onSaveLocationChanged(selectedSavePath)
                    hasPermissionError = false
                    selectedSaveUri = it.toString()
                    
                    // Even in the fallback case, save the URI to SharedPreferences
                    val sharedPrefs = context.getSharedPreferences("save_locations", Context.MODE_PRIVATE)
                    sharedPrefs.edit().apply {
                        putString(selectedSavePath, it.toString())
                        apply()
                    }
                    Log.d("ReusableSaveLocationSelector", "Using fallback name: $fallbackName")
                }
            } catch (e: SecurityException) {
                hasPermissionError = true
                Log.e("ReusableSaveLocationSelector", "Security exception: ${e.message}")
                Toast.makeText(context, "Error accessing directory: ${e.message}", Toast.LENGTH_LONG).show()
            } catch (e: Exception) {
                hasPermissionError = true
                Log.e("ReusableSaveLocationSelector", "Failed to access directory: ${e.message}")
                Toast.makeText(context, "Error: ${e.message}", Toast.LENGTH_LONG).show()
            }
        }
    }

    Column(modifier = Modifier.padding(top = 0.dp)){
        Text(text = "Save Location", style = MaterialTheme.typography.titleSmall, color = MaterialTheme.colorScheme.onSurface, modifier = Modifier.padding(bottom = 16.dp))
        // Save location card
        Card(modifier = modifier, colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surfaceVariant, contentColor = MaterialTheme.colorScheme.onSurfaceVariant), shape = RoundedCornerShape(10.dp),){
            Column(modifier = Modifier.fillMaxWidth().padding(16.dp)){
                Row(modifier = Modifier.fillMaxWidth(), verticalAlignment = Alignment.CenterVertically, horizontalArrangement = Arrangement.SpaceBetween){
                    Icon(imageVector = Icons.Filled.Save, contentDescription = "Folder Icon", modifier = Modifier.size(34.dp), tint = MaterialTheme.colorScheme.onSurface)
                    Spacer(modifier = Modifier.width(16.dp))
                    Column(modifier = Modifier.weight(1f)){
                        Row(modifier = Modifier.padding(bottom = 2.dp), verticalAlignment = Alignment.CenterVertically){
                            Text(text = "Save Location : ", style = MaterialTheme.typography.bodySmall, color = MaterialTheme.colorScheme.onSurfaceVariant, modifier = Modifier)
                            // Display selected path with error indication if needed
                            Text(text = selectedSavePath, style = MaterialTheme.typography.bodySmall, color = if (hasPermissionError) MaterialTheme.colorScheme.error else MaterialTheme.colorScheme.onSurface, maxLines = 2)
                        }
                        // Display save mode indicator
                        if (saveModeEnabled) Text(text = "Save Mode : ${if (saveMode == SaveMode.SEPARATELY) "Save Separately" else "Save as Archive"}", style = MaterialTheme.typography.bodySmall, color = MaterialTheme.colorScheme.onSurface)
                        if (hasPermissionError) Text(text = "Permission denied. Please select another location.", style = MaterialTheme.typography.bodySmall, color = MaterialTheme.colorScheme.error)
                    }
                    TextButton(onClick = { showSaveLocationDialog = true }, colors = ButtonDefaults.buttonColors(containerColor = MaterialTheme.colorScheme.secondaryContainer, contentColor = MaterialTheme.colorScheme.onSecondaryContainer), modifier = Modifier.size(width = 80.dp, height = 40.dp)){
                        Text(text = "Change", style = MaterialTheme.typography.bodySmall)
                    }
                }
            }
        }
    }

    // Save location dialog
    if (showSaveLocationDialog) {
        SaveLocationDialog(initialPath = selectedSavePath, initialSaveMode = saveMode, saveModeEnabled = saveModeEnabled, onDismiss = { showSaveLocationDialog = false }, onConfirm = { path, mode ->
                if (saveModeEnabled && mode != saveMode) {
                    // Update the save mode - do this first as it's not dependent on user pick location
                    saveMode = mode
                    onSaveModeChanged(mode)
                    Log.d("ReusableSaveLocationSelector", "Save mode changed to: $mode")
                }
                // If user manually entered a path, we launch the picker
                if (path != selectedSavePath) { dirPickerLauncher.launch(null) }
                showSaveLocationDialog = false
            },
            onPickLocation = {
                dirPickerLauncher.launch(null)
                showSaveLocationDialog = false
            }
        )
    }
}

/**
 * Dialog for selecting save location and mode
 */
@Composable
private fun SaveLocationDialog(initialPath: String, initialSaveMode: SaveMode, saveModeEnabled: Boolean, onDismiss: () -> Unit, onConfirm: (String, SaveMode) -> Unit, onPickLocation: () -> Unit) {
    var path by remember { mutableStateOf(initialPath) }
    var saveMode by remember { mutableStateOf(initialSaveMode) }
    
    Dialog(onDismissRequest = onDismiss) {
        Surface(
            shape = RoundedCornerShape(16.dp),
            color = MaterialTheme.colorScheme.surface,
            tonalElevation = 16.dp,
            contentColor = MaterialTheme.colorScheme.onSurfaceVariant
        ) {
            Column(modifier = Modifier.padding(20.dp).fillMaxWidth()) {
                Text(text = "Save Location Settings", style = MaterialTheme.typography.titleSmall, fontWeight = FontWeight.Normal, modifier = Modifier.padding(bottom = 16.dp))
                // Location input
                OutlinedTextField(
                    value = path,
                    onValueChange = { path = it },
                    label = { Text(text = "Save Location") },
                    modifier = Modifier.fillMaxWidth().padding(bottom = 8.dp),
                    trailingIcon = {
                        IconButton(onClick = onPickLocation) {
                            // This would ideally be an icon, but using text for simplicity
                            Icon(imageVector = Icons.Default.Folder, contentDescription = "Pick location")
                        }
                    }
                )
                
                // Save mode selection
                if (saveModeEnabled) {
                    Column(modifier = Modifier.fillMaxWidth().padding(vertical = 8.dp)) {
                        Text(text = "Save Mode", style = MaterialTheme.typography.bodyMedium, modifier = Modifier.padding(bottom = 4.dp))
                        // Save separately option
                        Row(verticalAlignment = Alignment.CenterVertically, modifier = Modifier.fillMaxWidth()) {
                            RadioButton(selected = saveMode == SaveMode.SEPARATELY, onClick = { saveMode = SaveMode.SEPARATELY })
                            Text(text = "Save files separately")
                        }
                        // Save as archive option
                        Row(verticalAlignment = Alignment.CenterVertically, modifier = Modifier.fillMaxWidth()) {
                            RadioButton(selected = saveMode == SaveMode.AS_ARCHIVE, onClick = { saveMode = SaveMode.AS_ARCHIVE })
                            Text(text = "Save as archive")
                        }
                    }
                }
                
                // Buttons
                Row(modifier = Modifier.fillMaxWidth().padding(top = 16.dp), horizontalArrangement = Arrangement.End) {
                    TextButton(onClick = onDismiss) { Text(text = "Cancel") }
                    Spacer(modifier = Modifier.width(8.dp))
                    Button(onClick = { onConfirm(path, saveMode) }, colors = ButtonDefaults.buttonColors(containerColor = MaterialTheme.colorScheme.surfaceVariant, contentColor = MaterialTheme.colorScheme.onSurfaceVariant)){
                        Text(text = "Save")
                    }
                }
            }
        }
    }
}

```

### `app\src\main\java\com\example\doc_tools\core\ui\components\file\FileBottomSheet.kt`

```kt
package com.example.doc_tools.core.ui.components.file

import android.content.Context
import android.net.Uri
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.itemsIndexed
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.CheckCircle
import androidx.compose.material.icons.filled.Clear
import androidx.compose.material.icons.filled.Close
import androidx.compose.material.icons.filled.Delete
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import coil.compose.AsyncImage
import coil.request.ImageRequest
import com.example.doc_tools.core.common.model.FileDetails
import com.example.doc_tools.core.utils.file.FileInfoUtils
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import androidx.compose.material.icons.filled.RemoveRedEye
import androidx.compose.material.icons.outlined.Circle
import com.example.doc_tools.core.utils.file.FileBottomSheetUtils
import kotlinx.coroutines.delay


@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun FileBottomSheet(
    show: Boolean,
    onDismiss: () -> Unit,
    fileUris: List<Uri>,
    title: String,
    onFilesUpdated: (List<Uri>) -> Unit,
    onFileView: ((Uri, String?) -> Unit)? = null,
    fileTypeIcon: ImageVector? = null,
    isDarkTheme: Boolean,
    useCheckboxes: Boolean = false,
    showIndexNumbers: Boolean = false,
    showFileSize: Boolean = true,
    showDimensions: Boolean = false,
    showImagePreview: Boolean = false,
    additionalItemContent: @Composable ((Uri, FileDetails?) -> Unit)? = null,
    messageScope: String = "file_operations",
    enableClearAll: Boolean = true,
    enableRemoveSelected: Boolean = true,
    enableFileViewButton: Boolean = true,
    enableFileRemoveButton: Boolean = true,
    enableSelection: Boolean = true,
) {
    if (!show) return

    val context = LocalContext.current
    val bottomSheetState = rememberModalBottomSheetState(skipPartiallyExpanded = false)
    val selectedItems = remember { mutableStateListOf<Uri>() }
    var isDeleting by remember { mutableStateOf(false) } 
    val coroutineScope = rememberCoroutineScope()

    // Cache FileDetails to avoid repeated I/O
    val fileDetailsCache = remember { mutableMapOf<Uri, FileDetails?>() }
    
    // Remember last operation message
    var operationMessage by remember { mutableStateOf<String?>(null) }
    
    // Function to reset selected items after operation
    fun resetSelection() {
        selectedItems.clear()
    }

    // Function to delete multiple files in a batch with logging
    fun deleteFiles(uris: List<Uri>) {
        if (uris.isEmpty()) return
        isDeleting = true
        operationMessage = "Removing files..."
        
        // Use the optimized FileBottomSheetUtils to handle removal
        FileBottomSheetUtils.removeFiles(
            uris = uris,
            currentUris = fileUris,
            onUpdate = { updatedList ->
                // First update the file list
                onFilesUpdated(updatedList)
                
                // Then clear the loading state with a small delay to ensure UI updates properly
                coroutineScope.launch {
                    delay(100)
                    isDeleting = false
                    resetSelection()
                    operationMessage = null
                }
            },
            context = context,
            scope = coroutineScope,
            showMessage = true,
            messageScope = messageScope
        )
    }
    
    // Function to clear all files using utils
    fun clearAll() {
        isDeleting = true
        operationMessage = "Clearing all files..."
        
        // Use the optimized FileBottomSheetUtils to handle clearing all
        FileBottomSheetUtils.clearAllFiles(
            onUpdate = { updatedList ->
                // First update the file list
                onFilesUpdated(updatedList)
                
                // Then clear the loading state with a small delay to ensure UI updates properly
                coroutineScope.launch {
                    delay(100)
                    isDeleting = false
                    resetSelection()
                    operationMessage = null
                }
            },
            context = context,
            scope = coroutineScope,
            fileCount = fileUris.size,
            showMessage = true,
            messageScope = messageScope
        )
    }

    // Cleanup when dismissed
    DisposableEffect(show) {
        onDispose {
            if (isDeleting) {
                // Cancel any ongoing operations when sheet is dismissed
                FileBottomSheetUtils.cancelAllOperations()
                isDeleting = false
                operationMessage = null
            }
        }
    }

    ModalBottomSheet(
        onDismissRequest = {
            onDismiss()
            selectedItems.clear()
        },
        containerColor = MaterialTheme.colorScheme.surface,
        contentColor = MaterialTheme.colorScheme.onSurface,
        sheetState = bottomSheetState
    ) {
        Column(modifier = Modifier.fillMaxWidth()) {
            // Header section
            Row(
                modifier = Modifier.fillMaxWidth().padding(start = 24.dp, end = 24.dp),
                horizontalArrangement = Arrangement.SpaceBetween,
                verticalAlignment = Alignment.CenterVertically
            ) {
                Text(
                    text = "$title (${fileUris.size})",
                    style = MaterialTheme.typography.titleMedium,
                    fontWeight = FontWeight.Normal
                )
                IconButton(
                    onClick = {
                        // Check if operations are in progress before dismissing
                        if (isDeleting) {
                            FileBottomSheetUtils.cancelAllOperations()
                            isDeleting = false
                        }
                        onDismiss()
                        selectedItems.clear()
                    }
                ) {
                    Icon(imageVector = Icons.Default.Close, contentDescription = "Close")
                }
            }

            // Action buttons
            if (fileUris.isNotEmpty() && !(showImagePreview && fileUris.size == 1)) {
                if (enableRemoveSelected || enableClearAll) {
                Row(
                    modifier = Modifier.fillMaxWidth().padding(all = 16.dp),
                    horizontalArrangement = Arrangement.spacedBy(8.dp)
                ) {
                        if (enableRemoveSelected) {
                    OutlinedButton(
                        onClick = {
                            if (selectedItems.isNotEmpty()) {
                                deleteFiles(selectedItems.toList())
                            }
                        },
                        enabled = !isDeleting && selectedItems.isNotEmpty(),
                        modifier = Modifier.weight(1f)
                    ) {
                        Row(
                            verticalAlignment = Alignment.CenterVertically,
                            horizontalArrangement = Arrangement.Center,
                            modifier = Modifier.fillMaxWidth()
                        ) {
                            Icon(
                                imageVector = Icons.Default.Clear,
                                contentDescription = "Remove Selected",
                                modifier = Modifier.size(16.dp)
                            )
                            Spacer(modifier = Modifier.width(8.dp))
                            Text(text = "Remove Selected")
                        }
                    }
                        }
                        if (enableClearAll) {
                    FilledTonalButton(
                        modifier = Modifier.weight(1f),
                        colors = ButtonDefaults.filledTonalButtonColors(
                            containerColor = MaterialTheme.colorScheme.secondaryContainer,
                            contentColor = MaterialTheme.colorScheme.onSecondaryContainer
                        ),
                        onClick = { clearAll() },
                        enabled = !isDeleting
                    ) {
                        Row(
                            verticalAlignment = Alignment.CenterVertically,
                            horizontalArrangement = Arrangement.Center,
                            modifier = Modifier.fillMaxWidth()
                        ) {
                            Icon(
                                imageVector = Icons.Default.Delete,
                                contentDescription = "Clear All",
                                modifier = Modifier.size(16.dp)
                            )
                            Spacer(modifier = Modifier.width(8.dp))
                            Text(text = "Clear All")
                                }
                        }
                    }
                }
                Spacer(modifier = Modifier.height(8.dp))
                }
            }

            HorizontalDivider(modifier = Modifier.fillMaxWidth(), color = MaterialTheme.colorScheme.outline)

            // Content section with overlay when deleting
            Box(modifier = Modifier.fillMaxSize()) {
                if (showImagePreview && fileUris.size == 1) {
                    SingleImagePreviewContent(
                        uri = fileUris[0],
                        context = context,
                        showFileSize = showFileSize,
                        showDimensions = showDimensions,
                        additionalItemContent = additionalItemContent
                    )
                } else {
                    FileListContent(
                        fileUris = fileUris,
                        context = context,
                        selectedItems = selectedItems,
                        onToggleSelection = { uri, selected ->
                            if (selected) selectedItems.add(uri) else selectedItems.remove(uri)
                        },
                        onFileView = onFileView,
                        onFileRemove = { uri -> 
                            isDeleting = true
                            operationMessage = "Removing file..."
                            
                            FileBottomSheetUtils.removeFile(
                                uri = uri,
                                currentUris = fileUris,
                                onUpdate = { updatedList ->
                                    // First update the file list
                                    onFilesUpdated(updatedList)
                                    
                                    // Then clear the loading state with a small delay to ensure UI updates properly
                                    coroutineScope.launch {
                                        delay(100)
                                        isDeleting = false
                                        operationMessage = null
                                    }
                                },
                                context = context,
                                scope = coroutineScope,
                                showMessage = true,
                                messageScope = messageScope
                            )
                        },
                        fileTypeIcon = fileTypeIcon,
                        useCheckboxes = useCheckboxes,
                        showIndexNumbers = showIndexNumbers,
                        showFileSize = showFileSize,
                        showDimensions = showDimensions,
                        isDarkTheme = isDarkTheme,
                        additionalItemContent = additionalItemContent,
                        isDeleting = isDeleting,
                        fileDetailsCache = fileDetailsCache,
                        enableFileViewButton = enableFileViewButton,
                        enableFileRemoveButton = enableFileRemoveButton,
                        enableSelection = enableSelection
                    )
                }
                if (isDeleting) {
                    Box(
                        modifier = Modifier.fillMaxSize().background(Color.Black.copy(alpha = 0.8f)),
                        contentAlignment = Alignment.Center
                    ) {
                        Column(
                            horizontalAlignment = Alignment.CenterHorizontally,
                            verticalArrangement = Arrangement.spacedBy(16.dp)
                        ) {
                            CircularProgressIndicator(color = MaterialTheme.colorScheme.onSurface)
                            
                            // Show operation message if available
                            operationMessage?.let { message ->
                                Text(
                                    text = message,
                                    color = MaterialTheme.colorScheme.onSurface,
                                    style = MaterialTheme.typography.bodyMedium
                                )
                            }
                        }
                    }
                }
            }
            Spacer(modifier = Modifier.height(32.dp))
        }
    }
}

@Composable
private fun SingleImagePreviewContent(
    uri: Uri,
    context: Context,
    showFileSize: Boolean,
    showDimensions: Boolean,
    additionalItemContent: @Composable ((Uri, FileDetails?) -> Unit)? = null
) {
    val fileDetails = remember(uri) { FileInfoUtils.getFileDetails(context, uri) }
    Column(
        modifier = Modifier.fillMaxWidth().padding(16.dp),
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Box(
            modifier = Modifier
                .weight(1f)
                .fillMaxWidth()
                .clip(RoundedCornerShape(12.dp))
                .background(Color(0xFF121212).copy(alpha = 0.1f)),
            contentAlignment = Alignment.Center
        ) {
            AsyncImage(
                model = ImageRequest.Builder(context)
                    .data(uri)
                    .crossfade(true)
                    .size(width = 300, height = 300)
                    .build(),
                contentDescription = "Image Preview",
                modifier = Modifier.fillMaxSize(),
                contentScale = ContentScale.Fit
            )
        }

        if (fileDetails != null) {
            Card(
                modifier = Modifier.fillMaxWidth().padding(top = 16.dp),
                colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surfaceVariant)
            ) {
                Column(modifier = Modifier.padding(16.dp)) {
                    Text(
                        text = fileDetails.name ?: "Image",
                        style = MaterialTheme.typography.titleMedium,
                        maxLines = 1,
                        overflow = TextOverflow.Ellipsis
                    )
                    if (showFileSize) {
                        Text(
                            text = FileInfoUtils.getFormattedFileSize(fileDetails.size),
                            style = MaterialTheme.typography.bodyMedium
                        )
                    }
                    if (showDimensions && fileDetails.dimensions != null) {
                        Text(
                            text = "${fileDetails.dimensions.first} x ${fileDetails.dimensions.second}",
                            style = MaterialTheme.typography.bodyMedium
                        )
                    }
                    additionalItemContent?.invoke(uri, fileDetails)
                }
            }
        }
    }
}

@Composable
private fun FileListContent(
    fileUris: List<Uri>,
    context: Context,
    selectedItems: List<Uri>,
    onToggleSelection: (Uri, Boolean) -> Unit,
    onFileView: ((Uri, String?) -> Unit)?,
    onFileRemove: (Uri) -> Unit,
    fileTypeIcon: ImageVector?,
    useCheckboxes: Boolean,
    showIndexNumbers: Boolean,
    showFileSize: Boolean,
    showDimensions: Boolean,
    isDarkTheme: Boolean,
    additionalItemContent: @Composable ((Uri, FileDetails?) -> Unit)? = null,
    isDeleting: Boolean,
    fileDetailsCache: MutableMap<Uri, FileDetails?>, // Added cache
    enableFileViewButton: Boolean = true,
    enableFileRemoveButton: Boolean = true,
    enableSelection: Boolean = true
) {
    LazyColumn(
        modifier = Modifier.fillMaxWidth(),
        verticalArrangement = Arrangement.spacedBy(8.dp),
        contentPadding = PaddingValues(16.dp)
    ) {
        itemsIndexed(items = fileUris, key = { _, uri -> uri.toString() }) { index, uri ->
            // Load FileDetails only if not cached
            val fileDetails by produceState<FileDetails?>(initialValue = fileDetailsCache[uri], uri) {
                if (fileDetailsCache[uri] == null) {
                    withContext(Dispatchers.IO) {
                        val details = FileInfoUtils.getFileDetails(context, uri)
                        fileDetailsCache[uri] = details
                        value = details
                    }
                }
            }
            val isSelected = selectedItems.contains(uri)

            FileListItem(
                uri = uri,
                fileDetails = fileDetails,
                index = if (showIndexNumbers) index + 1 else null,
                isSelected = isSelected,
                onToggleSelection = { onToggleSelection(uri, !isSelected) },
                onView = onFileView?.let { { it(uri, fileDetails?.mimeType) } },
                onRemove = { onFileRemove(uri) },
                fileTypeIcon = fileTypeIcon,
                useCheckbox = useCheckboxes,
                showFileSize = showFileSize,
                showDimensions = showDimensions,
                isDarkTheme = isDarkTheme,
                additionalContent = additionalItemContent?.let { { it(uri, fileDetails) } },
                enabled = !isDeleting,
                enableViewButton = enableFileViewButton,
                enableRemoveButton = enableFileRemoveButton,
                enableSelection = enableSelection
            )
        }
    }
}

@Composable
private fun FileListItem(
    uri: Uri,
    fileDetails: FileDetails?,
    index: Int?,
    isSelected: Boolean,
    onToggleSelection: () -> Unit,
    onView: (() -> Unit)?,
    onRemove: () -> Unit,
    fileTypeIcon: ImageVector?,
    useCheckbox: Boolean,
    showFileSize: Boolean,
    showDimensions: Boolean,
    isDarkTheme: Boolean,
    additionalContent: (@Composable () -> Unit)? = null,
    enabled: Boolean,
    enableViewButton: Boolean = true,
    enableRemoveButton: Boolean = true,
    enableSelection: Boolean = true
) {
    val backgroundColor = remember(isSelected, isDarkTheme) {
        if (isSelected) {
            if (isDarkTheme) Color(0xFF2D3748).copy(alpha = 0.7f) else Color(0xFFE6F0FF)
        } else {
            if (isDarkTheme) Color(0xFF1D232A) else Color(0xFFF8F9FA)
        }
    }

    Card(
        modifier = Modifier.fillMaxWidth(),
        colors = CardDefaults.cardColors(containerColor = backgroundColor)
    ) {
        Row(
            verticalAlignment = Alignment.CenterVertically,
            horizontalArrangement = Arrangement.spacedBy(8.dp),
            modifier = Modifier.padding(14.dp)
        ) {
            // Only show selection widget if enabled
            if (enableSelection) {
            Box(
                modifier = Modifier
                    .size(28.dp)
                    .clickable(onClick = onToggleSelection, enabled = enabled),
                contentAlignment = Alignment.Center
            ) {
                if (useCheckbox) {
                    Checkbox(
                        checked = isSelected,
                        onCheckedChange = { onToggleSelection() },
                        enabled = enabled
                    )
                } else {
                        Icon(
                            imageVector = if (isSelected) Icons.Filled.CheckCircle else Icons.Outlined.Circle,
                            contentDescription = if (isSelected) "Selected" else "Not Selected",
                            tint = if (isSelected) MaterialTheme.colorScheme.secondary else MaterialTheme.colorScheme.onSurface,
                            modifier = Modifier.size(28.dp)
                        )
                    }
                }
            }

            if (index != null) {
                Box(
                    contentAlignment = Alignment.Center,
                    modifier = Modifier
                        .size(28.dp)
                        .clip(CircleShape)
                        .background(MaterialTheme.colorScheme.primaryContainer)
                ) {
                    Text(
                        text = index.toString(),
                        style = MaterialTheme.typography.bodySmall.copy(fontSize = 12.sp),
                        color = MaterialTheme.colorScheme.onPrimaryContainer
                    )
                }
            }

            // File info section
            Column(modifier = Modifier.weight(1f).padding(horizontal = 8.dp)) {
                Text(
                    text = fileDetails?.name ?: uri.lastPathSegment ?: "Unknown file",
                    style = MaterialTheme.typography.bodyMedium.copy(fontSize = 13.sp),
                    maxLines = 1,
                    overflow = TextOverflow.Ellipsis,
                    color = MaterialTheme.colorScheme.onSurfaceVariant
                )
                if (showFileSize || (showDimensions && fileDetails?.dimensions != null)) {
                    Spacer(modifier = Modifier.height(4.dp))
                    Text(
                        text = buildString {
                            if (showFileSize) {
                                append(FileInfoUtils.getFormattedFileSize(fileDetails?.size ?: 0))
                            }
                            if (showDimensions && fileDetails?.dimensions != null) {
                                if (showFileSize) append(" • ")
                                append("${fileDetails.dimensions.first}x${fileDetails.dimensions.second}")
                            }
                        },
                        style = MaterialTheme.typography.bodySmall.copy(fontSize = 10.sp),
                    )
                }
                additionalContent?.invoke()
            }

            // Action buttons
            Row(
                horizontalArrangement = Arrangement.spacedBy(4.dp),
                verticalAlignment = Alignment.CenterVertically
            ) {
                if (onView != null && enableViewButton) {
                    IconButton(
                        onClick = onView,
                        modifier = Modifier.size(48.dp),
                        enabled = enabled
                    ) {
                        Icon(
                            imageVector = Icons.Default.RemoveRedEye,
                            contentDescription = "View",
                            tint = MaterialTheme.colorScheme.onSurfaceVariant
                        )
                    }
                }
                if (enableRemoveButton) {
                IconButton(
                    onClick = onRemove,
                    modifier = Modifier.size(48.dp),
                    enabled = enabled
                ) {
                        Icon(
                            imageVector = Icons.Default.Delete,
                            contentDescription = "Remove",
                            tint = MaterialTheme.colorScheme.onSurfaceVariant
                        )
                    }
                }
            }
        }
    }
}```

### `app\src\main\java\com\example\doc_tools\core\ui\components\file\FilePickerHandler.kt`

```kt
package com.example.doc_tools.core.ui.components.file

import android.net.Uri
import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.platform.LocalContext

/**
 * A centralized file picker handler that can be used for both single and multiple file selection.
 * 
 * @param single Whether to pick a single file (true) or multiple files (false)
 * @param supportedMimeTypes List of MIME types to filter for in the file picker
 * @param onPicked Callback when files are selected
 * @param content Composable slot that takes a function to launch the file picker and the current selected URIs
 */

@Composable
fun FilePickerHandler(
    single: Boolean,
    supportedMimeTypes: List<String> = listOf("*/*"),
    onPicked: (List<Uri>) -> Unit,
    content: @Composable (launchPicker: () -> Unit, selected: List<Uri>) -> Unit
) {
    val context = LocalContext.current
    var selectedUris by remember { mutableStateOf<List<Uri>>(emptyList()) }
    
    // Choose the appropriate contract based on whether we want single or multiple selection
    val launcher = if (single) {
        rememberLauncherForActivityResult(
            contract = ActivityResultContracts.OpenDocument(),
            onResult = { uri: Uri? ->
                uri?.let { selectedUri ->
                    try {
                        selectedUris = listOf(selectedUri)
                        onPicked(selectedUris)
                    } catch (e: SecurityException) {
                        // Handle error
                    }
                }
            }
        )
    } else {
        rememberLauncherForActivityResult(
            contract = ActivityResultContracts.OpenMultipleDocuments(),
            onResult = {
                uris: List<Uri>? ->
                uris?.let { newUris ->
                    if (newUris.isNotEmpty()) {
                        selectedUris = newUris
                        onPicked(selectedUris)
                    }
                }
            }
        )
    }
    val launchPicker: () -> Unit = { launcher.launch(supportedMimeTypes.toTypedArray()) }
    content(launchPicker, selectedUris)
}
```

### `app\src\main\java\com\example\doc_tools\core\ui\components\layout\AppTopBar.kt`

```kt
package com.example.doc_tools.core.ui.components.layout

import androidx.compose.foundation.layout.padding
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.filled.ArrowBack
import androidx.compose.material.icons.filled.DarkMode
import androidx.compose.material.icons.filled.LightMode
import androidx.compose.material.icons.filled.Settings
import androidx.compose.material3.CenterAlignedTopAppBar
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBarDefaults
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.graphicsLayer
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp

/**
 * A composable function that displays a customizable top app bar.
 *
 * @param title The title text to display in the app bar.
 * @param showBackButton Whether to show the back button. Defaults to `true`.
 * @param showThemeToggle Whether to show the theme toggle button. Defaults to `true`.
 * @param onBackClick A callback function invoked when the back button is clicked. Defaults to an empty lambda.
 * @param isDarkTheme Indicates whether the current theme is dark. Defaults to `false`.
 * @param onThemeToggleClick A callback function invoked when the theme toggle button is clicked. Defaults to an empty lambda.
 * @param enabled Whether the top bar buttons are enabled. When false, buttons are visually dimmed and not interactive. Defaults to `true`.
 */

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun AppTopBar(
    title: String,
    showBackButton: Boolean = true,
    showThemeToggle: Boolean = true,
    onBackClick: () -> Unit = {},
    isDarkTheme: Boolean = false,
    onThemeToggleClick: () -> Unit = {},
    onSettingsClick: (() -> Unit)? = null,
    enabled: Boolean = true
) {
    val themeIcon = if (isDarkTheme) Icons.Default.LightMode else Icons.Default.DarkMode
    val themeDescription = if (isDarkTheme) "Switch to Light Mode" else "Switch to Dark Mode"

    // Apply alpha to disabled buttons
    val disabledAlpha = if (enabled) 1f else 0.5f

    CenterAlignedTopAppBar(
        modifier = Modifier.padding(horizontal = 14.dp),
        colors = TopAppBarDefaults.centerAlignedTopAppBarColors(
            containerColor = Color.Transparent,
            titleContentColor = MaterialTheme.colorScheme.onPrimaryContainer,
            navigationIconContentColor = MaterialTheme.colorScheme.onPrimaryContainer,
            actionIconContentColor = MaterialTheme.colorScheme.onPrimaryContainer,
        ),
        title = {
            Text(
                text = title,
                maxLines = 1,
                overflow = TextOverflow.Ellipsis,
                style = MaterialTheme.typography.titleMedium
            )
        },
        navigationIcon = {
            if (showBackButton) {
                IconButton(
                    onClick = onBackClick,
                    enabled = enabled,
                    modifier = Modifier.graphicsLayer(alpha = disabledAlpha)
                ) {
                    Icon(
                        imageVector = Icons.AutoMirrored.Filled.ArrowBack,
                        contentDescription = "Back"
                    )
                }
            }
        },
        actions = {
            // Settings button
            if (onSettingsClick != null) {
                IconButton(
                    onClick = onSettingsClick,
                    enabled = enabled,
                    modifier = Modifier.graphicsLayer(alpha = disabledAlpha)
                ) {
                    Icon(
                        imageVector = Icons.Default.Settings,
                        contentDescription = "Settings"
                    )
                }
            }
            
            // Theme toggle button
//            if (showThemeToggle) {
//                IconButton(
//                    onClick = onThemeToggleClick,
//                    enabled = enabled,
//                    modifier = Modifier.graphicsLayer(alpha = disabledAlpha)
//                ) {
//                    Icon(
//                        imageVector = themeIcon,
//                        contentDescription = themeDescription
//                    )
//                }
//            }
        }
    )
}
```

### `app\src\main\java\com\example\doc_tools\core\ui\components\layout\BaseToolScreen.kt`

```kt
package com.example.doc_tools.core.ui.components.layout

import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Scaffold
import androidx.compose.material3.SnackbarHost
import androidx.compose.material3.SnackbarHostState
import androidx.compose.material3.SnackbarDuration
import androidx.compose.runtime.Composable
import androidx.compose.runtime.CompositionLocalProvider
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.compositionLocalOf
import androidx.compose.runtime.getValue
import androidx.compose.runtime.remember
import androidx.compose.runtime.rememberCoroutineScope
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.navigation.NavController
import com.example.doc_tools.core.navigation.AppDestinations
import com.example.doc_tools.core.presentation.state.MessageType
import com.example.doc_tools.core.presentation.state.ProcessingStateManager
import com.example.doc_tools.core.presentation.eventbus.UiMessageBus
import kotlinx.coroutines.flow.collectLatest
import kotlinx.coroutines.launch

// Composition local to provide processing state to all children
val LocalProcessingState = compositionLocalOf { false }

/**
 * Base screen layout for all tool screens with simplified layout to prevent measurement issues.
 * This composable provides a consistent structure for screens, including a top app bar,
 * optional loading indicator, and content area with optional scrolling.
 *
 * During processing, all inputs and interactive elements should be disabled.
 *
 * @param title The title to be displayed in the top app bar.
 * @param navController The navigation controller used for back navigation.
 * @param isDarkTheme A boolean indicating whether the dark theme is currently active.
 * @param onThemeToggle A lambda function to be invoked when the theme toggle button is clicked.
 * @param modifier Optional [Modifier] to be applied to the root Scaffold.
 * @param isLoading A boolean indicating whether a loading indicator should be displayed. When true, the content area will show a [CircularProgressIndicator].
 * @param contentScrollable A boolean indicating whether the content area should be vertically scrollable. Defaults to true.
 * @param messageScope An optional string to identify the message scope for displaying Snackbars and processing operations.
 * @param showBackButton A boolean indicating whether the back button should be shown in the top app bar. Defaults to true.
 * @param onProcessCancel A callback that will be invoked when the user cancels the current process.
 * @param content A composable lambda that defines the main content of the screen.
 */

@Composable
fun BaseToolScreen(
    title: String,
    navController: NavController,
    isDarkTheme: Boolean,
    onThemeToggle: () -> Unit,
    modifier: Modifier = Modifier,
    isLoading: Boolean = false,
    contentScrollable: Boolean = true,
    messageScope: String? = null,
    showBackButton: Boolean = true,
    showThemeToggle: Boolean = true,
    onProcessCancel: (() -> Unit)? = null,
    content: @Composable () -> Unit
){
    val snackbarHostState = remember { SnackbarHostState() }
    val coroutineScope = rememberCoroutineScope()
    val currentProcess by ProcessingStateManager.currentProcess.collectAsState()
    val isProcessing by ProcessingStateManager.isProcessing.collectAsState()

    // Collect messages from UiMessageBus
    LaunchedEffect(messageScope) {
        UiMessageBus.messages.collectLatest { messages ->
            val scopedMessages = messages.filter { it.scope == messageScope }
            scopedMessages.forEach { message ->
                when (message.type) {
                    MessageType.SUCCESS -> snackbarHostState.showSnackbar(message = message.text, duration = SnackbarDuration.Short)
                    MessageType.ERROR -> snackbarHostState.showSnackbar(message = message.text, duration = SnackbarDuration.Long)
                    else -> snackbarHostState.showSnackbar(message = message.text, duration = SnackbarDuration.Short)
                }
            }
        }
    }

    // Provide the current processing state to all children
    CompositionLocalProvider(LocalProcessingState provides isProcessing) {
        Scaffold( 
            topBar = {
                AppTopBar(
                    title = title,
                    showBackButton = showBackButton,
                    showThemeToggle = showThemeToggle,
                    onBackClick = {
                        // Only allow navigation if no process is running
                        if (!isProcessing) {
                            navController.popBackStack()
                        } else {
                            // Show message that operation is in progress
                            coroutineScope.launch {
                                snackbarHostState.showSnackbar(
                                    message = "Please cancel the current operation before navigating away",
                                    duration = SnackbarDuration.Short
                                )
                            }
                        }
                    },
                    isDarkTheme = isDarkTheme,
                    onThemeToggleClick = onThemeToggle,
                    onSettingsClick = {
                        // Only navigate to settings if no process is running
                        if (!isProcessing) {
                            // Don't navigate if we're already on the settings screen
                            if (title != "Settings") {
                                navController.navigate(AppDestinations.SETTINGS)
                            }
                        } else {
                            // Show message that operation is in progress
                            coroutineScope.launch {
                                snackbarHostState.showSnackbar(
                                    message = "Please cancel the current operation before navigating away",
                                    duration = SnackbarDuration.Short
                                )
                            }
                        }
                    },
                    enabled = !isProcessing // Disable buttons during processing
                )
            },  
            snackbarHost = { SnackbarHost(hostState = snackbarHostState) }, 
            modifier = modifier
        ) { innerPadding -> 
            // Use a simple Box for content area
            Box(modifier = Modifier.fillMaxSize().padding(innerPadding)) {
                if (isLoading) { // Center loading indicator
                    CircularProgressIndicator(
                        modifier = Modifier.size(48.dp).align(Alignment.Center), 
                        color = MaterialTheme.colorScheme.primary, 
                        strokeWidth = 4.dp
                    )
                } else { // Content area with fixed size and optional scroll
                    Box(modifier = Modifier.fillMaxSize().padding(horizontal = 8.dp)){
                        if (contentScrollable) { // Apply scrolling to content
                            Box(modifier = Modifier.fillMaxSize().verticalScroll(rememberScrollState())){ 
                                content() 
                            }
                        } else { // No scrolling applied here
                            content()
                        }
                    }
                }
            }
        }
    }
}
```

### `app\src\main\java\com\example\doc_tools\core\ui\components\overlay\ProcessingAwareComponent.kt`

```kt
package com.example.doc_tools.core.ui.components.overlay

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.rememberUpdatedState
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.alpha
import androidx.compose.ui.unit.dp
import com.example.doc_tools.core.ui.components.layout.LocalProcessingState

/**
 * A composable that makes its children aware of the current processing state.
 * 
 * This wrapper automatically disables its children and applies a reduced alpha
 * when processing is active, making it easy to disable entire sections of UI
 * during background operations.
 * 
 * @param content The content to be wrapped and made processing-aware
 * @param modifier Modifier to be applied to the container
 * @param forceEnabled If true, ignores the global processing state and always enables the component
 * @param disabledAlpha The alpha value to apply when disabled (defaults to 0.6f)
 */
@Composable
fun ProcessingAware(
    modifier: Modifier = Modifier,
    forceEnabled: Boolean = false,
    disabledAlpha: Float = 0.6f,
    content: @Composable (isEnabled: Boolean) -> Unit
) {
    // Get the current processing state from composition local
    val isProcessing = LocalProcessingState.current
    
    // Calculate if this component should be enabled
    val isEnabled by rememberUpdatedState(!isProcessing || forceEnabled)
    
    // Apply alpha based on enabled state
    val contentAlpha = if (isEnabled) 1f else disabledAlpha
    
    Column(modifier = modifier.alpha(contentAlpha), verticalArrangement = Arrangement.spacedBy(16.dp)) {
            // Pass the enabled state to the content
            content(isEnabled)
    }
}

```

### `app\src\main\java\com\example\doc_tools\core\ui\components\tool_layout\HeaderSection.kt`

```kt
package com.example.doc_tools.core.ui.components.tool_layout

import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

@Composable
fun HeaderSection(
    title: String,
    icon: ImageVector? = null,
    subtitle: String? = null,
    modifier: Modifier = Modifier,
    iconTint: Color = MaterialTheme.colorScheme.primary,
    textColor: Color = MaterialTheme.colorScheme.primary,
) {
    Row(verticalAlignment = Alignment.CenterVertically, modifier = modifier) {
        icon?.let {
            Icon(imageVector = it, contentDescription = null, tint = iconTint, modifier = Modifier.size(32.dp))
            Spacer(Modifier.width(8.dp))
        }
        Column {
            Text(text = title, style = MaterialTheme.typography.titleMedium, color = textColor)
            subtitle?.let {
                Spacer(Modifier.height(2.dp))
                Text(text = it, style = MaterialTheme.typography.bodySmall)
            }
        }
    }
}```

### `app\src\main\java\com\example\doc_tools\core\ui\theme\Color.kt`

```kt
package com.example.doc_tools.core.ui.theme

import androidx.compose.ui.graphics.Color

// ─── Light Theme Colors (Tailwind-Inspired) ─────────────────────────────────────
val LightPrimary = Color(0xFF38BDF8) // sky-500
val LightOnPrimary = Color(0xFF000000)
val LightPrimaryContainer = Color(0xFFBAE6FD) // sky-200
val LightOnPrimaryContainer = Color(0xFF083344)

val LightSecondary = Color(0xFFD1D5DB) // emerald-500
val LightOnSecondary = Color(0xFF374151)
val LightSecondaryContainer = Color(0xFFD1FAE5) // emerald-100
val LightOnSecondaryContainer = Color(0xFF064E3B)

val LightTertiary = Color(0xFF6366F1) // indigo-500
val LightOnTertiary = Color(0xFFFFFFFF)
val LightTertiaryContainer = Color(0xFFE0E7FF) // indigo-100
val LightOnTertiaryContainer = Color(0xFF312E81)

val LightError = Color(0xFFEF4444) // rose-500
val LightErrorContainer = Color(0xFFFECACA) // rose-200
val LightOnError = Color(0xFFFFFFFF)
val LightOnErrorContainer = Color(0xFF7F1D1D)

val LightBackground = Color(0xFFF3F4F6) // zinc-50
val LightOnBackground = Color(0xFF1E293B) // slate-900

val LightSurface = Color(0xFFFFFFFF) // pure white
val LightOnSurface = Color(0xFF4B5563) // slate-800

val LightSurfaceVariant = Color(0xFFE2E8F0) // slate-200
val LightOnSurfaceVariant = Color(0xFF475569) // slate-600

val LightOutline = Color(0xFF64748B) // slate-400
val LightOutlineVariant = Color(0xFFE2E8F0) // slate-300

val LightInverseOnSurface = Color(0xFFEFF6FF) // slate-100
val LightInverseSurface = Color(0xFF1E3A8A) // blue-900
val LightInversePrimary = Color(0xFF0284C7) // sky-600
val LightSurfaceTint = LightPrimary
val LightScrim = Color(0xFF000000)


// ─── Dark Theme Colors (Tailwind-Inspired) ──────────────────────────────────────
val DarkPrimary = Color(0xFF0F172A) // slate500
val DarkOnPrimary = Color(0xFFFFFFFF)
val DarkPrimaryContainer = Color(0xFF020617) // sky950
val DarkOnPrimaryContainer = Color(0xFFBAE6FD)

val DarkSecondary = Color(0xFF374151) // emerald-400
val DarkOnSecondary = Color(0xFFD1D5DB)
val DarkSecondaryContainer = Color(0xFF065F46) // emerald-700
val DarkOnSecondaryContainer = Color(0xFFD1FAE5)

val DarkTertiary = Color(0xFF8688AA) // indigo-400
val DarkOnTertiary = Color(0xFF1E1B4B)
val DarkTertiaryContainer = Color(0xFFFFFFFF) // indigo-700
val DarkOnTertiaryContainer = Color(0xFFFFFFFF)

val DarkError = Color(0xFFF87171) // rose-400
val DarkErrorContainer = Color(0xFF7F1D1D)
val DarkOnError = Color(0xFF1F0404)
val DarkOnErrorContainer = Color(0xFFFECACA)

val DarkBackground = Color(0xFF0F172A) // slate-900
val DarkOnBackground = Color(0xFFE2E8F0) // slate-200

val DarkSurface = Color(0xFF1E293B) // slate-800
val DarkOnSurface = Color(0xFF0EA5E9) // slate-200

val DarkSurfaceVariant = Color(0xFF334155) // slate-700
val DarkOnSurfaceVariant = Color(0xFFCBD5E1) // slate-300

val DarkOutline = Color(0xFF0EA5E9) // slate-500
val DarkOutlineVariant = Color(0xFF475569) // slate-600

val DarkInverseOnSurface = Color(0xFF004CC6)
val DarkInverseSurface = Color(0xFFBFDBFE) // blue-200
val DarkInversePrimary = Color(0xFF0EA5E9)
val DarkSurfaceTint = DarkPrimary
val DarkScrim = Color(0xFF000000)


// ─── PDF Section Accent ─────────────────────────────────────────────────────────
val pdfAccent = Color(0xFF000000) // purple-600
val pdfAccentContainer = Color(0xFFEDE9FE) // purple-100
val pdfAccentDark = Color(0xFFFFFFFF) // purple-200
val pdfAccentContainerDark = Color(0xFF4C1D95) // purple-900

// ─── Image Section Accent ───────────────────────────────────────────────────────
val imageAccent = Color(0xFF000000) // green-500
val imageAccentContainer = Color(0xFFD9F99D) // green-200
val imageAccentDark = Color(0xFFFFFFFF) // green-300
val imageAccentContainerDark = Color(0xFF14532D) // green-900

// ─── Tailwind Color Palette ───────────────────────────────────────────────────────
// Slate
val Slate50 = Color(0xFFF8FAFC)
val Slate100 = Color(0xFFF1F5F9)
val Slate200 = Color(0xFFE2E8F0)
val Slate300 = Color(0xFFCBD5E1)
val Slate400 = Color(0xFF94A3B8)
val Slate500 = Color(0xFF64748B)
val Slate600 = Color(0xFF475569)
val Slate700 = Color(0xFF334155)
val Slate800 = Color(0xFF1E293B)
val Slate900 = Color(0xFF0F172A)
val Slate950 = Color(0xFF020617)

// Gray
val Gray50 = Color(0xFFF9FAFB)
val Gray100 = Color(0xFFF3F4F6)
val Gray200 = Color(0xFFE5E7EB)
val Gray300 = Color(0xFFD1D5DB)
val Gray400 = Color(0xFF9CA3AF)
val Gray500 = Color(0xFF6B7280)
val Gray600 = Color(0xFF4B5563)
val Gray700 = Color(0xFF374151)
val Gray800 = Color(0xFF1F2937)
val Gray900 = Color(0xFF111827)
val Gray950 = Color(0xFF030712)

// Zinc
val Zinc50 = Color(0xFFFAFAFA)
val Zinc100 = Color(0xFFF4F4F5)
val Zinc200 = Color(0xFFE4E4E7)
val Zinc300 = Color(0xFFD4D4D8)
val Zinc400 = Color(0xFFA1A1AA)
val Zinc500 = Color(0xFF71717A)
val Zinc600 = Color(0xFF52525B)
val Zinc700 = Color(0xFF3F3F46)
val Zinc800 = Color(0xFF27272A)
val Zinc900 = Color(0xFF18181B)
val Zinc950 = Color(0xFF09090B)

// Neutral
val Neutral50 = Color(0xFFFAFAFA)
val Neutral100 = Color(0xFFF5F5F5)
val Neutral200 = Color(0xFFE5E5E5)
val Neutral300 = Color(0xFFD4D4D4)
val Neutral400 = Color(0xFFA3A3A3)
val Neutral500 = Color(0xFF737373)
val Neutral600 = Color(0xFF525252)
val Neutral700 = Color(0xFF404040)
val Neutral800 = Color(0xFF262626)
val Neutral900 = Color(0xFF171717)
val Neutral950 = Color(0xFF0A0A0A)

// Stone
val Stone50 = Color(0xFFFAFAF9)
val Stone100 = Color(0xFFF5F5F4)
val Stone200 = Color(0xFFE7E5E4)
val Stone300 = Color(0xFFD6D3D1)
val Stone400 = Color(0xFFA8A29E)
val Stone500 = Color(0xFF78716C)
val Stone600 = Color(0xFF57534E)
val Stone700 = Color(0xFF44403C)
val Stone800 = Color(0xFF292524)
val Stone900 = Color(0xFF1C1917)
val Stone950 = Color(0xFF0C0A09)

// Red
val Red50 = Color(0xFFFEF2F2)
val Red100 = Color(0xFFFEE2E2)
val Red200 = Color(0xFFFECACA)
val Red300 = Color(0xFFFCA5A5)
val Red400 = Color(0xFFF87171)
val Red500 = Color(0xFFEF4444)
val Red600 = Color(0xFFDC2626)
val Red700 = Color(0xFFB91C1C)
val Red800 = Color(0xFF991B1B)
val Red900 = Color(0xFF7F1D1D)
val Red950 = Color(0xFF450A0A)

// Orange
val Orange50 = Color(0xFFFFF7ED)
val Orange100 = Color(0xFFFFEDD5)
val Orange200 = Color(0xFFFED7AA)
val Orange300 = Color(0xFFFDBA74)
val Orange400 = Color(0xFFFB923C)
val Orange500 = Color(0xFFF97316)
val Orange600 = Color(0xFFEA580C)
val Orange700 = Color(0xFFC2410C)
val Orange800 = Color(0xFF9A3412)
val Orange900 = Color(0xFF7C2D12)
val Orange950 = Color(0xFF431407)

// Amber
val Amber50 = Color(0xFFFFFBEB)
val Amber100 = Color(0xFFFEF3C7)
val Amber200 = Color(0xFFFDE68A)
val Amber300 = Color(0xFFFCD34D)
val Amber400 = Color(0xFFFBBF24)
val Amber500 = Color(0xFFF59E0B)
val Amber600 = Color(0xFFD97706)
val Amber700 = Color(0xFFB45309)
val Amber800 = Color(0xFF92400E)
val Amber900 = Color(0xFF78350F)
val Amber950 = Color(0xFF451A03)

// Yellow
val Yellow50 = Color(0xFFFEFCE8)
val Yellow100 = Color(0xFFFEF9C3)
val Yellow200 = Color(0xFFFEF08A)
val Yellow300 = Color(0xFFFDE047)
val Yellow400 = Color(0xFFFACC15)
val Yellow500 = Color(0xFFEAB308)
val Yellow600 = Color(0xFFCA8A04)
val Yellow700 = Color(0xFFA16207)
val Yellow800 = Color(0xFF854D0E)
val Yellow900 = Color(0xFF713F12)
val Yellow950 = Color(0xFF422006)

// Lime
val Lime50 = Color(0xFFF7FEE7)
val Lime100 = Color(0xFFECFCCB)
val Lime200 = Color(0xFFD9F99D)
val Lime300 = Color(0xFFBEF264)
val Lime400 = Color(0xFFA3E635)
val Lime500 = Color(0xFF84CC16)
val Lime600 = Color(0xFF65A30D)
val Lime700 = Color(0xFF4D7C0F)
val Lime800 = Color(0xFF3F6212)
val Lime900 = Color(0xFF365314)
val Lime950 = Color(0xFF1A2E05)

// Green
val Green50 = Color(0xFFF0FDF4)
val Green100 = Color(0xFFDCFCE7)
val Green200 = Color(0xFFBBF7D0)
val Green300 = Color(0xFF86EFAC)
val Green400 = Color(0xFF4ADE80)
val Green500 = Color(0xFF22C55E)
val Green600 = Color(0xFF16A34A)
val Green700 = Color(0xFF15803D)
val Green800 = Color(0xFF166534)
val Green900 = Color(0xFF14532D)
val Green950 = Color(0xFF052E16)

// Emerald
val Emerald50 = Color(0xFFECFDF5)
val Emerald100 = Color(0xFFD1FAE5)
val Emerald200 = Color(0xFFA7F3D0)
val Emerald300 = Color(0xFF6EE7B7)
val Emerald400 = Color(0xFF34D399)
val Emerald500 = Color(0xFF10B981)
val Emerald600 = Color(0xFF059669)
val Emerald700 = Color(0xFF047857)
val Emerald800 = Color(0xFF065F46)
val Emerald900 = Color(0xFF064E3B)
val Emerald950 = Color(0xFF022C22)

// Teal
val Teal50 = Color(0xFFF0FDFA)
val Teal100 = Color(0xFFCCFBF1)
val Teal200 = Color(0xFF99F6E4)
val Teal300 = Color(0xFF5EEAD4)
val Teal400 = Color(0xFF2DD4BF)
val Teal500 = Color(0xFF14B8A6)
val Teal600 = Color(0xFF0D9488)
val Teal700 = Color(0xFF0F766E)
val Teal800 = Color(0xFF115E59)
val Teal900 = Color(0xFF134E4A)
val Teal950 = Color(0xFF042F2E)

// Cyan
val Cyan50 = Color(0xFFECFEFF)
val Cyan100 = Color(0xFFCFFAFE)
val Cyan200 = Color(0xFFA5F3FC)
val Cyan300 = Color(0xFF67E8F9)
val Cyan400 = Color(0xFF22D3EE)
val Cyan500 = Color(0xFF06B6D4)
val Cyan600 = Color(0xFF0891B2)
val Cyan700 = Color(0xFF0E7490)
val Cyan800 = Color(0xFF155E75)
val Cyan900 = Color(0xFF164E63)
val Cyan950 = Color(0xFF083344)

// Sky
val Sky50 = Color(0xFFF0F9FF)
val Sky100 = Color(0xFFE0F2FE)
val Sky200 = Color(0xFFBAE6FD)
val Sky300 = Color(0xFF7DD3FC)
val Sky400 = Color(0xFF38BDF8)
val Sky500 = Color(0xFF0EA5E9)
val Sky600 = Color(0xFF0284C7)
val Sky700 = Color(0xFF0369A1)
val Sky800 = Color(0xFF075985)
val Sky900 = Color(0xFF0C4A6E)
val Sky950 = Color(0xFF082F49)

// Blue
val Blue50 = Color(0xFFEFF6FF)
val Blue100 = Color(0xFFDBEAFE)
val Blue200 = Color(0xFFBFDBFE)
val Blue300 = Color(0xFF93C5FD)
val Blue400 = Color(0xFF60A5FA)
val Blue500 = Color(0xFF3B82F6)
val Blue600 = Color(0xFF2563EB)
val Blue700 = Color(0xFF1D4ED8)
val Blue800 = Color(0xFF1E40AF)
val Blue900 = Color(0xFF1E3A8A)
val Blue950 = Color(0xFF172554)

// Indigo
val Indigo50 = Color(0xFFEEF2FF)
val Indigo100 = Color(0xFFE0E7FF)
val Indigo200 = Color(0xFFC7D2FE)
val Indigo300 = Color(0xFFA5B4FC)
val Indigo400 = Color(0xFF818CF8)
val Indigo500 = Color(0xFF6366F1)
val Indigo600 = Color(0xFF4F46E5)
val Indigo700 = Color(0xFF4338CA)
val Indigo800 = Color(0xFF3730A3)
val Indigo900 = Color(0xFF312E81)
val Indigo950 = Color(0xFF1E1B4B)

// Violet
val Violet50 = Color(0xFFF5F3FF)
val Violet100 = Color(0xFFEDE9FE)
val Violet200 = Color(0xFFDDD6FE)
val Violet300 = Color(0xFFC4B5FD)
val Violet400 = Color(0xFFA78BFA)
val Violet500 = Color(0xFF8B5CF6)
val Violet600 = Color(0xFF7C3AED)
val Violet700 = Color(0xFF6D28D9)
val Violet800 = Color(0xFF5B21B6)
val Violet900 = Color(0xFF4C1D95)
val Violet950 = Color(0xFF2E1065)

// Purple
val Purple50 = Color(0xFFFAF5FF)
val Purple100 = Color(0xFFF3E8FF)
val Purple200 = Color(0xFFE9D5FF)
val Purple300 = Color(0xFFD8B4FE)
val Purple400 = Color(0xFFC084FC)
val Purple500 = Color(0xFFA855F7)
val Purple600 = Color(0xFF9333EA)
val Purple700 = Color(0xFF7E22CE)
val Purple800 = Color(0xFF6B21A8)
val Purple900 = Color(0xFF581C87)
val Purple950 = Color(0xFF3B0764)

// Fuchsia
val Fuchsia50 = Color(0xFFFDF4FF)
val Fuchsia100 = Color(0xFFFAE8FF)
val Fuchsia200 = Color(0xFFF5D0FE)
val Fuchsia300 = Color(0xFFF0ABFC)
val Fuchsia400 = Color(0xFFE879F9)
val Fuchsia500 = Color(0xFFD946EF)
val Fuchsia600 = Color(0xFFC026D3)
val Fuchsia700 = Color(0xFFA21CAF)
val Fuchsia800 = Color(0xFF86198F)
val Fuchsia900 = Color(0xFF701A75)
val Fuchsia950 = Color(0xFF4A044E)

// Pink
val Pink50 = Color(0xFFFDF2F8)
val Pink100 = Color(0xFFFCE7F3)
val Pink200 = Color(0xFFFBCFE8)
val Pink300 = Color(0xFFF9A8D4)
val Pink400 = Color(0xFFF472B6)
val Pink500 = Color(0xFFEC4899)
val Pink600 = Color(0xFFDB2777)
val Pink700 = Color(0xFFBE185D)
val Pink800 = Color(0xFF9D174D)
val Pink900 = Color(0xFF831843)
val Pink950 = Color(0xFF500724)

// Rose
val Rose50 = Color(0xFFFFF1F2)
val Rose100 = Color(0xFFFFE4E6)
val Rose200 = Color(0xFFFECDD3)
val Rose300 = Color(0xFFFDA4AF)
val Rose400 = Color(0xFFFB7185)
val Rose500 = Color(0xFFF43F5E)
val Rose600 = Color(0xFFE11D48)
val Rose700 = Color(0xFFBE123C)
val Rose800 = Color(0xFF9F1239)
val Rose900 = Color(0xFF881337)
val Rose950 = Color(0xFF4C0519)

// Base colors
val Black = Color(0xFF000000)
val White = Color(0xFFFFFFFF)
```

### `app\src\main\java\com\example\doc_tools\core\ui\theme\Shape.kt`

```kt
package com.example.doc_tools.core.ui.theme

import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Shapes
import androidx.compose.ui.unit.dp

/**
 * Defines the shapes used throughout the application.
 *
 * This object provides a set of predefined `RoundedCornerShape` instances
 * for different UI elements, promoting a consistent visual style.
 * The shapes are designed to offer a sharper and sleeker appearance.
 *
 * - `small`: Used for smaller elements or subtle corner rounding.
 * - `medium`: A common shape for elements like buttons and cards.
 * - `large`: Suitable for larger components or when a more pronounced rounded effect is desired.
 * - `extraSmall`: For very fine details where minimal rounding is needed.
 * - `extraLarge`: For substantial elements that benefit from a slightly more generous rounding.
 */

val Shapes = Shapes(
    small = RoundedCornerShape(4.dp),    // Sharper small corners
    medium = RoundedCornerShape(8.dp),   // Sharper medium corners (Buttons, Cards)
    large = RoundedCornerShape(16.dp),     // Sharper large corners
    extraSmall = RoundedCornerShape(2.dp), // Even sharper for subtle details
    extraLarge = RoundedCornerShape(32.dp)  // Slightly more rounded for larger elements
) 
```

### `app\src\main\java\com\example\doc_tools\core\ui\theme\Theme.kt`

```kt
package com.example.doc_tools.core.ui.theme

import android.app.Activity
import android.os.Build
import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.lightColorScheme
import androidx.compose.material3.darkColorScheme
import androidx.compose.material3.dynamicDarkColorScheme
import androidx.compose.material3.dynamicLightColorScheme
import androidx.compose.material3.ColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.runtime.SideEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.platform.LocalView
import androidx.core.view.WindowCompat

/**
 * Represents the available application themes.
 * Each enum constant corresponds to a distinct visual style for the app,
 * primarily based on Tailwind CSS color palettes.
 * Theme enum to allow easy switching between different Tailwind-based themes
 */
enum class AppTheme {
    DEFAULT,  // The original theme
    BLUE,     // Blue-based theme
    GREEN,    // Green-based theme
    PURPLE,   // Purple-based theme
    AMBER     // Amber-based theme
}

// Global theme selection (can be changed from settings)
var currentTheme by mutableStateOf(AppTheme.DEFAULT)

// Original Light Color Scheme
private val LightColorSchemeDefault = lightColorScheme(

    // TopAppBar background color
    primary = Slate900, // Dark for contrast
    onPrimary = Slate100, // Light text/icons on dark bar
    primaryContainer = Slate100, // Container variant, e.g., for elevated surfaces
    onPrimaryContainer = Slate900, // Text/icons on container

    // Interactive controls (like switches, checkboxes)
    secondary = Slate400, // Main accent color
    onSecondary = Slate600, // Text/icons on accent
    secondaryContainer = Slate400.copy(alpha = 0.2f), // Background for secondary elements
    onSecondaryContainer = Slate800, // Text on secondary background

    // Input fields and similar components
    tertiary = Slate600, // Used for input highlights, cursor, etc.
    onTertiary = Slate900,
    tertiaryContainer = Slate600.copy(alpha = 0.2f), // Background for input fields
    onTertiaryContainer = Slate900,

    // Backgrounds
    background = Slate100, // Page background
    onBackground = Slate900, // Default text

    // Cards, menus, and sheets
    surface = White, // Default surface color
    onSurface = Slate600, // Text/icons on surfaces

    surfaceVariant = Slate200, // For lower elevation components
    onSurfaceVariant = Slate900,

    // Inverse surface (used in bottom sheets, modals)
    inverseSurface = Slate800,
    inverseOnSurface = Slate100,

    // Error states
    error = Red600, // Error text/icons
    errorContainer = Red100, // Background for error messages
    onError = White,
    onErrorContainer = Red900,

    // Outlines for borders, dividers
    outline = Gray300,
    outlineVariant = Gray200,

    // Inverse primary (used in contrasting text or icons)
    inversePrimary = Indigo200,

    surfaceBright = White,
    surfaceDim = Slate200,

    // Surface tint (can affect elevation overlay)
    surfaceTint = Color.Transparent, // Optional: set to transparent to disable overlay

    // Scrim color for modals, drawers
    scrim = Color(0x80000000) // Semi-transparent black
)

// Original Dark Color Scheme
private val DarkColorSchemeDefault = darkColorScheme(

    // TopAppBar and primary UI elements
    primary = Cyan500, // Prominent top bar or FAB
    onPrimary = Cyan50, // Text/icons on primary
    primaryContainer = Cyan950.copy(alpha = 0.5f), // Container for elevated primary elements
    onPrimaryContainer = Cyan400, // Text/icons on primary container

    // Secondary controls (checkboxes, switches, etc.)
    secondary = Slate400, // Accent for toggles and secondary buttons
    onSecondary = Slate200, // Text/icons on secondary color
    secondaryContainer = Slate400.copy(alpha = 0.2f), // Background of secondary UI
    onSecondaryContainer = Slate200, // Text/icons on container

    // Tertiary use (text fields, highlights, etc.)
    tertiary = Cyan500, // For active input states
    onTertiary = Cyan400,
    tertiaryContainer = Cyan900.copy(alpha = 0.4f), // Input container or chips
    onTertiaryContainer = Cyan400,

    // Error colors
    error = Red400,
    onError = Slate950,
    errorContainer = Red950,
    onErrorContainer = Red100,

    // Background and general surface
    background = Gray900, // Main background
    onBackground = Slate100, // Primary text on background

    surface = Slate950, // Cards, sheets, surfaces
    onSurface = Slate400, // Text/icons on surfaces

    surfaceVariant = Slate900.copy(alpha = 0.9f), // For lower elevation components
    onSurfaceVariant = Slate200,

    // Dividers, outlines
    outline = Slate600,
    outlineVariant = Slate100,

    // Bottom sheet/modal contrast
    inverseSurface = Slate100, // Used for inverse contexts (e.g., sheets)
    inverseOnSurface = Slate900,

    // Slightly different primary for inverse context (like floating buttons)
    inversePrimary = Sky300,

    // Optional: no surface tint for clarity
    surfaceTint = Color.Transparent,

    // Scrim: for backdrops (e.g., dialogs, drawers)
    scrim = Color(0x80FFFFFF) // Semi-transparent white for dark mode
)

// Blue-based Light Theme (using Tailwind Blue palette)7
private val LightColorSchemeBlue = lightColorScheme(
    primary = Blue500,
    onPrimary = White,
    primaryContainer = Blue100,
    onPrimaryContainer = Blue900,
    secondary = Teal500,
    onSecondary = White,
    secondaryContainer = Teal100,
    onSecondaryContainer = Teal900,
    tertiary = Indigo500,
    onTertiary = White,
    tertiaryContainer = Indigo100,
    onTertiaryContainer = Indigo900,
    error = Red500,
    errorContainer = Red100,
    onError = White,
    onErrorContainer = Red900,
    background = Gray50,
    onBackground = Gray900,
    surface = White,
    onSurface = Gray800,
    surfaceVariant = Gray200,
    onSurfaceVariant = Gray600,
    outline = Gray400,
    inverseOnSurface = Gray100,
    inverseSurface = Blue900,
    inversePrimary = Blue300,
    surfaceTint = Blue500,
    outlineVariant = Gray300,
    scrim = Black,
)

// Blue-based Dark Theme (using Tailwind Blue palette)
private val DarkColorSchemeBlue = darkColorScheme(
    primary = Blue400,
    onPrimary = Blue950,
    primaryContainer = Blue800,
    onPrimaryContainer = Blue100,
    secondary = Teal400,
    onSecondary = Teal950,
    secondaryContainer = Teal800,
    onSecondaryContainer = Teal100,
    tertiary = Indigo400,
    onTertiary = Indigo950,
    tertiaryContainer = Indigo800,
    onTertiaryContainer = Indigo100,
    error = Red400,
    errorContainer = Red900,
    onError = Red950,
    onErrorContainer = Red100,
    background = Gray900,
    onBackground = Gray100,
    surface = Gray800,
    onSurface = Gray200,
    surfaceVariant = Gray700,
    onSurfaceVariant = Gray300,
    outline = Gray500,
    inverseOnSurface = Gray800,
    inverseSurface = Blue200,
    inversePrimary = Blue500,
    surfaceTint = Blue400,
    outlineVariant = Gray600,
    scrim = Black,
)

// Green-based Light Theme (using Tailwind Green palette)
private val LightColorSchemeGreen = lightColorScheme(
    primary = Green500,
    onPrimary = White,
    primaryContainer = Green100,
    onPrimaryContainer = Green900,
    secondary = Cyan500,
    onSecondary = White,
    secondaryContainer = Cyan100,
    onSecondaryContainer = Cyan900,
    tertiary = Emerald500,
    onTertiary = White,
    tertiaryContainer = Emerald100,
    onTertiaryContainer = Emerald900,
    error = Red500,
    errorContainer = Red100,
    onError = White,
    onErrorContainer = Red900,
    background = Gray50,
    onBackground = Gray900,
    surface = White,
    onSurface = Gray800,
    surfaceVariant = Gray200,
    onSurfaceVariant = Gray600,
    outline = Gray400,
    inverseOnSurface = Gray100,
    inverseSurface = Green900,
    inversePrimary = Green300,
    surfaceTint = Green500,
    outlineVariant = Gray300,
    scrim = Black,
)

// Green-based Dark Theme (using Tailwind Green palette)
private val DarkColorSchemeGreen = darkColorScheme(
    primary = Green400,
    onPrimary = Green950,
    primaryContainer = Green800,
    onPrimaryContainer = Green100,
    secondary = Cyan400,
    onSecondary = Cyan950,
    secondaryContainer = Cyan800,
    onSecondaryContainer = Cyan100,
    tertiary = Emerald400,
    onTertiary = Emerald950,
    tertiaryContainer = Emerald800,
    onTertiaryContainer = Emerald100,
    error = Red400,
    errorContainer = Red900,
    onError = Red950,
    onErrorContainer = Red100,
    background = Gray900,
    onBackground = Gray100,
    surface = Gray800,
    onSurface = Gray200,
    surfaceVariant = Gray700,
    onSurfaceVariant = Gray300,
    outline = Gray500,
    inverseOnSurface = Gray800,
    inverseSurface = Green200,
    inversePrimary = Green500,
    surfaceTint = Green400,
    outlineVariant = Gray600,
    scrim = Black,
)

// Purple-based Light Theme (using Tailwind Purple palette)
private val LightColorSchemePurple = lightColorScheme(
    primary = Purple500,
    onPrimary = White,
    primaryContainer = Purple100,
    onPrimaryContainer = Purple900,
    secondary = Violet500,
    onSecondary = White,
    secondaryContainer = Violet100,
    onSecondaryContainer = Violet900,
    tertiary = Fuchsia500,
    onTertiary = White,
    tertiaryContainer = Fuchsia100,
    onTertiaryContainer = Fuchsia900,
    error = Red500,
    errorContainer = Red100,
    onError = White,
    onErrorContainer = Red900,
    background = Gray50,
    onBackground = Gray900,
    surface = White,
    onSurface = Gray800,
    surfaceVariant = Gray200,
    onSurfaceVariant = Gray600,
    outline = Gray400,
    inverseOnSurface = Gray100,
    inverseSurface = Purple900,
    inversePrimary = Purple300,
    surfaceTint = Purple500,
    outlineVariant = Gray300,
    scrim = Black,
)

// Purple-based Dark Theme (using Tailwind Purple palette)
private val DarkColorSchemePurple = darkColorScheme(
    primary = Purple400,
    onPrimary = Purple950,
    primaryContainer = Purple800,
    onPrimaryContainer = Purple100,
    secondary = Violet400,
    onSecondary = Violet950,
    secondaryContainer = Violet800,
    onSecondaryContainer = Violet100,
    tertiary = Fuchsia400,
    onTertiary = Fuchsia950,
    tertiaryContainer = Fuchsia800,
    onTertiaryContainer = Fuchsia100,
    error = Red400,
    errorContainer = Red900,
    onError = Red950,
    onErrorContainer = Red100,
    background = Gray900,
    onBackground = Gray100,
    surface = Gray800,
    onSurface = Gray200,
    surfaceVariant = Gray700,
    onSurfaceVariant = Gray300,
    outline = Gray500,
    inverseOnSurface = Gray800,
    inverseSurface = Purple200,
    inversePrimary = Purple500,
    surfaceTint = Purple400,
    outlineVariant = Gray600,
    scrim = Black,
)

// Amber-based Light Theme (using Tailwind Amber palette)
private val LightColorSchemeAmber = lightColorScheme(
    primary = Amber500,
    onPrimary = White,
    primaryContainer = Amber100,
    onPrimaryContainer = Amber900,
    secondary = Orange500,
    onSecondary = White,
    secondaryContainer = Orange100,
    onSecondaryContainer = Orange900,
    tertiary = Yellow500,
    onTertiary = White,
    tertiaryContainer = Yellow100,
    onTertiaryContainer = Yellow900,
    error = Red500,
    errorContainer = Red100,
    onError = White,
    onErrorContainer = Red900,
    background = Gray50,
    onBackground = Gray900,
    surface = White,
    onSurface = Gray800,
    surfaceVariant = Gray200,
    onSurfaceVariant = Gray600,
    outline = Gray400,
    inverseOnSurface = Gray100,
    inverseSurface = Amber900,
    inversePrimary = Amber300,
    surfaceTint = Amber500,
    outlineVariant = Gray300,
    scrim = Black,
)

// Amber-based Dark Theme (using Tailwind Amber palette)
private val DarkColorSchemeAmber = darkColorScheme(
    primary = Amber400,
    onPrimary = Amber950,
    primaryContainer = Amber800,
    onPrimaryContainer = Amber100,
    secondary = Orange400,
    onSecondary = Orange950,
    secondaryContainer = Orange800,
    onSecondaryContainer = Orange100,
    tertiary = Yellow400,
    onTertiary = Yellow950,
    tertiaryContainer = Yellow800,
    onTertiaryContainer = Yellow100,
    error = Red400,
    errorContainer = Red900,
    onError = Red950,
    onErrorContainer = Red100,
    background = Gray900,
    onBackground = Gray100,
    surface = Gray800,
    onSurface = Gray200,
    surfaceVariant = Gray700,
    onSurfaceVariant = Gray300,
    outline = Gray500,
    inverseOnSurface = Gray800,
    inverseSurface = Amber200,
    inversePrimary = Amber500,
    surfaceTint = Amber400,
    outlineVariant = Gray600,
    scrim = Black,
)

// Function to get the current theme color scheme based on theme selection
private fun getColorScheme(darkTheme: Boolean, theme: AppTheme): ColorScheme {
    val baseScheme = when (theme) {
        AppTheme.DEFAULT -> if (darkTheme) DarkColorSchemeDefault else LightColorSchemeDefault
        AppTheme.BLUE -> if (darkTheme) DarkColorSchemeBlue else LightColorSchemeBlue
        AppTheme.GREEN -> if (darkTheme) DarkColorSchemeGreen else LightColorSchemeGreen
        AppTheme.PURPLE -> if (darkTheme) DarkColorSchemePurple else LightColorSchemePurple
        AppTheme.AMBER -> if (darkTheme) DarkColorSchemeAmber else LightColorSchemeAmber
    }
    
    // This ensures that even if other themes don't have differentiated colors,
    // they will still use the proper separation of UI elements
    return baseScheme
}

@Composable
fun Pdf_img_tools_appTheme(
    darkTheme: Boolean = isSystemInDarkTheme(),
    // Dynamic color is available on Android 12+
    dynamicColor: Boolean = false,
    theme: AppTheme = currentTheme,
    content: @Composable () -> Unit
) {
    val colorScheme = when {
        dynamicColor && Build.VERSION.SDK_INT >= Build.VERSION_CODES.S -> {
            val context = LocalContext.current
            if (darkTheme) dynamicDarkColorScheme(context) else dynamicLightColorScheme(context)
        }
        else -> getColorScheme(darkTheme, theme)
    }
    
    val view = LocalView.current
    if (!view.isInEditMode) {
        SideEffect {
            val window = (view.context as Activity).window
            WindowCompat.getInsetsController(window, view).isAppearanceLightStatusBars = !darkTheme
            WindowCompat.getInsetsController(window, view).isAppearanceLightNavigationBars = !darkTheme
        }
    }

    MaterialTheme(
        colorScheme = colorScheme,
        typography = Typography,
        shapes = Shapes, 
        content = content
    )
}

```

### `app\src\main\java\com\example\doc_tools\core\ui\theme\Type.kt`

```kt
package com.example.doc_tools.core.ui.theme

import androidx.compose.material3.Typography
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.sp

// Set of Material typography styles to start with
// Refer to https://material.io/design/typography/the-type-system.html#type-scale
// for more information on when to use each style.

val Typography = Typography(
    // Display styles are for very large, short, and important text or numerals.
    // They should be used sparingly, such as for hero text or screen titles.
    displayLarge = TextStyle(
        fontFamily = FontFamily.Default,
        fontWeight = FontWeight.Normal,
        fontSize = 57.sp,
        lineHeight = 64.sp,
        letterSpacing = (-0.25).sp
    ), // Used for the largest text on the screen, short and important text or numerals
    displayMedium = TextStyle(
        fontFamily = FontFamily.Default,
        fontWeight = FontWeight.Normal,
        fontSize = 45.sp,
        lineHeight = 52.sp,
        letterSpacing = 0.sp
    ), // Slightly smaller than displayLarge, for prominent screen titles
    displaySmall = TextStyle(
        fontFamily = FontFamily.Default,
        fontWeight = FontWeight.Normal,
        fontSize = 36.sp,
        lineHeight = 44.sp,
        letterSpacing = 0.sp
    ), // Smaller still, suitable for less prominent screen titles or hero text
    headlineLarge = TextStyle(
        fontFamily = FontFamily.Default,
        fontWeight = FontWeight.Normal,
        fontSize = 32.sp,
        lineHeight = 40.sp,
        letterSpacing = 0.sp
    ), // For high-emphasis text, shorter than body text, typically used for section titles
    headlineMedium = TextStyle(
        fontFamily = FontFamily.Default,
        fontWeight = FontWeight.Normal,
        fontSize = 28.sp,
        lineHeight = 36.sp,
        letterSpacing = 0.sp
    ), // Medium-emphasis headlines, for subheadings or less prominent section titles
    headlineSmall = TextStyle(
        fontFamily = FontFamily.Default,
        fontWeight = FontWeight.Normal,
        fontSize = 24.sp,
        lineHeight = 32.sp,
        letterSpacing = 0.sp
    ), // The smallest headline, for less important subheadings or annotations
    titleLarge = TextStyle(
        fontFamily = FontFamily.Default,
        fontWeight = FontWeight.Normal,
        fontSize = 22.sp,
        lineHeight = 28.sp,
        letterSpacing = 0.sp
    ), // For medium-emphasis text, such as the title of a card or list item
    titleMedium = TextStyle(
        fontFamily = FontFamily.Default,
        fontWeight = FontWeight.Medium,
        fontSize = 16.sp,
        lineHeight = 24.sp,
        letterSpacing = 0.15.sp
    ), // Slightly smaller title, often used for subtitles or less prominent titles
    titleSmall = TextStyle(
        fontFamily = FontFamily.Default,
        fontWeight = FontWeight.Medium,
        fontSize = 14.sp,
        lineHeight = 20.sp,
        letterSpacing = 0.1.sp
    ), // The smallest title, for minor titles or annotations
    bodyLarge = TextStyle(
        fontFamily = FontFamily.Default,
        fontWeight = FontWeight.Normal,
        fontSize = 16.sp,
        lineHeight = 24.sp,
        letterSpacing = 0.5.sp
    ), // For longer passages of text, like articles or detailed descriptions
    bodyMedium = TextStyle(
        fontFamily = FontFamily.Default,
        fontWeight = FontWeight.Normal,
        fontSize = 14.sp,
        lineHeight = 20.sp,
        letterSpacing = 0.25.sp
    ), // Default body text size, suitable for most text content
    bodySmall = TextStyle(
        fontFamily = FontFamily.Default,
        fontWeight = FontWeight.Normal,
        fontSize = 12.sp,
        lineHeight = 16.sp,
        letterSpacing = 0.4.sp
    ), // Smaller body text, often used for captions or less important supporting text
    labelLarge = TextStyle(
        fontFamily = FontFamily.Default,
        fontWeight = FontWeight.Medium,
        fontSize = 14.sp,
        lineHeight = 20.sp,
        letterSpacing = 0.1.sp
    ), // For text in components like buttons or tabs
    labelMedium = TextStyle(
        fontFamily = FontFamily.Default,
        fontWeight = FontWeight.Medium,
        fontSize = 12.sp,
        lineHeight = 16.sp,
        letterSpacing = 0.5.sp
    ), // Smaller label text, often used for form field labels or captions
    labelSmall = TextStyle(
        fontFamily = FontFamily.Default,
        fontWeight = FontWeight.Medium,
        fontSize = 11.sp,
        lineHeight = 16.sp,
        letterSpacing = 0.5.sp
    ) // The smallest label, for very small text elements like icon labels or legal text
)
```

### `app\src\main\java\com\example\doc_tools\core\utils\file\FileActionsUtils.kt`

```kt
package com.example.doc_tools.core.utils.file

import android.content.ActivityNotFoundException
import android.content.Context
import android.content.Intent
import android.net.Uri
import android.util.Log
import androidx.core.content.FileProvider
import com.example.doc_tools.core.common.model.FileDetails
import java.io.File

/**
 * Utility object for common file actions such as viewing and sharing files.
 * This object provides methods to handle different file types (PDF, image, archive)
 * and a generic method to view any file based on its MIME type. It also includes
 * a method to share files with other applications.
 */

object FileActionsUtils {
    private fun getContentUri(context: Context, uri: Uri): Uri {
        return if (uri.scheme == "file") {
            val file = File(uri.path!!)
            FileProvider.getUriForFile(
                context,
                "${context.applicationContext.packageName}.fileprovider",
                file
            )
        } else {
            uri
        }
    }

    /**
     * Reusable function to view PDF files
     */
    fun viewPdf(context: Context, uri: Uri?) {
        if (uri == null) return
        val contentUri = getContentUri(context, uri)
        val intent = Intent(Intent.ACTION_VIEW).apply {
            setDataAndType(contentUri, "application/pdf")
            addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION)
        }
        try {
            context.startActivity(intent)
        } catch (e: ActivityNotFoundException) {
            Log.e("OutputFileDetails", "No PDF viewer found")
        }
    }

    /**
     * Reusable function to view image files
     */
    fun viewImage(context: Context, uri: Uri, mimeType: String?) {
        val contentUri = getContentUri(context, uri)
        val intent = Intent(Intent.ACTION_VIEW).apply {
            setDataAndType(contentUri, mimeType ?: "image/*")
            addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION)
        }
        try {
            context.startActivity(intent)
        } catch (e: ActivityNotFoundException) {
            Log.e("OutputFileDetails", "No image viewer found")
        }
    }

    /**
     * Reusable function to view archive files
     */
    fun viewArchive(context: Context, uri: Uri, mimeType: String?) {
        val contentUri = getContentUri(context, uri)
        val intent = Intent(Intent.ACTION_VIEW).apply {
            setDataAndType(contentUri, mimeType ?: "application/zip")
            addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION)
        }
        try {
            context.startActivity(intent)
        } catch (e: ActivityNotFoundException) {
            Log.e("OutputFileDetails", "No archive viewer found for $mimeType")
        }
    }

    /**
     * Generic function to view any file based on its MIME type
     */
    fun viewFile(context: Context, uri: Uri, mimeType: String?) {
        val contentUri = getContentUri(context, uri)
        when {
            mimeType?.startsWith("application/") == true && (mimeType.endsWith("zip") || mimeType.endsWith("rar") || mimeType.endsWith("7z")) ->
                viewArchive(context, contentUri, mimeType)
            mimeType?.startsWith("image/") == true ->
                viewImage(context, contentUri, mimeType)
            mimeType == "application/pdf" ->
                viewPdf(context, contentUri)
            else -> {
                val intent = Intent(Intent.ACTION_VIEW).apply {
                    setDataAndType(contentUri, mimeType ?: "*/*")
                    addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION)
                }
                try {
                    context.startActivity(intent)
                } catch (e: ActivityNotFoundException) {
                    Log.e("OutputFileDetails", "No viewer found for $mimeType")
                }
            }
        }
    }

    /**
     * Share a file with other apps
     */
    fun shareFile(context: Context, uri: Uri?, mimeType: String?) {
        try {
            // Create a sharing intent
            val shareIntent = Intent().apply {
                action = Intent.ACTION_SEND

                // If the URI is a file:// URI, convert it to a content:// URI using FileProvider
                if (uri?.scheme == "file") {
                    val file = File(uri.path!!)
                    val contentUri = FileProvider.getUriForFile(
                        context,
                        context.applicationContext.packageName + ".fileprovider",
                        file
                    )
                    putExtra(Intent.EXTRA_STREAM, contentUri)
                } else {
                    // If it's already a content:// URI, use it directly
                    putExtra(Intent.EXTRA_STREAM, uri)
                }

                type = mimeType ?: "*/*"
                addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION)
            }

            val chooserIntent = Intent.createChooser(
                shareIntent,
                "Share via"
            )

            context.startActivity(chooserIntent)
        } catch (e: Exception) {
            Log.e("OutputFileDetails", "Error sharing file: ${e.message}")
        }
    }

    fun smartFileView(
        context: Context,
        fileDetails: FileDetails,
        multipleFiles: List<FileDetails>? = null,
        onShowBottomSheet: () -> Unit,
        isDarkTheme: Boolean
    ) {
        when {
            // For archives, open directly with system viewer
            fileDetails.mimeType?.let { mime ->
                mime.startsWith("application/") && (
                        mime.endsWith("zip") ||
                                mime.endsWith("rar") ||
                                mime.endsWith("7z") ||
                                mime.contains("compressed")
                        )
            } ?: false -> {
                viewFile(context, fileDetails.uri, fileDetails.mimeType)
            }
            // For multiple files, show bottom sheet
            multipleFiles?.isNotEmpty() == true -> {
                onShowBottomSheet()
            }
            // Fallback to single file view
            else -> {
                viewFile(context, fileDetails.uri, fileDetails.mimeType)
            }
        }
    }
}```

### `app\src\main\java\com\example\doc_tools\core\utils\file\FileBottomSheetUtils.kt`

```kt
package com.example.doc_tools.core.utils.file

import android.content.Context
import android.net.Uri
import android.util.Log
import android.widget.Toast
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.Job
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import kotlin.system.measureTimeMillis

/**
 * Utility class for handling file operations in FileBottomSheet.
 * This centralizes all file operations across different features that use FileBottomSheet.
 */
object FileBottomSheetUtils {

    // Keep track of active operations to prevent duplicate operations
    private val activeOperations = mutableMapOf<String, Job>()

    /**
     * Remove a single file from a list
     * @param uri URI of the file to remove
     * @param currentUris Current list of URIs
     * @param onUpdate Callback to update the UI state with new list
     * @param context Context for access to file system
     * @param scope CoroutineScope for async operations
     * @param onOperationStart Optional callback when operation starts
     * @param onOperationComplete Optional callback when operation completes
     * @param showMessage Whether to show feedback messages to the user
     * @param showProgressOverlay Whether to show the central progress overlay
     */
    fun removeFile(
        uri: Uri,
        currentUris: List<Uri>,
        onUpdate: (List<Uri>) -> Unit,
        context: Context,
        scope: CoroutineScope,
        onOperationStart: (() -> Unit)? = null,
        onOperationComplete: (() -> Unit)? = null,
        showMessage: Boolean = true,
        messageScope: String = "file_operations",
        showProgressOverlay: Boolean = false
    ) {
        // Generate a unique operation ID to prevent duplicate operations
        val operationId = "remove_${uri.hashCode()}_${System.currentTimeMillis()}"

        // Check if an operation is already in progress for this URI
        if (activeOperations.containsKey("remove_${uri.hashCode()}")) {
            Log.d("FileBottomSheetUtils", "Operation already in progress for URI: $uri")
            return
        }

        // Notify operation start
        onOperationStart?.invoke()

        // Start a new operation
        val job = scope.launch {
            // Use try-finally to ensure we always clean up
            try {
                withContext(Dispatchers.Default) {
                    val time = measureTimeMillis {
                        Log.d("FileBottomSheetUtils", "Removing file: $uri")

                        // Create a new list without the removed URI - using filterNot for efficiency
                        val updatedList = currentUris.filterNot { it == uri }

                        // Add a small delay for UI to catch up (especially for large lists)
                        delay(200)

                        // Update UI on main thread
                        withContext(Dispatchers.Main) {
                            onUpdate(updatedList)

                            // Show toast message directly
                            if (showMessage) {
                                Toast.makeText(
                                    context,
                                    "File removed successfully",
                                    Toast.LENGTH_SHORT
                                ).show()
                            }
                        }
                    }
                    Log.d("FileBottomSheetUtils", "File removal completed in $time ms")
                }
            } catch (e: Exception) {
                Log.e("FileBottomSheetUtils", "Error removing file: ${e.message}")
                // Show error message on main thread
                if (showMessage) {
                    withContext(Dispatchers.Main) {
                        Toast.makeText(
                            context,
                            "Failed to remove file: ${e.message}",
                            Toast.LENGTH_SHORT
                        ).show()
                    }
                }
            } finally {
                withContext(Dispatchers.Main) {
                    // Always notify completion to clear loading state
                    onOperationComplete?.invoke()
                    // Remove from active operations
                    activeOperations.remove("remove_${uri.hashCode()}")
                }
            }
        }

        // Store the job in active operations
        activeOperations["remove_${uri.hashCode()}"] = job
    }

    /**
     * Remove multiple files from a list with efficient batch processing
     * @param uris URIs of the files to remove
     * @param currentUris Current list of URIs
     * @param onUpdate Callback to update the UI state with new list
     * @param context Context for access to file system
     * @param scope CoroutineScope for async operations
     * @param onOperationStart Optional callback when operation starts
     * @param onOperationComplete Optional callback when operation completes
     * @param showMessage Whether to show feedback messages to the user
     */
    fun removeFiles(
        uris: List<Uri>,
        currentUris: List<Uri>,
        onUpdate: (List<Uri>) -> Unit,
        context: Context,
        scope: CoroutineScope,
        onOperationStart: (() -> Unit)? = null,
        onOperationComplete: (() -> Unit)? = null,
        showMessage: Boolean = true,
        messageScope: String = "file_operations"
    ) {
        if (uris.isEmpty()) return

        // Generate a unique operation ID to prevent duplicate operations
        val operationId = "remove_batch_${System.currentTimeMillis()}"

        // Avoid processing if another batch is in progress
        if (activeOperations.any { it.key.startsWith("remove_batch_") }) {
            Log.d("FileBottomSheetUtils", "Batch removal operation already in progress")
            return
        }

        // Notify operation start
        onOperationStart?.invoke()

        val job = scope.launch {
            try {
                withContext(Dispatchers.Default) {
                    val time = measureTimeMillis {
                        Log.d("FileBottomSheetUtils", "Removing ${uris.size} files")

                        // Use a HashSet for more efficient lookups in large lists
                        val urisToRemove = uris.toHashSet()
                        val updatedList = currentUris.filterNot { it in urisToRemove }

                        // Calculate a delay based on number of files
                        val operationDelay = when {
                            uris.size > 50 -> 600L  // More than 50 files
                            uris.size > 20 -> 400L  // 21-50 files
                            else -> 200L           // 1-20 files
                        }

                        // Show batch operation is in progress
                        val removedCount = currentUris.size - updatedList.size

                        // Add delay for processing
                        delay(operationDelay)

                        // Update UI on main thread
                        withContext(Dispatchers.Main) {
                            onUpdate(updatedList)

                            // Show toast message directly
                            if (showMessage && removedCount > 0) {
                                Toast.makeText(
                                    context,
                                    "$removedCount files removed successfully",
                                    Toast.LENGTH_SHORT
                                ).show()
                            }
                        }
                    }
                    Log.d("FileBottomSheetUtils", "Batch removal completed in $time ms")
                }
            } catch (e: Exception) {
                Log.e("FileBottomSheetUtils", "Error removing files: ${e.message}")
                // Show error message on main thread
                if (showMessage) {
                    withContext(Dispatchers.Main) {
                        Toast.makeText(
                            context,
                            "Failed to remove files: ${e.message}",
                            Toast.LENGTH_SHORT
                        ).show()
                    }
                }
            } finally {
                withContext(Dispatchers.Main) {
                    // Make sure to clear loading state
                    onOperationComplete?.invoke()
                    // Remove from active operations
                    activeOperations.remove(operationId)
                }
            }
        }

        // Store the job in active operations
        activeOperations[operationId] = job
    }

    /**
     * Clear all files with optimized performance and user feedback
     * @param onUpdate Callback to update the UI state with empty list
     * @param context Context for access to file system
     * @param scope CoroutineScope for async operations
     * @param onOperationStart Optional callback when operation starts
     * @param onOperationComplete Optional callback when operation completes
     * @param fileCount Current count of files for feedback message
     * @param showMessage Whether to show feedback messages to the user
     */
    fun clearAllFiles(
        onUpdate: (List<Uri>) -> Unit,
        context: Context,
        scope: CoroutineScope,
        onOperationStart: (() -> Unit)? = null,
        onOperationComplete: (() -> Unit)? = null,
        fileCount: Int = 0,
        showMessage: Boolean = true,
        messageScope: String = "file_operations"
    ) {
        // Generate a unique operation ID
        val operationId = "clear_all_${System.currentTimeMillis()}"

        // Check if a clear operation is already in progress
        if (activeOperations.any { it.key.startsWith("clear_all_") }) {
            Log.d("FileBottomSheetUtils", "Clear all operation already in progress")
            return
        }

        // Notify operation start
        onOperationStart?.invoke()

        val job = scope.launch {
            try {
                withContext(Dispatchers.Default) {
                    val time = measureTimeMillis {
                        Log.d("FileBottomSheetUtils", "Clearing all files")

                        // Calculate a delay based on number of files
                        val operationDelay = when {
                            fileCount > 50 -> 600L  // More than 50 files
                            fileCount > 20 -> 400L  // 21-50 files
                            else -> 200L           // 1-20 files
                        }

                        // Add delay for processing
                        delay(operationDelay)

                        // Update UI with empty list
                        withContext(Dispatchers.Main) {
                            onUpdate(emptyList())

                            // Show toast message directly
                            if (showMessage && fileCount > 0) {
                                Toast.makeText(
                                    context,
                                    "All files cleared successfully",
                                    Toast.LENGTH_SHORT
                                ).show()
                            }
                        }
                    }
                    Log.d("FileBottomSheetUtils", "Clear all completed in $time ms")
                }
            } catch (e: Exception) {
                Log.e("FileBottomSheetUtils", "Error clearing files: ${e.message}")
                // Show error message on main thread
                if (showMessage) {
                    withContext(Dispatchers.Main) {
                        Toast.makeText(
                            context,
                            "Failed to clear files: ${e.message}",
                            Toast.LENGTH_SHORT
                        ).show()
                    }
                }
            } finally {
                withContext(Dispatchers.Main) {
                    // Ensure loading state is cleared
                    onOperationComplete?.invoke()
                    // Remove from active operations
                    activeOperations.remove(operationId)
                }
            }
        }

        // Store the job in active operations
        activeOperations[operationId] = job
    }

    /**
     * Update the list of images after reordering or deleting in the bottom sheet
     * @param updatedUris The new list of URIs after reordering/deletion
     * @param context Context for access to file system
     * @param scope CoroutineScope for async operations
     * @param onUrisUpdate Callback to update the UI state with new URI list
     * @param onDetailsUpdate Callback to update the UI state with new details map
     * @param currentDetailsMap Current map of file details, keyed by URI
     * @param getFileDetails Function to get file details for a URI
     * @param clearOutputDetails Optional callback to clear output details when list changes
     * @param onOperationStart Optional callback when operation starts
     * @param onOperationComplete Optional callback when operation completes
     */
    fun updateImagesList(
        updatedUris: List<Uri>,
        context: Context,
        scope: CoroutineScope,
        onUrisUpdate: (List<Uri>) -> Unit,
        onDetailsUpdate: ((Map<Uri, Any>) -> Unit)? = null,
        currentDetailsMap: Map<Uri, Any>? = null,
        getFileDetails: (suspend (Context, Uri) -> Any?)? = null,
        clearOutputDetails: (() -> Unit)? = null,
        onOperationStart: (() -> Unit)? = null,
        onOperationComplete: (() -> Unit)? = null
    ) {
        // Generate a unique operation ID
        val operationId = "update_list_${System.currentTimeMillis()}"

        // Check if an update operation is already in progress
        if (activeOperations.any { it.key.startsWith("update_list_") }) {
            Log.d("FileBottomSheetUtils", "Update list operation already in progress")
            return
        }

        // Notify operation start
        onOperationStart?.invoke()

        // First update the URI list immediately
        onUrisUpdate(updatedUris)

        // Clear output details if callback provided
        clearOutputDetails?.invoke()

        // If we don't need to update details map, finish early
        if (onDetailsUpdate == null || currentDetailsMap == null || getFileDetails == null) {
            onOperationComplete?.invoke()
            return
        }

        val job = scope.launch {
            try {
                withContext(Dispatchers.Default) {
                    val time = measureTimeMillis {
                        Log.d(
                            "FileBottomSheetUtils",
                            "Updating file details for ${updatedUris.size} files"
                        )

                        val newDetailsMap = currentDetailsMap.toMutableMap()

                        // Remove details for images that are no longer in the list
                        val removedUris = newDetailsMap.keys.filter { it !in updatedUris }
                        removedUris.forEach { newDetailsMap.remove(it) }

                        // Add details for new images
                        val newUris = updatedUris.filter { it !in newDetailsMap.keys }
                        for (uri in newUris) {
                            val fileDetails = getFileDetails(context, uri)
                            if (fileDetails != null) {
                                newDetailsMap[uri] = fileDetails
                            }
                        }

                        // Update UI on main thread
                        withContext(Dispatchers.Main) {
                            onDetailsUpdate(newDetailsMap)
                        }
                    }
                    Log.d("FileBottomSheetUtils", "Details update completed in $time ms")
                }
            } catch (e: Exception) {
                Log.e("FileBottomSheetUtils", "Error updating file details: ${e.message}")
            } finally {
                withContext(Dispatchers.Main) {
                    // Ensure loading state is cleared
                    onOperationComplete?.invoke()
                    // Remove from active operations
                    activeOperations.remove(operationId)
                }
            }
        }

        // Store the job in active operations
        activeOperations[operationId] = job
    }

    /**
     * Cancel all active file operations
     */
    fun cancelAllOperations() {
        activeOperations.forEach { (_, job) ->
            job.cancel()
        }
        activeOperations.clear()
    }
}```

### `app\src\main\java\com\example\doc_tools\core\utils\file\FileIconUtils.kt`

```kt
package com.example.doc_tools.core.utils.file

import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.filled.InsertDriveFile
import androidx.compose.material.icons.filled.Description
import androidx.compose.material.icons.filled.Image
import androidx.compose.ui.graphics.vector.ImageVector

object FileIconUtils {

    /**
     * get "ICON'S" based on it's MIME type - confuse
     */
    fun getIconForMimeType(mimeType: String?): ImageVector {
        return when {
            mimeType == null -> Icons.AutoMirrored.Filled.InsertDriveFile
            mimeType.startsWith("image/") -> Icons.Default.Image
            mimeType == "application/pdf" -> Icons.Default.Description
            else -> Icons.AutoMirrored.Filled.InsertDriveFile
        }
    }
}```

### `app\src\main\java\com\example\doc_tools\core\utils\file\FileInfoUtils.kt`

```kt
package com.example.doc_tools.core.utils.file

import android.content.Context
import android.database.Cursor
import android.net.Uri
import android.provider.OpenableColumns
import com.example.doc_tools.core.common.model.FileDetails
import com.example.doc_tools.core.utils.image.ImageUtils
import com.example.doc_tools.core.utils.pdf.PdfUtils
import java.io.File
import java.util.Locale
import kotlin.math.log10
import kotlin.math.pow

/**
 * -- getFileName.
 * -- getFileSize.
 * -- getFileDetails.
 * -- getMimeType.
 * -- getFormattedFileSize.
 */

object FileInfoUtils {
    /**
     * Get "FILE NAME" from URI
     *
     */
    fun getFileName(context: Context, uri: Uri): String {
        var name: String? = null
        if (uri.scheme == "content") {
            val cursor: Cursor? = context.contentResolver.query(uri, null, null, null, null)
            cursor?.use {
                if (it.moveToFirst()) {
                    val nameIndex = it.getColumnIndex(OpenableColumns.DISPLAY_NAME)
                    if (nameIndex != -1) {
                        name = it.getString(nameIndex)
                    }
                }
            }
        }
        if (name == null) {
            name = uri.path
            val cut = name?.lastIndexOf('/')
            if (cut != -1 && cut != null) {
                name = name?.substring(cut + 1)
            }
        }
        return name ?: "Unknown" // Provide default
    }

    /**
     * get "FILE SIZE" from URI
     */
    fun getFileSize(context: Context, uri: Uri): Long {
        var size: Long = 0
        if (uri.scheme == "content") {
            val cursor: Cursor? = context.contentResolver.query(uri, null, null, null, null)
            cursor?.use {
                if (it.moveToFirst()) {
                    val sizeIndex = it.getColumnIndex(OpenableColumns.SIZE)
                    if (sizeIndex != -1 && !it.isNull(sizeIndex)) {
                        size = it.getLong(sizeIndex)
                    }
                }
            }
        } else if (uri.scheme == "file") {
            val file = File(uri.path ?: return 0)
            if (file.exists()) {
                size = file.length()
            }
        }
        return size
    }

    /**
     * get "BASIC FILE DETAILS" from URI
     */
    fun getFileDetails(context: Context, uri: Uri): FileDetails {
        val contentResolver = context.contentResolver
        val name = getFileName(context, uri)
        val size = getFileSize(context, uri)
        val path = UriUtils.getFilePath(context, uri)
        val mimeType = getMimeType(context, uri)

        var dimensions: Pair<Int, Int>? = null
        var pageCount: Int? = null

        if (mimeType?.startsWith("image/") == true) {
            dimensions = ImageUtils.getImageDimensions(context, uri)
        } else if (mimeType == "application/pdf") {
            pageCount = PdfUtils.getPageCount(context, uri)
        }

        return FileDetails(
            uri = uri,
            name = name,
            size = size,
            mimeType = mimeType ?: "application/octet-stream",
            path = path,
            dimensions = dimensions,
            pageCount = pageCount // ✅ Added to return value
        )
    }

    /**
     * get "MIME TYPE" from URI
     */
    fun getMimeType(context: Context, uri: Uri): String? {
        return context.contentResolver.getType(uri)
    }

    /**
     * get "FORMATTED FILE SIZE" in (KB, MB, GB) - file
     */
    fun getFormattedFileSize(sizeBytes: Long): String {
        if (sizeBytes <= 0) return "0 B"
        val units = arrayOf("B", "KB", "MB", "GB", "TB")
        val digitGroups = (log10(sizeBytes.toDouble()) / log10(1024.0)).toInt()
        val safeDigitGroups = digitGroups.coerceIn(0, units.size - 1)  // Prevent index out of bounds for extremely large files
        return String.Companion.format(Locale.getDefault(), "%.1f %s", sizeBytes / 1024.0.pow(safeDigitGroups.toDouble()), units[safeDigitGroups])
    }

}```

### `app\src\main\java\com\example\doc_tools\core\utils\file\FileIoUtils.kt`

```kt
package com.example.doc_tools.core.utils.file

import android.content.ContentValues
import android.content.Context
import android.content.Intent
import android.net.Uri
import android.os.Build
import android.os.Environment
import android.provider.DocumentsContract
import android.provider.MediaStore
import android.util.Log
import android.widget.Toast
import java.io.File
import java.io.FileInputStream
import java.io.FileOutputStream
import java.io.IOException
import java.text.SimpleDateFormat
import java.util.Date
import java.util.Locale
import java.util.zip.ZipEntry
import java.util.zip.ZipOutputStream

object FileIoUtils {

    /**
     * Create a temporary file in the app's cache directory
     */
    fun createTempFile(context: Context, prefix: String, suffix: String): File? { // Return nullable
        return try {
            val timeStamp = SimpleDateFormat("yyyyMMdd_HHmmss", Locale.getDefault()).format(Date())
            val fileName = "${prefix}_${timeStamp}"
            File.createTempFile(fileName, suffix, context.cacheDir)
        }
        catch (e: IOException) {
            e.printStackTrace() // Log error
            null
        }
    }

    /**
     *  Function to "SAVE FILE" (from cache) to external storage (Downloads)
     *  Returns the final Uri if successful, null otherwise
     */
    fun saveFileToDownloads(
        context: Context,
        sourceFile: File,
        outputFileName: String, // Desired output filename (e.g., compressed_myfile.pdf)
        mimeType: String
    ): Uri? {
        if (!sourceFile.exists()) return null
        val resolver = context.contentResolver
        val contentValues = ContentValues().apply {
            put(MediaStore.MediaColumns.DISPLAY_NAME, outputFileName)
            put(MediaStore.MediaColumns.MIME_TYPE, mimeType)
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
                put(MediaStore.MediaColumns.RELATIVE_PATH, Environment.DIRECTORY_DOWNLOADS + File.separator + "PDF_IMG_Tools") // Subfolder
                put(MediaStore.MediaColumns.IS_PENDING, 1)
            }
        }

        val collectionUri = if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
            MediaStore.Downloads.getContentUri(MediaStore.VOLUME_EXTERNAL_PRIMARY)
        }
        else {
            // Fallback for older versions (might need WRITE_EXTERNAL_STORAGE permission)
            val downloadsDir = Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_DOWNLOADS)
            val appDir = File(downloadsDir, "PDF_IMG_Tools")
            if (!appDir.exists() && !appDir.mkdirs()) {
                return null // Failed to create directory
            }
            val targetFile = File(appDir, outputFileName)
            // For older versions, we write directly and return the file Uri
            try {
                FileOutputStream(targetFile).use { outputStream ->
                    // Use FileInputStream for older Android versions
                    FileInputStream(sourceFile).use { inputStream ->
                        inputStream.copyTo(outputStream)
                    }
                }
                return Uri.fromFile(targetFile) // Return file Uri for older versions
            } catch (e: IOException) {
                e.printStackTrace()
                return null
            }
        }

        var outputUri: Uri? = null
        try {
            outputUri = resolver.insert(collectionUri, contentValues)
            outputUri?.let { targetUri ->
                resolver.openOutputStream(targetUri)?.use { outputStream ->
                    sourceFile.inputStream().use { inputStream ->
                        inputStream.copyTo(outputStream)
                    }
                }
                if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
                    contentValues.clear()
                    contentValues.put(MediaStore.MediaColumns.IS_PENDING, 0)
                    resolver.update(targetUri, contentValues, null, null)
                }
            }
        } catch (e: Exception) {
            e.printStackTrace()
            outputUri?.let { resolver.delete(it, null, null) }  // Clean up if insert failed or writing failed
            outputUri = null
        } finally {
            // Consider deleting the temporary cache file here or after confirmation
            // sourceFile.delete()
        }
        return outputUri // Uri of the saved file in Downloads
    }

    /**
     * Save a file to a specific directory using the Storage Access Framework
     * @param context Context
     * @param sourceFile Source file to copy
     * @param destinationDirUri Directory URI selected via SAF (Storage Access Framework)
     * @param filename Filename to save as
     * @param mimeType MIME type of the file
     * @return Uri of the saved file, or null if save failed
     */
    fun saveFileToDirectory(
        context: Context,
        sourceFile: File,
        destinationDirUri: Uri,
        filename: String,
        mimeType: String?
    ): Uri? {
        try {
            Log.d("FileIoUtils", "Starting saveFileToDirectory with destination: $destinationDirUri")
            Log.d("FileIoUtils", "URI authority: ${destinationDirUri.authority}, scheme: ${destinationDirUri.scheme}")

            // Show a toast with the URI for debugging
            Toast.makeText(
                context,
                "Trying to save to: ${destinationDirUri.lastPathSegment}",
                Toast.LENGTH_SHORT
            ).show()

            // First verify the source file exists and is readable
            if (!sourceFile.exists() || !sourceFile.canRead()) {
                Log.e("FileIoUtils", "Source file doesn't exist or can't be read: ${sourceFile.absolutePath}")
                Toast.makeText(context, "Source file error: ${sourceFile.name}", Toast.LENGTH_LONG).show()
                return null
            }

            // Log source file details
            Log.d("FileIoUtils", "Source file: ${sourceFile.absolutePath}, size: ${sourceFile.length()} bytes")

            // Make sure we have the right flags for the destination directory URI
            val takeFlags = Intent.FLAG_GRANT_READ_URI_PERMISSION or Intent.FLAG_GRANT_WRITE_URI_PERMISSION

            // Try to persist permissions if we don't already have them
            try {
                context.contentResolver.takePersistableUriPermission(destinationDirUri, takeFlags)
                Log.d("FileIoUtils", "Took persistable URI permission for $destinationDirUri")
            } catch (e: SecurityException) {
                // This may fail if we already have the permission or if permission isn't persistable
                Log.w("FileIoUtils", "Could not take persistable permission: ${e.message}")
                Toast.makeText(context, "Permission warning - continuing anyway", Toast.LENGTH_SHORT).show()
                // Continue anyway as we might still have permission for this session
            }

            // Sanitize filename to avoid special characters that might cause issues
            val sanitizedFilename = filename.replace("[\\\\/:*?\"<>|]".toRegex(), "_")

            Log.d("FileIoUtils", "Sanitized filename: $sanitizedFilename")

            // Alternative approach that sometimes works better for certain providers
            try {
                // Create a new file URI and get an output stream
                var newFileUri: Uri? = null

                // Determine if this is a tree URI that needs special handling
                val isTreeUri = destinationDirUri.toString().contains("/tree/")
                Log.d("FileIoUtils", "Destination URI: $destinationDirUri, isTreeUri=$isTreeUri")

                if (isTreeUri) {
                    try {
                        // For tree URIs, always use the childDocuments approach
                        val docId = DocumentsContract.getTreeDocumentId(destinationDirUri)
                        Log.d("FileIoUtils", "Tree document ID: $docId")

                        // Get the document URI first (not children URI)
                        val documentUri = DocumentsContract.buildDocumentUriUsingTree(
                            destinationDirUri,
                            docId
                        )
                        Log.d("FileIoUtils", "Document URI: $documentUri")

                        // Now create the new file in this directory
                        newFileUri = DocumentsContract.createDocument(
                            context.contentResolver,
                            documentUri,
                            mimeType ?: "application/octet-stream",
                            sanitizedFilename
                        )
                        Log.d("FileIoUtils", "Created document using tree URI: $newFileUri")
                    } catch (e: Exception) {
                        Log.e("FileIoUtils", "Error with tree URI approach: ${e.javaClass.simpleName} - ${e.message}")
                        // Fall back to standard approach as last resort
                    }
                } else {
                    // Standard DocumentsContract approach for non-tree URIs
                    Log.d("FileIoUtils", "Attempting to create document using standard DocumentsContract")
                    try {
                        newFileUri = DocumentsContract.createDocument(
                            context.contentResolver,
                            destinationDirUri,
                            mimeType ?: "application/octet-stream",
                            sanitizedFilename
                        )
                        Log.d("FileIoUtils", "DocumentsContract created URI: $newFileUri")
                    } catch (e: Exception) {
                        Log.e("FileIoUtils", "Error with DocumentsContract: ${e.javaClass.simpleName} - ${e.message}")
                    }
                }

                // If we still don't have a file URI, try one more approach for certain providers
                if (newFileUri == null && isTreeUri) {
                    Log.d("FileIoUtils", "Trying alternative tree URI approach with children")
                    try {
                        // Last attempt: try using buildChildDocumentsUriUsingTree
                        val docId = DocumentsContract.getTreeDocumentId(destinationDirUri)
                        val childrenUri = DocumentsContract.buildChildDocumentsUriUsingTree(
                            destinationDirUri,
                            docId
                        )

                        Log.d("FileIoUtils", "Using children URI: $childrenUri")

                        // Try to create document with children URI
                        newFileUri = DocumentsContract.createDocument(
                            context.contentResolver,
                            destinationDirUri, // Use original URI as last resort
                            mimeType ?: "application/octet-stream",
                            sanitizedFilename
                        )
                        Log.d("FileIoUtils", "Created document using alternative approach: $newFileUri")
                    } catch (e: Exception) {
                        Log.e("FileIoUtils", "Error with alternative approach: ${e.javaClass.simpleName} - ${e.message}")
                        // At this point, we've tried everything - log failure but continue to try openOutputStream approach
                    }
                }

                // If we have a URI, try to write to it
                if (newFileUri != null) {
                    Log.d("FileIoUtils", "Got URI for new file: $newFileUri")

                    var success = false
                    try {
                        context.contentResolver.openOutputStream(newFileUri)?.use { outputStream ->
                            FileInputStream(sourceFile).use { inputStream ->
                                // Use java.nio for faster copying
                                val buffer = ByteArray(8 * 1024)
                                var bytesRead: Int
                                while (inputStream.read(buffer).also { bytesRead = it } > 0) {
                                    outputStream.write(buffer, 0, bytesRead)
                                }
                                outputStream.flush()
                                success = true
                            }
                        }
                    } catch (e: Exception) {
                        Log.e("FileIoUtils", "Error writing to output stream: ${e.message}")
                        Toast.makeText(context, "Error writing file: ${e.message}", Toast.LENGTH_LONG).show()

                        // Try to delete the partial file
                        try {
                            DocumentsContract.deleteDocument(context.contentResolver, newFileUri)
                        } catch (e2: Exception) {
                            Log.e("FileIoUtils", "Could not delete partial file: ${e2.message}")
                        }
                        return null
                    }

                    if (success) {
                        Log.d("FileIoUtils", "File successfully saved to $newFileUri")
                        Toast.makeText(context, "File saved successfully", Toast.LENGTH_SHORT).show()
                        return newFileUri
                    }
                } else {
                    Log.e("FileIoUtils", "Could not create document URI")
                    Toast.makeText(context, "Could not create file at selected location", Toast.LENGTH_LONG).show()
                }
            } catch (e: Exception) {
                Log.e("FileIoUtils", "Error in saveFileToDirectory: ${e.javaClass.simpleName} - ${e.message}")
                Toast.makeText(context, "Error: ${e.message}", Toast.LENGTH_LONG).show()
                e.printStackTrace()
            }

            return null
        }
        catch (e: Exception) {
            Log.e("FileIoUtils", "Unexpected error: ${e.javaClass.simpleName} - ${e.message}")
            Toast.makeText(context, "Unexpected error: ${e.message}", Toast.LENGTH_LONG).show()
            e.printStackTrace()
            return null
        }
    }

    /**
     * Creates "ZIP ARCHIVE" containing all provided files
     * @param sourceFiles List of files to add to the archive
     * @param outputFile The output ZIP file
     * @return true if the archive was created successfully
     */
    fun createZipArchive(sourceFiles: List<File>, outputFile: File): Boolean {
        try {
            if (outputFile.exists()) {
                outputFile.delete()
            }
            ZipOutputStream(FileOutputStream(outputFile)).use { zipOut ->
                for (sourceFile in sourceFiles) {
                    if (sourceFile.exists()) {
                        val zipEntry = ZipEntry(sourceFile.name)
                        zipOut.putNextEntry(zipEntry)

                        FileInputStream(sourceFile).use { fileIn ->
                            val buffer = ByteArray(1024)
                            var len: Int
                            while (fileIn.read(buffer).also { len = it } != -1) {
                                zipOut.write(buffer, 0, len)
                            }
                        }
                    }
                }
            }
            return true
        } catch (e: Exception) {
            e.printStackTrace()
            return false
        }
    }

    /**
     * Make createOutputFile use createTempOutputFile to avoid confusion.
     */
    @Deprecated("Use createTempOutputFile for temporary files", ReplaceWith("createTempFile(context, prefix, suffix)"))
    fun createOutputFile(context: Context, prefix: String, suffix: String): File? {
        return createTempFile(context, prefix, suffix)
    }

    /**
     * Create an "OUTPUT FILE" placeholder (primarily for naming/path structure, might not be needed with MediaStore)
     * DEPRECATED if using MediaStore for saving.
     */
    @Deprecated("Use MediaStore or SAF for saving files to shared storage.")
    fun createOutputFileInAppDir(context: Context, prefix: String, suffix: String): File {
        val timeStamp = SimpleDateFormat("yyyyMMdd_HHmmss", Locale.getDefault()).format(Date())
        val fileName = "${prefix}_${timeStamp}${suffix}"

        val directory =
            File(context.getExternalFilesDir(Environment.DIRECTORY_DOWNLOADS), "PDF_IMG_Tools")
        if (!directory.exists()) {
            directory.mkdirs()
        }
        return File(directory, fileName)
    }

}```

### `app\src\main\java\com\example\doc_tools\core\utils\file\SaveLocationUtils.kt`

```kt
package com.example.doc_tools.core.utils.file

import android.content.Context
import android.net.Uri
import android.util.Log
import com.example.doc_tools.core.domain.model.SaveMode
import java.io.File
import kotlin.collections.iterator

/**
 * Provides utility functions for managing save locations, particularly in conjunction with the
 * `ReusableSaveLocationSelector` component. This object handles validation of save paths,
 * retrieval of URIs for custom directories, and the actual saving of files to either the
 * default Downloads folder or a user-selected custom location.
 *
 * The `ReusableSaveLocationSelector` component allows users to choose a save location, which can be
 * the default Downloads folder or a custom directory. This utility class provides the backend logic
 * to interpret the selected path, retrieve the corresponding URI (if it's a custom location), and
 * then save the file to the chosen destination. It also supports saving files individually or as
 * part of a ZIP archive.
 */

object SaveLocationUtils {

    /**
     * Validates if the save location is valid
     *
     * @param savePath The save path string
     * @return true if the save location is valid
     */

    fun validateSaveLocation(savePath: String): Boolean {
        return savePath.isNotEmpty()
    }

    /**
     * Get the URI for the custom directory selected by a user
     *
     * @param context The application context
     * @param savePath The save path string from the ReusableSaveLocationSelector
     * @return The URI to use for saving, or null if we should use the default Downloads folder
     */
    fun getSaveLocationUri(context: Context, savePath: String): Uri? {
        // If the path is "Downloads" or empty, return null to indicate using the default Downloads folder
        if (savePath.isEmpty() || savePath == "Downloads") {
            return null
        }

        // Check if we have a saved URI for this path in SharedPreferences
        val sharedPrefs = context.getSharedPreferences("save_locations", Context.MODE_PRIVATE)
        val uriString = sharedPrefs.getString(savePath, null)

        if (uriString != null) {
            try {
                Log.d("SaveLocationUtils", "Found URI for $savePath: $uriString")
                return Uri.parse(uriString)
            } catch (e: Exception) {
                Log.e("SaveLocationUtils", "Error parsing URI: ${e.message}")
            }
        } else {
            Log.w("SaveLocationUtils", "No URI found for path: $savePath")
        }

        // Fallback: check if path starts with 'Selected:' which indicates a fallback path name
        if (savePath.startsWith("Selected:")) {
            // Look through all saved URIs in case the display name doesn't match but we still have the URI
            val allEntries = sharedPrefs.all
            for (entry in allEntries) {
                Log.d("SaveLocationUtils", "Checking saved location: ${entry.key} = ${entry.value}")
            }
        }

        return null
    }

    /**
     * Saves a file to the selected location
     *
     * @param context The application context
     * @param sourceFile The source file to save
     * @param outputFileName The output file name
     * @param mimeType The mime type of the file
     * @param savePath The save path from ReusableSaveLocationSelector
     * @param saveMode The save mode (SEPARATELY or AS_ARCHIVE)
     * @return The URI of the saved file, or null if saving failed
     */
    fun saveToLocation(
        context: Context,
        sourceFile: File,
        outputFileName: String,
        mimeType: String,
        savePath: String,
        saveMode: SaveMode
    ): Uri? {
        Log.d("SaveLocationUtils", "Saving file to: $savePath using mode: $saveMode")

        // If savePath is Downloads or empty, use the Downloads folder
        val isDefaultDownloads = savePath.isEmpty() || savePath == "Downloads"

        // Get the directory URI if using a custom location
        val saveLocationUri = if (!isDefaultDownloads) {
            val uri = getSaveLocationUri(context, savePath)
            Log.d("SaveLocationUtils", "Custom location URI: $uri")
            uri
        } else {
            Log.d("SaveLocationUtils", "Using default Downloads location")
            null
        }

        // Determine final filename based on mode
        val finalFileName = when (saveMode) {
            SaveMode.AS_ARCHIVE -> "${outputFileName}.zip"
            else -> outputFileName
        }

        // If saveMode is AS_ARCHIVE, create a ZIP archive first
        val fileToSave = if (saveMode == SaveMode.AS_ARCHIVE) {
            val zipFile = File(context.cacheDir, finalFileName)
            val success = FileIoUtils.createZipArchive(listOf(sourceFile), zipFile)
            Log.d("SaveLocationUtils", "Created ZIP archive: $success, file exists: ${zipFile.exists()}, size: ${zipFile.length()} bytes")
            zipFile
        } else {
            sourceFile
        }

        // Determine correct mime type for archives
        val finalMimeType = if (saveMode == SaveMode.AS_ARCHIVE) {
            "application/zip"
        } else {
            mimeType
        }

        // Check if we actually got a valid URI for manual location
        if (!isDefaultDownloads && saveLocationUri == null) {
            Log.w("SaveLocationUtils", "Failed to get URI for manual location. Falling back to Downloads")
            return FileIoUtils.saveFileToDownloads(context, fileToSave, finalFileName, finalMimeType)
        }

        // Save to the appropriate location
        return if (isDefaultDownloads || saveLocationUri == null) {
            // Save to Downloads
            Log.d("SaveLocationUtils", "Saving to Downloads: $finalFileName")
            FileIoUtils.saveFileToDownloads(
                context,
                fileToSave,
                finalFileName,
                finalMimeType
            )
        } else {
            // Save to custom location
            Log.d("SaveLocationUtils", "Saving to custom location: $savePath, $finalFileName")
            FileIoUtils.saveFileToDirectory(
                context,
                fileToSave,
                saveLocationUri,
                finalFileName,
                finalMimeType
            )
        }
    }

}```

### `app\src\main\java\com\example\doc_tools\core\utils\file\UriUtils.kt`

```kt
package com.example.doc_tools.core.utils.file

import android.content.Context
import android.net.Uri
import android.provider.DocumentsContract
import android.provider.MediaStore

/**
 * - getFilePath
 * - getDirectoryName
 */

object UriUtils {

    /**
     *  get "DISPLAYABLE PATH", might not always work depending on Uri source
     *  This is complex and might not work for all URIs (especially cloud/SAF ones)
     *  For simplicity, we'll often just show the filename or "Content URI"
     */
    fun getFilePath(context: Context, uri: Uri): String? {
        if (uri.scheme == "file") {
            return uri.path
        }
        if (uri.scheme == "content") {
            val projection = arrayOf(MediaStore.MediaColumns.DATA) // Attempt to get path from MediaStore for common media types
            try {
                context.contentResolver.query(uri, projection, null, null, null)?.use { cursor ->
                    if (cursor.moveToFirst()) {
                        val columnIndex = cursor.getColumnIndexOrThrow(MediaStore.MediaColumns.DATA)
                        return cursor.getString(columnIndex)
                    }
                }
            }
            catch (e: Exception) {
                // Ignore if column doesn't exist or other error
            }

            return uri.toString() // Fallback for content URIs - Return the URI string itself for clarity
        }

        return uri.toString() // Fallback
    }

    /**
     * Get directory name and path from DocumentsContract Uri
     * @param context Context
     * @param uri DocumentsContract Uri for a directory
     * @return Full readable path of the directory, or null if it couldn't be determined
     */
    fun getDirectoryName(context: Context, uri: Uri): String? {
        try {
            // Handle tree URIs from Storage Access Framework
            if (uri.toString().startsWith("content://com.android.externalstorage.documents/tree/")) {

                val decoded = Uri.decode(uri.toString())
                val path = decoded.replace("content://com.android.externalstorage.documents/tree/", "")

                // Handle primary storage
                if (path.startsWith("primary:")) {
                    val relativePath = path.substring("primary:".length)
                    return if (relativePath.isEmpty()) {
                        "Internal Storage"
                    } else {
                        "Internal Storage/$relativePath"
                    }
                }

                // Handle SD Card or other storage
                val storageMatch = Regex("([^:]+):(.*)").matchEntire(path)
                if (storageMatch != null) {
                    val (storageId, relativePath) = storageMatch.destructured
                    val storageName = when(storageId) {
                        "primary" -> "Internal Storage"
                        "home" -> "Home"
                        "documents" -> "Documents"
                        "downloads" -> "Downloads"
                        else -> "SD Card"
                    }

                    return if (relativePath.isEmpty()) {
                        storageName
                    } else {
                        "$storageName/$relativePath"
                    }
                }

                return "Selected: $path" // Fallback if pattern doesn't match
            }

            // For document URIs, try to get a more readable path
            val cursor = context.contentResolver.query(
                uri,
                arrayOf(DocumentsContract.Document.COLUMN_DISPLAY_NAME, DocumentsContract.Document.COLUMN_DOCUMENT_ID),
                null, null, null
            )

            var directoryPath: String? = null
            cursor?.use {
                if (it.moveToFirst()) {
                    // Try to get display name
                    val displayNameIndex = it.getColumnIndex(DocumentsContract.Document.COLUMN_DISPLAY_NAME)
                    val documentIdIndex = it.getColumnIndex(DocumentsContract.Document.COLUMN_DOCUMENT_ID)

                    val displayName = if (displayNameIndex != -1) it.getString(displayNameIndex) else null
                    val documentId = if (documentIdIndex != -1) it.getString(documentIdIndex) else null

                    // Create readable path
                    directoryPath = when {
                        displayName != null && documentId != null -> {
                            val basePath = documentId.split(":").lastOrNull() ?: ""
                            if (basePath.isEmpty()) displayName else "$displayName ($basePath)"
                        }
                        displayName != null -> displayName
                        documentId != null -> documentId
                        else -> uri.lastPathSegment
                    }
                }
            }
            return directoryPath ?: uri.lastPathSegment
        } catch (e: Exception) {
            e.printStackTrace()
            // Fallback to a more user-friendly message with the URI
            return "Selected Location: ${uri.lastPathSegment ?: "Unknown"}"
        }
    }
}```

### `app\src\main\java\com\example\doc_tools\core\utils\image\ImageFormat.kt`

```kt
package com.example.doc_tools.core.utils.image

import android.graphics.Bitmap
import android.os.Build

// Define ImageFormat enum class
enum class ImageFormat(
    val extension: String,
    val mimeType: String,
    val compressFormat: Bitmap.CompressFormat,
    val displayName: String,
    val supportsQuality: Boolean
) {
    JPG("jpg", "image/jpeg", Bitmap.CompressFormat.JPEG, "JPEG", true),
    PNG("png", "image/png", Bitmap.CompressFormat.PNG, "PNG", false),
    // For WebP formats, we need to handle Android version compatibility
    WEBP_LOSSY("webp", "image/webp",
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R)
            Bitmap.CompressFormat.WEBP_LOSSY
        else
            @Suppress("DEPRECATION") Bitmap.CompressFormat.WEBP, "WebP (Lossy)", true
    ),
    WEBP_LOSSLESS("webp", "image/webp",
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R)
            Bitmap.CompressFormat.WEBP_LOSSLESS
        else
            @Suppress("DEPRECATION") Bitmap.CompressFormat.WEBP, "WebP (Lossless)", true
    );

    // Re-add the companion object with fromMimeType
    companion object {
        fun fromMimeType(mimeType: String?): ImageFormat? {
            return when (mimeType?.lowercase()) {
                "image/jpeg", "image/jpg" -> JPG
                "image/png" -> PNG
                "image/webp" -> WEBP_LOSSY // Default to lossy for webp
                else -> null // Unknown or unsupported
            }
        }

        fun getFormatNames(): List<String> {
            return values().map { it.displayName }
        }

        fun fromDisplayName(name: String): ImageFormat {
            return values().find { it.displayName == name } ?: JPG
        }

        // Helper to determine if WEBP types are fully supported
        fun isWebpTypeSupported(): Boolean {
            return Build.VERSION.SDK_INT >= Build.VERSION_CODES.R
        }
    }
}```

### `app\src\main\java\com\example\doc_tools\core\utils\image\ImageUtils.kt`

```kt
package com.example.doc_tools.core.utils.image

import android.content.Context
import android.graphics.BitmapFactory
import android.net.Uri

object ImageUtils {

    /**
     * get "IMAGE DIMENSION'S" from URI without loading the full bitmap
     */
    fun getImageDimensions(context: Context, uri: Uri): Pair<Int, Int>? {
        val options = BitmapFactory.Options().apply {
            inJustDecodeBounds = true // Only decode bounds, not the full bitmap
        }
        try {
            context.contentResolver.openInputStream(uri)?.use { inputStream ->
                BitmapFactory.decodeStream(inputStream, null, options)
                if (options.outWidth > 0 && options.outHeight > 0) {
                    return Pair(options.outWidth, options.outHeight)
                }
            }
        } catch (e: Exception) {
            e.printStackTrace() // Handle exceptions like FileNotFoundException
            return null
        }
        return null
    }

}```

### `app\src\main\java\com\example\doc_tools\core\utils\pdf\PdfUtils.kt`

```kt
package com.example.doc_tools.core.utils.pdf

import android.content.Context
import android.net.Uri
import com.tom_roush.pdfbox.pdmodel.PDDocument
import java.io.InputStream

object PdfUtils {

    /**
     * get "PDF PAGE COUNT" from URI
     */
    fun getPageCount(context: Context, uri: Uri): Int? {
        return try {
            val inputStream: InputStream? = context.contentResolver.openInputStream(uri)
            inputStream?.use { stream ->
                PDDocument.load(stream).use { document ->
                    document.numberOfPages
                }
            }
        } catch (e: Exception) {
            e.printStackTrace()
            null
        }
    }

}```

### `app\src\main\java\com\example\doc_tools\features\home\presentation\ui\HomeScreen.kt`

```kt
package com.example.doc_tools.features.home.presentation.ui

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.MaterialTheme
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.navigation.NavController
import com.example.doc_tools.features.home.data.repository.ToolRepository
import com.example.doc_tools.core.ui.components.layout.BaseToolScreen
import com.example.doc_tools.core.ui.components.tool_layout.HeaderSection
import com.example.doc_tools.features.home.presentation.ui.components.FixedToolsGrid

/**
 * Composable function that displays the home screen of the application.
 *
 * This screen serves as the main entry point and showcases different categories of tools,
 * such as PDF tools and Image tools. It utilizes a [BaseToolScreen] for common UI elements
 * like the app bar and theme toggle. The tools within each category are displayed in a grid format.
 *
 * @param navController The [NavController] used for navigating to different tool screens.aa
 * @param isDarkTheme A boolean indicating whether the dark theme is currently active.A
 * @param onThemeToggle A lambda function to be invoked when the theme toggle button is clicked.
 * @param modifier An optional [Modifier] to be applied to the root composable of this screen.
 */

@Composable
fun HomeScreen(
    navController: NavController,
    isDarkTheme: Boolean,
    onThemeToggle: () -> Unit,
    modifier: Modifier = Modifier
){
    val toolRepository = remember { ToolRepository() }
    val pdfTools = remember { toolRepository.getPdfTools() }
    val imageTools = remember { toolRepository.getImageTools() }
    val messageScope = "home"

    BaseToolScreen(
        title = "Doc Tools",
        navController = navController,
        isDarkTheme = isDarkTheme,
        onThemeToggle = onThemeToggle,
        messageScope = messageScope,
        modifier = modifier,
        contentScrollable = true,
        showBackButton = false,
        showThemeToggle = false // Hide theme toggle since it's now in Settings
    ) {
        Column(modifier = Modifier.fillMaxSize().background(color = MaterialTheme.colorScheme.surface, shape = MaterialTheme.shapes.extraLarge).padding(16.dp)){
            HeaderSection(title = "Pdf Tools", textColor = MaterialTheme.colorScheme.onSurface, modifier = Modifier.padding(vertical = 16.dp))
            FixedToolsGrid(tools = pdfTools, navController = navController, isDarkTheme = isDarkTheme)
            HeaderSection(title = "Image Tools", textColor = MaterialTheme.colorScheme.onSurface, modifier = Modifier.padding(vertical = 16.dp))
            FixedToolsGrid(tools = imageTools, navController = navController, isDarkTheme = isDarkTheme)
        }
    }
}
```

### `app\src\main\java\com\example\doc_tools\features\home\presentation\ui\components\FixedToolGrid.kt`

```kt
package com.example.doc_tools.features.home.presentation.ui.components

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.navigation.NavController
import com.example.doc_tools.core.presentation.state.ToolItem
import com.example.doc_tools.core.ui.components.card.ToolCard

/**
 * A fixed grid layout that displays tools in rows with 2 items per row
 */
@Composable
fun FixedToolsGrid(tools: List<ToolItem>, navController: NavController, isDarkTheme: Boolean, modifier: Modifier = Modifier){
    Column(modifier = modifier.fillMaxWidth()) {
        tools.chunked(2).forEach { rowItems ->
            Row(modifier = Modifier.fillMaxWidth().padding(vertical = 6.dp), horizontalArrangement = Arrangement.spacedBy(8.dp)){
                rowItems.forEach { tool ->
                    Box(modifier = Modifier.weight(1f)){
                        ToolCard(toolItem = tool, onClick = { navController.navigate(tool.route) }, isDarkTheme = isDarkTheme)
                    }
                }
                //                if (rowItems.size == 1) { Spacer(modifier = Modifier.weight(1f)) }
            }
        }
    }
}```

### `app\src\main\java\com\example\doc_tools\features\image\compressimages\presentation\state\CompressImagesUiState.kt`

```kt
package com.example.doc_tools.features.image.compressimages.presentation.state

import android.net.Uri
import com.example.doc_tools.core.common.model.FileDetails
import com.example.doc_tools.core.domain.model.SaveMode

/**
 * Data class representing the UI state for the Compress Images screen
 */
data class CompressImagesUiState(
    val selectedImageUris: List<Uri> = emptyList(),
    val imageDetailsMap: Map<Uri, FileDetails> = emptyMap(),
    val compressionQuality: Float = 80f,
    val isProcessing: Boolean = false,
    val processingProgress: Float = -1f,
    val outputDetailsList: List<FileDetails> = emptyList(),
    val savePath: String = "Downloads",
    val saveMode: SaveMode = SaveMode.SEPARATELY,
    val showSelectedImagesBottomSheet: Boolean = false,
    val showAllImagesBottomSheet: Boolean = false,
    val errorMessage: String? = null,
    val compressionFormat: String = "JPEG"
)```

### `app\src\main\java\com\example\doc_tools\features\image\compressimages\presentation\ui\CompressImagesScreen.kt`

```kt
package com.example.doc_tools.features.image.compressimages.presentation.ui

import android.content.Context
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Compress
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.HorizontalDivider
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation.NavController
import com.example.doc_tools.core.domain.model.SaveMode
import com.example.doc_tools.core.ui.components.button.ProgressToolButton
import com.example.doc_tools.core.ui.components.card.FileInfoActionCard
import com.example.doc_tools.core.ui.components.file.ChangeSaveLocation
import com.example.doc_tools.core.ui.components.file.FileBottomSheet
import com.example.doc_tools.core.ui.components.layout.BaseToolScreen
import com.example.doc_tools.core.ui.components.overlay.ProcessingAware
import com.example.doc_tools.core.ui.components.tool_layout.HeaderSection
import com.example.doc_tools.core.utils.file.FileActionsUtils
import com.example.doc_tools.core.utils.file.FileActionsUtils.viewFile
import com.example.doc_tools.features.image.compressimages.presentation.state.CompressImagesUiState
import com.example.doc_tools.features.image.compressimages.presentation.ui.components.CompressionSettingsSection
import com.example.doc_tools.features.image.compressimages.presentation.ui.components.FileSelectionSection
import com.example.doc_tools.features.image.compressimages.presentation.viewmodel.CompressImagesViewModel


/**
 * Screen for compressing image files
 */
@Composable
fun CompressImagesScreen(
    navController: NavController,
    isDarkTheme: Boolean,
    onThemeToggle: () -> Unit,
    modifier: Modifier = Modifier,
    viewModel: CompressImagesViewModel = viewModel()
) {
    val context = LocalContext.current
    val uiState = viewModel.uiState
    val formatOptions = listOf("JPEG", "PNG")
    val messageScope = "compress_images"

    BaseToolScreen(
        title = "Compress Images",
        navController = navController,
        isDarkTheme = isDarkTheme,
        onThemeToggle = onThemeToggle,
        contentScrollable = true,
        messageScope = messageScope,
        showThemeToggle = false, // Hide theme toggle since it's now in Settings
        modifier = modifier
    ) {
        Card(
            modifier = Modifier.fillMaxWidth().padding(vertical = 8.dp),
            colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surface, contentColor = MaterialTheme.colorScheme.onSurface),
            elevation = CardDefaults.cardElevation(defaultElevation = 1.dp),
            shape = RoundedCornerShape(24.dp)
        ) {
            Column(verticalArrangement = Arrangement.spacedBy(16.dp), modifier = Modifier.padding(24.dp)) {

                HeaderSection(icon = Icons.Default.Compress, title = "Compress Images", subtitle = "Reduce the size of images by applying compression.")
                HorizontalDivider(color = MaterialTheme.colorScheme.outline)
                ProcessingAware { isEnabled -> FileSelectionSection(uiState, context, viewModel, isDarkTheme, isEnabled) }
                HorizontalDivider(color = MaterialTheme.colorScheme.outline)
                ProcessingAware { isEnabled -> CompressionSettingsSection(uiState, viewModel, isEnabled) }

                if (uiState.selectedImageUris.isNotEmpty()) {
                    ProcessingAware { isEnabled ->
                        ChangeSaveLocation(
                            visible = true,
                            defaultSaveLocation = uiState.savePath,
                            onSaveLocationChanged = { if (isEnabled) viewModel.updateSavePath(it) },
                            saveModeEnabled = true,
                            initialSaveMode = uiState.saveMode,
                            onSaveModeChanged = { if (isEnabled) viewModel.updateSaveMode(it) },
                            modifier = Modifier.fillMaxWidth()
                        )
                    }
                }

                ProgressToolButton(
                    onClick = { 
                        if (uiState.isProcessing) {
                            viewModel.cancelCompression()
                        } else {
                            viewModel.compressImages(context, messageScope)
                        }
                    },
                    isProcessing = uiState.isProcessing,
                    progress = uiState.processingProgress,
                    enabled = uiState.selectedImageUris.isNotEmpty(),
                    text = "Compress Images",
                    icon = Icons.Default.Compress,
                    errorMessage = if (uiState.isProcessing) null else uiState.errorMessage,
                    processingText = "Compression in progress",
                )

                ProcessingAware { isEnabled ->
                    if (uiState.outputDetailsList.isNotEmpty()) {
                        val compressedTotal = uiState.outputDetailsList.sumOf { it.size }
                        val summaryDetails = uiState.outputDetailsList.firstOrNull()?.copy(
                            name = when {
                                uiState.saveMode == SaveMode.AS_ARCHIVE -> "PDF_extracted_images.zip"
                                uiState.outputDetailsList.size == 1 -> uiState.outputDetailsList.first().name
                                else -> "${uiState.outputDetailsList.size} Extracted Images"
                            },
                            size = compressedTotal
                        )
                        summaryDetails?.let {
                            Text(text = "Compressed Image Detail's", style = MaterialTheme.typography.bodyMedium, fontWeight = FontWeight.SemiBold, color = MaterialTheme.colorScheme.onSurfaceVariant)
                            FileInfoActionCard(
                                file = it,
                                showSize = true,
                                showFormat = true,
                                onOpen = { if (isEnabled) {
                                    FileActionsUtils.smartFileView(
                                        context = context,
                                        fileDetails = it,
                                        multipleFiles = uiState.outputDetailsList,
                                        onShowBottomSheet = { if (isEnabled) viewModel.toggleAllImagesBottomSheet(true) },
                                        isDarkTheme = isDarkTheme
                                    )
                                } },
                                onDelete = { if (isEnabled) viewModel.clearOutputDetails() },
                                isDarkTheme = isDarkTheme,
                                enabled = isEnabled
                            )
                        }
                    }
                }
            }
        }
        if (uiState.showSelectedImagesBottomSheet && !uiState.isProcessing) {
            FileBottomSheet(
                show = uiState.showSelectedImagesBottomSheet && uiState.selectedImageUris.isNotEmpty(),
                onDismiss = { viewModel.toggleSelectedImagesBottomSheet(false) },
                fileUris = uiState.selectedImageUris,
                title = "Selected Images",
                onFilesUpdated = { updatedUris -> viewModel.updateImagesList(context, updatedUris) },
                onFileView = { uri, mimeType -> viewFile(context, uri, mimeType ?: "image/*") },
                isDarkTheme = isDarkTheme
            )
        }
        if (uiState.showAllImagesBottomSheet && !uiState.isProcessing) {
            FileBottomSheet(
                show = uiState.showAllImagesBottomSheet && uiState.outputDetailsList.isNotEmpty(),
                onDismiss = { viewModel.toggleAllImagesBottomSheet(false) },
                fileUris = uiState.outputDetailsList.map { it.uri },
                title = "Compressed Images",
                onFilesUpdated = { /* Compressed images don't need updating */ },
                onFileView = { uri, mimeType -> viewFile(context, uri, mimeType) },
                isDarkTheme = isDarkTheme,
                enableSelection = false,
                enableRemoveSelected = false,
                enableClearAll = false,
                enableFileRemoveButton = false
            )
        }
    }
}

```

### `app\src\main\java\com\example\doc_tools\features\image\compressimages\presentation\ui\components\CompressionSettingSection.kt`

```kt
package com.example.doc_tools.features.image.compressimages.presentation.ui.components

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Slider
import androidx.compose.material3.SliderDefaults
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import com.example.doc_tools.core.ui.components.button.ChipButton
import com.example.doc_tools.core.ui.components.feedback.WarningBanner
import com.example.doc_tools.features.image.compressimages.presentation.state.CompressImagesUiState
import com.example.doc_tools.features.image.compressimages.presentation.viewmodel.CompressImagesViewModel

@Composable
internal fun CompressionSettingsSection(
    uiState: CompressImagesUiState,
    viewModel: CompressImagesViewModel,
    isEnabled: Boolean
) {
    Column {
        Text(text = "Select Output Format", style = MaterialTheme.typography.bodyMedium, fontWeight = FontWeight.SemiBold, color = MaterialTheme.colorScheme.onSurfaceVariant)
        Spacer(modifier = Modifier.height(4.dp))
        Text(text = "Choose the image output format for compressed images", style = MaterialTheme.typography.bodySmall)
        Spacer(modifier = Modifier.height(8.dp))
        Row(modifier = Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.spacedBy(12.dp)) {
            listOf("JPEG", "PNG").forEach { format ->
                ChipButton(
                    label = format,
                    icon = null,
                    selected = (format == uiState.compressionFormat),
                    onClick = { if (isEnabled) viewModel.updateCompressionFormat(format) },
                    enabled = isEnabled,
                    modifier = Modifier.padding(horizontal = 32.dp, vertical = 16.dp),
                )
            }
        }
        Spacer(modifier = Modifier.height(16.dp))
        Text(text = "Adjust Quality", style = MaterialTheme.typography.bodyMedium, fontWeight = FontWeight.SemiBold, color = MaterialTheme.colorScheme.onSurfaceVariant)
        Spacer(modifier = Modifier.height(4.dp))

        // Show format-specific quality explanation
        if (uiState.compressionFormat == "PNG") {
            WarningBanner("PNG is a lossless format that doesn't use quality settings")
//            Text(
//                "PNG is a lossless format that doesn't use quality settings",
//                style = MaterialTheme.typography.bodySmall,
//                color = MaterialTheme.colorScheme.error
//            )
        } else {
            Text(text = "Compression Quality ${uiState.compressionQuality.toInt()}%", style = MaterialTheme.typography.bodySmall)
        }

        Slider(
            value = uiState.compressionQuality,
            onValueChange = { if (isEnabled) viewModel.updateCompressionQuality(it) },
            valueRange = 10f..100f,
            steps = 17,
            colors = SliderDefaults.colors(
                thumbColor = MaterialTheme.colorScheme.primary,
                activeTrackColor = MaterialTheme.colorScheme.primary,
                activeTickColor = MaterialTheme.colorScheme.onPrimary
            ),
            enabled = isEnabled && uiState.compressionFormat != "PNG",
            modifier = Modifier.fillMaxWidth()
        )
    }
}```

### `app\src\main\java\com\example\doc_tools\features\image\compressimages\presentation\ui\components\FileSelectionSection.kt`

```kt
package com.example.doc_tools.features.image.compressimages.presentation.ui.components

import android.content.Context
import android.net.Uri
import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.rounded.FileOpen
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import com.example.doc_tools.core.common.model.FileDetails
import com.example.doc_tools.core.ui.components.card.FileInfoActionCard
import com.example.doc_tools.core.ui.components.file.FilePickerHandler
import com.example.doc_tools.features.image.compressimages.presentation.state.CompressImagesUiState
import com.example.doc_tools.features.image.compressimages.presentation.viewmodel.CompressImagesViewModel

@Composable
internal fun FileSelectionSection(
    uiState: CompressImagesUiState,
    context: Context,
    viewModel: CompressImagesViewModel,
    isDarkTheme: Boolean,
    isEnabled: Boolean
) {
    Column {
        Text(text = "Select Images", style = MaterialTheme.typography.bodyMedium, fontWeight = FontWeight.SemiBold, color = MaterialTheme.colorScheme.onSurfaceVariant)
        Spacer(modifier = Modifier.height(4.dp))
        Text(text = "Select one or more image files to compress", style = MaterialTheme.typography.bodySmall)
        Spacer(modifier = Modifier.height(8.dp))
        FilePickerHandler(
            single = false,
            supportedMimeTypes = listOf("image/*"),
            onPicked = { uris -> if (isEnabled && uris.isNotEmpty()) viewModel.addImages(context, uris) }
        ) { launchPicker, _ ->
            OutlinedButton(
                onClick = launchPicker,
                shape = RoundedCornerShape(14.dp),
                colors = ButtonDefaults.outlinedButtonColors(containerColor = MaterialTheme.colorScheme.primaryContainer, contentColor = MaterialTheme.colorScheme.onPrimaryContainer),
                contentPadding = PaddingValues(24.dp),
                border = BorderStroke(1.dp, MaterialTheme.colorScheme.onPrimaryContainer),
                modifier = Modifier.fillMaxWidth(),
                enabled = isEnabled
            ) {
                Icon(Icons.Rounded.FileOpen, contentDescription = null, modifier = Modifier.size(ButtonDefaults.IconSize))
                Spacer(modifier = Modifier.size(ButtonDefaults.IconSpacing))
                Text(text = "Select Images")
            }
        }
        if (uiState.selectedImageUris.isNotEmpty()) {
            val totalSize = uiState.imageDetailsMap.values.sumOf { it.size }
            val summaryDetails = FileDetails(
                name = "${uiState.selectedImageUris.size} Images Selected",
                uri = uiState.selectedImageUris.firstOrNull() ?: Uri.EMPTY,
                size = totalSize,
                mimeType = "image/*",
                path = "Various locations"
            )
            Spacer(modifier = Modifier.height(16.dp))
            Text(text = "Selected Image Detail's", style = MaterialTheme.typography.bodyMedium, fontWeight = FontWeight.SemiBold, color = MaterialTheme.colorScheme.onSurfaceVariant)
            Spacer(modifier = Modifier.height(16.dp))
            FileInfoActionCard(
                file = summaryDetails,
                showSize = true,
                showFormat = true,
                labelOverrides = mapOf("size" to "Total Size"),
                onOpen = { if (isEnabled) viewModel.toggleSelectedImagesBottomSheet(true) },
                onDelete = { if (isEnabled) viewModel.clearAllImages() },
                isDarkTheme = isDarkTheme,
                enabled = isEnabled
            )
        }
    }
}```

### `app\src\main\java\com\example\doc_tools\features\image\compressimages\presentation\viewmodel\CompressImagesViewModel.kt`

```kt
package com.example.doc_tools.features.image.compressimages.presentation.viewmodel

import android.content.Context
import android.net.Uri
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.doc_tools.features.image.compressimages.data.local.CompressImagesService
import com.example.doc_tools.features.image.compressimages.presentation.state.CompressImagesUiState
import com.example.doc_tools.core.common.model.FileDetails
import com.example.doc_tools.core.utils.image.ImageFormat
import com.example.doc_tools.core.domain.model.SaveMode
import com.example.doc_tools.core.presentation.state.ProcessingStateManager
import com.example.doc_tools.core.utils.file.SaveLocationUtils
import com.example.doc_tools.core.presentation.eventbus.UiMessageBus
import com.example.doc_tools.core.utils.file.FileBottomSheetUtils
import com.example.doc_tools.core.utils.file.FileInfoUtils
import com.example.doc_tools.core.utils.file.FileIoUtils
import kotlinx.coroutines.Job
import kotlinx.coroutines.delay
import kotlinx.coroutines.isActive
import kotlinx.coroutines.launch

/**
 * ViewModel for the Compress Images screen.
 *
 * This ViewModel is responsible for managing the UI state and business logic
 * related to image compression. It handles operations such as:
 * - Adding and removing images for compression.
 * - Updating compression settings (quality, format, save path, save mode).
 * - Initiating and managing the image compression process.
 * - Displaying progress and results of the compression.
 * - Handling errors and user feedback.
 * - Managing visibility of bottom sheets for selected and output images.
 */

class CompressImagesViewModel : ViewModel() {

    // The UI state exposed to the UI layer
    var uiState by mutableStateOf(CompressImagesUiState())
        private set

    // Reference to the current compression job
    private var compressionJob: Job? = null

    /**
     * Compresses the selected images based on the current UI state settings.
     *
     * This function performs the following steps:
     * 1. Validates that at least one image is selected and a valid save location is specified.
     * 2. Initializes the UI state for processing, showing a progress indicator.
     * 3. Launches a coroutine to perform the compression in the background.
     * 4. Iterates through each selected image URI:
     *     a. Retrieves the original file details.
     *     b. Creates a temporary file for the compressed image.
     *     c. Calls the `ImageService` to convert and compress the image to the specified format and quality.
     *     d. If compression is successful:
     *         i. Saves the compressed image to the chosen save location using the specified save mode.
     *         ii. Adds the details of the saved compressed file to a list.
     *         iii. Deletes the temporary compressed file.
     *     e. If compression fails, shows an error message and deletes the temporary file.
     *     f. Updates the processing progress.
     * 5. After processing all images:
     *     a. Updates the UI state with the list of output file details.
     *     b. Shows a success message indicating the number of images compressed and the percentage of space saved (if applicable).
     *     c. If the save mode is `ZIP_ARCHIVE` and more than one image was compressed:
     *         i. Creates a temporary ZIP file.
     *         ii. Adds each compressed image to the ZIP archive.
     *         iii. Saves the ZIP file to the chosen location.
     *         iv. Shows a success message for the ZIP file creation.
     *         v. Deletes the temporary ZIP file.
     *     d. If no images were successfully compressed, shows an error message.
     * 6. Catches any exceptions during the process and displays an error message.
     * 7. Finally, resets the processing state in the UI.
     *
     * @param context The Android [android.content.Context] used for file operations and accessing resources.
     * @param messageScope A string identifier for the [UiMessageBus] to display messages in the correct UI scope.
     */

    fun compressImages(context: Context, messageScope: String = "compress_images") {
        if (uiState.selectedImageUris.isEmpty()) {
            UiMessageBus.showError("Please select at least one image", messageScope)
            return
        }

        // Check global processing state - don't allow multiple processes
        if (!ProcessingStateManager.startProcess(messageScope)) {
            UiMessageBus.showError("Another process is already running. Please wait or cancel it first.", messageScope)
            return
        }

        // Start processing
        uiState = uiState.copy(
            isProcessing = true,
            processingProgress = 0f,
            errorMessage = null
        )

        viewModelScope.launch {
            try {
                val imageService = CompressImagesService(context)
                val results = mutableListOf<FileDetails>()
                val totalImages = uiState.selectedImageUris.size
                var processedCount = 0

                // Setup progress monitoring job
                val progressJob = launch {
                    while (isActive) {
                        delay(300) // Update every 300ms
                        val progress = if (totalImages > 0) {
                            processedCount.toFloat() / totalImages.toFloat()
                        } else 0f

                        // Update UI state with progress
                        uiState = uiState.copy(processingProgress = progress)

                        // Update global progress state
                        ProcessingStateManager.updateProgress(progress, messageScope)

                        // Stop if processing was cancelled
                        if (!uiState.isProcessing) break
                    }
                }

                for ((index, uri) in uiState.selectedImageUris.withIndex()) {
                    val imageDetails = uiState.imageDetailsMap[uri] ?: continue

                    // Check if processing was cancelled
                    if (!uiState.isProcessing) break

                    // Get the correct format from the format name
                    val imageFormat = when(uiState.compressionFormat.uppercase()) {
                        "JPEG" -> ImageFormat.JPG
                        "PNG" -> ImageFormat.PNG
                        else -> ImageFormat.JPG
                    }

                    // Create a temporary file for processing
                    val fileName = "compressed_${System.currentTimeMillis()}"
                    val extension = if (uiState.compressionFormat.uppercase() == "JPEG") ".jpg" else ".png"
                    val tempFile = FileIoUtils.createTempFile(
                        context,
                        fileName,
                        extension
                    ) ?: throw Exception("Failed to create temporary file")

                    // Call the service with the correct method
                    val result = imageService.convertImageFormat(
                        inputUri = uri,
                        outputFile = tempFile,
                        format = imageFormat,
                        quality = uiState.compressionQuality.toInt()
                    )

                    processedCount++

                    result.fold(
                        onSuccess = { processedFile ->
                            // Save to the desired location
                            val outputFileName = "compressed_${imageDetails.name}"

                            val savedUri = SaveLocationUtils.saveToLocation(
                                context = context,
                                sourceFile = processedFile,
                                outputFileName = outputFileName,
                                mimeType = "image/${extension.replace(".", "")}",
                                savePath = uiState.savePath,
                                saveMode = uiState.saveMode
                            )

                            if (savedUri != null) {
                                val fileDetails = FileInfoUtils.getFileDetails(context, savedUri)
                                if (fileDetails != null) {
                                    results.add(fileDetails)
                                }
                            }

                            // Clean up temp file
                            processedFile.delete()
                        },
                        onFailure = { error ->
                            // Continue processing other images even if one fails
                            UiMessageBus.showError("Failed to process ${imageDetails.name}: ${error.message}", messageScope)
                            tempFile.delete()
                        }
                    )
                }

                // Cancel progress monitoring job
                progressJob.cancel()

                if (results.isNotEmpty()) {
                    uiState = uiState.copy(
                        outputDetailsList = results,
                        processingProgress = 1f // Set to 100% when complete
                    )

                    val totalOriginal = uiState.imageDetailsMap.values.sumOf { it.size }
                    val totalCompressed = results.sumOf { it.size }
                    val savedPercent = ((totalOriginal - totalCompressed) * 100 / totalOriginal.toFloat()).toInt()

                    UiMessageBus.showSuccess(
                        "Compressed ${results.size} images (saved $savedPercent% space)",
                        messageScope
                    )
                } else {
                    UiMessageBus.showError("No images were compressed successfully", messageScope)
                }
            } catch (e: Exception) {
                UiMessageBus.showError("Error: ${e.message}", messageScope)
            } finally {
                uiState = uiState.copy(
                    isProcessing = false,
                    processingProgress = -1f
                )
                // End the process in the global state manager
                ProcessingStateManager.endProcess(messageScope)
            }
        }
    }


    /**
     * Update images list directly (used with FileBottomSheetUtils)
     */
    fun updateImagesList(context: Context, updatedUris: List<Uri>) {
        if (updatedUris.isEmpty()) {
            clearAllImages()
            return
        }

        FileBottomSheetUtils.updateImagesList(
            updatedUris = updatedUris,
            context = context,
            scope = viewModelScope,
            onUrisUpdate = { newUris ->
                uiState = uiState.copy(selectedImageUris = newUris)
            },
            onDetailsUpdate = { newDetailsMap ->
                @Suppress("UNCHECKED_CAST")
                uiState = uiState.copy(imageDetailsMap = newDetailsMap as Map<Uri, FileDetails>)
            },
            currentDetailsMap = uiState.imageDetailsMap,
            getFileDetails = { ctx, uri -> FileInfoUtils.getFileDetails(ctx, uri) },
            clearOutputDetails = { uiState = uiState.copy(outputDetailsList = emptyList()) }
        )
    }


    /**
     * Adds a list of image URIs to the current list of selected images.
     *
     * This function updates the UI state with the new list of selected images and clears
     * any existing output details. It then triggers an update of the image details
     * for the newly added images. If the provided list of URIs is empty, the function
     * returns without making any changes.
     *
     * @param context The application context, used for accessing content resolvers and file systems.
     * @param uris A list of [Uri] objects representing the images to be added.
     */
    fun addImages(context: Context, uris: List<Uri>) {
        if (uris.isEmpty()) return

        val updatedUris = uiState.selectedImageUris.toMutableList()
        updatedUris.addAll(uris)

        uiState = uiState.copy(
            selectedImageUris = updatedUris,
            outputDetailsList = emptyList()
        )
        // Update image details
        updateImageDetails(context)
    }


    /**
     * Removes a specified image from the list of selected images.
     * After removing the image, it updates the UI state and then refreshes
     * the details of the remaining selected images.
     *
     * @param context The application context, used to access content resolver and other system services.
     * @param uri The URI of the image to be removed.
     */
    fun removeImage(context: Context, uri: Uri) {
        val updatedUris = uiState.selectedImageUris.toMutableList()
        updatedUris.remove(uri)
        uiState = uiState.copy(selectedImageUris = updatedUris)
        // Update image details
        updateImageDetails(context)
    }


    /**
     * Clears all selected images from the UI state.
     * This function resets the list of selected image URIs, the map of image details,
     * the list of output details, and hides the selected images bottom sheet.
     */
    fun clearAllImages() {
        uiState = uiState.copy(
            selectedImageUris = emptyList(),
            imageDetailsMap = emptyMap(),
            outputDetailsList = emptyList(),
            showSelectedImagesBottomSheet = false
        )
    }


    /**
     * Updates the details for all selected images.
     * This function iterates through the `selectedImageUris` in the current UI state,
     * retrieves the file details for each URI using `FileUtils.getFileDetails`,
     * and updates the `imageDetailsMap` in the UI state with the fetched details.
     * This operation is performed asynchronously within a `viewModelScope.launch` block.
     *
     * @param context The application context, used to access content resolver for file details.
     */
    private fun updateImageDetails(context: Context) {
        viewModelScope.launch {
            val detailsMap = mutableMapOf<Uri, FileDetails>()

            for (uri in uiState.selectedImageUris) {
                val details = FileInfoUtils.getFileDetails(context, uri)
                if (details != null) {
                    detailsMap[uri] = details
                }
            }

            uiState = uiState.copy(imageDetailsMap = detailsMap)
        }
    }


    /**
     * Updates the compression quality setting in the UI state.
     *
     * @param quality The new compression quality value (typically between 0.0f and 1.0f,
     *                but the actual scale might depend on the underlying image processing library).
     */
    fun updateCompressionQuality(quality: Float) {
        uiState = uiState.copy(compressionQuality = quality)
    }


    /**
     * Updates the save path for the compressed images.
     * This path determines where the processed images will be stored.
     *
     * @param path The new save path string. This can be a directory path.
     */
    fun updateSavePath(path: String) {
        if (uiState.outputDetailsList.isNotEmpty()) {
            uiState = uiState.copy(savePath = path, outputDetailsList = emptyList())
        } else {
            uiState = uiState.copy(savePath = path)
        }
    }


    /**
     * Updates the save mode in the UI state.
     * The save mode determines how the compressed images are saved,
     * e.g., as individual files or as a ZIP archive.
     *
     * @param saveMode The new save mode to set.
     */
    fun updateSaveMode(saveMode: SaveMode) {
        if (uiState.outputDetailsList.isNotEmpty()) {
            uiState = uiState.copy(saveMode = saveMode, outputDetailsList = emptyList())
        } else {
            uiState = uiState.copy(saveMode = saveMode)
        }
    }


    /**
     * Updates the compression format in the UI state.
     *
     * @param format The new compression format to set (e.g., "JPEG", "PNG").
     */
    fun updateCompressionFormat(format: String) {
        uiState = uiState.copy(compressionFormat = format)
    }


    /**
     * Toggles the visibility of the bottom sheet that displays the list of selected images.
     *
     * @param show True to show the bottom sheet, false to hide it.
     */
    fun toggleSelectedImagesBottomSheet(show: Boolean) {
        uiState = uiState.copy(showSelectedImagesBottomSheet = show)
    }


    /**
     * Toggles the visibility of the bottom sheet displaying all output images.
     *
     * @param show True to show the bottom sheet, false to hide it.
     */
    fun toggleAllImagesBottomSheet(show: Boolean) {
        uiState = uiState.copy(showAllImagesBottomSheet = show)
    }


    /**
     * Cancels the ongoing image compression process.
     *
     * This function stops the current compression job, resets the compression job reference,
     * and updates the UI state to reflect that processing has stopped and clears the progress.
     */
    fun cancelCompression() {
        uiState = uiState.copy(isProcessing = false, processingProgress = -1f)
        // End the process in the global state manager
        ProcessingStateManager.endProcess("compress_images")
    }

    /**
     * Clears the list of output details from the UI state.
     * This is typically called when the user wants to clear the results of a previous compression operation.
     */
    fun clearOutputDetails() {
        uiState = uiState.copy(outputDetailsList = emptyList())
    }

}```

### `app\src\main\java\com\example\doc_tools\features\image\convertimages\presentation\state\ConvertImagesUiState.kt`

```kt
package com.example.doc_tools.features.image.convertimages.presentation.state

import android.net.Uri
import com.example.doc_tools.core.common.model.FileDetails
import com.example.doc_tools.core.utils.image.ImageFormat
import com.example.doc_tools.core.domain.model.SaveMode

/**
 * UI state for the ConvertImages screen
 */
data class ConvertImagesUiState(
    // Input image
    val selectedImageUri: Uri? = null,
    val originalImageDetails: FileDetails? = null,

    // Output details
    val outputDetails: FileDetails? = null,

    // Format and quality settings
    val selectedFormat: ImageFormat = ImageFormat.JPG,
    val quality: Float = 80f,
    val formatMenuExpanded: Boolean = false,

    // Save options
    val savePath: String = "",
    val saveMode: SaveMode = SaveMode.SEPARATELY,

    // Processing state
    val isProcessing: Boolean = false,
    val processingProgress: Float = -1f,
    val errorMessage: String? = null
) {
    /**
     * Helper method to get an ImageFormat by name
     */
    fun getFormatByName(name: String): ImageFormat {
        return when (name.uppercase()) {
            "JPEG" -> ImageFormat.JPG
            "PNG" -> ImageFormat.PNG
            "WEBP" -> ImageFormat.WEBP_LOSSY
            else -> ImageFormat.JPG
        }
    }
}```

### `app\src\main\java\com\example\doc_tools\features\image\convertimages\presentation\ui\ConvertImagesScreen.kt`

```kt
package com.example.doc_tools.features.image.convertimages.presentation.ui

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Transform
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.HorizontalDivider
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation.NavController
import com.example.doc_tools.core.ui.components.button.ProgressToolButton
import com.example.doc_tools.core.ui.components.card.FileInfoActionCard
import com.example.doc_tools.core.ui.components.file.ChangeSaveLocation
import com.example.doc_tools.core.ui.components.layout.BaseToolScreen
import com.example.doc_tools.core.ui.components.overlay.ProcessingAware
import com.example.doc_tools.core.ui.components.tool_layout.HeaderSection
import com.example.doc_tools.core.utils.file.FileActionsUtils.shareFile
import com.example.doc_tools.core.utils.file.FileActionsUtils.viewFile
import com.example.doc_tools.features.image.convertimages.presentation.ui.components.ConversionSettingsSection
import com.example.doc_tools.features.image.convertimages.presentation.ui.components.FileSelectionSection
import com.example.doc_tools.features.image.convertimages.presentation.viewmodel.ConvertImagesViewModel


/**
 * Screen for converting image format and quality
 */
@Composable
fun ConvertImagesScreen(
    navController: NavController,
    isDarkTheme: Boolean,
    onThemeToggle: () -> Unit,
    modifier: Modifier = Modifier,
    viewModel: ConvertImagesViewModel = viewModel()
) {
    val context = LocalContext.current
    val uiState = viewModel.uiState
    val messageScope = "convert_images"

    BaseToolScreen(
        title = "Convert Images",
        navController = navController,
        isDarkTheme = isDarkTheme,
        onThemeToggle = onThemeToggle,
        contentScrollable = true,
        messageScope = messageScope,
        showThemeToggle = false, // Hide theme toggle since it's now in Settings
        modifier = modifier
    ) {
        Card(
            modifier = Modifier.fillMaxWidth().padding(vertical = 8.dp),
            colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surface),
            elevation = CardDefaults.cardElevation(defaultElevation = 1.dp),
            shape = RoundedCornerShape(16.dp)
        ) {
            Column(modifier = Modifier.padding(24.dp), verticalArrangement = Arrangement.spacedBy(16.dp)) {

                HeaderSection(icon = Icons.Default.Transform, title = "Convert Image Format", subtitle = "Convert images between JPG, PNG, and WebP formats.")
                HorizontalDivider(color = MaterialTheme.colorScheme.outline)
                ProcessingAware { isEnabled -> FileSelectionSection(uiState, context, viewModel, isDarkTheme, isEnabled) }
                HorizontalDivider(color = MaterialTheme.colorScheme.outline)
                ProcessingAware { isEnabled -> ConversionSettingsSection(uiState, viewModel, isEnabled) }
                
                if (uiState.originalImageDetails != null) {
                    ProcessingAware { isEnabled ->
                        ChangeSaveLocation(
                            visible = true,
                            defaultSaveLocation = uiState.savePath,
                            onSaveLocationChanged = { if (isEnabled) viewModel.updateSavePath(it) },
                            saveModeEnabled = false,
                            initialSaveMode = uiState.saveMode,
                            onSaveModeChanged = { if (isEnabled) viewModel.updateSaveMode(it) },
                            modifier = Modifier.fillMaxWidth()
                        )
                    }
                }

                // Progress button remains interactive for cancellation
                ProgressToolButton(
                    onClick = { 
                        if (uiState.isProcessing) {
                            viewModel.cancelProcessing()
                        } else {
                            viewModel.convertImage(context, messageScope)
                        }
                    },
                    isProcessing = uiState.isProcessing,
                    progress = uiState.processingProgress,
                    enabled = uiState.selectedImageUri != null,
                    text = "Convert Image",
                    icon = Icons.Default.Transform,
                    errorMessage = if (uiState.isProcessing) null else uiState.errorMessage,
                    processingText = "Conversion in progress",
                )

                ProcessingAware { isEnabled ->
                    uiState.outputDetails?.let { details ->
                        Text("Converted Image Format Detail's", style = MaterialTheme.typography.bodyMedium, fontWeight = FontWeight.SemiBold, color = MaterialTheme.colorScheme.onSurfaceVariant)
                        FileInfoActionCard(
                            file = details,
                            showName = true,
                            showSize = true,
                            showFormat = true,
                            showDimensions = true,
                            onOpen = { if (isEnabled) viewFile(context, details.uri, details.mimeType) },
                            onShare = { if (isEnabled) shareFile(context, details.uri, details.mimeType) },
                            onDelete = { if (isEnabled) viewModel.clearOutputDetails() },
                            isDarkTheme = isDarkTheme,
                            enabled = isEnabled
                        )
                    }
                }
            }
        }
    }
}
```

### `app\src\main\java\com\example\doc_tools\features\image\convertimages\presentation\ui\components\ConversionSettingSection.kt`

```kt
package com.example.doc_tools.features.image.convertimages.presentation.ui.components

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Slider
import androidx.compose.material3.SliderDefaults
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import com.example.doc_tools.core.ui.components.button.ChipButton
import com.example.doc_tools.features.image.convertimages.presentation.state.ConvertImagesUiState
import com.example.doc_tools.features.image.convertimages.presentation.viewmodel.ConvertImagesViewModel

@Composable
internal fun ConversionSettingsSection(
    uiState: ConvertImagesUiState,
    viewModel: ConvertImagesViewModel,
    isEnabled: Boolean
) {
    Column(modifier = Modifier.fillMaxWidth()) {
        Text("Select Output Format", style = MaterialTheme.typography.bodyMedium, fontWeight = FontWeight.SemiBold, color = MaterialTheme.colorScheme.onSurfaceVariant)
        Spacer(modifier = Modifier.height(4.dp))
        Text("Choose the desired format for your converted image", style = MaterialTheme.typography.bodySmall)
        Spacer(modifier = Modifier.height(8.dp))
        Row(modifier = Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.spacedBy(12.dp)) {
            listOf("JPEG", "PNG", "WebP").forEach { format ->
                ChipButton(
                    label = format,
                    icon = null,
                    selected = when (format) {
                        "JPEG" -> uiState.selectedFormat.displayName == "JPEG"
                        "PNG" -> uiState.selectedFormat.displayName == "PNG"
                        "WebP" -> uiState.selectedFormat.displayName.contains("WebP", ignoreCase = true)
                        else -> false
                    },
                    onClick = {
                        if (isEnabled) viewModel.updateSelectedFormat(uiState.getFormatByName(format))
                    },
                    enabled = isEnabled,
                    modifier = Modifier.padding(horizontal = 32.dp, vertical = 16.dp),
                )
            }
        }
        Spacer(modifier = Modifier.height(16.dp))

        // Always show quality slider, regardless of format
        Text("Adjust Quality", style = MaterialTheme.typography.bodyMedium, fontWeight = FontWeight.SemiBold, color = MaterialTheme.colorScheme.onSurfaceVariant)
        Spacer(modifier = Modifier.height(4.dp))

        // Show format-specific quality explanation
        if (uiState.selectedFormat.displayName == "PNG") {
            Text(
                "PNG is a lossless format that doesn't use quality settings",
                style = MaterialTheme.typography.bodySmall,
                color = MaterialTheme.colorScheme.error
            )
        } else {
            Text("Compression Quality ${uiState.quality.toInt()}%", style = MaterialTheme.typography.bodySmall)
        }

        Slider(
            value = uiState.quality,
            onValueChange = { if (isEnabled) viewModel.updateQuality(it) },
            valueRange = 10f..100f,
            steps = 8,
            modifier = Modifier.fillMaxWidth(),
            colors = SliderDefaults.colors(
                thumbColor = MaterialTheme.colorScheme.primary,
                activeTrackColor = MaterialTheme.colorScheme.primary,
                activeTickColor = MaterialTheme.colorScheme.onPrimary,
            ),
            enabled = isEnabled && uiState.selectedFormat.supportsQuality
        )

        // Add spacer at the bottom for better UI spacing
        Spacer(modifier = Modifier.height(8.dp))
    }
}```

### `app\src\main\java\com\example\doc_tools\features\image\convertimages\presentation\ui\components\FileSelectionSection.kt`

```kt
package com.example.doc_tools.features.image.convertimages.presentation.ui.components

import android.content.Context
import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.rounded.FileOpen
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import com.example.doc_tools.core.ui.components.card.FileInfoActionCard
import com.example.doc_tools.core.ui.components.file.FilePickerHandler
import com.example.doc_tools.core.utils.file.FileActionsUtils.viewFile
import com.example.doc_tools.features.image.convertimages.presentation.state.ConvertImagesUiState
import com.example.doc_tools.features.image.convertimages.presentation.viewmodel.ConvertImagesViewModel

@Composable
internal fun FileSelectionSection(
    uiState: ConvertImagesUiState,
    context: Context,
    viewModel: ConvertImagesViewModel,
    isDarkTheme: Boolean,
    isEnabled: Boolean
) {
    Column {
        Text("Select Image", style = MaterialTheme.typography.bodyMedium, fontWeight = FontWeight.SemiBold, color = MaterialTheme.colorScheme.onSurfaceVariant)
        Spacer(modifier = Modifier.height(4.dp))
        Text("Select image for change format Ex: 'jpg' to 'png'", style = MaterialTheme.typography.bodySmall)
        Spacer(modifier = Modifier.height(8.dp))

        FilePickerHandler(
            single = true,
            supportedMimeTypes = listOf("image/*"),
            onPicked = { uris -> if (uris.isNotEmpty() && isEnabled) viewModel.selectImage(context, uris.first()) }
        ) { launchPicker, _ ->
            OutlinedButton(
                onClick = launchPicker,
                shape = RoundedCornerShape(14.dp),
                colors = ButtonDefaults.outlinedButtonColors(
                    containerColor = MaterialTheme.colorScheme.primaryContainer,
                    contentColor = MaterialTheme.colorScheme.onPrimaryContainer
                ),
                contentPadding = PaddingValues(24.dp),
                border = BorderStroke(1.dp, MaterialTheme.colorScheme.onPrimaryContainer),
                modifier = Modifier.fillMaxWidth(),
                enabled = isEnabled
            ) {
                Icon(Icons.Rounded.FileOpen, contentDescription = null, modifier = Modifier.size(ButtonDefaults.IconSize))
                Spacer(modifier = Modifier.size(ButtonDefaults.IconSpacing))
                Text("Select Image")
            }
        }

        uiState.originalImageDetails?.let { details ->
            Spacer(modifier = Modifier.height(16.dp))
            Text("Selected Image Detail's", style = MaterialTheme.typography.bodyMedium, fontWeight = FontWeight.SemiBold, color = MaterialTheme.colorScheme.onSurfaceVariant)
            Spacer(modifier = Modifier.height(16.dp))

            FileInfoActionCard(
                file = details,
                showName = true,
                showSize = true,
                showFormat = true,
                showDimensions = true,
                onOpen = { if (isEnabled) viewFile(context, details.uri, details.mimeType) },
                onDelete = { if (isEnabled) viewModel.clearSelectedImage() },
                isDarkTheme = isDarkTheme,
                enabled = isEnabled
            )
        }
    }
}```

### `app\src\main\java\com\example\doc_tools\features\image\convertimages\presentation\viewmodel\ConvertImagesViewModel.kt`

```kt
package com.example.doc_tools.features.image.convertimages.presentation.viewmodel

import android.content.Context
import android.net.Uri
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.doc_tools.features.image.convertimages.data.local.ConvertImagesFormatService
import com.example.doc_tools.features.image.convertimages.presentation.state.ConvertImagesUiState
import com.example.doc_tools.core.utils.image.ImageFormat
import com.example.doc_tools.core.domain.model.SaveMode
import com.example.doc_tools.core.presentation.state.ProcessingStateManager
import com.example.doc_tools.core.utils.file.SaveLocationUtils
import com.example.doc_tools.core.presentation.eventbus.UiMessageBus
import com.example.doc_tools.core.utils.file.FileInfoUtils
import com.example.doc_tools.core.utils.file.FileIoUtils
import kotlinx.coroutines.delay
import kotlinx.coroutines.isActive
import kotlinx.coroutines.launch

/**
 * ViewModel for the ConvertImages screen
 */
class ConvertImagesViewModel : ViewModel() {

    var uiState by mutableStateOf(ConvertImagesUiState())
        private set

    /**
     * Select an image for conversion
     */
    fun selectImage(context: Context, uri: Uri) {
        val details = FileInfoUtils.getFileDetails(context, uri)
        uiState = uiState.copy(
            selectedImageUri = uri,
            originalImageDetails = details,
            outputDetails = null
        )
    }

    /**
     * Clear the selected image
     */
    fun clearSelectedImage() {
        uiState = uiState.copy(
            selectedImageUri = null,
            originalImageDetails = null,
            outputDetails = null
        )
    }

    /**
     * Clear the output details
     */
    fun clearOutputDetails() {
        uiState = uiState.copy(outputDetails = null)
    }

    /**
     * Update the selected format
     */
    fun updateSelectedFormat(format: ImageFormat) {
        uiState = uiState.copy(selectedFormat = format)
    }

    /**
     * Update the quality setting
     */
    fun updateQuality(quality: Float) {
        uiState = uiState.copy(quality = quality)
    }

    /**
     * Toggle the format menu
     */
    fun toggleFormatMenu(expanded: Boolean) {
        uiState = uiState.copy(formatMenuExpanded = expanded)
    }

    /**
     * Update the save path
     */
    fun updateSavePath(path: String) {
        uiState = uiState.copy(savePath = path)
    }

    /**
     * Update the save mode
     */
    fun updateSaveMode(mode: SaveMode) {
        uiState = uiState.copy(saveMode = mode)
    }

    /**
     * Convert the selected image to the chosen format
     */
    fun convertImage(context: Context, messageScope: String = "convert_images") {
        if (uiState.selectedImageUri == null) {
            UiMessageBus.showError("Please select an image to convert", messageScope)
            return
        }

        // Check global processing state - don't allow multiple processes
        if (!ProcessingStateManager.startProcess(messageScope)) {
            UiMessageBus.showError("Another process is already running. Please wait or cancel it first.", messageScope)
            return
        }

        // Start processing
        uiState = uiState.copy(
            isProcessing = true,
            processingProgress = 0f,
            errorMessage = null
        )

        viewModelScope.launch {
            try {
                val imageFormat = uiState.selectedFormat
                val originalUri = uiState.selectedImageUri ?: return@launch

                // Setup progress monitor
                val progressJob = launch {
                    var progress = 0f
                    while (isActive && progress < 0.95f) {
                        delay(200)
                        progress += 0.05f
                        uiState = uiState.copy(processingProgress = progress)
                        ProcessingStateManager.updateProgress(progress, messageScope)

                        if (!uiState.isProcessing) break
                    }
                }

                // Create temporary file for output
                val originalFileName = uiState.originalImageDetails?.name ?: "converted"
                val fileExtension = when (imageFormat.displayName) {
                    "JPEG", "JPG" -> ".jpg"
                    "PNG" -> ".png"
                    "WebP (Lossy)", "WebP (Lossless)" -> ".webp"
                    else -> ".jpg"
                }

                val tempFile = FileIoUtils.createTempFile(
                    context,
                    "converted_$originalFileName",
                    fileExtension
                )

                if (tempFile == null) {
                    UiMessageBus.showError("Failed to create temporary file", messageScope)
                    progressJob.cancel()
                    uiState = uiState.copy(isProcessing = false, processingProgress = -1f)
                    ProcessingStateManager.endProcess(messageScope)
                    return@launch
                }

                // Perform the conversion
                val convertService = ConvertImagesFormatService(context)
                val result = convertService.convertImageFormat(
                    inputUri = originalUri,
                    outputFile = tempFile,
                    format = imageFormat,
                    quality = uiState.quality.toInt()
                )

                progressJob.cancel()

                result.fold(
                    onSuccess = {
                        // Generate output filename
                        val outputFileName = "converted_${originalFileName}${fileExtension}"

                        // Save to chosen location
                        val savedUri = SaveLocationUtils.saveToLocation(
                            context = context,
                            sourceFile = tempFile,
                            outputFileName = outputFileName,
                            mimeType = "image/${imageFormat.displayName.lowercase()}",
                            savePath = uiState.savePath,
                            saveMode = uiState.saveMode
                        )

                        if (savedUri != null) {
                            val fileDetails = FileInfoUtils.getFileDetails(context, savedUri)
                            if (fileDetails != null) {
                                uiState = uiState.copy(outputDetails = fileDetails, processingProgress = 1f)
                                UiMessageBus.showSuccess("Image converted successfully", messageScope)
                            }
                        } else {
                            UiMessageBus.showError("Failed to save converted image", messageScope)
                        }
                        tempFile.delete()
                    },
                    onFailure = { error ->
                        UiMessageBus.showError("Failed to convert image: ${error.message}", messageScope)
                        tempFile.delete()
                    }
                )
            } catch (e: Exception) {
                UiMessageBus.showError("Error: ${e.message}", messageScope)
            } finally {
                // End processing
                uiState = uiState.copy(isProcessing = false, processingProgress = -1f)
                ProcessingStateManager.endProcess(messageScope)
            }
        }
    }

    /**
     * Cancel the conversion process
     */
    fun cancelProcessing() {
        uiState = uiState.copy(isProcessing = false, processingProgress = -1f)
        // End process in global state manager
        ProcessingStateManager.endProcess("convert_images")
    }
}```

### `app\src\main\java\com\example\doc_tools\features\pdf\compresspdf\domain\model\CompressionMode.kt`

```kt
package com.example.doc_tools.features.pdf.compresspdf.domain.model

/**
 * Available compression modes for PDF compression
 */
enum class CompressionMode {
    /**
     * Automatically choose the best mode based on PDF content
     */
    AUTO,

    /**
     * Only optimize metadata and remove unnecessary information
     */
    METADATA_ONLY,

    /**
     * Selectively compress images while preserving text and vector graphics
     */
    SMART,

    /**
     * Rasterize entire document (convert all pages to images)
     */
    RASTERIZE
}```

### `app\src\main\java\com\example\doc_tools\features\pdf\compresspdf\presentation\state\CompressPdfUiState.kt`

```kt
package com.example.doc_tools.features.pdf.compresspdf.presentation.state

import android.net.Uri
import com.example.doc_tools.core.common.model.FileDetails
import com.example.doc_tools.core.domain.model.SaveMode

/**
 * Data class representing the UI state for the Compress PDF screen
 */
data class CompressPdfUiState(
    val selectedPdfUri: Uri? = null,
    val compressionQuality: Float = 75f,
    val isProcessing: Boolean = false,
    val progress: Float = -1f,
    val fileSize: Long = 0L,
    val showLargeFileWarning: Boolean = false,
    val outputDetails: FileDetails? = null,
    val pdfPageCount: Int = 0,
    val savePath: String = "Downloads",
    val saveMode: SaveMode = SaveMode.SEPARATELY,
    val errorMessage: String? = null,
    val estimatedTimeRemaining: String? = null
)```

### `app\src\main\java\com\example\doc_tools\features\pdf\compresspdf\presentation\ui\CompressPdfScreen.kt`

```kt
package com.example.doc_tools.features.pdf.compresspdf.presentation.ui

import androidx.navigation.NavController
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Compress
import androidx.compose.material.icons.filled.Warning
import androidx.compose.material.icons.rounded.Compress
import androidx.compose.material3.AlertDialog
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.HorizontalDivider
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.SnackbarHostState
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.lifecycle.viewmodel.compose.viewModel
import com.example.doc_tools.core.ui.components.layout.BaseToolScreen
import com.example.doc_tools.core.ui.components.tool_layout.HeaderSection
import com.example.doc_tools.core.ui.components.card.FileInfoActionCard
import com.example.doc_tools.core.ui.components.button.ProgressToolButton
import com.example.doc_tools.core.ui.components.file.ChangeSaveLocation
import com.example.doc_tools.core.ui.components.overlay.ProcessingAware
import com.example.doc_tools.features.pdf.compresspdf.presentation.viewmodel.CompressPdfViewModel
import com.example.doc_tools.core.utils.file.FileInfoUtils
import com.example.doc_tools.core.utils.file.FileActionsUtils.viewFile
import com.example.doc_tools.core.utils.file.FileActionsUtils.shareFile
import com.example.doc_tools.features.pdf.compresspdf.presentation.ui.components.CompressionQualitySection
import com.example.doc_tools.features.pdf.compresspdf.presentation.ui.components.FileSelectionSection


/**
 *
 * Composable function for the Compress PDF screen.
 * This screen allows users to select a PDF file, adjust compression quality,
 * and then compress the file to reduce its size.
 *
 * @param navController The NavController for navigating between screens.
 * @param isDarkTheme A boolean indicating whether the dark theme is currently active.
 * @param onThemeToggle A lambda function to toggle the theme.
 * @param modifier A Modifier to be applied to the root composable.
 * @param viewModel The [CompressPdfViewModel] instance for managing the screen's state and logic.
 * Defaults to a new instance provided by `viewModel()`.
 *
 */

@Composable
fun CompressPdfScreen(
    navController: NavController,
    isDarkTheme: Boolean,
    onThemeToggle: () -> Unit,
    modifier: Modifier = Modifier,
    viewModel: CompressPdfViewModel = viewModel()
) {
    val context = LocalContext.current
    val uiState = viewModel.uiState
    val snackbarHostState = remember { SnackbarHostState() }
    val messageScope = "compress_pdf"

    BaseToolScreen(
        title = "Compress PDF",
        navController = navController,
        isDarkTheme = isDarkTheme,
        onThemeToggle = onThemeToggle,
        contentScrollable = true,
        messageScope = messageScope,
        showThemeToggle = false, // Hide theme toggle since it's now in Settings
        modifier = modifier
    ) {
        Card(
            modifier = Modifier.fillMaxWidth().padding(vertical = 8.dp),
            colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surface, contentColor = MaterialTheme.colorScheme.onSurface),
            elevation = CardDefaults.cardElevation(defaultElevation = 1.dp),
            shape = RoundedCornerShape(24.dp)
        ) {
            Column(modifier = Modifier.padding(24.dp), verticalArrangement = Arrangement.spacedBy(16.dp)) {
                HeaderSection(icon = Icons.Rounded.Compress, title = "Compress PDF", subtitle = "Reduce PDF file size while preserving quality.")
                HorizontalDivider(color = MaterialTheme.colorScheme.outline)
                FileSelectionSection(uiState, context, viewModel, isDarkTheme)
                HorizontalDivider(color = MaterialTheme.colorScheme.outline)
                ProcessingAware { isEnabled -> CompressionQualitySection(uiState, viewModel, isEnabled) }

                if (uiState.selectedPdfUri != null) {
                    ChangeSaveLocation(
                        visible = true,
                        defaultSaveLocation = uiState.savePath,
                        onSaveLocationChanged = { viewModel.updateSavePath(it) },
                        saveModeEnabled = false,
                        initialSaveMode = uiState.saveMode,
                        onSaveModeChanged = { viewModel.changeSaveMode(it) },
                        modifier = Modifier.fillMaxWidth()
                    )
                }

                // Progress button should remain interactive even during processing
                ProgressToolButton(
                    onClick = { 
                        if (uiState.isProcessing) {
                            viewModel.cancelCompression()
                        } else {
                            viewModel.startCompression(context, messageScope)
                        }
                    },
                    isProcessing = uiState.isProcessing,
                    progress = uiState.progress,
                    enabled = uiState.selectedPdfUri != null,
                    text = "Compress PDF",
                    icon = Icons.Default.Compress,
                    errorMessage = if (uiState.isProcessing) null else uiState.errorMessage,
                    processingText = "Compression in progress"
                )
                
                ProcessingAware { isEnabled ->
                    uiState.outputDetails?.let { details ->
                        Text(text = "Compressed File Detail's", style = MaterialTheme.typography.bodyMedium, fontWeight = FontWeight.SemiBold, color = MaterialTheme.colorScheme.onSurfaceVariant)
                        FileInfoActionCard(
                            file = details,
                            showSize = false,
                            showFormat = true,
                            showCompression = true,
                            compressionInfo = uiState.selectedPdfUri?.let { uri ->
                                val originalSize = FileInfoUtils.getFileSize(context, uri)
                                if (originalSize > 0 && details.size > 0) Pair(originalSize, details.size) else null
                            },
                            onOpen = { if (isEnabled) viewFile(context, details.uri, details.mimeType) },
                            onShare = { if (isEnabled) shareFile(context, details.uri, details.mimeType) },
                            onDelete = { if (isEnabled) viewModel.clearOutputDetails() },
                            isDarkTheme = isDarkTheme,
                            enabled = isEnabled
                        )
                    }
                }
            }
        }
    }

    // Small components below
    if (uiState.showLargeFileWarning) {
        AlertDialog(
            onDismissRequest = { viewModel.dismissLargeFileWarning() },
            icon = { Icon(imageVector = Icons.Filled.Warning, contentDescription = null, tint = MaterialTheme.colorScheme.error) },
            title = { Text("Large File Detected") },
            text = { Text("This file is quite large. Compression may take several minutes.") },
            confirmButton = { TextButton(onClick = { viewModel.dismissLargeFileWarning() }) { Text("Understand") } }
        )
    }
}


```

### `app\src\main\java\com\example\doc_tools\features\pdf\compresspdf\presentation\ui\components\CompressionQualitySection.kt`

```kt
package com.example.doc_tools.features.pdf.compresspdf.presentation.ui.components

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Slider
import androidx.compose.material3.SliderDefaults
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import com.example.doc_tools.features.pdf.compresspdf.presentation.state.CompressPdfUiState
import com.example.doc_tools.features.pdf.compresspdf.presentation.viewmodel.CompressPdfViewModel

@Composable
internal fun CompressionQualitySection(uiState: CompressPdfUiState, viewModel: CompressPdfViewModel, isEnabled: Boolean) {
    Column(modifier = Modifier.fillMaxWidth()) {
        Text(text = "Adjust Quality", style = MaterialTheme.typography.bodyMedium, fontWeight = FontWeight.SemiBold, color = MaterialTheme.colorScheme.onSurfaceVariant)
        Spacer(modifier = Modifier.height(4.dp))
        Text(text = "Compression quality ${uiState.compressionQuality.toInt()}%", style = MaterialTheme.typography.bodySmall)
        Spacer(modifier = Modifier.height(4.dp))
        Slider(
            value = uiState.compressionQuality,
            onValueChange = { if (isEnabled) viewModel.updateQuality(it) },
            valueRange = 10f..100f,
            steps = 9,
            modifier = Modifier.fillMaxWidth(),
            colors = SliderDefaults.colors(
                thumbColor = MaterialTheme.colorScheme.primary,
                activeTrackColor = MaterialTheme.colorScheme.primary,
                activeTickColor = MaterialTheme.colorScheme.onPrimary,
            ),
            enabled = isEnabled
        )
        Spacer(modifier = Modifier.height(8.dp))
        Row(modifier = Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.SpaceBetween) {
            Text(text = "Smaller size", style = MaterialTheme.typography.bodySmall)
            Text(text = "Better quality", style = MaterialTheme.typography.bodySmall)
        }
    }
}```

### `app\src\main\java\com\example\doc_tools\features\pdf\compresspdf\presentation\ui\components\FileSelectionSection.kt`

```kt
package com.example.doc_tools.features.pdf.compresspdf.presentation.ui.components

import android.content.Context
import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.rounded.FileOpen
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import com.example.doc_tools.core.common.model.FileDetails
import com.example.doc_tools.core.ui.components.card.FileInfoActionCard
import com.example.doc_tools.core.ui.components.file.FilePickerHandler
import com.example.doc_tools.core.ui.components.overlay.ProcessingAware
import com.example.doc_tools.core.utils.file.FileActionsUtils.viewFile
import com.example.doc_tools.core.utils.file.FileInfoUtils
import com.example.doc_tools.features.pdf.compresspdf.presentation.state.CompressPdfUiState
import com.example.doc_tools.features.pdf.compresspdf.presentation.viewmodel.CompressPdfViewModel

@Composable
internal fun FileSelectionSection(uiState: CompressPdfUiState, context: Context, viewModel: CompressPdfViewModel, isDarkTheme: Boolean) {
    Column {
        Text(text = "Select Pdf File", style = MaterialTheme.typography.bodyMedium, fontWeight = FontWeight.SemiBold, color = MaterialTheme.colorScheme.onSurfaceVariant)
        Spacer(modifier = Modifier.height(4.dp))
        Text(text = "Choose the PDF file you want to compress from your device's storage.", style = MaterialTheme.typography.bodySmall)
        Spacer(modifier = Modifier.height(8.dp))

        if (uiState.selectedPdfUri == null) {
            ProcessingAware { isEnabled ->
                FilePickerHandler(
                    single = true,
                    supportedMimeTypes = listOf("application/pdf"),
                    onPicked = { uris -> if (uris.isNotEmpty() && isEnabled) viewModel.onFilePicked(context, uris.first()) }
                ) { launchPicker, _ ->
                    OutlinedButton(
                        onClick = launchPicker,
                        shape = RoundedCornerShape(14.dp),
                        colors = ButtonDefaults.outlinedButtonColors(containerColor = MaterialTheme.colorScheme.primaryContainer, contentColor = MaterialTheme.colorScheme.onPrimaryContainer),
                        contentPadding = PaddingValues(24.dp),
                        border = BorderStroke(1.dp, MaterialTheme.colorScheme.onPrimaryContainer),
                        modifier = Modifier.fillMaxWidth(),
                        enabled = isEnabled
                    ) {
                        Icon(Icons.Rounded.FileOpen, contentDescription = null, modifier = Modifier.size(ButtonDefaults.IconSize))
                        Spacer(modifier = Modifier.size(ButtonDefaults.IconSpacing))
                        Text(text = "Select PDF File")
                    }
                }
            }
        }
        else {
            ProcessingAware { isEnabled ->
                Text(text = "Selected File Detail's", style = MaterialTheme.typography.bodyMedium, fontWeight = FontWeight.SemiBold, color = MaterialTheme.colorScheme.onSurfaceVariant)
                FileInfoActionCard(
                    file = FileDetails(
                        name = FileInfoUtils.getFileName(context, uiState.selectedPdfUri) ?: "Unknown",
                        size = uiState.fileSize,
                        mimeType = "application/pdf",
                        uri = uiState.selectedPdfUri,
                        pageCount = uiState.pdfPageCount.takeIf { it > 0 }
                    ),
                    showSize = true,
                    showFormat = true,
                    showPages = true,
                    onDelete = { if (isEnabled) viewModel.clearSelectedFile() },
                    onOpen = { if (isEnabled) viewFile(context, uiState.selectedPdfUri, "application/pdf") },
                    isDarkTheme = isDarkTheme,
                    enabled = isEnabled
                )
            }
        }
    }
}
```

### `app\src\main\java\com\example\doc_tools\features\pdf\compresspdf\presentation\viewmodel\CompressPdfViewModel.kt`

```kt
package com.example.doc_tools.features.pdf.compresspdf.presentation.viewmodel

import android.content.Context
import android.net.Uri
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.doc_tools.features.pdf.compresspdf.data.local.CompressPdfService
import com.example.doc_tools.features.pdf.compresspdf.presentation.state.CompressPdfUiState
import com.example.doc_tools.core.domain.model.SaveMode
import com.example.doc_tools.core.presentation.state.ProcessingStateManager
import com.example.doc_tools.core.utils.file.SaveLocationUtils
import com.example.doc_tools.core.presentation.eventbus.UiMessageBus
import com.example.doc_tools.core.utils.file.FileInfoUtils
import com.example.doc_tools.core.utils.file.FileIoUtils
import kotlinx.coroutines.Job
import kotlinx.coroutines.launch
import java.io.FileOutputStream

/**
 * ViewModel for the Compress PDF screen.
 *
 * This ViewModel is responsible for managing the UI state and handling the business logic
 * related to compressing PDF files. It interacts with the `PdfService` to perform
 * the actual compression and uses `FileUtils` and `SaveLocationUtils` for file operations.
 *
 * Key responsibilities include:
 * - Managing the selected PDF file and its details (URI, size, page count).
 * - Handling user input for compression quality, save mode, and save path.
 * - Initiating and managing the asynchronous PDF compression process.
 * - Updating the UI with progress, estimated time remaining, and results (success/failure).
 * - Displaying appropriate messages (errors, snackbars, success notifications) via `UiMessageBus`.
 * - Handling potential errors and exceptions during the compression process.
 * - Providing methods to clear selected files, output details, and cancel ongoing operations.
 *
 * The UI state is exposed via a `CompressPdfUiState` object, which is observed by the UI layer
 * to reflect changes in real-time.
 */
class CompressPdfViewModel : ViewModel() {

    // The UI state exposed to the UI layer
    var uiState by mutableStateOf(CompressPdfUiState())
        private set

    // Private properties
    private var compressionJob: Job? = null
    private var startTime: Long = 0

    /**
     * Starts the PDF compression process.
     *
     * This function performs the following steps:
     * 1. Validates that a PDF file has been selected and a save location is specified.
     * 2. Cancels any ongoing compression job.
     * 3. Launches a new coroutine to handle the compression process asynchronously.
     * 4. Updates the UI state to indicate processing and reset progress.
     * 5. Creates a temporary file to store the input PDF.
     * 6. Copies the selected PDF content to the temporary file.
     * 7. Calls the `PdfService.compressPdf()` method to perform the actual compression.
     *    - During compression, it updates the UI with progress and estimated time remaining.
     * 8. Handles the result of the compression:
     *    - **On success:**
     *        - Determines the output filename.
     *        - Saves the compressed file to the specified location and save mode.
     *        - Displays a success message.
     *        - Updates the UI with details of the compressed file (size, compression ratio).
     *        - Cleans up temporary files.
     *    - **On failure:**
     *        - Displays an error message.
     *        - Cleans up the temporary input file.
     * 9. Catches any exceptions during the process and displays an error message.
     * 10. In the `finally` block, resets the processing state, progress, and estimated time remaining,
     *     and clears the compression job.
     *
     * @param context The application context.
     * @param messageScope A string identifier for the UI scope where messages (errors, snackbars) should be displayed.
     */
    fun startCompression(context: Context, messageScope: String) {
        val currentState = uiState
        val selectedUri = currentState.selectedPdfUri

        // Clear any previous error message
        uiState = currentState.copy(errorMessage = null)

        if (selectedUri == null) {
            UiMessageBus.showError("Please select a PDF file first", messageScope)
            return
        }

        // Validate save location
        if (!SaveLocationUtils.validateSaveLocation(currentState.savePath)) {
            UiMessageBus.showSnackbar("Please specify a save location", messageScope)
            return
        }

        // Check global processing state - don't allow multiple processes
        if (!ProcessingStateManager.startProcess(messageScope)) {
            UiMessageBus.showError("Another process is already running. Please wait or cancel it first.", messageScope)
            return
        }

        // Cancel any existing job
        compressionJob?.cancel()

        // Start new compression job
        compressionJob = viewModelScope.launch {
            try {
                // Set UI state to processing mode
                uiState = currentState.copy(
                    isProcessing = true,
                    progress = 0f
                )
                startTime = System.currentTimeMillis()

                val pdfService = CompressPdfService(context)

                // 1. Create temp file for processing
                val tempInputFile = FileIoUtils.createTempFile(context, "pdf_input", ".pdf")
                if (tempInputFile == null) {
                    UiMessageBus.showError("Failed to create temporary file", messageScope)
                    uiState = uiState.copy(isProcessing = false)
                    ProcessingStateManager.endProcess(messageScope)
                    return@launch
                }

                // 2. Copy the selected PDF to the temp file
                context.contentResolver.openInputStream(selectedUri)?.use { input ->
                    FileOutputStream(tempInputFile).use { output ->
                        input.copyTo(output)
                    }
                }

                // Final compression quality as int
                val quality = currentState.compressionQuality.toInt()

                // 3. Compress the PDF and get resulting file
                val compressionResult = pdfService.compressPdf(
                    inputFile = tempInputFile,
                    compressionLevel = quality,
                    onProgressUpdate = { progress ->
                        uiState = uiState.copy(progress = progress)

                        // Update global progress state
                        ProcessingStateManager.updateProgress(progress, messageScope)

                        // Calculate estimated time remaining
                        if (progress > 0.05f) { // Only estimate after some progress
                            val elapsedTime = System.currentTimeMillis() - startTime
                            val totalEstimatedTime = (elapsedTime / progress).toLong()
                            val remainingTime = totalEstimatedTime - elapsedTime
                            uiState = uiState.copy(estimatedTimeRemaining = formatTimeRemaining(remainingTime))
                        }
                    }
                )

                compressionResult.fold(
                    onSuccess = { compressedFile ->
                        // 3. Determine final output filename
                        val originalFileName = FileInfoUtils.getFileName(context, selectedUri)
                        // Ensure .pdf extension is removed if present before appending
                        val baseName = originalFileName.removeSuffix(".pdf")
                        val outputFileName = "compressed_${baseName}.pdf"

                        // 4. Save to chosen location based on selected type
                        val finalUri = SaveLocationUtils.saveToLocation(
                            context,
                            compressedFile,
                            outputFileName,
                            "application/pdf",
                            currentState.savePath,
                            currentState.saveMode
                        )

                        if (finalUri != null) {
                            UiMessageBus.showSnackbar("PDF compressed successfully!", messageScope)
                            // 5. Get details of the FINAL saved file
                            val details = FileInfoUtils.getFileDetails(context, finalUri)

                            uiState = uiState.copy(outputDetails = details)

                            // Get compression ratio
                            val originalSize = FileInfoUtils.getFileSize(context, selectedUri)
                            val compressedSize = details?.size ?: 0
                            val compressionRatio = if (originalSize > 0) {
                                (1 - (compressedSize.toFloat() / originalSize)).coerceIn(0f, 1f)
                            } else 0f

                            UiMessageBus.showSuccess("PDF compressed by ${(compressionRatio * 100).toInt()}%!", messageScope)
                        } else {
                            UiMessageBus.showError("Failed to save compressed file", messageScope)
                            uiState = uiState.copy(outputDetails = null)
                        }

                        // Clean up temp files
                        tempInputFile.delete()
                        compressedFile.delete()
                    },
                    onFailure = { error ->
                        UiMessageBus.showError("Compression failed: ${error.message}", messageScope)
                        tempInputFile.delete()
                    }
                )
            } catch (e: Exception) {
                UiMessageBus.showError("Error: ${e.message}", messageScope)
                ProcessingStateManager.endProcess(messageScope)
            } finally {
                // Always reset UI state when done
                uiState = uiState.copy(
                    isProcessing = false,
                    progress = -1f,
                    estimatedTimeRemaining = null
                )
                compressionJob = null
                // Ensure we end the process even if something goes wrong
                ProcessingStateManager.endProcess(messageScope)
            }
        }
    }

    /**
     * Handles when a PDF file is picked from the file picker
     */
    fun onFilePicked(context: Context, uri: Uri) {
        val fileSize = FileInfoUtils.getFileSize(context, uri)

        uiState = uiState.copy(
            selectedPdfUri = uri,
            outputDetails = null,
            fileSize = fileSize,
            showLargeFileWarning = fileSize > 10 * 1024 * 1024 // Show warning for files > 10MB
        )

        // Extract page count using PdfService
        viewModelScope.launch {
            try {
                val pdfService = CompressPdfService(context)
                val pageCount = pdfService.getPageCount(context, uri)
                uiState = uiState.copy(pdfPageCount = pageCount)
            } catch (e: Exception) {
                // Handle error, but don't show to user since this is auxiliary functionality
                uiState = uiState.copy(pdfPageCount = 0)
            }
        }
    }

    /**
     * Updates the compression quality value
     */
    fun updateQuality(quality: Float) {
        uiState = uiState.copy(compressionQuality = quality)
    }

    /**
     * Changes the save mode
     */
    fun changeSaveMode(saveMode: SaveMode) {
        if (uiState.outputDetails != null) {
            uiState = uiState.copy(saveMode = saveMode, outputDetails = null)
        } else {
            uiState = uiState.copy(saveMode = saveMode)
        }
    }

    /**
     * Updates the save path
     */
    fun updateSavePath(path: String) {
        if (uiState.outputDetails != null) {
            uiState = uiState.copy(savePath = path, outputDetails = null)
        } else {
            uiState = uiState.copy(savePath = path)
        }
    }

    /**
     * Dismisses the large file warning
     */
    fun dismissLargeFileWarning() {
        uiState = uiState.copy(showLargeFileWarning = false)
    }

    /**
     * Clears the selected PDF file
     */
    fun clearSelectedFile() {
        uiState = uiState.copy(selectedPdfUri = null, outputDetails = null, pdfPageCount = 0)
    }

    /**
     * Clears the output details
     */
    fun clearOutputDetails() {
        uiState = uiState.copy(outputDetails = null, pdfPageCount = 0)
    }

    /**
     * Cancels the ongoing compression job
     */
    fun cancelCompression() {
        compressionJob?.cancel()
        compressionJob = null
        uiState = uiState.copy(isProcessing = false, progress = -1f, estimatedTimeRemaining = null)
        // Make sure to end the process when canceling
        ProcessingStateManager.endProcess("compress_pdf")
    }

    /**
     * Format milliseconds into a human-readable time remaining string
     */
    private fun formatTimeRemaining(milliseconds: Long): String {
        if (milliseconds <= 0) return "less than a second"

        val seconds = milliseconds / 1000
        val minutes = seconds / 60

        return when {
            minutes > 0 -> "$minutes min ${seconds % 60} sec"
            seconds > 0 -> "$seconds seconds"
            else -> "less than a second"
        }
    }
}```

### `app\src\main\java\com\example\doc_tools\features\pdf\imagestopdf\presentation\state\ImagesToPdfUiState.kt`

```kt
package com.example.doc_tools.features.pdf.imagestopdf.presentation.state

import android.net.Uri
import com.example.doc_tools.core.common.model.FileDetails
import com.example.doc_tools.core.domain.model.SaveMode

/**
 * Data class representing the UI state for the Images to PDF screen
 */
data class ImagesToPdfUiState(
    val selectedImageUris: List<Uri> = emptyList(),
    val imageDetailsMap: Map<Uri, FileDetails> = emptyMap(),
    val isProcessing: Boolean = false,
    val processingProgress: Float = -1f,
    val outputDetails: FileDetails? = null,
    val pdfPageCount: Int = 0,
    val savePath: String = "Downloads",
    val saveMode: SaveMode = SaveMode.SEPARATELY,
    val showSelectedImagesBottomSheet: Boolean = false,
    val errorMessage: String? = null,
    val paperSize: String = "A4",
    val imageAlignment: String = "FIT_PAGE"
)```

### `app\src\main\java\com\example\doc_tools\features\pdf\imagestopdf\presentation\ui\ImagesToPdfScreen.kt`

```kt
package com.example.doc_tools.features.pdf.imagestopdf.presentation.ui

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.PictureAsPdf
import androidx.compose.material.icons.rounded.PictureAsPdf
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.HorizontalDivider
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation.NavController
import com.example.doc_tools.core.ui.components.button.ProgressToolButton
import com.example.doc_tools.core.ui.components.card.FileInfoActionCard
import com.example.doc_tools.core.ui.components.file.ChangeSaveLocation
import com.example.doc_tools.core.ui.components.file.FileBottomSheet
import com.example.doc_tools.core.ui.components.layout.BaseToolScreen
import com.example.doc_tools.core.ui.components.overlay.ProcessingAware
import com.example.doc_tools.core.ui.components.tool_layout.HeaderSection
import com.example.doc_tools.core.utils.file.FileActionsUtils.shareFile
import com.example.doc_tools.core.utils.file.FileActionsUtils.viewFile
import com.example.doc_tools.features.pdf.imagestopdf.presentation.ui.components.FileSelectionSection
import com.example.doc_tools.features.pdf.imagestopdf.presentation.ui.components.PdfSettingsSection
import com.example.doc_tools.features.pdf.imagestopdf.presentation.viewmodel.ImagesToPdfViewModel


/**
 * Screen for converting images to PDF
 */
@Composable
fun ImagesToPdfScreen(
    navController: NavController,
    isDarkTheme: Boolean,
    onThemeToggle: () -> Unit,
    modifier: Modifier = Modifier,
    viewModel: ImagesToPdfViewModel = viewModel()
) {
    val context = LocalContext.current
    val uiState = viewModel.uiState
    val messageScope = "images_to_pdf"

    BaseToolScreen(
        title = "Images to PDF",
        navController = navController,
        isDarkTheme = isDarkTheme,
        onThemeToggle = onThemeToggle,
        contentScrollable = true,
        messageScope = messageScope,
        showThemeToggle = false, // Hide theme toggle since it's now in Settings
        modifier = modifier
    ) {
        Card(
            modifier = Modifier.fillMaxWidth().padding(vertical = 8.dp),
            colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surface, contentColor = MaterialTheme.colorScheme.onSurface),
            elevation = CardDefaults.cardElevation(defaultElevation = 1.dp),
            shape = RoundedCornerShape(24.dp)
        ) {
            Column(verticalArrangement = Arrangement.spacedBy(16.dp), modifier = Modifier.padding(24.dp)) {
                HeaderSection(icon = Icons.Rounded.PictureAsPdf, title = "Images to PDF", subtitle = "Convert images into a JPG, PNG, WebP into a single PDF document.")
                HorizontalDivider(color = MaterialTheme.colorScheme.outline)
                ProcessingAware { isEnabled -> FileSelectionSection(uiState, context, viewModel, isDarkTheme, isEnabled) }
                HorizontalDivider(color = MaterialTheme.colorScheme.outline)
                ProcessingAware { isEnabled -> PdfSettingsSection(uiState, viewModel, isEnabled) }
                
                if (uiState.selectedImageUris.isNotEmpty()) {
                    ProcessingAware { isEnabled ->
                        ChangeSaveLocation(
                            visible = true,
                            defaultSaveLocation = uiState.savePath,
                            onSaveLocationChanged = { if (isEnabled) viewModel.updateSavePath(it) },
                            saveModeEnabled = false,
                            initialSaveMode = uiState.saveMode,
                            onSaveModeChanged = { if (isEnabled) viewModel.updateSaveMode(it) },
                            modifier = Modifier.fillMaxWidth()
                        )
                    }
                }
                
                // Progress button should remain interactive
                ProgressToolButton(
                    onClick = {
                        if (uiState.isProcessing) {
                            viewModel.cancelProcessing() 
                        } else {
                            viewModel.convertImagesToPdf(context, messageScope)
                        }
                    },
                    isProcessing = uiState.isProcessing,
                    progress = uiState.processingProgress,
                    enabled = uiState.selectedImageUris.isNotEmpty(),
                    text = "Create PDF",
                    icon = Icons.Default.PictureAsPdf,
                    errorMessage = if (uiState.isProcessing) null else uiState.errorMessage,
                    processingText = "Processing",
                )
                
                ProcessingAware { isEnabled ->
                    uiState.outputDetails?.let { details ->
                        Text(text = "Converted pdf detail's", style = MaterialTheme.typography.bodyMedium, fontWeight = FontWeight.SemiBold, color = MaterialTheme.colorScheme.onSurfaceVariant)
                        FileInfoActionCard(
                            file = details,
                            showSize = true,
                            showFormat = true,
                            showPages = true,
                            onOpen = { if (isEnabled) viewFile(context, details.uri, details.mimeType) },
                            onShare = { if (isEnabled) shareFile(context, details.uri, details.mimeType) },
                            onDelete = { if (isEnabled) viewModel.clearOutputDetails() },
                            isDarkTheme = isDarkTheme,
                            enabled = isEnabled
                        )
                    }
                }
            }
        }
        
        // Only show the bottom sheet if not processing
        if (uiState.showSelectedImagesBottomSheet && !uiState.isProcessing) {
            FileBottomSheet(
                show = uiState.showSelectedImagesBottomSheet && uiState.selectedImageUris.isNotEmpty(),
                onDismiss = { viewModel.toggleImagesBottomSheet(false) },
                fileUris = uiState.selectedImageUris,
                title = "Selected Images",
                showDimensions = true,
                onFilesUpdated = { viewModel.updateImagesList(context, it) },
                isDarkTheme = isDarkTheme,
                onFileView = { uri, mimeType -> viewFile(context, uri, mimeType) },
                enableFileViewButton = true
            )
        }
    }
}
```

### `app\src\main\java\com\example\doc_tools\features\pdf\imagestopdf\presentation\ui\components\FileSelectionSection.kt`

```kt
package com.example.doc_tools.features.pdf.imagestopdf.presentation.ui.components

import android.content.Context
import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.rounded.FileOpen
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.core.net.toUri
import com.example.doc_tools.core.common.model.FileDetails
import com.example.doc_tools.core.ui.components.card.FileInfoActionCard
import com.example.doc_tools.core.ui.components.file.FilePickerHandler
import com.example.doc_tools.features.pdf.imagestopdf.presentation.state.ImagesToPdfUiState
import com.example.doc_tools.features.pdf.imagestopdf.presentation.viewmodel.ImagesToPdfViewModel

@Composable
internal fun FileSelectionSection(
    uiState: ImagesToPdfUiState,
    context: Context,
    viewModel: ImagesToPdfViewModel,
    isDarkTheme: Boolean,
    isEnabled: Boolean
) {
    Column {
        Text(text = "Select images", style = MaterialTheme.typography.bodyMedium, fontWeight = FontWeight.SemiBold, color = MaterialTheme.colorScheme.onSurfaceVariant)
        Spacer(modifier = Modifier.height(4.dp))
        Text(text = "Select one or more image files to convert", style = MaterialTheme.typography.bodySmall)
        Spacer(modifier = Modifier.height(8.dp))
        FilePickerHandler(
            single = false,
            supportedMimeTypes = listOf("image/*"),
            onPicked = { uris -> if (isEnabled) viewModel.addImages(context, uris) }
        ) { launchPicker, _ ->
            OutlinedButton(
                onClick = launchPicker,
                shape = RoundedCornerShape(14.dp),
                colors = ButtonDefaults.outlinedButtonColors(containerColor = MaterialTheme.colorScheme.primaryContainer, contentColor = MaterialTheme.colorScheme.onPrimaryContainer),
                contentPadding = PaddingValues(24.dp),
                border = BorderStroke(1.dp, MaterialTheme.colorScheme.onPrimaryContainer),
                modifier = Modifier.fillMaxWidth().padding(vertical = 0.dp),
                enabled = isEnabled
            ) {
                Icon(Icons.Rounded.FileOpen, contentDescription = null, modifier = Modifier.size(ButtonDefaults.IconSize))
                Spacer(modifier = Modifier.size(ButtonDefaults.IconSpacing))
                Text(text = "Select Images")
            }
        }
        if (uiState.selectedImageUris.isNotEmpty()) {
            val totalSize = uiState.imageDetailsMap.values.sumOf { it.size }
            val summaryDetails = FileDetails(
                name = "${uiState.selectedImageUris.size} Images Selected",
                uri = uiState.selectedImageUris.firstOrNull() ?: "content://placeholder/images_pdf".toUri(),
                size = totalSize,
                mimeType = "image/*",
                path = "Various locations"
            )
            Spacer(modifier = Modifier.height(16.dp))
            Text(text = "Selected image detail's", style = MaterialTheme.typography.bodyMedium, fontWeight = FontWeight.SemiBold, color = MaterialTheme.colorScheme.onSurfaceVariant)
            Spacer(modifier = Modifier.height(16.dp))
            FileInfoActionCard(
                file = summaryDetails,
                showSize = true,
                showFormat = true,
                labelOverrides = mapOf("size" to "Total Size"),
                onOpen = { if (isEnabled) viewModel.toggleImagesBottomSheet(true) },
                onDelete = { if (isEnabled) viewModel.clearAllImages() },
                isDarkTheme = isDarkTheme,
                enabled = isEnabled
            )
        }
    }
}


```

### `app\src\main\java\com\example\doc_tools\features\pdf\imagestopdf\presentation\ui\components\PdfSettingSection.kt`

```kt
package com.example.doc_tools.features.pdf.imagestopdf.presentation.ui.components

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.height
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Description
import androidx.compose.material.icons.filled.PhotoSizeSelectLarge
import androidx.compose.material.icons.filled.VerticalAlignCenter
import androidx.compose.material.icons.filled.ViewAgenda
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import com.example.doc_tools.core.ui.components.button.ChipButton
import com.example.doc_tools.features.pdf.imagestopdf.presentation.state.ImagesToPdfUiState
import com.example.doc_tools.features.pdf.imagestopdf.presentation.viewmodel.ImagesToPdfViewModel

@Composable
internal fun PdfSettingsSection(
    uiState: ImagesToPdfUiState,
    viewModel: ImagesToPdfViewModel,
    isEnabled: Boolean
) {
    Column {
        // Paper Size selection with ChipButton
        Text(
            text = "Paper Size",
            style = MaterialTheme.typography.bodyMedium,
            fontWeight = FontWeight.SemiBold,
            color = MaterialTheme.colorScheme.onSurfaceVariant
        )
        Spacer(modifier = Modifier.height(4.dp))
        Text(
            text = "Select the paper size for the PDF",
            style = MaterialTheme.typography.bodySmall,
            color = MaterialTheme.colorScheme.onSurfaceVariant.copy(alpha = 0.7f)
        )
        Spacer(modifier = Modifier.height(8.dp))
        val paperSizes = listOf("A4", "LETTER", "LEGAL")
        Row(horizontalArrangement = Arrangement.spacedBy(12.dp)) {
            paperSizes.forEach { size ->
                val icon = when (size) {
                    "A4" -> Icons.Default.Description
                    "LETTER" -> Icons.Default.ViewAgenda
                    "LEGAL" -> Icons.Default.PhotoSizeSelectLarge
                    else -> null
                }
                ChipButton(
                    label = size,
                    icon = null,
                    selected = uiState.paperSize == size,
                    onClick = { if (isEnabled) viewModel.updatePaperSize(size) },
                    enabled = isEnabled
                )
            }
        }
        Spacer(modifier = Modifier.height(16.dp))
        // Image Alignment selection with ChipButton
        Text(
            text = "Image Alignment",
            style = MaterialTheme.typography.bodyMedium,
            fontWeight = FontWeight.SemiBold,
            color = MaterialTheme.colorScheme.onSurfaceVariant
        )
        Spacer(modifier = Modifier.height(4.dp))
        Text(
            text = "Choose how images are aligned on the page",
            style = MaterialTheme.typography.bodySmall,
            color = MaterialTheme.colorScheme.onSurfaceVariant.copy(alpha = 0.7f)
        )
        Spacer(modifier = Modifier.height(8.dp))
        val alignments = listOf("FIT_PAGE", "CENTER", "ACTUAL_SIZE")
        Row(horizontalArrangement = Arrangement.spacedBy(12.dp)) {
            alignments.forEach { alignment ->
                val icon = when (alignment) {
                    "FIT_PAGE" -> Icons.Default.PhotoSizeSelectLarge
                    "CENTER" -> Icons.Default.VerticalAlignCenter
                    "ACTUAL_SIZE" -> Icons.Default.Description
                    else -> null
                }
                ChipButton(
                    label = alignment.replace('_', ' '),
                    icon = icon,
                    selected = uiState.imageAlignment == alignment,
                    onClick = { if (isEnabled) viewModel.updateImageAlignment(alignment) },
                    enabled = isEnabled
                )
            }
        }
    }
}```

### `app\src\main\java\com\example\doc_tools\features\pdf\imagestopdf\presentation\viewmodel\ImagesToPdfViewModel.kt`

```kt
package com.example.doc_tools.features.pdf.imagestopdf.presentation.viewmodel

import android.content.Context
import android.net.Uri
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.doc_tools.features.pdf.imagestopdf.data.local.ImagesToPdfService
import com.example.doc_tools.features.pdf.imagestopdf.presentation.state.ImagesToPdfUiState
import com.example.doc_tools.core.common.model.FileDetails
import com.example.doc_tools.core.domain.model.SaveMode
import com.example.doc_tools.core.presentation.state.ProcessingStateManager
import com.example.doc_tools.core.utils.file.SaveLocationUtils
import com.example.doc_tools.core.presentation.eventbus.UiMessageBus
import com.example.doc_tools.core.utils.file.FileBottomSheetUtils
import com.example.doc_tools.core.utils.file.FileInfoUtils
import com.example.doc_tools.core.utils.file.FileIoUtils
import kotlinx.coroutines.launch

/**
 * ViewModel for the Images to PDF screen.
 *
 * This ViewModel handles the business logic and state management for the Images to PDF feature.
 * It manages the list of selected images, their details, and the conversion process.
 * It also handles user interactions such as adding/removing images, setting conversion options,
 * and initiating the PDF conversion.
 *
 * Key Responsibilities:
 * - Managing the list of selected image URIs ([ImagesToPdfUiState.selectedImageUris]).
 * - Fetching and storing details for each selected image ([ImagesToPdfUiState.imageDetailsMap]).
 * - Handling user input for conversion options like save path, save mode, paper size, and image alignment.
 * - Performing the conversion of selected images to a PDF file.
 * - Updating the UI with processing status, progress, and any error messages.
 * - Managing the display of a bottom sheet for selected images.
 *
 * The main UI state is exposed via [uiState], which is an instance of [ImagesToPdfUiState].
 * All updates to the UI state are done by creating a new copy of the state object.
 *
 * The core conversion logic is encapsulated in the [convertImagesToPdf] function, which:
 * 1. Validates that at least one image is selected and a valid save location is provided.
 * 2. Creates a temporary file for the PDF output.
 * 3. Uses [PdfService.imagesToPdf] to perform the actual conversion.
 * 4. Saves the generated PDF to the user-specified location using [SaveLocationUtils].
 * 5. Updates the UI with the details of the created PDF or an error message.
 * 6. Cleans up temporary files.
 *
 * Other functions allow for:
 * - Adding and removing images from the selection ([addImages], [removeImage]).
 * - Clearing all selected images ([clearAllImages]).
 * - Updating image conversion parameters ([updateSavePath], [updateSaveMode], [updatePaperSize], [updateImageAlignment]).
 * - Toggling the visibility of a bottom sheet showing selected images ([toggleImagesBottomSheet]).
 * - Cancelling an ongoing conversion process ([cancelProcessing]).
 * - Clearing details of the previously generated PDF ([clearOutputDetails]).
 */

class ImagesToPdfViewModel : ViewModel() {

    // The UI state exposed to the UI layer
    var uiState by mutableStateOf(ImagesToPdfUiState())
        private set

    /**
     * Converts the selected images to a PDF file.
     *
     * This function performs the following steps:
     * 1. Validates that at least one image is selected.
     * 2. Validates the save location.
     * 3. Sets the UI state to indicate processing has started.
     * 4. Launches a coroutine to perform the conversion asynchronously:
     *    a. Creates a temporary output file for the PDF.
     *    b. Uses [PdfService.imagesToPdf] to convert the images.
     *    c. If successful:
     *        i. Generates a filename with the current date and time.
     *        ii. Saves the temporary PDF to the specified save location using [SaveLocationUtils.saveToLocation].
     *        iii. Updates the UI state with the details of the saved PDF and displays a success message.
     *        iv. Deletes the temporary output file.
     *    d. If unsuccessful:
     *        i. Displays an error message.
     *        ii. Deletes the temporary output file.
     * 5. Catches any exceptions during the process and displays an error message.
     * 6. Finally, updates the UI state to indicate processing has finished.
     *
     * @param context The application context.
     * @param messageScope A string identifier for the message scope, used by [UiMessageBus] to display messages.
     */

    fun convertImagesToPdf(context: Context, messageScope: String = "images_to_pdf") {

        if (uiState.selectedImageUris.isEmpty()) {
            UiMessageBus.showError("Please select at least one image to convert", messageScope)
            return
        }

        // Check global processing state - don't allow multiple processes
        if (!ProcessingStateManager.startProcess(messageScope)) {
            UiMessageBus.showError("Another process is already running. Please wait or cancel it first.", messageScope)
            return
        }

        uiState = uiState.copy(isProcessing = true, processingProgress = 0f)

        viewModelScope.launch {
            try {
                val imagesToPdfService = ImagesToPdfService(context)

                // Create a temporary file to store the converted PDF
                val tempOutputFile = FileIoUtils.createTempFile(context, "images_to_pdf", ".pdf")
                if (tempOutputFile == null) {
                    UiMessageBus.showError("Failed to create temporary file", messageScope)
                    uiState = uiState.copy(isProcessing = false)
                    ProcessingStateManager.endProcess(messageScope)
                    return@launch
                }

                // Convert images to PDF
                val result = imagesToPdfService.imagesToPdf(
                    imageUris = uiState.selectedImageUris,
                    outputFile = tempOutputFile,
                    paperSize = uiState.paperSize,
                    imageAlignment = uiState.imageAlignment,
                    onProgressUpdate = { progress ->
                        uiState = uiState.copy(processingProgress = progress)
                        // Update global progress
                        ProcessingStateManager.updateProgress(progress, messageScope)
                    }
                )

                result.fold(
                    onSuccess = { conversionResult ->
                        // Save the file to user's preferred location
                        val outputFileName = "images_to_pdf_${System.currentTimeMillis()}.pdf"
                        val savedUri = SaveLocationUtils.saveToLocation(
                            context = context,
                            sourceFile = tempOutputFile,
                            outputFileName = outputFileName,
                            mimeType = "application/pdf",
                            savePath = uiState.savePath,
                            saveMode = uiState.saveMode
                        )

                        // Clean up the temporary file
                        tempOutputFile.delete()

                        if (savedUri != null) {
                            val details = FileInfoUtils.getFileDetails(context, savedUri)
                            uiState = uiState.copy(
                                isProcessing = false,
                                processingProgress = 1f,
                                outputDetails = details,
                                errorMessage = null
                            )
                            UiMessageBus.showSuccess("Images converted to PDF successfully", messageScope)
                        } else {
                            uiState = uiState.copy(
                                isProcessing = false,
                                processingProgress = 0f,
                                errorMessage = "Failed to save the converted PDF file"
                            )
                            UiMessageBus.showError("Failed to save the converted PDF file", messageScope)
                        }
                    },
                    onFailure = { error ->
                        tempOutputFile.delete()
                        uiState = uiState.copy(
                            isProcessing = false,
                            processingProgress = 0f,
                            errorMessage = "Conversion failed: ${error.message}"
                        )
                        UiMessageBus.showError("Failed to convert images to PDF: ${error.message}", messageScope)
                    }
                )
            } catch (e: Exception) {
                    uiState = uiState.copy(
                        isProcessing = false,
                        processingProgress = 0f,
                        errorMessage = "Error: ${e.message}"
                    )
                    UiMessageBus.showError("Error during conversion: ${e.message}", messageScope)
                }
            finally {
                    // Always make sure to end the process in the global state manager
                    ProcessingStateManager.endProcess(messageScope)
            }
        }
    }

    /**
     * Update the image list directly (used with FileBottomSheetUtils)
     */
    fun updateImages(context: Context, updatedUris: List<Uri>) {
        uiState = uiState.copy(
            selectedImageUris = updatedUris,
            outputDetails = null
        )
        // Update image details
        updateImageDetails(context)
    }

    /**
     * Add images to the list
     */
    fun addImages(context: Context, uris: List<Uri>) {
        if (uris.isEmpty()) return

        val updatedUris = uiState.selectedImageUris.toMutableList()
        updatedUris.addAll(uris)

        uiState = uiState.copy(
            selectedImageUris = updatedUris,
            outputDetails = null
        )
        // Update image details
        updateImageDetails(context)
    }

    /**
     * Remove an image from the list
     */
    fun removeImage(context: Context, uri: Uri) {
        val updatedUris = uiState.selectedImageUris.toMutableList()
        updatedUris.remove(uri)
        uiState = uiState.copy(selectedImageUris = updatedUris)
        // Update image details
        updateImageDetails(context)
    }

    /**
     * Update details for all selected images
     */
    private fun updateImageDetails(context: Context) {
        viewModelScope.launch {
            val detailsMap = mutableMapOf<Uri, FileDetails>()

            for (uri in uiState.selectedImageUris) {
                val details = FileInfoUtils.getFileDetails(context, uri)
                if (details != null) { detailsMap[uri] = details }
            }
            uiState = uiState.copy(imageDetailsMap = detailsMap)
        }
    }

    /**
     * Clear all selected images
     */
    fun clearAllImages() {
        uiState = uiState.copy(selectedImageUris = emptyList(), imageDetailsMap = emptyMap(), outputDetails = null, showSelectedImagesBottomSheet = false)
    }

    /**
     * Update the save path
     */
    fun updateSavePath(path: String) {
        if (uiState.outputDetails != null) {
            uiState = uiState.copy(savePath = path, outputDetails = null)
        } else {
            uiState = uiState.copy(savePath = path)
        }
    }

    /**
     * Update the save mode
     */
    fun updateSaveMode(saveMode: SaveMode) {
        if (uiState.outputDetails != null) {
            uiState = uiState.copy(saveMode = saveMode, outputDetails = null)
        } else {
            uiState = uiState.copy(saveMode = saveMode)
        }
    }

    /**
     * Update the paper size
     */
    fun updatePaperSize(size: String) {
        uiState = uiState.copy(paperSize = size)
    }

    /**
     * Update the image alignment
     */
    fun updateImageAlignment(alignment: String) {
        uiState = uiState.copy(imageAlignment = alignment)
    }

    /**
     * Toggle the images bottom sheet visibility
     */
    fun toggleImagesBottomSheet(show: Boolean) {
        uiState = uiState.copy(showSelectedImagesBottomSheet = show)
    }

    /**
     * Update the list of images after reordering or deleting in the bottom sheet
     */
    fun updateImagesList(context: Context, updatedUris: List<Uri>) {
        FileBottomSheetUtils.updateImagesList(
            updatedUris = updatedUris,
            context = context,
            scope = viewModelScope,
            onUrisUpdate = { newUris ->
                uiState = uiState.copy(selectedImageUris = newUris)
            },
            onDetailsUpdate = { newDetailsMap ->
                @Suppress("UNCHECKED_CAST")
                uiState = uiState.copy(imageDetailsMap = newDetailsMap as Map<Uri, FileDetails>)
            },
            currentDetailsMap = uiState.imageDetailsMap,
            getFileDetails = { ctx, uri -> FileInfoUtils.getFileDetails(ctx, uri) },
            clearOutputDetails = { uiState = uiState.copy(outputDetails = null) }
        )
    }

    /**
     * Cancel the current processing
     */
    fun cancelProcessing() {
        uiState = uiState.copy(isProcessing = false, processingProgress = 0f)
        // End the process in the global state manager
        ProcessingStateManager.endProcess("images_to_pdf")
    }

    /**
     * Clear output details
     */
    fun clearOutputDetails() {
        uiState = uiState.copy(outputDetails = null)
    }

}```

### `app\src\main\java\com\example\doc_tools\features\pdf\mergepdf\domain\model\MergeResult.kt`

```kt
package com.example.doc_tools.features.pdf.mergepdf.domain.model

import java.io.File

/**
 * Result object for merge operations
 */
data class MergeResult(
    val file: File,
    val totalPages: Int
)```

### `app\src\main\java\com\example\doc_tools\features\pdf\mergepdf\presentation\state\MergePdfUiState.kt`

```kt
package com.example.doc_tools.features.pdf.mergepdf.presentation.state

import android.net.Uri
import com.example.doc_tools.core.common.model.FileDetails
import com.example.doc_tools.core.domain.model.SaveMode

/**
 * Data class representing the UI state for the Merge PDF screen
 */
data class MergePdfUiState(
    val selectedPdfUris: List<Uri> = emptyList(),
    val showSelectedFilesSheet: Boolean = false,
    val isProcessing: Boolean = false,
    val processingProgress: Float = -1f,
    val outputDetails: FileDetails? = null,
    val totalPageCount: Int = 0,
    val savePath: String = "Downloads",
    val saveMode: SaveMode = SaveMode.SEPARATELY,
    val showSaveLocationSelector: Boolean = false,
    val showConfirmMergeDialog: Boolean = false,
    val selectedItemsToRemove: List<Uri> = emptyList(),
    val showOutputFileBottomSheet: Boolean = false,
    val errorMessage: String? = null,
    val pdfDetailsMap: Map<android.net.Uri, com.example.doc_tools.core.common.model.FileDetails> = emptyMap()
)```

### `app\src\main\java\com\example\doc_tools\features\pdf\mergepdf\presentation\ui\MergePdfScreen.kt`

```kt
package com.example.doc_tools.features.pdf.mergepdf.presentation.ui

import android.content.Context
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.MergeType
import androidx.compose.material.icons.filled.PictureAsPdf
import androidx.compose.material.icons.rounded.Merge
import androidx.compose.material3.AlertDialog
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.HorizontalDivider
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.rememberCoroutineScope
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.core.net.toUri
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation.NavController
import com.example.doc_tools.core.common.model.FileDetails
import com.example.doc_tools.core.ui.components.button.ProgressToolButton
import com.example.doc_tools.core.ui.components.card.FileInfoActionCard
import com.example.doc_tools.core.ui.components.file.ChangeSaveLocation
import com.example.doc_tools.core.ui.components.file.FileBottomSheet
import com.example.doc_tools.core.ui.components.layout.BaseToolScreen
import com.example.doc_tools.core.ui.components.overlay.ProcessingAware
import com.example.doc_tools.core.ui.components.tool_layout.HeaderSection
import com.example.doc_tools.core.utils.file.FileActionsUtils.shareFile
import com.example.doc_tools.core.utils.file.FileActionsUtils.viewFile
import com.example.doc_tools.core.utils.file.FileInfoUtils
import com.example.doc_tools.features.pdf.mergepdf.presentation.state.MergePdfUiState
import com.example.doc_tools.features.pdf.mergepdf.presentation.ui.components.FileSelectionSection
import com.example.doc_tools.features.pdf.mergepdf.presentation.viewmodel.MergePdfViewModel
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.launch


/**
 * Screen for merging multiple PDF files into a single PDF
 */
@Composable
fun MergePdfScreen(
    navController: NavController,
    isDarkTheme: Boolean,
    onThemeToggle: () -> Unit,
    modifier: Modifier = Modifier,
    viewModel: MergePdfViewModel = viewModel()
) {
    val context = LocalContext.current
    val coroutineScope = rememberCoroutineScope()
    val uiState = viewModel.uiState
    val messageScope = "merge_pdf"

    BaseToolScreen(
        title = "Merge PDFs",
        navController = navController,
        isDarkTheme = isDarkTheme,
        onThemeToggle = onThemeToggle,
        contentScrollable = false,
        messageScope = messageScope,
        showThemeToggle = false, // Hide theme toggle since it's now in Settings
        modifier = modifier
    ) {
        Card(modifier = Modifier.fillMaxWidth().padding(vertical = 8.dp), shape = RoundedCornerShape(24.dp), colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surface, contentColor = MaterialTheme.colorScheme.onSurface), elevation = CardDefaults.cardElevation(defaultElevation = 1.dp)) {

            Column(modifier = Modifier.fillMaxWidth().verticalScroll(rememberScrollState()).padding(24.dp), verticalArrangement = Arrangement.spacedBy(16.dp)) {

                HeaderSection(icon = Icons.Rounded.Merge, title = "Merge PDFs", subtitle = "Combine multiple PDF files into a single PDF document.")
                HorizontalDivider(color = MaterialTheme.colorScheme.outline)
                ProcessingAware { isEnabled -> FileSelectionSection(viewModel, context, isEnabled) }
                ProcessingAware { isEnabled -> SelectedFilesSection(context, uiState, viewModel, isDarkTheme, isEnabled) }
                
                if(uiState.selectedPdfUris.isNotEmpty()) {
                    ProcessingAware { isEnabled ->
                        ChangeSaveLocation(
                            visible = true,
                            defaultSaveLocation = uiState.savePath,
                            onSaveLocationChanged = { if (isEnabled) viewModel.updateSavePath(it) },
                            saveModeEnabled = false,
                            initialSaveMode = uiState.saveMode,
                            onSaveModeChanged = { if (isEnabled) viewModel.changeSaveMode(it) },
                            modifier = Modifier.fillMaxWidth()
                        )
                    }
                }
                
                // Progress button with different behavior
                ProgressToolButton(
                    onClick = { 
                        if (uiState.isProcessing) {
                            viewModel.cancelMerge()
                        } else {
                            viewModel.toggleConfirmMergeDialog(true)
                        }
                    },
                    enabled = uiState.selectedPdfUris.size >= 2,  // Always enabled if files are selected
                    isProcessing = uiState.isProcessing,
                    progress = uiState.processingProgress,
                    text = "Merge PDFs",
                    icon = Icons.Default.MergeType,
                    processingText = "Merging in progress",
                )
                
                ProcessingAware { isEnabled ->
                    uiState.outputDetails?.let { details ->
                        Text(text = "Merged File Detail's", style = MaterialTheme.typography.bodyMedium, fontWeight = FontWeight.SemiBold, color = MaterialTheme.colorScheme.onSurfaceVariant)
                        //    Spacer(modifier = Modifier.height(16.dp))
                        FileInfoActionCard(
                            file = details,
                            showSize = true,
                            showFormat = true,
                            showPages = true,
                            showCompression = false,
                            labelOverrides = mapOf("size" to "Size", "format" to "Type", "pages" to "Pages"),
                            onOpen = { if (isEnabled) viewFile(context, details.uri, details.mimeType) },
                            onShare = { if (isEnabled) shareFile(context, details.uri, details.mimeType) },
                            onDelete = { if (isEnabled) viewModel.clearOutputDetails() },
                            isDarkTheme = isDarkTheme,
                            enabled = isEnabled
                        )
                    }
                }
            }
        }
        
        // Only show sheets and dialogs if not processing
        if (uiState.showSelectedFilesSheet && !uiState.isProcessing) {
            FileBottomSheet(
                show = uiState.showSelectedFilesSheet,
                onDismiss = { viewModel.toggleSelectedFilesSheet(false) },
                fileUris = uiState.selectedPdfUris,
                title = "Selected PDFs",
                onFilesUpdated = { updatedUris -> viewModel.updatePdfFiles(updatedUris, context) },
                isDarkTheme = isDarkTheme,
                fileTypeIcon = Icons.Default.PictureAsPdf,
                useCheckboxes = true,
                showIndexNumbers = true,
                showFileSize = true,
                showDimensions = false
            )
        }
        
        if (uiState.showConfirmMergeDialog && !uiState.isProcessing) {
            AlertDialog(
                onDismissRequest = { viewModel.toggleConfirmMergeDialog(false) },
                title = { Text("Confirm Merge") },
                text = { Text("Merge ${uiState.selectedPdfUris.size} PDF files into a single document?") },
                confirmButton = {
                    TextButton( onClick = {
                        viewModel.toggleConfirmMergeDialog(false)
                        coroutineScope.launch { viewModel.mergePdfFiles(context) }
                    }) {
                        Text(text = "Merge")
                    }
                },
                dismissButton = {
                    TextButton(onClick = { viewModel.toggleConfirmMergeDialog(false) }) {
                        Text(text = "Cancel")
                    }
                }
            )
        }
    }
}

@Composable
private fun SelectedFilesSection(
    context: Context,
    uiState: MergePdfUiState,
    viewModel: MergePdfViewModel,
    isDarkTheme: Boolean,
    isEnabled: Boolean
) {
    if (uiState.selectedPdfUris.isNotEmpty()) {
        val totalSize = uiState.selectedPdfUris.sumOf { FileInfoUtils.getFileSize(context, it) }
        val firstPdfUri = uiState.selectedPdfUris.firstOrNull() ?: "content://placeholder/merge_pdf".toUri()
        val Details = FileDetails(
            name = "${uiState.selectedPdfUris.size} PDFs Selected",
            uri = firstPdfUri,
            size = totalSize,
            mimeType = "application/pdf",
            path = "Various locations",
            pageCount = uiState.totalPageCount
        )
        Text(text = "Selected File Detail's", style = MaterialTheme.typography.bodyMedium, fontWeight = FontWeight.SemiBold, color = MaterialTheme.colorScheme.onSurfaceVariant)
//        Spacer(modifier = Modifier.height(16.dp))
        FileInfoActionCard(
            file = Details,
            showSize = true,
            showFormat = true,
            showPages = true,
            showCompression = false,
            labelOverrides = mapOf("size" to "Total Size", "format" to "Type", "pages" to "Total Pages"),
            onOpen = { if (isEnabled) viewModel.toggleSelectedFilesSheet(true) },
            onDelete = { if (isEnabled) viewModel.clearAllPdfs(context) },
            isDarkTheme = isDarkTheme,
            enabled = isEnabled
        )
    }
}


```

### `app\src\main\java\com\example\doc_tools\features\pdf\mergepdf\presentation\ui\components\FileSelectionSection.kt`

```kt
package com.example.doc_tools.features.pdf.mergepdf.presentation.ui.components

import android.content.Context
import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.rounded.FileOpen
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import com.example.doc_tools.core.ui.components.file.FilePickerHandler
import com.example.doc_tools.features.pdf.mergepdf.presentation.viewmodel.MergePdfViewModel

@Composable
internal fun FileSelectionSection(
    viewModel: MergePdfViewModel,
    context: Context,
    isEnabled: Boolean
) {
    Column {
        Text(
            text = "Select Pdf Files",
            style = MaterialTheme.typography.bodyMedium,
            fontWeight = FontWeight.SemiBold,
            color = MaterialTheme.colorScheme.onSurfaceVariant
        )
        Spacer(modifier = Modifier.height(4.dp))
        Text(text = "Choose two or more PDF files from your device to combine.", style = MaterialTheme.typography.bodySmall)
        Spacer(modifier = Modifier.height(8.dp))
        FilePickerHandler(
            single = false,
            supportedMimeTypes = listOf("application/pdf"),
            onPicked = { uris -> if (isEnabled) viewModel.addPdfFiles(uris, context) }
        ) { launchPicker, _ ->
            OutlinedButton(
                onClick = launchPicker,
                shape = RoundedCornerShape(14.dp),
                colors = ButtonDefaults.outlinedButtonColors(
                    containerColor = MaterialTheme.colorScheme.primaryContainer,
                    contentColor = MaterialTheme.colorScheme.onPrimaryContainer
                ),
                contentPadding = PaddingValues(24.dp),
                border = BorderStroke(1.dp, MaterialTheme.colorScheme.onPrimaryContainer),
                modifier = Modifier.fillMaxWidth(),
                enabled = isEnabled
            ) {
                Icon(
                    imageVector = Icons.Rounded.FileOpen,
                    contentDescription = null,
                    modifier = Modifier.size(ButtonDefaults.IconSize)
                )
                Spacer(modifier = Modifier.size(ButtonDefaults.IconSpacing))
                Text("Select PDF Files")
            }
        }
    }
}```

### `app\src\main\java\com\example\doc_tools\features\pdf\mergepdf\presentation\viewmodel\MergePdfViewModel.kt`

```kt
package com.example.doc_tools.features.pdf.mergepdf.presentation.viewmodel

import android.content.Context
import android.net.Uri
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.doc_tools.features.pdf.mergepdf.data.local.MergePdfService
import com.example.doc_tools.features.pdf.mergepdf.presentation.state.MergePdfUiState
import com.example.doc_tools.core.domain.model.SaveMode
import com.example.doc_tools.core.presentation.state.ProcessingStateManager
import com.example.doc_tools.core.utils.file.SaveLocationUtils
import com.example.doc_tools.core.presentation.eventbus.UiMessageBus
import com.example.doc_tools.core.utils.file.FileInfoUtils
import com.example.doc_tools.core.utils.file.FileIoUtils
import com.example.doc_tools.core.utils.pdf.PdfUtils
import com.example.doc_tools.core.utils.file.FileBottomSheetUtils
import kotlinx.coroutines.launch
import kotlin.collections.plus

/**
 * ViewModel for the Merge PDF screen that handles business logic and state management.
 *
 * This ViewModel manages the state of the Merge PDF screen, including the list of selected PDF files,
 * save location, and the progress of the merging process. It provides functions to add, remove, and
 * clear PDF files, as well as to initiate the merging process.
 *
 * The `mergePdfFiles` function is the core of this ViewModel. It performs the following steps:
 * 1. Validates that at least two PDF files are selected and a valid save location is specified.
 * 2. Updates the UI state to indicate that processing has started.
 * 3. Creates a temporary file to store the merged PDF.
 * 4. Calls the `PdfService.mergePdfFiles` method to perform the actual merging, with progress updates
 *    reported via a callback.
 * 5. If merging is successful, saves the temporary file to the specified save location using `SaveLocationUtils`.
 * 6. Displays a success message and updates the UI state with the details of the final saved file.
 * 7. Deletes the temporary file.
 * 8. If any error occurs during the process, displays an appropriate error message via `UiMessageBus`.
 * 9. Finally, updates the UI state to indicate that processing has finished.
 */
class MergePdfViewModel : ViewModel() {

    // The UI state exposed to the UI layer
    var uiState by mutableStateOf(MergePdfUiState())
        private set

    /**
     * Merges the selected PDF files into a single PDF file.
     *
     * This function first validates that at least two PDF files are selected and a valid save location is specified.
     * It then initiates the merging process by updating the UI state to reflect that processing has started.
     *
     * A temporary file is created to store the merged PDF. The `PdfService.mergePdfFiles` method is called
     * to perform the actual merging. Progress updates are reported via a callback, which updates the UI.
     *
     * Upon successful merging, the temporary file is saved to the specified save location using `SaveLocationUtils`.
     * A success message is displayed, and the details of the final saved file are updated in the UI state.
     * The temporary file is then deleted.
     *
     * If any error occurs during the process (e.g., failure to create a temporary file, merging error, saving error),
     * an appropriate error message is displayed via `UiMessageBus`.
     *
     * Finally, regardless of success or failure, the UI state is updated to indicate that processing has finished.
     *
     * @param context The application context.
     * @param messageScope A string identifier for the scope of UI messages, defaults to "merge_pdf".
     */
    suspend fun mergePdfFiles(context: Context, messageScope: String = "merge_pdf") {
        if (uiState.selectedPdfUris.size < 2) {
            UiMessageBus.showError("Please select at least 2 PDF files to merge", messageScope)
            return
        }

        // Check global processing state - don't allow multiple processes
        if (!ProcessingStateManager.startProcess(messageScope)) {
            UiMessageBus.showError("Another process is already running. Please wait or cancel it first.", messageScope)
            return
        }

        // Start merging process
        uiState = uiState.copy(isProcessing = true, processingProgress = 0f, showConfirmMergeDialog = false)

        viewModelScope.launch {
            try {
                val pdfService = MergePdfService(context)

                // Create temporary output file
                val tempOutputFile = FileIoUtils.createTempFile(context, "merged_pdf", ".pdf")
                if (tempOutputFile == null) {
                    UiMessageBus.showError("Failed to create temporary file", messageScope)
                    uiState = uiState.copy(isProcessing = false)
                    ProcessingStateManager.endProcess(messageScope)
                    return@launch
                }

                val mergeResult = pdfService.mergePdfFiles(
                    context = context,
                    pdfUris = uiState.selectedPdfUris,
                    outputFile = tempOutputFile,
                    onProgressUpdate = { current, total ->
                        val progress = current.toFloat() / total.toFloat()
                        uiState = uiState.copy(processingProgress = progress)
                        // Update global progress
                        ProcessingStateManager.updateProgress(progress, messageScope)
                    }
                )

                mergeResult.fold(
                    onSuccess = { result ->

                        val updatedTotalPageCount = result.totalPages
                        // Determine final output filename
                        val outputFileName = "merged_${System.currentTimeMillis()}.pdf"
                        // Save the merged file using SaveLocationUtils
                        val savedFileUri = SaveLocationUtils.saveToLocation(
                            context,
                            tempOutputFile,
                            outputFileName,
                            "application/pdf",
                            uiState.savePath,
                            uiState.saveMode
                        )

                        if (savedFileUri != null) {
                            UiMessageBus.showSuccess("${uiState.selectedPdfUris.size} PDFs merged successfully!", messageScope)
                            // Get details of the FINAL saved file
                            val details = FileInfoUtils.getFileDetails(context, savedFileUri)
                            uiState = uiState.copy(outputDetails = details, totalPageCount = updatedTotalPageCount)

                        } else {
                            UiMessageBus.showError("Failed to save merged file", messageScope)
                        }
                        // Clean up
                        tempOutputFile.delete()
                    },

                    onFailure = { error ->
                        UiMessageBus.showError("Failed to merge PDFs: ${error.message}", messageScope)
                    }
                )

            } catch (e: Exception) {
                UiMessageBus.showError("Error: ${e.message}", messageScope)
                ProcessingStateManager.endProcess(messageScope)
            } finally {
                uiState = uiState.copy(isProcessing = false, processingProgress = -1f)
                ProcessingStateManager.endProcess(messageScope)
            }
        }
    }

    /**
     * Update the list of PDF files directly (used with FileBottomSheetUtils)
     */
    fun updatePdfFiles(updatedUris: List<Uri>, context: Context? = null) {
        if (updatedUris.isEmpty()) {
            clearAllPdfs(context)
            return
        }
        if (context == null) {
            uiState = uiState.copy(selectedPdfUris = updatedUris, outputDetails = null)
            return
        }
        FileBottomSheetUtils.updateImagesList(
            updatedUris = updatedUris,
            context = context,
            scope = viewModelScope,
            onUrisUpdate = { newUris ->
                uiState = uiState.copy(selectedPdfUris = newUris)
            },
            onDetailsUpdate = { newDetailsMap ->
                @Suppress("UNCHECKED_CAST")
                uiState = uiState.copy(pdfDetailsMap = newDetailsMap as Map<Uri, com.example.doc_tools.core.common.model.FileDetails>)
            },
            currentDetailsMap = uiState.pdfDetailsMap,
            getFileDetails = { ctx, uri -> FileInfoUtils.getFileDetails(ctx, uri) },
            clearOutputDetails = { uiState = uiState.copy(outputDetails = null) }
        )
    }

    /**
     * Add PDFs to the list of files to merge and calculate page counts
     */
    fun addPdfFiles(uris: List<Uri>, context: Context? = null) {
        if (uris.isNotEmpty()) {
            val updatedUris = uiState.selectedPdfUris + uris
            uiState = uiState.copy(selectedPdfUris = updatedUris, outputDetails = null)
            // Calculate page count asynchronously to avoid UI freeze
            if (context != null) {
                viewModelScope.launch {
                    calculateTotalPageCount(updatedUris, context)
                }
            }
        }
    }

    /**
     * Remove a single PDF from the list
     */
    fun removePdf(uri: Uri, context: Context? = null) {
        val updatedUris = uiState.selectedPdfUris.filter { it != uri }
        uiState = uiState.copy(
            selectedPdfUris = updatedUris
        )
        // Recalculate page count after removing a PDF
        if (context != null) {
            viewModelScope.launch {
                calculateTotalPageCount(updatedUris, context)
            }
        }
    }

    /**
     * Remove multiple PDFs from the list
     */
    fun removeSelectedPdfs(context: Context? = null) {
        val updatedUris = uiState.selectedPdfUris.filter { it !in uiState.selectedItemsToRemove }
        uiState = uiState.copy(
            selectedPdfUris = updatedUris,
            selectedItemsToRemove = emptyList()
        )
        // Recalculate page count after removing PDFs
        if (context != null) {
            viewModelScope.launch {
                calculateTotalPageCount(updatedUris, context)
            }
        }
    }

    /**
     * Clear all selected PDFs
     */
    fun clearAllPdfs(context: Context? = null) {
        uiState = uiState.copy(selectedPdfUris = emptyList(), outputDetails = null, totalPageCount = 0)
    }

    /**
     * Toggle item selection in the removal list
     */
    fun toggleItemSelection(uri: Uri) {
        val currentSelection = uiState.selectedItemsToRemove.toMutableList()

        if (uri in currentSelection) {
            currentSelection.remove(uri)
        } else {
            currentSelection.add(uri)
        }
        uiState = uiState.copy(selectedItemsToRemove = currentSelection)
    }

    /**
     * Updates the save path
     */
    fun updateSavePath(path: String) {
        if (uiState.outputDetails != null) {
            uiState = uiState.copy(savePath = path, outputDetails = null)
        } else {
            uiState = uiState.copy(savePath = path)
        }
    }

    /**
     * Changes the save mode
     */
    fun changeSaveMode(saveMode: SaveMode) {
        if (uiState.outputDetails != null) {
            uiState = uiState.copy(saveMode = saveMode, outputDetails = null)
        } else {
            uiState = uiState.copy(saveMode = saveMode)
        }
    }

    /**
     * Shows/hides the selected files sheet
     */
    fun toggleSelectedFilesSheet(show: Boolean) {
        uiState = uiState.copy(showSelectedFilesSheet = show)
    }

    /**
     * Shows/hides the output file sheet
     */
    fun toggleOutputFileSheet(show: Boolean) {
        uiState = uiState.copy(showOutputFileBottomSheet = show)
    }

    /**
     * Shows/hides the confirm merge dialog
     */
    fun toggleConfirmMergeDialog(show: Boolean) {
        uiState = uiState.copy(showConfirmMergeDialog = show)
    }

    /**
     * Clears the output details
     */
    fun clearOutputDetails() {
        uiState = uiState.copy(outputDetails = null)
    }

    /**
     * Cancels the ongoing merge process
     */
    fun cancelMerge() {
        uiState = uiState.copy(isProcessing = false, processingProgress = -1f)
        ProcessingStateManager.endProcess("merge_pdf")
    }

    /**
     * Calculates the total page count for all selected PDF files
     */

    private suspend fun calculateTotalPageCount(pdfUris: List<Uri>, context: Context) {
        if (pdfUris.isEmpty()) {
            uiState = uiState.copy(totalPageCount = 0)
            return
        }

        var totalPages = 0
        pdfUris.forEach { uri ->
            val pageCount = PdfUtils.getPageCount(context, uri)
            if (pageCount != null) {
                totalPages += pageCount
            }
        }

        uiState = uiState.copy(totalPageCount = totalPages)
    }
}```

### `app\src\main\java\com\example\doc_tools\features\pdf\pdftoimages\PdfConversionNotificationHelper.kt`

```kt
package com.example.doc_tools.features.pdf.pdftoimages

import android.app.NotificationChannel
import android.app.NotificationManager
import android.content.Context
import android.os.Build
import androidx.core.app.NotificationCompat
import androidx.core.content.ContextCompat
import com.example.doc_tools.R

/**
 * Helper class for creating and updating notifications for PDF to Images conversion.
 * Shows progress updates for long-running conversions.
 */
class PdfConversionNotificationHelper(private val context: Context) {

    companion object {
        private const val CHANNEL_ID = "pdf_conversion_channel"
        private const val NOTIFICATION_ID = 101
    }

    private val notificationManager = context.getSystemService(Context.NOTIFICATION_SERVICE) as NotificationManager
    private val notificationBuilder = NotificationCompat.Builder(context, CHANNEL_ID)
        .setSmallIcon(android.R.drawable.ic_menu_gallery)
        .setContentTitle("Converting PDF to Images")
        .setOngoing(true)
        .setPriority(NotificationCompat.PRIORITY_LOW)
        .setProgress(0, 0, true)
        .setAutoCancel(false)

    /**
     * Create the notification channel (required for Android 8.0+)
     */
    fun createNotificationChannel() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            val channel = NotificationChannel(
                CHANNEL_ID,
                "PDF Conversion",
                NotificationManager.IMPORTANCE_LOW
            ).apply {
                description = "Shows progress when converting PDFs to images"
                setShowBadge(false)
            }
            notificationManager.createNotificationChannel(channel)
        }
    }

    /**
     * Show the initial progress notification
     * @param current Current page being processed
     * @param total Total number of pages
     */
    fun showProgressNotification(current: Int, total: Int) {
        notificationBuilder
            .setContentText("Processing page $current of $total")
            .setProgress(total, current, false)
        
        notificationManager.notify(NOTIFICATION_ID, notificationBuilder.build())
    }

    /**
     * Update the progress notification
     * @param current Current page being processed
     * @param total Total number of pages
     */
    fun updateProgressNotification(current: Int, total: Int) {
        notificationBuilder
            .setContentText("Processing page $current of $total")
            .setProgress(total, current, false)
        
        notificationManager.notify(NOTIFICATION_ID, notificationBuilder.build())
    }

    /**
     * Show the completed notification
     * @param total Total number of pages processed
     */
    fun showCompletedNotification(total: Int) {
        notificationBuilder
            .setContentText("Converted $total pages to images")
            .setProgress(0, 0, false)
            .setOngoing(false)
            .setAutoCancel(true)
        
        notificationManager.notify(NOTIFICATION_ID, notificationBuilder.build())
    }

    /**
     * Cancel the notification
     */
    fun cancelNotification() {
        notificationManager.cancel(NOTIFICATION_ID)
    }
} ```

### `app\src\main\java\com\example\doc_tools\features\pdf\pdftoimages\presentation\state\PdfToImagesUiState.kt`

```kt
package com.example.doc_tools.features.pdf.pdftoimages.presentation.state

import android.net.Uri
import com.example.doc_tools.core.common.model.FileDetails
import com.example.doc_tools.core.domain.model.SaveMode

/**
 * Data class representing the UI state for the PDF to Images screen
 */
data class PdfToImagesUiState(
    val selectedPdfUri: Uri? = null,
    val outputImages: List<FileDetails> = emptyList(),
    val selectedImageIndices: Set<Int> = emptySet(),
    val isProcessing: Boolean = false,
    val processingProgress: Float = -1f,
    val pdfPageCount: Int = 0,
    val savePath: String = "Downloads",
    val saveMode: SaveMode = SaveMode.SEPARATELY,
    val outputFormat: String = "PNG",
    val showBottomSheet: Boolean = false,
    val errorMessage: String? = null,
    val originalFileDetails: FileDetails? = null,
    val dpi: Int = 200
)```

### `app\src\main\java\com\example\doc_tools\features\pdf\pdftoimages\presentation\ui\PdfToImagesScreen.kt`

```kt
package com.example.doc_tools.features.pdf.pdftoimages.presentation.ui

import android.net.Uri
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Image
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.HorizontalDivider
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation.NavController
import com.example.doc_tools.core.common.model.FileDetails
import com.example.doc_tools.core.domain.model.SaveMode
import com.example.doc_tools.core.ui.components.button.ProgressToolButton
import com.example.doc_tools.core.ui.components.card.FileInfoActionCard
import com.example.doc_tools.core.ui.components.file.ChangeSaveLocation
import com.example.doc_tools.core.ui.components.file.FileBottomSheet
import com.example.doc_tools.core.ui.components.layout.BaseToolScreen
import com.example.doc_tools.core.ui.components.overlay.ProcessingAware
import com.example.doc_tools.core.ui.components.tool_layout.HeaderSection
import com.example.doc_tools.core.utils.file.FileActionsUtils
import com.example.doc_tools.core.utils.file.FileActionsUtils.shareFile
import com.example.doc_tools.core.utils.file.FileActionsUtils.viewFile
import com.example.doc_tools.features.pdf.pdftoimages.presentation.ui.components.DpiSelectionSection
import com.example.doc_tools.features.pdf.pdftoimages.presentation.ui.components.FileSelectionSection
import com.example.doc_tools.features.pdf.pdftoimages.presentation.ui.components.ImageFormatSection
import com.example.doc_tools.features.pdf.pdftoimages.presentation.viewmodel.PdfToImagesViewModel


/**
 * Screen for converting PDF to images
 */
@Composable
fun PdfToImagesScreen(
    navController: NavController,
    isDarkTheme: Boolean,
    onThemeToggle: () -> Unit,
    modifier: Modifier = Modifier,
    viewModel: PdfToImagesViewModel = viewModel()
) {
    val context = LocalContext.current
    val uiState = viewModel.uiState
    val imageFormats = listOf("PNG", "JPEG")
    val dpiOptions = listOf(100, 150, 200, 300)
    val messageScope = "pdf_to_images"

    BaseToolScreen(
        title = "PDF to Images",
        navController = navController,
        isDarkTheme = isDarkTheme,
        onThemeToggle = onThemeToggle,
        contentScrollable = true,
        messageScope = messageScope,
        showThemeToggle = false, // Hide theme toggle since it's now in Settings
        modifier = modifier
    ) {
        Card(modifier = Modifier.fillMaxWidth().padding(vertical = 8.dp), colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surface, contentColor = MaterialTheme.colorScheme.onSurface), elevation = CardDefaults.cardElevation(defaultElevation = 2.dp), shape = RoundedCornerShape(24.dp)) {

            Column(modifier = Modifier.padding(24.dp), verticalArrangement = Arrangement.spacedBy(16.dp) ) {

                HeaderSection(icon = Icons.Default.Image, title = "PDF to Images", subtitle = "Extract pages from PDF files into images PNG, JPEG.")
                HorizontalDivider(color = MaterialTheme.colorScheme.outline)
                ProcessingAware { isEnabled -> FileSelectionSection(uiState, context, viewModel, isDarkTheme, isEnabled) }
                HorizontalDivider(color = MaterialTheme.colorScheme.outline)
                ProcessingAware { isEnabled -> ImageFormatSection(uiState, imageFormats, viewModel, isEnabled) }
                ProcessingAware { isEnabled -> DpiSelectionSection(uiState, dpiOptions, viewModel, isEnabled) }
                
                if (uiState.selectedPdfUri != null) {
                    ProcessingAware { isEnabled ->
                        ChangeSaveLocation(
                            visible = true,
                            defaultSaveLocation = uiState.savePath,
                            onSaveLocationChanged = { if (isEnabled) viewModel.updateSavePath(it) },
                            saveModeEnabled = true,
                            initialSaveMode = uiState.saveMode,
                            onSaveModeChanged = { if (isEnabled) viewModel.updateSaveMode(it) },
                            modifier = Modifier.fillMaxWidth()
                        )
                    }
                }
                
                // Progress button should remain interactive for cancellation
                ProgressToolButton(
                    onClick = { 
                        if (uiState.isProcessing) {
                            viewModel.cancelProcessing()
                        } else {
                            viewModel.convertPdfToImages(context, messageScope)
                        }
                    },
                    isProcessing = uiState.isProcessing,
                    progress = uiState.processingProgress,
                    enabled = uiState.selectedPdfUri != null,
                    text = "Convert PDF To Images",
                    icon = Icons.Default.Image,
                    errorMessage = if (uiState.isProcessing) null else uiState.errorMessage,
                    processingText = "Conversion in Progress",
                )
                
                ProcessingAware { isEnabled ->

                    if (uiState.outputImages.isNotEmpty()) {

                        val totalSize = uiState.outputImages.sumOf { it.size }

                        val summaryFileDetails = FileDetails(
                            uri = uiState.outputImages.firstOrNull()?.uri ?: Uri.EMPTY,
                            name = when {
                                uiState.saveMode == SaveMode.AS_ARCHIVE -> "PDF_extracted_images.zip"
                                uiState.outputImages.size == 1 -> uiState.outputImages.first().name
                                else -> "${uiState.outputImages.size} Extracted Images"
                            },
                            size = totalSize,
                            mimeType = if (uiState.saveMode == SaveMode.AS_ARCHIVE) "application/zip" else "image/*",
                            path = uiState.savePath
                        )
                        Text(text = "Converted image's detail", style = MaterialTheme.typography.bodyMedium, fontWeight = FontWeight.SemiBold, color = MaterialTheme.colorScheme.onSurfaceVariant)
                        FileInfoActionCard(
                            file = summaryFileDetails,
                            showSize = true,
                            showFormat = true,
                            labelOverrides = mapOf("size" to "Total Size"),
                            onOpen = {
                                if (isEnabled) {
                                    FileActionsUtils.smartFileView(
                                        context = context,
                                        fileDetails = summaryFileDetails,
                                        multipleFiles = if (uiState.saveMode == SaveMode.AS_ARCHIVE) null else uiState.outputImages,
                                        onShowBottomSheet = { viewModel.toggleBottomSheet(true) },
                                        isDarkTheme = isDarkTheme
                                    )
                                }
                            },
                            onShare = { if (isEnabled) shareFile(context, summaryFileDetails.uri, summaryFileDetails.mimeType) },
                            onDelete = { if (isEnabled) viewModel.clearAllImages() },
                            isDarkTheme = isDarkTheme,
                            enabled = isEnabled
                        )
                    }
                }
            }
        }
        
        // Only show bottom sheet if not processing
        if (uiState.showBottomSheet && !uiState.isProcessing && uiState.outputImages.isNotEmpty()) {
            FileBottomSheet(
                show = uiState.showBottomSheet && uiState.outputImages.isNotEmpty(),
                onDismiss = { viewModel.toggleBottomSheet(false) },
                fileUris = uiState.outputImages.map { it.uri },
                title = "Extracted Images",
                onFilesUpdated = { updatedUris -> viewModel.updateOutputImages(updatedUris) },
                onFileView = { uri, mimeType -> viewFile(context, uri, mimeType) },
                isDarkTheme = isDarkTheme,
                enableSelection = false,
                enableRemoveSelected = false,
                enableClearAll = false,
                enableFileRemoveButton = false
            )
        }
    }
}
```

### `app\src\main\java\com\example\doc_tools\features\pdf\pdftoimages\presentation\ui\components\DpiSelectionSection.kt`

```kt
package com.example.doc_tools.features.pdf.pdftoimages.presentation.ui.components

import android.annotation.SuppressLint
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.SliderDefaults
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import com.example.doc_tools.features.pdf.pdftoimages.presentation.state.PdfToImagesUiState
import com.example.doc_tools.features.pdf.pdftoimages.presentation.viewmodel.PdfToImagesViewModel

@SuppressLint("UnrememberedMutableState")
@OptIn(ExperimentalMaterial3Api::class)
@Composable
internal fun DpiSelectionSection(
    uiState: PdfToImagesUiState,
    dpiOptions: List<Int>,
    viewModel: PdfToImagesViewModel,
    isEnabled: Boolean
) {
    Column {
        Text(text = "Image Quality (DPI)", style = MaterialTheme.typography.bodyMedium, fontWeight = FontWeight.SemiBold, color = MaterialTheme.colorScheme.onSurfaceVariant)
        Spacer(modifier = Modifier.height(4.dp))
        Text(text = "Higher DPI means better quality but larger file sizes.", style = MaterialTheme.typography.bodySmall)
        Spacer(modifier = Modifier.height(8.dp))

        val minDpi = 100
        val maxDpi = 300
        val step = 50
        val sliderSteps = (maxDpi - minDpi) / step - 1

        Text(text = "${uiState.dpi} DPI", style = MaterialTheme.typography.labelLarge)
        androidx.compose.material3.Slider(
            value = uiState.dpi.toFloat(),
            onValueChange = { if (isEnabled) viewModel.updateDpi(it.toInt()) },
            valueRange = minDpi.toFloat()..maxDpi.toFloat(),
            steps = sliderSteps,
            enabled = isEnabled,
            modifier = Modifier.fillMaxWidth(),
            colors = SliderDefaults.colors(
                thumbColor = MaterialTheme.colorScheme.primary,
                activeTrackColor = MaterialTheme.colorScheme.primary,
                activeTickColor = MaterialTheme.colorScheme.onPrimary,
            ),
        )
    }
}```

### `app\src\main\java\com\example\doc_tools\features\pdf\pdftoimages\presentation\ui\components\FileSelectionSection.kt`

```kt
package com.example.doc_tools.features.pdf.pdftoimages.presentation.ui.components

import android.content.Context
import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.rounded.FileOpen
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import com.example.doc_tools.core.ui.components.card.FileInfoActionCard
import com.example.doc_tools.core.ui.components.file.FilePickerHandler
import com.example.doc_tools.core.utils.file.FileActionsUtils.viewFile
import com.example.doc_tools.features.pdf.pdftoimages.presentation.state.PdfToImagesUiState
import com.example.doc_tools.features.pdf.pdftoimages.presentation.viewmodel.PdfToImagesViewModel

@Composable
internal fun FileSelectionSection(
    uiState: PdfToImagesUiState,
    context: Context,
    viewModel: PdfToImagesViewModel,
    isDarkTheme: Boolean,
    isEnabled: Boolean
) {
    Column {
        Text(text = "Select Pdf File", style = MaterialTheme.typography.bodyMedium, fontWeight = FontWeight.SemiBold, color = MaterialTheme.colorScheme.onSurfaceVariant)
        Spacer(modifier = Modifier.height(4.dp))
        Text(text = "Select a pdf file to remove pages into images format.", style = MaterialTheme.typography.bodySmall)
        Spacer(modifier = Modifier.height(8.dp))

        FilePickerHandler(
            single = true,
            supportedMimeTypes = listOf("application/pdf"),
            onPicked = { uris -> if (uris.isNotEmpty() && isEnabled) { viewModel.setPdfFile(context, uris.first()) } }
        ) { launchPicker, _ ->
            OutlinedButton(
                onClick = { launchPicker() },
                shape = RoundedCornerShape(14.dp),
                colors = ButtonDefaults.outlinedButtonColors(containerColor = MaterialTheme.colorScheme.primaryContainer, contentColor = MaterialTheme.colorScheme.onPrimaryContainer),
                contentPadding = PaddingValues(24.dp),
                border = BorderStroke(1.dp, MaterialTheme.colorScheme.onPrimaryContainer),
                modifier = Modifier.fillMaxWidth(),
                enabled = isEnabled
            ) {
                Icon(imageVector = Icons.Rounded.FileOpen, contentDescription = null, modifier = Modifier.size(ButtonDefaults.IconSize))
                Spacer(modifier = Modifier.size(ButtonDefaults.IconSpacing))
                Text(text = "Select PDF File")
            }
        }

        uiState.originalFileDetails?.let {
            Spacer(modifier = Modifier.height(16.dp))
            Text(text = "Selected File Detail's", style = MaterialTheme.typography.bodyMedium, fontWeight = FontWeight.SemiBold, color = MaterialTheme.colorScheme.onSurfaceVariant)
            Spacer(modifier = Modifier.height(16.dp))
            FileInfoActionCard(
                file = it,
                showName = true,
                showSize = true,
                showFormat = true,
                showPages = true,
                onOpen = { if (isEnabled) uiState.selectedPdfUri?.let { uri -> viewFile(context, uri, it.mimeType) } },
                onDelete = { if (isEnabled) viewModel.clearPdfFile() },
                isDarkTheme = isDarkTheme,
                enabled = isEnabled
            )
        }
    }
}```

### `app\src\main\java\com\example\doc_tools\features\pdf\pdftoimages\presentation\ui\components\ImageFormatSection.kt`

```kt
package com.example.doc_tools.features.pdf.pdftoimages.presentation.ui.components

import android.annotation.SuppressLint
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Image
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import com.example.doc_tools.core.ui.components.button.ChipButton
import com.example.doc_tools.features.pdf.pdftoimages.presentation.state.PdfToImagesUiState
import com.example.doc_tools.features.pdf.pdftoimages.presentation.viewmodel.PdfToImagesViewModel

@SuppressLint("UnrememberedMutableState")
@OptIn(ExperimentalMaterial3Api::class)
@Composable
internal fun ImageFormatSection(
    uiState: PdfToImagesUiState,
    formats: List<String>,
    viewModel: PdfToImagesViewModel,
    isEnabled: Boolean
) {
    Column {
        Text(text = "Select Image Format", style = MaterialTheme.typography.bodyMedium, fontWeight = FontWeight.SemiBold, color = MaterialTheme.colorScheme.onSurfaceVariant)
        Spacer(modifier = Modifier.height(4.dp))
        Text(text = "Choose the image format for the output files (PNG or JPEG).", style = MaterialTheme.typography.bodySmall)
        Spacer(modifier = Modifier.height(8.dp))

        Row(horizontalArrangement = Arrangement.spacedBy(12.dp)) {
            formats.forEach { format ->
                val icon = when (format.uppercase()) {
                    "PNG" -> Icons.Default.Image
                    "JPEG" -> Icons.Default.Image
                    else -> null
                }
                ChipButton(
                    label = format,
                    icon = null,
                    selected = uiState.outputFormat.equals(format, ignoreCase = true),
                    onClick = { if (isEnabled) viewModel.updateOutputFormat(format) },
                    enabled = isEnabled,
                    modifier = Modifier.padding(horizontal = 32.dp, vertical = 16.dp),
                )
            }
        }
    }
}```

### `app\src\main\java\com\example\doc_tools\features\pdf\pdftoimages\presentation\viewmodel\PdfToImagesViewModel.kt`

```kt
package com.example.doc_tools.features.pdf.pdftoimages.presentation.viewmodel

import android.content.Context
import android.net.Uri
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.doc_tools.features.pdf.pdftoimages.PdfConversionNotificationHelper
import com.example.doc_tools.core.domain.model.SaveMode

import com.example.doc_tools.core.common.model.FileDetails
import com.example.doc_tools.core.utils.file.FileInfoUtils
import com.example.doc_tools.core.utils.file.SaveLocationUtils
import com.example.doc_tools.core.presentation.eventbus.UiMessageBus
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import java.io.File
import kotlinx.coroutines.withContext

import com.example.doc_tools.features.pdf.pdftoimages.data.local.PdfToImagesService
import com.example.doc_tools.features.pdf.pdftoimages.presentation.state.PdfToImagesUiState
import com.example.doc_tools.core.presentation.state.ProcessingStateManager
import com.example.doc_tools.core.utils.file.FileIoUtils

/**
 * ViewModel for the PDF to Images screen that handles business logic and state management.
 *
 * This ViewModel manages the state of the PDF to Images feature, including:
 * - The selected PDF file and its details.
 * - The output format, DPI, save path, and save mode for the converted images.
 * - The list of generated images and their selection state.
 * - The visibility of the bottom sheet for image actions.
 * - The processing state and progress of the PDF to image conversion.
 *
 * It provides functions to:
 * - Set the selected PDF file and load its page count.
 * - Update the output settings (format, DPI, save path, save mode).
 * - Toggle the selection of individual images.
 * - Show or hide the image actions bottom sheet.
 * - Remove individual images from the output list.
 * - Clear all generated images.
 * - Clear the selected PDF file.
 * - Cancel an ongoing conversion process.
 * - Initiate the conversion of the selected PDF to images.
 *
 * The `convertPdfToImages` function handles the core conversion logic, including:
 * - Validation of input (selected PDF and save location).
 * - Creation of a temporary directory for intermediate image files.
 * - Calling the `PdfService` to perform the actual conversion.
 * - Saving the generated images to the specified location using `SaveLocationUtils`.
 * - Updating the UI state with the results and showing appropriate messages via `UiMessageBus`.
 * - Cleaning up temporary files and directories.
 * - Handling potential errors and exceptions during the process.
 */

class PdfToImagesViewModel : ViewModel() {

    // The UI state exposed to the UI layer
    var uiState by mutableStateOf(PdfToImagesUiState())
        private set

    /**
     * Converts the selected PDF file to a series of images using optimized processing.
     * This approach is optimized for large PDFs with many pages and prevents UI freezing.
     *
     * @param context The application context.
     * @param messageScope A string identifier for the scope of UI messages, used by `UiMessageBus`.
     */
    fun convertPdfToImages(context: Context, messageScope: String = "pdf_to_images") {
        val currentState = uiState
        
        if (currentState.selectedPdfUri == null) {
            UiMessageBus.showError("Please select a PDF file", messageScope)
            return
        }
        
        // Check global processing state - don't allow multiple processes
        if (!ProcessingStateManager.startProcess(messageScope)) {
            UiMessageBus.showError("Another process is already running. Please wait or cancel it first.", messageScope)
            return
        }
        
        // Update local state to show processing
        uiState = uiState.copy(
            isProcessing = true,
            processingProgress = 0f,
            errorMessage = null
        )

        viewModelScope.launch {
            try {
                val pdfService = PdfToImagesService(context)
                val uri = uiState.selectedPdfUri ?: return@launch

                // Create temp directory for extracted images
                val tempDir = File(context.cacheDir, "pdf_images_${System.currentTimeMillis()}")
                if (!tempDir.exists()) {
                    tempDir.mkdirs()
                }

                // Get page count to determine if notification is needed
                val pageCount = pdfService.getPageCount(context, uri)
                val useNotification = pageCount > 20 // Show notification for PDFs with more than 20 pages
                
                if (useNotification) {
                    // Create notification for progress tracking
                    val notificationHelper = PdfConversionNotificationHelper(context)
                    notificationHelper.createNotificationChannel()
                    notificationHelper.showProgressNotification(0, pageCount)
                    
                    // Convert PDF to images with optimized service and progress callback
                    val result = pdfService.pdfToImages(
                        inputUri = uri,
                        outputDir = tempDir,
                        format = uiState.outputFormat,
                        dpi = uiState.dpi.toFloat(),
                        progressCallback = { progress ->
                            // Update UI state
                            uiState = uiState.copy(processingProgress = progress)
                            ProcessingStateManager.updateProgress(progress, messageScope)
                            
                            // Update notification (don't need to do this in a separate coroutine)
                            val currentPage = (progress * pageCount).toInt().coerceIn(0, pageCount)
                            notificationHelper.updateProgressNotification(currentPage, pageCount)
                        }
                    )
                    
                    // Complete or cancel notification
                    result.fold(
                        onSuccess = {
                            notificationHelper.showCompletedNotification(pageCount)
                            handleConversionSuccess(context, tempDir, it, messageScope)
                        },
                        onFailure = { error ->
                            notificationHelper.cancelNotification()
                            UiMessageBus.showError("Failed to convert PDF: ${error.message}", messageScope)
                            tempDir.deleteRecursively()
                            finishProcessing()
                        }
                    )
                } else {
                    // For smaller PDFs, use direct conversion with progress callback
                    val result = pdfService.pdfToImages(
                        inputUri = uri,
                        outputDir = tempDir,
                        format = uiState.outputFormat,
                        dpi = uiState.dpi.toFloat(),
                        progressCallback = { progress ->
                            // Update UI state
                            uiState = uiState.copy(processingProgress = progress)
                            ProcessingStateManager.updateProgress(progress, messageScope)
                        }
                    )
                    
                    // Process results
                    result.fold(
                        onSuccess = { imageFiles ->
                            handleConversionSuccess(context, tempDir, imageFiles, messageScope)
                        },
                        onFailure = { error ->
                            UiMessageBus.showError("Failed to convert PDF: ${error.message}", messageScope)
                            tempDir.deleteRecursively()
                            finishProcessing()
                        }
                    )
                }

            } catch (e: Exception) {
                UiMessageBus.showError("Error: ${e.message}", messageScope)
                finishProcessing()
            }
        }
    }

    /**
     * Handle successful PDF to images conversion
     */
    private suspend fun handleConversionSuccess(
        context: Context, 
        tempDir: File,
        imageFiles: List<File>,
        messageScope: String
    ) = withContext(Dispatchers.IO) {
        try {
            // Sort files by page number
            val sortedFiles = imageFiles.sortedBy { 
                val pageNum = it.name.replace(Regex("[^0-9]"), "").toIntOrNull() ?: 0
                pageNum
            }
            
            if (sortedFiles.isEmpty()) {
                UiMessageBus.showError("No images were generated", messageScope)
                tempDir.deleteRecursively()
                finishProcessing()
                return@withContext
            }
            
            // Save images based on save mode
            val savedImages = mutableListOf<FileDetails>()
            
            if (uiState.saveMode == SaveMode.AS_ARCHIVE) {
                // Zip the images
                val tempZipFile = File(tempDir, "pdf_images_${System.currentTimeMillis()}.zip")
                val success = FileIoUtils.createZipArchive(sortedFiles, tempZipFile)
                
                if (success) {
                    val zipFileName = "pdf_images_${System.currentTimeMillis()}"
                    val archiveUri = SaveLocationUtils.saveToLocation(
                        context = context,
                        sourceFile = tempZipFile,
                        outputFileName = zipFileName,
                        mimeType = "application/zip",
                        savePath = uiState.savePath,
                        saveMode = SaveMode.SEPARATELY // Don't wrap zip in another zip
                    )
                    
                    if (archiveUri != null) {
                        val archiveDetails = FileInfoUtils.getFileDetails(context, archiveUri)
                        withContext(Dispatchers.Main) {
                            uiState = uiState.copy(outputImages = listOfNotNull(archiveDetails))
                        }
                        UiMessageBus.showSuccess(
                            "Extracted ${imageFiles.size} images and saved as ZIP archive",
                            messageScope
                        )
                    } else {
                        UiMessageBus.showError("Failed to save ZIP archive", messageScope)
                    }
                    
                    tempZipFile.delete()
                } else {
                    UiMessageBus.showError("Failed to create ZIP archive", messageScope)
                }
            } else {
                // Save images individually
                sortedFiles.forEachIndexed { index, imageFile ->
                    val fileName = "page_${index + 1}.${uiState.outputFormat.lowercase()}"
                    val mimeType = when (uiState.outputFormat.uppercase()) {
                        "PNG" -> "image/png"
                        "JPEG", "JPG" -> "image/jpeg"
                        else -> "image/png"
                    }
                    
                    val savedUri = SaveLocationUtils.saveToLocation(
                        context = context,
                        sourceFile = imageFile,
                        outputFileName = fileName,
                        mimeType = mimeType,
                        savePath = uiState.savePath,
                        saveMode = uiState.saveMode
                    )
                    
                    if (savedUri != null) {
                        val imageDetails = FileInfoUtils.getFileDetails(context, savedUri)
                        savedImages.add(imageDetails)
                    }
                }
                
                if (savedImages.isNotEmpty()) {
                    withContext(Dispatchers.Main) {
                        uiState = uiState.copy(outputImages = savedImages)
                    }
                    UiMessageBus.showSuccess(
                        "Extracted ${savedImages.size} images from PDF",
                        messageScope
                    )
                } else {
                    UiMessageBus.showError("Failed to save any images", messageScope)
                }
            }
            
            // Clean up temp directory
            tempDir.deleteRecursively()
            finishProcessing()
        } catch (e: Exception) {
            UiMessageBus.showError("Error saving images: ${e.message}", messageScope)
            tempDir.deleteRecursively()
            finishProcessing()
        }
    }
    
    /**
     * Clean up processing state
     */
    private fun finishProcessing() {
        uiState = uiState.copy(
            isProcessing = false,
            processingProgress = -1f
        )
        // End the process in the global state manager
        ProcessingStateManager.endProcess("pdf_to_images")
    }

    /**
     * Set the selected PDF file
     */
    fun setPdfFile(context: Context, uri: Uri) {
        uiState = uiState.copy(selectedPdfUri = uri, outputImages = emptyList(), originalFileDetails = FileInfoUtils.getFileDetails(context, uri))
        // Load page count in background
        viewModelScope.launch {
            try {
                val pdfService = PdfToImagesService(context)
                val pageCount = pdfService.getPageCount(context, uri)
                uiState = uiState.copy(pdfPageCount = pageCount)
            } catch (e: Exception) {
                // Handle error silently
                uiState = uiState.copy(pdfPageCount = 0)
            }
        }
    }

    /**
     * Remove an image from the output list
     */
    fun removeImage(uri: Uri) {
        val index = uiState.outputImages.indexOfFirst { it.uri == uri }
        if (index >= 0) {
            val updatedImages = uiState.outputImages.toMutableList()
            updatedImages.removeAt(index)

            // Update selected indices to account for removed image
            val selectedIndices = uiState.selectedImageIndices.toMutableSet()
            selectedIndices.remove(index)
            val adjustedIndices = selectedIndices.map {
                if (it > index) it - 1 else it
            }.toSet()

            uiState = uiState.copy(
                outputImages = updatedImages,
                selectedImageIndices = adjustedIndices,
                showBottomSheet = updatedImages.isNotEmpty() && uiState.showBottomSheet
            )
        }
    }

    /**
     * Toggle selection of an image in the list
     */
    fun toggleImageSelection(index: Int) {
        val currentSelectedIndices = uiState.selectedImageIndices.toMutableSet()
        if (index in currentSelectedIndices) {
            currentSelectedIndices.remove(index)
        } else {
            currentSelectedIndices.add(index)
        }
        uiState = uiState.copy(selectedImageIndices = currentSelectedIndices)
    }

    /**
     * Update the output format
     */
    fun updateOutputFormat(format: String) {
        uiState = uiState.copy(outputFormat = format)
    }

    /**
     * Update the DPI setting
     */
    fun updateDpi(dpi: Int) {
        uiState = uiState.copy(dpi = dpi)
    }

    /**
     * Update the save path
     */
    fun updateSavePath(path: String) {
        if (uiState.outputImages.isNotEmpty()) {
            uiState = uiState.copy(savePath = path, outputImages = emptyList(), selectedImageIndices = emptySet(), showBottomSheet = false)
        } else {
            uiState = uiState.copy(savePath = path)
        }
    }

    /**
     * Update the save mode
     */
    fun updateSaveMode(saveMode: SaveMode) {
        if (uiState.outputImages.isNotEmpty()) {
            uiState = uiState.copy(saveMode = saveMode, outputImages = emptyList(), selectedImageIndices = emptySet(), showBottomSheet = false)
        } else {
            uiState = uiState.copy(saveMode = saveMode)
        }
    }

    /**
     * Toggle the bottom sheet visibility
     */
    fun toggleBottomSheet(show: Boolean) {
        uiState = uiState.copy(showBottomSheet = show)
    }

    /**
     * Clear all output images
     */
    fun clearAllImages() {
        uiState = uiState.copy(outputImages = emptyList(), selectedImageIndices = emptySet(), showBottomSheet = false)
    }

    /**
     * Clear the selected PDF file
     */
    fun clearPdfFile() {
        uiState = uiState.copy(selectedPdfUri = null, originalFileDetails = null, pdfPageCount = 0)
    }

    /**
     * Cancel the current processing
     */
    fun cancelProcessing() {
        uiState = uiState.copy(isProcessing = false, processingProgress = 0f)
        // End the process in the global state manager
        ProcessingStateManager.endProcess("pdf_to_images")
    }

    /**
     * Update output images list directly (used with FileBottomSheetUtils)
     */
    fun updateOutputImages(updatedUris: List<Uri>) {
        if (updatedUris.isEmpty()) {
            clearAllImages()
            return
        }
        
        // Keep only the FileDetails that match the updated URIs
        val updatedDetails = uiState.outputImages.filter { 
            it.uri in updatedUris 
        }
        
        uiState = uiState.copy(outputImages = updatedDetails)
    }
}

/**
 * Context provider for accessing application context in static methods
 */
object AppContextProvider {
    lateinit var appContext: Context
}
```

### `app\src\main\java\com\example\doc_tools\features\pdf\splitpdf\presentation\state\SplitPdfUiState.kt`

```kt
package com.example.doc_tools.features.pdf.splitpdf.presentation.state

import android.net.Uri
import com.example.doc_tools.core.common.model.FileDetails
import com.example.doc_tools.core.domain.model.SaveMode

/**
 * UI State for the Split PDF feature
 */
data class SplitPdfUiState(
    // Input state
    val selectedPdfUri: Uri? = null,
    val startPage: String = "",
    val endPage: String = "",

    // PDF properties
    val pdfPageCount: Int = 0,
    val pdfFileName: String = "",
    val pdfFileSize: Long = 0L,
    val selectedPdfDetails: FileDetails? = null,

    // Processing state
    val isProcessing: Boolean = false,
    val processingProgress: Float = 0f,

    // Output state
    val outputDetails: List<FileDetails>? = null,

    // Save location settings
    val savePath: String = "",
    val saveMode: SaveMode = SaveMode.SEPARATELY,
    val showSaveLocationSelector: Boolean = false,

    // Validation and error states
    val isStartPageValid: Boolean = true,
    val isEndPageValid: Boolean = true,
    val isRangeValid: Boolean = true,
    val errorMessage: String? = null
)```

### `app\src\main\java\com\example\doc_tools\features\pdf\splitpdf\presentation\ui\SplitPdfScreen.kt`

```kt
package com.example.doc_tools.features.pdf.splitpdf.presentation.ui

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ContentCut
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.HorizontalDivider
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation.NavController
import com.example.doc_tools.core.ui.components.button.ProgressToolButton
import com.example.doc_tools.core.ui.components.card.FileInfoActionCard
import com.example.doc_tools.core.ui.components.file.ChangeSaveLocation
import com.example.doc_tools.core.ui.components.layout.BaseToolScreen
import com.example.doc_tools.core.ui.components.overlay.ProcessingAware
import com.example.doc_tools.core.ui.components.tool_layout.HeaderSection
import com.example.doc_tools.core.utils.file.FileActionsUtils.shareFile
import com.example.doc_tools.core.utils.file.FileActionsUtils.viewFile
import com.example.doc_tools.features.pdf.splitpdf.presentation.ui.components.FileSelectionSection
import com.example.doc_tools.features.pdf.splitpdf.presentation.ui.components.PageRangeSection
import com.example.doc_tools.features.pdf.splitpdf.presentation.viewmodel.SplitPdfViewModel


/**
 * Screen for splitting PDF files by page range
 */
@Composable
fun SplitPdfScreen(navController: NavController, isDarkTheme: Boolean, onThemeToggle: () -> Unit) {

    val context = LocalContext.current
    val viewModel: SplitPdfViewModel = viewModel { SplitPdfViewModel(context) }
    val uiState by viewModel.uiState.collectAsState()
    val messageScope = "split_pdf"

    BaseToolScreen(
        title = "Split PDF",
        navController = navController,
        isDarkTheme = isDarkTheme,
        onThemeToggle = onThemeToggle,
        messageScope = messageScope,
        showThemeToggle = false // Hide theme toggle since it's now in Settings
    ) {
        Card(
            modifier = Modifier.fillMaxWidth().padding(vertical = 8.dp),
            colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surface, contentColor = MaterialTheme.colorScheme.onSurface),
            elevation = CardDefaults.cardElevation(defaultElevation = 1.dp),
            shape = RoundedCornerShape(24.dp)
        ) {
            Column(modifier = Modifier.padding(24.dp), verticalArrangement = Arrangement.spacedBy(16.dp) ) {

                HeaderSection(icon = Icons.Filled.ContentCut, title = "Split PDF", subtitle = "Break pdf into smaller manageable Pdf files.")
                HorizontalDivider(color = MaterialTheme.colorScheme.outline)
                ProcessingAware { isEnabled -> FileSelectionSection(uiState, viewModel, isDarkTheme, isEnabled) }
                HorizontalDivider(color = MaterialTheme.colorScheme.outline)
                ProcessingAware { isEnabled -> PageRangeSection(uiState, viewModel, isEnabled) }
                
                if(uiState.selectedPdfUri != null) {
                    ProcessingAware { isEnabled ->
                        ChangeSaveLocation(
                            visible = true,
                            defaultSaveLocation = uiState.savePath,
                            onSaveLocationChanged = { if (isEnabled) viewModel.updateSaveLocation(it) },
                            saveModeEnabled = false,
                            initialSaveMode = uiState.saveMode,
                            onSaveModeChanged = { if (isEnabled) viewModel.updateSaveMode(it) },
                        )
                    }
                }
                
                // Progress button should remain interactive
                ProgressToolButton(
                    text = "Split PDF",
                    onClick = { 
                        if (uiState.isProcessing) {
                            viewModel.cancelOperation()
                        } else {
                            viewModel.splitPdf(messageScope)
                        }
                    },
                    isProcessing = uiState.isProcessing,
                    progress = uiState.processingProgress,
                    icon = Icons.Filled.ContentCut,
                    enabled = uiState.selectedPdfUri != null && uiState.isRangeValid,
                    processingText = "Splitting in progress",
                )
                
                ProcessingAware { isEnabled ->

                    uiState.errorMessage?.let {
                        Text(it, color = MaterialTheme.colorScheme.error, style = MaterialTheme.typography.bodyMedium, modifier = Modifier.padding(top = 16.dp))
                    }

                    uiState.outputDetails?.forEach { details ->
                        Text(text = "Splitted File Detail's", style = MaterialTheme.typography.bodyMedium, fontWeight = FontWeight.SemiBold, color = MaterialTheme.colorScheme.onSurfaceVariant)
                        FileInfoActionCard(
                            file = details,
                            showName = true,
                            showSize = true,
                            showFormat = true,
                            showPages = true,
                            onOpen = { if (isEnabled) viewFile(context, details.uri, details.mimeType) },
                            onShare = { if (isEnabled) shareFile(context, details.uri, details.mimeType) },
                            onDelete = { if (isEnabled) viewModel.resetOutput() },
                            isDarkTheme = isDarkTheme,
                            enabled = isEnabled
                        )
                    }
                }
            }
        }
    }
}



```

### `app\src\main\java\com\example\doc_tools\features\pdf\splitpdf\presentation\ui\components\FileSelectionSection.kt`

```kt
package com.example.doc_tools.features.pdf.splitpdf.presentation.ui.components

import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.rounded.FileOpen
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import com.example.doc_tools.core.ui.components.card.FileInfoActionCard
import com.example.doc_tools.core.ui.components.file.FilePickerHandler
import com.example.doc_tools.core.utils.file.FileActionsUtils.viewFile
import com.example.doc_tools.features.pdf.splitpdf.presentation.state.SplitPdfUiState
import com.example.doc_tools.features.pdf.splitpdf.presentation.viewmodel.SplitPdfViewModel

@Composable
internal fun FileSelectionSection(
    uiState: SplitPdfUiState,
    viewModel: SplitPdfViewModel,
    isDarkTheme: Boolean,
    isEnabled: Boolean
) {
    Column {
        val context = LocalContext.current
        Text(text = "Select Pdf File", style = MaterialTheme.typography.bodyMedium, fontWeight = FontWeight.SemiBold, color = MaterialTheme.colorScheme.onSurfaceVariant)
        Text(text = "Choose a single PDF document that you wish to divide into smaller sections.", style = MaterialTheme.typography.bodySmall, modifier = Modifier.padding(vertical = 4.dp))
        Spacer(modifier = Modifier.height(8.dp))
        if (uiState.selectedPdfUri == null) {
            FilePickerHandler(
                single = true,
                supportedMimeTypes = listOf("application/pdf"),
                onPicked = { uris -> if (isEnabled) uris.firstOrNull()?.let { viewModel.onFilePicked(it) } }
            ) { launchPicker, _ ->
                OutlinedButton(
                    onClick = launchPicker,
                    shape = RoundedCornerShape(14.dp),
                    colors = ButtonDefaults.outlinedButtonColors(containerColor = MaterialTheme.colorScheme.primaryContainer, contentColor = MaterialTheme.colorScheme.onPrimaryContainer),
                    contentPadding = PaddingValues(24.dp),
                    border = BorderStroke(1.dp, MaterialTheme.colorScheme.onPrimaryContainer),
                    modifier = Modifier.fillMaxWidth(),
                    enabled = isEnabled
                ) {
                    Icon(imageVector = Icons.Rounded.FileOpen, contentDescription = null, modifier = Modifier.padding(end = 8.dp))
                    Text(text = "Select PDF File")
                }
            }
        } else {
            uiState.selectedPdfDetails?.let {
                Text(text = "Selected File Detail's", style = MaterialTheme.typography.bodyMedium, fontWeight = FontWeight.SemiBold, color = MaterialTheme.colorScheme.onSurfaceVariant)
                Spacer(modifier = Modifier.height(16.dp))
                FileInfoActionCard(
                    file = it,
                    showName = true,
                    showSize = true,
                    showFormat = true,
                    showPages = true,
                    onOpen = { if (isEnabled) viewFile(context, it.uri, it.mimeType) },
                    onDelete = { if (isEnabled) viewModel.clearPdfFile() },
                    isDarkTheme = isDarkTheme,
                    enabled = isEnabled
                )
            }
        }
    }
}```

### `app\src\main\java\com\example\doc_tools\features\pdf\splitpdf\presentation\ui\components\PageRangeSection.kt`

```kt
package com.example.doc_tools.features.pdf.splitpdf.presentation.ui.components

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import com.example.doc_tools.features.pdf.splitpdf.presentation.state.SplitPdfUiState
import com.example.doc_tools.features.pdf.splitpdf.presentation.viewmodel.SplitPdfViewModel

@Composable
internal fun PageRangeSection(
    uiState: SplitPdfUiState,
    viewModel: SplitPdfViewModel,
    isEnabled: Boolean
) {
    Column() {
        Text(text = "Select Page Range", style = MaterialTheme.typography.bodyMedium, fontWeight = FontWeight.SemiBold, color = MaterialTheme.colorScheme.onSurfaceVariant)
        Text(text = "Enter the valid page ranges to split the PDF.", style = MaterialTheme.typography.bodySmall, modifier = Modifier.padding(vertical = 4.dp))
        Row(modifier = Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.spacedBy(16.dp)) {
            OutlinedTextField(
                value = uiState.startPage,
                onValueChange = { if (isEnabled) viewModel.onStartPageChanged(it) },
                label = { Text("Start Page") },
                keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number),
                isError = !uiState.isStartPageValid,
                modifier = Modifier.weight(1f).padding(bottom = 8.dp),
                enabled = isEnabled
            )
            OutlinedTextField(
                value = uiState.endPage,
                onValueChange = { if (isEnabled) viewModel.onEndPageChanged(it) },
                label = { Text("End Page") },
                keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number),
                isError = !uiState.isEndPageValid,
                modifier = Modifier.weight(1f).padding(bottom = 8.dp),
                enabled = isEnabled
            )
        }
        if (!uiState.isRangeValid) {
            Text(text = "Start page must be less than or equal to end page", color = MaterialTheme.colorScheme.error, style = MaterialTheme.typography.bodySmall, modifier = Modifier.padding(vertical = 8.dp))
        }
        Text(text = "Valid range: 1 - ${uiState.pdfPageCount}", style = MaterialTheme.typography.bodySmall, modifier = Modifier.padding(top = 4.dp))
    }
}```

### `app\src\main\java\com\example\doc_tools\features\pdf\splitpdf\presentation\viewmodel\SplitPdfViewModel.kt`

```kt
package com.example.doc_tools.features.pdf.splitpdf.presentation.viewmodel

import android.content.Context
import android.net.Uri
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.doc_tools.features.pdf.splitpdf.data.local.SplitPdfService
import com.example.doc_tools.features.pdf.splitpdf.presentation.state.SplitPdfUiState
import com.example.doc_tools.core.common.model.FileDetails
import com.example.doc_tools.core.domain.model.SaveMode
import com.example.doc_tools.core.presentation.state.ProcessingStateManager
import com.example.doc_tools.core.utils.file.SaveLocationUtils
import com.example.doc_tools.core.presentation.eventbus.UiMessageBus
import com.example.doc_tools.core.utils.file.FileInfoUtils
import kotlinx.coroutines.delay
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.update
import kotlinx.coroutines.launch
import java.io.File

/**
 * ViewModel for the Split PDF feature.
 *
 * This ViewModel manages the UI state and logic for the Split PDF feature. It handles
 * user interactions, validates inputs, and coordinates with the [PdfService] to
 * perform the PDF splitting operation.
 *
 * Key Responsibilities:
 * - Managing the UI state ([SplitPdfUiState]) for the Split PDF screen.
 * - Handling PDF file selection and retrieving file details (name, size, page count).
 * - Validating user inputs for start page, end page, and save location.
 * - Initiating the PDF splitting process via [PdfService.splitPdf].
 * - Handling the results of the splitting operation (success or failure).
 * - Saving the split PDF files to the user-selected location.
 * - Displaying appropriate messages (success, error) to the user via [UiMessageBus].
 * - Resetting the UI state and clearing selected files.
 *
 * @property context The application context, used for accessing resources and services.
 */

class SplitPdfViewModel(private val context: Context) : ViewModel() {

    private val _uiState = MutableStateFlow(SplitPdfUiState())
    val uiState: StateFlow<SplitPdfUiState> = _uiState.asStateFlow()

    private val pdfService = SplitPdfService(context)

    /**
     * Splits the selected PDF file based on the specified page range.
     *
     * This function performs the following steps:
     * 1. Retrieves the current UI state, including the selected PDF URI and page range.
     * 2. Validates the page inputs (start page, end page, and range). If validation fails,
     *    an error message is displayed, and the function returns.
     * 3. Validates the save location. If the save location is invalid, an error message
     *    is displayed, and the function returns.
     * 4. Checks the global processing state to ensure only one process is running.
     * 5. Converts the start and end page inputs to integers.
     * 6. Launches a coroutine in the `viewModelScope` to perform the splitting operation asynchronously.
     * 7. Sets the UI state to indicate that processing has started.
     * 8. Creates a temporary output directory in the application's cache directory if it doesn't already exist.
     * 9. Creates a page range list containing a single pair of start and end pages.
     * 10. Calls the `pdfService.splitPdf()` method to perform the actual PDF splitting.
     *11. Handles the result of the `splitPdf()` operation:
     *    - **On Success:**
     *        - Iterates through the temporary output files.
     *        - For each temporary file:
     *            - Constructs an output filename that includes the page range.
     *            - Saves the temporary file to the user-selected save location using `SaveLocationUtils.saveToLocation()`.
     *            - If the save is successful, retrieves the file details and adds them to a list of saved files.
     *            - Deletes the temporary file.
     *        - If any files were successfully saved:
     *            - Displays a success message.
     *            - Updates the UI state with the details of the saved files, sets processing to false, and progress to 1f.
     *        - If no files were saved:
     *            - Displays an error message.
     *            - Updates the UI state to indicate failure.
     *    - **On Failure:**
     *        - Displays an error message with the reason for failure.
     *        - Updates the UI state to indicate failure.
     */
    fun splitPdf(messageScope: String = "split_pdf") {
        val currentState = _uiState.value
        val uri = currentState.selectedPdfUri ?: return

        // Perform validation one more time
        validatePageInputs()

        // Check if validation passed
        if (!currentState.isStartPageValid || !currentState.isEndPageValid || !currentState.isRangeValid) {
            UiMessageBus.showError("Please fix the page range before splitting", messageScope)
            return
        }

        // Validate save location
        if (!SaveLocationUtils.validateSaveLocation(currentState.savePath)) {
            UiMessageBus.showError("Please specify a valid save location", messageScope)
            return
        }

        // Check global processing state - don't allow multiple processes
        if (!ProcessingStateManager.startProcess(messageScope)) {
            UiMessageBus.showError("Another process is already running. Please wait or cancel it first.", messageScope)
            return
        }

        val startPage = currentState.startPage.toInt()
        val endPage = currentState.endPage.toInt()

        viewModelScope.launch {
            try {
                // Set processing state
                _uiState.update { it.copy(isProcessing = true, errorMessage = null, processingProgress = 0f)}

                // Create temp output directory for processing
                val tempOutputDir = File(context.cacheDir, "split_pdfs_temp")

                if (!tempOutputDir.exists()) {
                    tempOutputDir.mkdirs()
                }

                val pageRange = listOf(Pair(startPage, endPage)) // Create page range for splitting

                // Mock progress updates for now since we don't have actual progress in splitPdf service
                val progressJob = launch {
                    for (i in 1..100) {
                        delay(50)  // Simulate work
                        val progress = i / 100f
                        _uiState.update { it.copy(processingProgress = progress) }
                        ProcessingStateManager.updateProgress(progress, messageScope)
                        if (!_uiState.value.isProcessing) break
                    }
                }

                val result = pdfService.splitPdf(uri, tempOutputDir, pageRange) // Call PDF service to split the PDF

                // Cancel the progress updates
                progressJob.cancel()

                result.fold(
                    onSuccess = { tempOutputFiles ->
                        // List to store final saved files after moving to user-selected location
                        val savedFiles = mutableListOf<FileDetails>()
                        // Use SaveLocationUtils to save each split PDF to the selected location
                        for (tempFile in tempOutputFiles) {
                            try {
                                // Use page range in the filename to make it descriptive
                                val outputFileName = "${currentState.pdfFileName.substringBeforeLast('.')}_pages_${startPage}_to_${endPage}.pdf"
                                // Save the file to the user-selected location
                                val savedUri = SaveLocationUtils.saveToLocation(
                                    context,
                                    tempFile,
                                    outputFileName,
                                    "application/pdf",
                                    currentState.savePath,
                                    currentState.saveMode
                                )
                                // If save was successful, create FileDetails and add to list
                                if (savedUri != null) {
                                    val details = FileInfoUtils.getFileDetails(context, savedUri)
                                    if (details != null) { savedFiles.add(details) }
                                }

                                tempFile.delete() // Delete the temp file regardless of whether save was successful

                            } catch (e: Exception) {
                                tempFile.delete()  // Log error but continue with other files
                            }
                        }

                        if (savedFiles.isNotEmpty()) {
                            UiMessageBus.showSuccess("PDF split successfully!", messageScope)
                            _uiState.update { it.copy(isProcessing = false, outputDetails = savedFiles, processingProgress = 1f )}
                        } else {
                            UiMessageBus.showError("Failed to save split PDF files", messageScope)
                            _uiState.update { it.copy(isProcessing = false, errorMessage = "Failed to save split PDF files", processingProgress = 0f )}
                        }
                    },

                    onFailure = { error ->
                        UiMessageBus.showError("Failed to split PDF: ${error.message}", messageScope)
                        _uiState.update { it.copy(isProcessing = false, errorMessage = "Failed to split PDF: ${error.message}", processingProgress = 0f )}
                    }
                )

            } catch (e: Exception) {
                UiMessageBus.showError("Error: ${e.message}", messageScope)
                _uiState.update { it.copy(isProcessing = false, errorMessage = "Error: ${e.message}", processingProgress = 0f) }
            } finally {
                // End the process in the global state manager
                ProcessingStateManager.endProcess(messageScope)
            }
        }
    }

    /**
     * Handle when a PDF file is picked
     */
    fun onFilePicked(uri: Uri) {
        viewModelScope.launch {
            // Reset any previous state
            _uiState.update { it.copy(selectedPdfUri = uri, startPage = "1", endPage = "", isStartPageValid = true, isEndPageValid = true, isRangeValid = true, errorMessage = null, outputDetails = null, isProcessing = false, processingProgress = 0f, showSaveLocationSelector = true )}

            // Get PDF information
            val fileName = FileInfoUtils.getFileName(context, uri)
            val fileSize = FileInfoUtils.getFileSize(context, uri) ?: 0L
            val mimeType = FileInfoUtils.getMimeType(context, uri) ?: "application/pdf"
            val pageCount = pdfService.getPageCount(context, uri) ?: 0  // Get page count

            // Create FileDetails object for the selected PDF
            val fileDetails = FileDetails(
                uri = uri,
                name = fileName,
                size = fileSize,
                mimeType = mimeType,
                pageCount = pageCount
            )
            _uiState.update { it.copy(pdfFileName = fileName, pdfFileSize = fileSize, pdfPageCount = pageCount, endPage = pageCount.toString(), selectedPdfDetails = fileDetails, savePath = "Downloads" )}
        }
    }

    /**
     * Validate page inputs to ensure they are valid numbers within the PDF page range
     */
    private fun validatePageInputs() {
        val currentState = _uiState.value
        val pageCount = currentState.pdfPageCount
        if (pageCount == 0) return // Can't validate if we don't know the page count
        val startPageValue = currentState.startPage.toIntOrNull()
        val endPageValue = currentState.endPage.toIntOrNull()
        val isStartPageValid = startPageValue != null && startPageValue >= 1 && startPageValue <= pageCount  // Validate start page
        val isEndPageValid = endPageValue != null && endPageValue >= 1 && endPageValue <= pageCount          // Validate end page
        val isRangeValid = startPageValue != null && endPageValue != null && startPageValue <= endPageValue  // Validate range (start page <= end page)
        _uiState.update { it.copy(isStartPageValid = isStartPageValid, isEndPageValid = isEndPageValid, isRangeValid = isRangeValid )}
    }

    /**
     * Update the save location
     */
    fun updateSaveLocation(path: String) {
        if (_uiState.value.outputDetails != null) {
            _uiState.update { it.copy(savePath = path, outputDetails = null) }
        } else {
            _uiState.update { it.copy(savePath = path) }
        }
    }

    /**
     * Update the save mode
     */
    fun updateSaveMode(saveMode: SaveMode) {
        if (_uiState.value.outputDetails != null) {
            _uiState.update { it.copy(saveMode = saveMode, outputDetails = null) }
        } else {
            _uiState.update { it.copy(saveMode = saveMode) }
        }
    }

    /**
     * Toggle the save location selector visibility
     */
    fun toggleSaveLocationSelector(show: Boolean) {
        _uiState.update { it.copy(showSaveLocationSelector = show) }
    }

    /**
     * Update the start page input value
     */
    fun onStartPageChanged(value: String) {
        _uiState.update { it.copy(startPage = value) }
        validatePageInputs()
    }

    /**
     * Update the end page input value
     */
    fun onEndPageChanged(value: String) {
        _uiState.update { it.copy(endPage = value) }
        validatePageInputs()
    }

    /**
     * Clear the selected PDF file
     */
    fun clearPdfFile() {
        _uiState.update { it.copy(selectedPdfUri = null, selectedPdfDetails = null, pdfPageCount = 0, pdfFileName = "", pdfFileSize = 0L, startPage = "", endPage = "", isStartPageValid = false, isEndPageValid = false, isRangeValid = false)}
    }

    /**
     * Clear output and reset to input state
     */
    fun resetOutput() {
        _uiState.update { it.copy(outputDetails = null, processingProgress = 0f, errorMessage = null )}
    }

    /**
     * Cancels the ongoing split operation
     */
    fun cancelOperation() {
        // Update the UI state to indicate processing has stopped
        _uiState.update { it.copy(isProcessing = false, processingProgress = 0f, errorMessage = null) }
        // End the process in the global state manager
        ProcessingStateManager.endProcess("split_pdf")
    }
}```

### `app\src\main\java\com\example\doc_tools\features\settings\presentation\ui\SettingsScreen.kt`

```kt
package com.example.doc_tools.features.settings.presentation.ui

import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.selection.selectable
import androidx.compose.foundation.selection.selectableGroup
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.BrightnessAuto
import androidx.compose.material.icons.filled.Close
import androidx.compose.material.icons.filled.DarkMode
import androidx.compose.material.icons.filled.Email
import androidx.compose.material.icons.filled.Info
import androidx.compose.material.icons.filled.LightMode
import androidx.compose.material.icons.filled.PrivacyTip
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.HorizontalDivider
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.ModalBottomSheet
import androidx.compose.material3.RadioButton
import androidx.compose.material3.Text
import androidx.compose.material3.rememberModalBottomSheetState
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.semantics.Role
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.core.content.ContextCompat.startActivity
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation.NavController
import com.example.doc_tools.core.ui.components.layout.BaseToolScreen
import com.example.doc_tools.features.settings.presentation.ui.components.SettingItem
import com.example.doc_tools.features.settings.presentation.ui.components.SettingsSection
import com.example.doc_tools.features.settings.presentation.ui.components.ThemeOption
import com.example.doc_tools.features.settings.presentation.viewmodel.SettingsViewModel
import com.example.doc_tools.features.settings.presentation.viewmodel.ThemeMode

/**
 * Composable function that displays the settings screen of the application.
 *
 * @param navController The [NavController] used for navigation.
 * @param isDarkTheme A boolean indicating whether the dark theme is currently active.
 * @param onThemeToggle A lambda function to be invoked when the theme toggle is clicked.
 * @param modifier An optional [Modifier] to be applied to the composable.
 */
@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun SettingsScreen(
    navController: NavController,
    isDarkTheme: Boolean,
    onThemeToggle: () -> Unit,
    modifier: Modifier = Modifier
) {
    val viewModel: SettingsViewModel = viewModel()
    val uiState by viewModel.uiState.collectAsState()
    val context = LocalContext.current
    val bottomSheetState = rememberModalBottomSheetState(skipPartiallyExpanded = false)
    
    BaseToolScreen(
        title = "Settings",
        navController = navController,
        isDarkTheme = isDarkTheme,
        onThemeToggle = onThemeToggle,
        showBackButton = true,
        contentScrollable = true,
        modifier = modifier
    ) {
        Column(modifier = Modifier.fillMaxSize().background(MaterialTheme.colorScheme.surface, shape = RoundedCornerShape(24.dp)).padding(24.dp)) {

            SettingsSection(title = "Theme Settings") {

                val currentSystemTheme = isSystemInDarkTheme()
                var selectedTheme by remember { 
                    mutableStateOf(
                        when {
                            isDarkTheme && currentSystemTheme -> ThemeMode.SYSTEM
                            isDarkTheme -> ThemeMode.DARK
                            else -> ThemeMode.LIGHT
                        }
                    ) 
                }
                
                // Theme options
                Column(Modifier.selectableGroup()) {

                    ThemeOption(title = "Light", icon = Icons.Default.LightMode, selected = selectedTheme == ThemeMode.LIGHT,
                        onClick = { 
                            selectedTheme = ThemeMode.LIGHT
                            if (isDarkTheme) onThemeToggle()
                            viewModel.updateThemeMode(ThemeMode.LIGHT)
                        }
                    )
                    
                    ThemeOption(title = "Dark", icon = Icons.Default.DarkMode, selected = selectedTheme == ThemeMode.DARK,
                        onClick = { 
                            selectedTheme = ThemeMode.DARK
                            if (!isDarkTheme) onThemeToggle()
                            viewModel.updateThemeMode(ThemeMode.DARK)
                        }
                    )
                    
                    ThemeOption(title = "System Default", icon = Icons.Default.BrightnessAuto, selected = selectedTheme == ThemeMode.SYSTEM,
                        onClick = { 
                            selectedTheme = ThemeMode.SYSTEM
                            if (isDarkTheme != currentSystemTheme) onThemeToggle()
                            viewModel.updateThemeMode(ThemeMode.SYSTEM)
                        }
                    )
                }
            }
            
            Spacer(modifier = Modifier.height(24.dp))
            
            // About section
            SettingsSection(title = "About") {
                // App version
                SettingItem(title = "Version", description = uiState.appVersion, icon = Icons.Default.Info, onClick = { })
                // Privacy policy
                SettingItem(title = "Privacy Policy", description = "View our privacy policy", icon = Icons.Default.PrivacyTip, onClick = { viewModel.setPrivacyDialogVisible(true) })
                // Contact developer
                SettingItem(title = "Contact Developer", description = "Send feedback or report issues", icon = Icons.Default.Email,
                    onClick = {
                        val emailIntent = viewModel.contactDeveloper()
                        try {
                            startActivity(context, emailIntent, null)
                        } catch (e: Exception) {
                            // Handle case where no email app is available
                        }
                    }
                )
            }
        }
        
        // Privacy Policy Bottom Sheet
        if (uiState.isPrivacyDialogVisible) {
            ModalBottomSheet(onDismissRequest = { viewModel.setPrivacyDialogVisible(false) }, sheetState = bottomSheetState, containerColor = MaterialTheme.colorScheme.surface,
                contentColor = MaterialTheme.colorScheme.onSurface
            ) {
                Column(modifier = Modifier.fillMaxWidth()) {
                    // Header with title and close button
                    Row(modifier = Modifier.fillMaxWidth().padding(start = 24.dp, end = 24.dp), horizontalArrangement = Arrangement.SpaceBetween, verticalAlignment = Alignment.CenterVertically) {
                        Text(text = "Privacy Policy", style = MaterialTheme.typography.titleLarge, fontWeight = FontWeight.Normal)
                        IconButton(onClick = { viewModel.setPrivacyDialogVisible(false) }) {
                            Icon(imageVector = Icons.Default.Close, contentDescription = "Close")
                        }
                    }

                    HorizontalDivider(modifier = Modifier.fillMaxWidth(), color = MaterialTheme.colorScheme.outline)

                    // Content
                    Text(text = "This app works fully offline. No data is collected or shared.", modifier = Modifier.padding(24.dp))
                    Spacer(modifier = Modifier.height(32.dp))
                }
            }
        }
    }
}





```

### `app\src\main\java\com\example\doc_tools\features\settings\presentation\ui\components\SettingItem.kt`

```kt
package com.example.doc_tools.features.settings.presentation.ui.components

import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.unit.dp

@Composable
fun SettingItem(title: String, description: String, icon: ImageVector, onClick: () -> Unit) {

    Row(
        modifier = Modifier.fillMaxWidth().clickable(onClick = onClick).padding(vertical = 14.dp, horizontal = 8.dp),
        verticalAlignment = Alignment.CenterVertically
    ) {
        Icon(imageVector = icon, contentDescription = null, tint = MaterialTheme.colorScheme.onSurface,
            modifier = Modifier.size(18.dp)
        )

        Spacer(modifier = Modifier.width(16.dp))

        Column(modifier = Modifier.weight(1f)) {
            Text(
                text = title,
                style = MaterialTheme.typography.bodyMedium,
                color = MaterialTheme.colorScheme.onSurfaceVariant
            )
            Spacer(modifier = Modifier.height(4.dp))

            Text(
                text = description,
                style = MaterialTheme.typography.bodySmall,
                color = MaterialTheme.colorScheme.onSurfaceVariant.copy(alpha = 0.6f),
            )
        }
    }
}```

### `app\src\main\java\com\example\doc_tools\features\settings\presentation\ui\components\SettingsSection.kt`

```kt
package com.example.doc_tools.features.settings.presentation.ui.components

import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.HorizontalDivider
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

@Composable
fun SettingsSection(title: String, content: @Composable () -> Unit) {
    Column(modifier = Modifier.fillMaxWidth()) {
        Text(
            text = title,
            style = MaterialTheme.typography.titleSmall,
            color = MaterialTheme.colorScheme.onSurfaceVariant,
            modifier = Modifier.padding(vertical = 16.dp)
        )

        HorizontalDivider(modifier = Modifier.padding(bottom = 8.dp), color = MaterialTheme.colorScheme.outline, thickness = 1.dp, )

        Card(
            modifier = Modifier.fillMaxWidth(),
            colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surface),
            shape = RoundedCornerShape(12.dp)
        ) {
            Column {
                content()
            }
        }
    }
}```

### `app\src\main\java\com\example\doc_tools\features\settings\presentation\ui\components\ThemeOption.kt`

```kt
package com.example.doc_tools.features.settings.presentation.ui.components

import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.selection.selectable
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.RadioButton
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.semantics.Role
import androidx.compose.ui.unit.dp

@Composable
fun ThemeOption(title: String, icon: ImageVector, selected: Boolean, onClick: () -> Unit) {
    Row(
        modifier = Modifier.fillMaxWidth().selectable(
            selected = selected,
            onClick = onClick,
            role = Role.RadioButton
        )
            .padding(vertical = 12.dp, horizontal = 8.dp),
        verticalAlignment = Alignment.CenterVertically
    ) {
        Icon(
            imageVector = icon,
            contentDescription = null,
            tint = MaterialTheme.colorScheme.onSurfaceVariant,
            modifier = Modifier.size(18.dp)
        )

        Spacer(modifier = Modifier.width(16.dp))

        Text(
            text = title,
            style = MaterialTheme.typography.bodyMedium,
            modifier = Modifier.weight(1f)
        )

        RadioButton(
            selected = selected,
            onClick = null // null because the parent is already selectable
        )
    }
}```

### `app\src\main\java\com\example\doc_tools\features\settings\presentation\viewmodel\SettingsViewModel.kt`

```kt
package com.example.doc_tools.features.settings.presentation.viewmodel

import android.app.Application
import android.content.Intent
import android.content.pm.PackageManager
import android.net.Uri
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch

/**
 * Enum representing the available theme modes
 */
enum class ThemeMode {
    LIGHT, DARK, SYSTEM
}

/**
 * Data class representing the UI state for the Settings screen
 */
data class SettingsUiState(
    val themeMode: ThemeMode = ThemeMode.SYSTEM,
    val appVersion: String = "",
    val isPrivacyDialogVisible: Boolean = false
)

/**
 * ViewModel for the Settings screen
 */
class SettingsViewModel(application: Application) : AndroidViewModel(application) {
    
    private val _uiState = MutableStateFlow(SettingsUiState())
    val uiState: StateFlow<SettingsUiState> = _uiState.asStateFlow()
    
    init {
        loadAppVersion()
    }
    
    /**
     * Loads the app version from the package info
     */
    private fun loadAppVersion() {
        viewModelScope.launch {
            try {
                val packageInfo = getApplication<Application>().packageManager.getPackageInfo(
                    getApplication<Application>().packageName, 0
                )
                _uiState.value = _uiState.value.copy(
                    appVersion = "${packageInfo.versionName} (${packageInfo.versionCode})"
                )
            } catch (e: PackageManager.NameNotFoundException) {
                _uiState.value = _uiState.value.copy(appVersion = "Unknown")
            }
        }
    }
    
    /**
     * Updates the theme mode
     */
    fun updateThemeMode(themeMode: ThemeMode) {
        _uiState.value = _uiState.value.copy(themeMode = themeMode)
    }
    
    /**
     * Shows or hides the privacy dialog
     */
    fun setPrivacyDialogVisible(visible: Boolean) {
        _uiState.value = _uiState.value.copy(isPrivacyDialogVisible = visible)
    }
    
    /**
     * Opens email to contact developer
     */
    fun contactDeveloper(emailAddress: String = "developer@example.com"): Intent {
        return Intent(Intent.ACTION_SENDTO).apply {
            data = Uri.parse("mailto:$emailAddress")
            putExtra(Intent.EXTRA_SUBJECT, "Doc Tools App Feedback")
        }
    }
} ```

### `app\src\main\res\drawable\ic_compress_images.xml`

```xml
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="24dp"
    android:height="24dp"
    android:viewportWidth="24"
    android:viewportHeight="24"
    android:tint="?attr/colorOnSurface"
    android:autoMirrored="true">
    <path
        android:fillColor="@android:color/white"
        android:pathData="M12,17.67C15.44,17.67 18.08,18.5 19.71,19.2C19.92,19.22 20,19.17 20,19.1V8.76C20,8.73 19.97,8.7 19.86,8.71C18.11,9.53 15.09,10.69 12,10.69C8.91,10.69 5.89,9.53 4.14,8.71C4.03,8.7 4,8.73 4,8.76V19.1C4,19.17 4.08,19.22 4.29,19.2C5.92,18.5 8.56,17.67 12,17.67ZM22,19.09C22,19.92 21.52,20.55 20.95,20.89C20.38,21.22 19.62,21.34 18.92,21.04C17.49,20.42 15.11,19.67 12,19.67C8.89,19.67 6.51,20.42 5.08,21.04C4.38,21.34 3.62,21.22 3.06,20.89C2.49,20.55 2,19.92 2,19.09V8.76C2,7.2 3.68,6.29 4.99,6.9C6.65,7.67 9.35,8.69 12,8.69C14.65,8.69 17.35,7.67 19.01,6.9C20.32,6.29 22,7.2 22,8.76V19.09Z"/>
    <path
        android:fillColor="@android:color/white"
        android:pathData="M18.89,3.44C19.9,3.13 21,3.87 21,5V8H19V5.56C18.22,5.9 17.19,6.32 16.1,6.68C14.78,7.12 13.27,7.5 12,7.5C10.73,7.5 9.22,7.12 7.9,6.68C6.81,6.32 5.78,5.9 5,5.56V8H3V5C3,3.8 4.25,3.03 5.31,3.51C6.09,3.86 7.27,4.37 8.53,4.78C9.8,5.2 11.06,5.5 12,5.5C12.94,5.5 14.2,5.2 15.47,4.78C16.73,4.37 17.91,3.86 18.69,3.51L18.89,3.44Z"/>
    <path
        android:fillColor="@android:color/white"
        android:pathData="M17.12,16.02C17.28,16.21 17.14,16.5 16.89,16.5H7.22C6.96,16.5 6.82,16.18 7.01,15.99L9.8,13.2C9.91,13.09 10.09,13.08 10.21,13.19L11.53,14.34C11.65,14.44 11.84,14.43 11.95,14.31L13.76,12.27C13.89,12.13 14.11,12.14 14.22,12.29L17.12,16.02Z"/>
</vector>
```

### `app\src\main\res\drawable\ic_default_foreground.xml`

```xml
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="108dp"
    android:height="108dp"
    android:viewportWidth="960"
    android:viewportHeight="960"
    android:tint="#111111"
    android:autoMirrored="true">
  <group android:scaleX="0.58"
      android:scaleY="0.58"
      android:translateX="201.6"
      android:translateY="201.6">
    <path
        android:fillColor="@android:color/white"
        android:pathData="M320,520L640,520L640,440L320,440L320,520ZM320,640L640,640L640,560L320,560L320,640ZM320,760L520,760L520,680L320,680L320,760ZM240,880Q207,880 183.5,856.5Q160,833 160,800L160,160Q160,127 183.5,103.5Q207,80 240,80L560,80L800,320L800,800Q800,833 776.5,856.5Q753,880 720,880L240,880ZM520,360L520,160L240,160Q240,160 240,160Q240,160 240,160L240,800Q240,800 240,800Q240,800 240,800L720,800Q720,800 720,800Q720,800 720,800L720,360L520,360ZM240,160L240,160L240,360L240,360L240,160L240,360L240,360L240,800Q240,800 240,800Q240,800 240,800L240,800Q240,800 240,800Q240,800 240,800L240,160Q240,160 240,160Q240,160 240,160Z"/>
  </group>
</vector>
```

### `app\src\main\res\mipmap-anydpi-v26\ic_doc_tools.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="@color/ic_default_background"/>
    <foreground android:drawable="@drawable/ic_default_foreground"/>
</adaptive-icon>```

### `app\src\main\res\mipmap-anydpi-v26\ic_doc_tools_round.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="@color/ic_default_background"/>
    <foreground android:drawable="@drawable/ic_default_foreground"/>
</adaptive-icon>```

### `app\src\main\res\values\colors.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="purple_200">#FFBB86FC</color>
    <color name="purple_500">#FF6200EE</color>
    <color name="purple_700">#FF3700B3</color>
    <color name="teal_200">#FF03DAC5</color>
    <color name="teal_700">#FF018786</color>
    <color name="black">#FF000000</color>
    <color name="white">#FFFFFFFF</color>
</resources>```

### `app\src\main\res\values\ic_default_background.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="ic_default_background">#FFFFFF</color>
</resources>```

### `app\src\main\res\values\strings.xml`

```xml
<resources>
    <string name="app_name">Doc tools</string>
</resources>```

### `app\src\main\res\values\themes.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <style name="Theme.Pdf_img_tools_app" parent="android:Theme.Material.Light.NoActionBar" />
</resources>```

### `app\src\main\res\xml\backup_rules.xml`

```xml
<?xml version="1.0" encoding="utf-8"?><!--
   Sample backup rules file; uncomment and customize as necessary.
   See https://developer.android.com/guide/topics/data/autobackup
   for details.
   Note: This file is ignored for devices older than API 31
   See https://developer.android.com/about/versions/12/backup-restore
-->
<full-backup-content>
    <!--
   <include domain="sharedpref" path="."/>
   <exclude domain="sharedpref" path="device.xml"/>
-->
</full-backup-content>```

### `app\src\main\res\xml\data_extraction_rules.xml`

```xml
<?xml version="1.0" encoding="utf-8"?><!--
   Sample data extraction rules file; uncomment and customize as necessary.
   See https://developer.android.com/about/versions/12/backup-restore#xml-changes
   for details.
-->
<data-extraction-rules>
    <cloud-backup>
        <!-- TODO: Use <include> and <exclude> to control what is backed up.
        <include .../>
        <exclude .../>
        -->
    </cloud-backup>
    <!--
    <device-transfer>
        <include .../>
        <exclude .../>
    </device-transfer>
    -->
</data-extraction-rules>```

### `app\src\main\res\xml\file_paths.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<paths>
    <cache-path
        name="resize_cache"
        path="resize_temp/" />
    <files-path
        name="resize_files"
        path="resize/" />
    <external-path
        name="external_files"
        path="." />
</paths>```

### `app\src\test\java\com\example\doc_tools\ExampleUnitTest.kt`

```kt
package com.example.doc_tools

import org.junit.Test

import org.junit.Assert.*

/**
 * Example local unit test, which will execute on the development machine (host).
 *
 * See [testing documentation](http://d.android.com/tools/testing).
 */
class ExampleUnitTest {
    @Test
    fun addition_isCorrect() {
        assertEquals(4, 2 + 2)
    }
}```

### `gradle\libs.versions.toml`

```toml
[versions]
agp = "8.10.0"
kotlin = "2.0.21"
coreKtx = "1.16.0"
junit = "4.13.2"
junitVersion = "1.2.1"
espressoCore = "3.6.1"
lifecycleRuntimeKtx = "2.8.7"
activityCompose = "1.10.1"
composeBom = "2024.09.00"

[libraries]
androidx-core-ktx = { group = "androidx.core", name = "core-ktx", version.ref = "coreKtx" }
junit = { group = "junit", name = "junit", version.ref = "junit" }
androidx-junit = { group = "androidx.test.ext", name = "junit", version.ref = "junitVersion" }
androidx-espresso-core = { group = "androidx.test.espresso", name = "espresso-core", version.ref = "espressoCore" }
androidx-lifecycle-runtime-ktx = { group = "androidx.lifecycle", name = "lifecycle-runtime-ktx", version.ref = "lifecycleRuntimeKtx" }
androidx-activity-compose = { group = "androidx.activity", name = "activity-compose", version.ref = "activityCompose" }
androidx-compose-bom = { group = "androidx.compose", name = "compose-bom", version.ref = "composeBom" }
androidx-ui = { group = "androidx.compose.ui", name = "ui" }
androidx-ui-graphics = { group = "androidx.compose.ui", name = "ui-graphics" }
androidx-ui-tooling = { group = "androidx.compose.ui", name = "ui-tooling" }
androidx-ui-tooling-preview = { group = "androidx.compose.ui", name = "ui-tooling-preview" }
androidx-ui-test-manifest = { group = "androidx.compose.ui", name = "ui-test-manifest" }
androidx-ui-test-junit4 = { group = "androidx.compose.ui", name = "ui-test-junit4" }
androidx-material3 = { group = "androidx.compose.material3", name = "material3" }

[plugins]
android-application = { id = "com.android.application", version.ref = "agp" }
kotlin-android = { id = "org.jetbrains.kotlin.android", version.ref = "kotlin" }
kotlin-compose = { id = "org.jetbrains.kotlin.plugin.compose", version.ref = "kotlin" }

```

### `gradle\wrapper\gradle-wrapper.properties`

```properties
#Sun Apr 13 16:00:56 IST 2025
distributionBase=GRADLE_USER_HOME
distributionPath=wrapper/dists
distributionUrl=https\://services.gradle.org/distributions/gradle-8.11.1-bin.zip
zipStoreBase=GRADLE_USER_HOME
zipStorePath=wrapper/dists
```

