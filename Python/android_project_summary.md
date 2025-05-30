# 🧠 Project Full Summary

- Root Dir: `C:\Users\Purve\AndroidStudioProjects\pdf_img_tools_app`

## 📁 Folder Structure

```
pdf_img_tools_app/
├── .cursor
│   └── rules
├── .gitignore
├── .kotlin
│   ├── errors
│   │   ├── errors-1744569361420.log
│   │   ├── errors-1745049206722.log
│   │   ├── errors-1745600496650.log
│   │   └── errors-1747998708624.log
│   └── sessions
├── .windsurf
│   └── rules
│       └── rules.md
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
│       │               └── pdf_img_tools_app
│       │                   └── ExampleInstrumentedTest.kt
│       ├── main
│       │   ├── AndroidManifest.xml
│       │   ├── java
│       │   │   └── com
│       │   │       └── example
│       │   │           └── pdf_img_tools_app
│       │   │               ├── MainActivity.kt
│       │   │               ├── config
│       │   │               │   └── FeatureFlags.kt
│       │   │               ├── core
│       │   │               │   ├── AppNavigation.kt
│       │   │               │   ├── CommonToolState.kt
│       │   │               │   ├── FileArchiverViewModel.kt
│       │   │               │   └── ui
│       │   │               │       ├── components
│       │   │               │       │   ├── CheckerboardBackground.kt
│       │   │               │       │   ├── CommonUIComponents.kt
│       │   │               │       │   ├── DetailRow.kt
│       │   │               │       │   ├── ImageCanvas.kt
│       │   │               │       │   ├── ProcessingIndicator.kt
│       │   │               │       │   ├── ThemeSelector.kt
│       │   │               │       │   └── ToolProgressIndicator.kt
│       │   │               │       └── theme
│       │   │               │           ├── Color.kt
│       │   │               │           ├── Shape.kt
│       │   │               │           ├── Theme.kt
│       │   │               │           └── Type.kt
│       │   │               ├── data
│       │   │               │   └── repository
│       │   │               │       └── ToolRepository.kt
│       │   │               ├── features
│       │   │               │   ├── home
│       │   │               │   │   └── HomeScreen.kt
│       │   │               │   ├── image
│       │   │               │   │   ├── compressimages
│       │   │               │   │   │   ├── CompressImagesScreen.kt
│       │   │               │   │   │   ├── CompressImagesUiState.kt
│       │   │               │   │   │   └── CompressImagesViewModel.kt
│       │   │               │   │   ├── convertimages
│       │   │               │   │   │   ├── ConvertImagesScreen.kt
│       │   │               │   │   │   ├── ConvertImagesUiState.kt
│       │   │               │   │   │   └── ConvertImagesViewModel.kt
│       │   │               │   │   ├── imageresizer
│       │   │               │   │   │   ├── ImageResizerScreen.kt
│       │   │               │   │   │   └── ImageResizerViewModel.kt
│       │   │               │   │   └── resizeimages
│       │   │               │   │       ├── BatchImageResizeViewModel.kt
│       │   │               │   │       ├── ResizeImagesScreen.kt
│       │   │               │   │       └── ResizeImagesUiState.kt
│       │   │               │   └── pdf
│       │   │               │       ├── compresspdf
│       │   │               │       │   ├── CompressPdfScreen.kt
│       │   │               │       │   ├── CompressPdfUiState.kt
│       │   │               │       │   └── CompressPdfViewModel.kt
│       │   │               │       ├── imagestopdf
│       │   │               │       │   ├── ImagesToPdfScreen.kt
│       │   │               │       │   ├── ImagesToPdfUiState.kt
│       │   │               │       │   └── ImagesToPdfViewModel.kt
│       │   │               │       ├── mergepdf
│       │   │               │       │   ├── MergePdfScreen.kt
│       │   │               │       │   ├── MergePdfUiState.kt
│       │   │               │       │   └── MergePdfViewModel.kt
│       │   │               │       ├── pdftoimages
│       │   │               │       │   ├── PdfToImagesScreen.kt
│       │   │               │       │   ├── PdfToImagesUiState.kt
│       │   │               │       │   └── PdfToImagesViewModel.kt
│       │   │               │       └── splitpdf
│       │   │               │           ├── SplitPdfScreen.kt
│       │   │               │           ├── SplitPdfUiState.kt
│       │   │               │           └── SplitPdfViewModel.kt
│       │   │               ├── model
│       │   │               │   ├── ImageCanvasState.kt
│       │   │               │   ├── ImageResizeTemplate.kt
│       │   │               │   ├── ResizeMode.kt
│       │   │               │   ├── ResizedImage.kt
│       │   │               │   ├── SaveLocationType.kt
│       │   │               │   ├── SaveMode.kt
│       │   │               │   ├── ToolItem.kt
│       │   │               │   └── UiMessageData.kt
│       │   │               ├── navigation
│       │   │               │   └── AppDestinations.kt
│       │   │               ├── service
│       │   │               │   ├── ImageResizeService.kt
│       │   │               │   ├── ImageService.kt
│       │   │               │   └── PdfService.kt
│       │   │               ├── ui
│       │   │               │   └── components
│       │   │               │       ├── AppTopBar.kt
│       │   │               │       ├── BaseToolScreen.kt
│       │   │               │       ├── FileBottomSheet.kt
│       │   │               │       ├── FilePickerHandler.kt
│       │   │               │       ├── ImageBatchComponents.kt
│       │   │               │       ├── InlineMessage.kt
│       │   │               │       ├── MessageDialog.kt
│       │   │               │       ├── OutputFileDetails.kt
│       │   │               │       ├── ProgressToolButton.kt
│       │   │               │       ├── ReusableSaveLocationSelector.kt
│       │   │               │       ├── SaveAsArchiveDialog.kt
│       │   │               │       ├── SingleFilePicker.kt
│       │   │               │       ├── SmartMessageDisplay.kt
│       │   │               │       ├── ToolCard.kt
│       │   │               │       └── UiMessageDisplay.kt
│       │   │               ├── utils
│       │   │               │   ├── ArchiveUtils.kt
│       │   │               │   ├── DisplayMethod.kt
│       │   │               │   ├── FileUtils.kt
│       │   │               │   ├── MessageDisplayManager.kt
│       │   │               │   ├── NotificationUtils.kt
│       │   │               │   ├── SaveLocationUtils.kt
│       │   │               │   └── UiMessageBus.kt
│       │   │               └── viewmodel
│       │   └── res
│       │       ├── drawable
│       │       │   ├── ic_launcher_background.xml
│       │       │   └── ic_launcher_foreground.xml
│       │       ├── mipmap-anydpi-v26
│       │       │   ├── ic_launcher.xml
│       │       │   └── ic_launcher_round.xml
│       │       ├── mipmap-hdpi
│       │       │   ├── ic_launcher.webp
│       │       │   └── ic_launcher_round.webp
│       │       ├── mipmap-mdpi
│       │       │   ├── ic_launcher.webp
│       │       │   └── ic_launcher_round.webp
│       │       ├── mipmap-xhdpi
│       │       │   ├── ic_launcher.webp
│       │       │   └── ic_launcher_round.webp
│       │       ├── mipmap-xxhdpi
│       │       │   ├── ic_launcher.webp
│       │       │   └── ic_launcher_round.webp
│       │       ├── mipmap-xxxhdpi
│       │       │   ├── ic_launcher.webp
│       │       │   └── ic_launcher_round.webp
│       │       ├── values
│       │       │   ├── colors.xml
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
│                       └── pdf_img_tools_app
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
| AppContent       | function       | app\src\main\java\com\example\pdf_img_tools_app\MainActivity.kt |
| AppDestinations  | class          | app\src\main\java\com\example\pdf_img_tools_app\core\AppNavigation.kt |
| AppDestinations  | class          | app\src\main\java\com\example\pdf_img_tools_app\navigation\AppDestinations.kt |
| AppNavigation    | function       | app\src\main\java\com\example\pdf_img_tools_app\core\AppNavigation.kt |
| AppSnackbarHost  | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\NotificationUtils.kt |
| AppTopBar        | function       | app\src\main\java\com\example\pdf_img_tools_app\ui\components\AppTopBar.kt |
| ArchiveUtils     | class          | app\src\main\java\com\example\pdf_img_tools_app\utils\ArchiveUtils.kt |
| BaseToolScreen   | function       | app\src\main\java\com\example\pdf_img_tools_app\ui\components\BaseToolScreen.kt |
| BatchImageResizeViewModel | class          | app\src\main\java\com\example\pdf_img_tools_app\features\image\resizeimages\BatchImageResizeViewModel.kt |
| CheckerboardBackground | function       | app\src\main\java\com\example\pdf_img_tools_app\core\ui\components\CheckerboardBackground.kt |
| ClearAll         | class          | app\src\main\java\com\example\pdf_img_tools_app\utils\UiMessageBus.kt |
| ClearScope       | class          | app\src\main\java\com\example\pdf_img_tools_app\utils\UiMessageBus.kt |
| ColorConverter   | class          | app\src\main\java\com\example\pdf_img_tools_app\core\ui\components\ProcessingIndicator.kt |
| CommonToolState  | class          | app\src\main\java\com\example\pdf_img_tools_app\core\CommonToolState.kt |
| CompactDetailRow | function       | app\src\main\java\com\example\pdf_img_tools_app\ui\components\OutputFileDetails.kt |
| CompressButton   | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\compressimages\CompressImagesScreen.kt |
| CompressImagesScreen | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\compressimages\CompressImagesScreen.kt |
| CompressImagesUiState | class          | app\src\main\java\com\example\pdf_img_tools_app\features\image\compressimages\CompressImagesUiState.kt |
| CompressImagesViewModel | class          | app\src\main\java\com\example\pdf_img_tools_app\features\image\compressimages\CompressImagesViewModel.kt |
| CompressPdfScreen | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\compresspdf\CompressPdfScreen.kt |
| CompressPdfUiState | class          | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\compresspdf\CompressPdfUiState.kt |
| CompressPdfViewModel | class          | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\compresspdf\CompressPdfViewModel.kt |
| CompressionQualitySection | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\compresspdf\CompressPdfScreen.kt |
| CompressionSettingsSection | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\compressimages\CompressImagesScreen.kt |
| ConfirmMergeDialog | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\mergepdf\MergePdfScreen.kt |
| ConversionSettingsSection | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\convertimages\ConvertImagesScreen.kt |
| ConvertButton    | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\convertimages\ConvertImagesScreen.kt |
| ConvertButton    | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\imagestopdf\ImagesToPdfScreen.kt |
| ConvertButton    | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\pdftoimages\PdfToImagesScreen.kt |
| ConvertImagesScreen | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\convertimages\ConvertImagesScreen.kt |
| ConvertImagesUiState | class          | app\src\main\java\com\example\pdf_img_tools_app\features\image\convertimages\ConvertImagesUiState.kt |
| ConvertImagesViewModel | class          | app\src\main\java\com\example\pdf_img_tools_app\features\image\convertimages\ConvertImagesViewModel.kt |
| CustomLocationSelector | function       | app\src\main\java\com\example\pdf_img_tools_app\ui\components\SaveAsArchiveDialog.kt |
| CustomSnackbar   | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\NotificationUtils.kt |
| DetailRow        | function       | app\src\main\java\com\example\pdf_img_tools_app\core\ui\components\DetailRow.kt |
| Dismiss          | class          | app\src\main\java\com\example\pdf_img_tools_app\utils\UiMessageBus.kt |
| DpiSelectionSection | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\pdftoimages\PdfToImagesScreen.kt |
| ErrorMessage     | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\splitpdf\SplitPdfScreen.kt |
| ExampleInstrumentedTest | class          | app\src\androidTest\java\com\example\pdf_img_tools_app\ExampleInstrumentedTest.kt |
| ExampleUnitTest  | class          | app\src\test\java\com\example\pdf_img_tools_app\ExampleUnitTest.kt |
| Factory          | class          | app\src\main\java\com\example\pdf_img_tools_app\features\image\resizeimages\BatchImageResizeViewModel.kt |
| FeatureFlags     | class          | app\src\main\java\com\example\pdf_img_tools_app\config\FeatureFlags.kt |
| FileArchiverViewModel | class          | app\src\main\java\com\example\pdf_img_tools_app\core\FileArchiverViewModel.kt |
| FileBottomSheet  | function       | app\src\main\java\com\example\pdf_img_tools_app\ui\components\FileBottomSheet.kt |
| FileDetails      | class          | app\src\main\java\com\example\pdf_img_tools_app\utils\FileUtils.kt |
| FileListItem     | function       | app\src\main\java\com\example\pdf_img_tools_app\ui\components\FileBottomSheet.kt |
| FilePickerHandler | function       | app\src\main\java\com\example\pdf_img_tools_app\ui\components\FilePickerHandler.kt |
| FilePickerSection | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\mergepdf\MergePdfScreen.kt |
| FileSelectionSection | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\compressimages\CompressImagesScreen.kt |
| FileSelectionSection | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\convertimages\ConvertImagesScreen.kt |
| FileSelectionSection | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\resizeimages\ResizeImagesScreen.kt |
| FileSelectionSection | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\compresspdf\CompressPdfScreen.kt |
| FileSelectionSection | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\imagestopdf\ImagesToPdfScreen.kt |
| FileSelectionSection | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\pdftoimages\PdfToImagesScreen.kt |
| FileSelectionSection | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\splitpdf\SplitPdfScreen.kt |
| FileSelectorCard | function       | app\src\main\java\com\example\pdf_img_tools_app\ui\components\ImageBatchComponents.kt |
| FileUtils        | class          | app\src\main\java\com\example\pdf_img_tools_app\utils\FileUtils.kt |
| FixedToolsGrid   | function       | app\src\main\java\com\example\pdf_img_tools_app\features\home\HomeScreen.kt |
| FormatDropdown   | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\convertimages\ConvertImagesScreen.kt |
| FormatOption     | function       | app\src\main\java\com\example\pdf_img_tools_app\ui\components\ImageBatchComponents.kt |
| HandleSnackbarMessages | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\MessageDisplayManager.kt |
| HeaderSection    | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\compressimages\CompressImagesScreen.kt |
| HeaderSection    | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\convertimages\ConvertImagesScreen.kt |
| HeaderSection    | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\resizeimages\ResizeImagesScreen.kt |
| HeaderSection    | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\compresspdf\CompressPdfScreen.kt |
| HeaderSection    | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\imagestopdf\ImagesToPdfScreen.kt |
| HeaderSection    | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\mergepdf\MergePdfScreen.kt |
| HeaderSection    | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\pdftoimages\PdfToImagesScreen.kt |
| HeaderSection    | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\splitpdf\SplitPdfScreen.kt |
| HomeScreen       | function       | app\src\main\java\com\example\pdf_img_tools_app\features\home\HomeScreen.kt |
| ImageCanvas      | function       | app\src\main\java\com\example\pdf_img_tools_app\core\ui\components\ImageCanvas.kt |
| ImageCanvasState | class          | app\src\main\java\com\example\pdf_img_tools_app\model\ImageCanvasState.kt |
| ImageDimensions  | class          | app\src\main\java\com\example\pdf_img_tools_app\utils\FileUtils.kt |
| ImageFormatSection | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\pdftoimages\PdfToImagesScreen.kt |
| ImagePreviewItem | function       | app\src\main\java\com\example\pdf_img_tools_app\ui\components\ImageBatchComponents.kt |
| ImageResizeService | class          | app\src\main\java\com\example\pdf_img_tools_app\service\ImageResizeService.kt |
| ImageResizerScreen | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\imageresizer\ImageResizerScreen.kt |
| ImageResizerViewModel | class          | app\src\main\java\com\example\pdf_img_tools_app\features\image\imageresizer\ImageResizerViewModel.kt |
| ImageSelectionArea | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\imageresizer\ImageResizerScreen.kt |
| ImageService     | class          | app\src\main\java\com\example\pdf_img_tools_app\service\ImageService.kt |
| ImageThumbnailList | function       | app\src\main\java\com\example\pdf_img_tools_app\ui\components\ImageBatchComponents.kt |
| ImagesToPdfScreen | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\imagestopdf\ImagesToPdfScreen.kt |
| ImagesToPdfUiState | class          | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\imagestopdf\ImagesToPdfUiState.kt |
| ImagesToPdfViewModel | class          | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\imagestopdf\ImagesToPdfViewModel.kt |
| InlineMessage    | function       | app\src\main\java\com\example\pdf_img_tools_app\ui\components\InlineMessage.kt |
| MainActivity     | class          | app\src\main\java\com\example\pdf_img_tools_app\MainActivity.kt |
| MergePdfScreen   | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\mergepdf\MergePdfScreen.kt |
| MergePdfUiState  | class          | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\mergepdf\MergePdfUiState.kt |
| MergePdfViewModel | class          | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\mergepdf\MergePdfViewModel.kt |
| MergeResult      | class          | app\src\main\java\com\example\pdf_img_tools_app\service\PdfService.kt |
| MessageDialogHandler | function       | app\src\main\java\com\example\pdf_img_tools_app\ui\components\MessageDialog.kt |
| MessageDisplayManager | class          | app\src\main\java\com\example\pdf_img_tools_app\utils\MessageDisplayManager.kt |
| MessageEvent     | class          | app\src\main\java\com\example\pdf_img_tools_app\utils\UiMessageBus.kt |
| MessageHandlingScope | function       | app\src\main\java\com\example\pdf_img_tools_app\ui\components\UiMessageDisplay.kt |
| OutputDetailsSection | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\compressimages\CompressImagesScreen.kt |
| OutputDetailsSection | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\convertimages\ConvertImagesScreen.kt |
| OutputDetailsSection | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\imagestopdf\ImagesToPdfScreen.kt |
| OutputDetailsSection | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\splitpdf\SplitPdfScreen.kt |
| OutputFileDetails | function       | app\src\main\java\com\example\pdf_img_tools_app\ui\components\OutputFileDetails.kt |
| OutputFileDetailsSection | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\mergepdf\MergePdfScreen.kt |
| OutputImagesBottomSheet | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\pdftoimages\PdfToImagesScreen.kt |
| OutputOptionsCard | function       | app\src\main\java\com\example\pdf_img_tools_app\ui\components\ImageBatchComponents.kt |
| OutputOptionsSection | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\resizeimages\ResizeImagesScreen.kt |
| OutputSummary    | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\pdftoimages\PdfToImagesScreen.kt |
| PageRangeSection | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\splitpdf\SplitPdfScreen.kt |
| PdfService       | class          | app\src\main\java\com\example\pdf_img_tools_app\service\PdfService.kt |
| PdfSettingsSection | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\imagestopdf\ImagesToPdfScreen.kt |
| PdfToImagesScreen | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\pdftoimages\PdfToImagesScreen.kt |
| PdfToImagesUiState | class          | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\pdftoimages\PdfToImagesUiState.kt |
| PdfToImagesViewModel | class          | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\pdftoimages\PdfToImagesViewModel.kt |
| Pdf_img_tools_appTheme | function       | app\src\main\java\com\example\pdf_img_tools_app\core\ui\theme\Theme.kt |
| PermissionRationaleCard | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\imageresizer\ImageResizerScreen.kt |
| PresetOption     | function       | app\src\main\java\com\example\pdf_img_tools_app\ui\components\ImageBatchComponents.kt |
| ProcessButtonSection | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\resizeimages\ResizeImagesScreen.kt |
| ProcessedImagesSection | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\resizeimages\ResizeImagesScreen.kt |
| ProcessingIndicator | function       | app\src\main\java\com\example\pdf_img_tools_app\core\ui\components\ProcessingIndicator.kt |
| ProcessingOverlay | function       | app\src\main\java\com\example\pdf_img_tools_app\core\ui\components\ProcessingIndicator.kt |
| ProgressToolButton | function       | app\src\main\java\com\example\pdf_img_tools_app\ui\components\ProgressToolButton.kt |
| QualitySlider    | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\convertimages\ConvertImagesScreen.kt |
| ResizeImagesScreen | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\resizeimages\ResizeImagesScreen.kt |
| ResizeImagesUiState | class          | app\src\main\java\com\example\pdf_img_tools_app\features\image\resizeimages\ResizeImagesUiState.kt |
| ResizeModeCard   | function       | app\src\main\java\com\example\pdf_img_tools_app\ui\components\ImageBatchComponents.kt |
| ResizeOptionsArea | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\imageresizer\ImageResizerScreen.kt |
| ResizeOptionsSection | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\resizeimages\ResizeImagesScreen.kt |
| ResizedImage     | class          | app\src\main\java\com\example\pdf_img_tools_app\model\ResizedImage.kt |
| ResizedImage     | class          | app\src\main\java\com\example\pdf_img_tools_app\service\ImageResizeService.kt |
| ReusableSaveLocationSelector | function       | app\src\main\java\com\example\pdf_img_tools_app\ui\components\ReusableSaveLocationSelector.kt |
| ReusableSaveLocationSelectorPreview | function       | app\src\main\java\com\example\pdf_img_tools_app\ui\components\ReusableSaveLocationSelector.kt |
| SaveAsArchiveDialog | function       | app\src\main\java\com\example\pdf_img_tools_app\ui\components\SaveAsArchiveDialog.kt |
| SaveLocationDialog | function       | app\src\main\java\com\example\pdf_img_tools_app\ui\components\ReusableSaveLocationSelector.kt |
| SaveLocationDialogPreview | function       | app\src\main\java\com\example\pdf_img_tools_app\ui\components\ReusableSaveLocationSelector.kt |
| SaveLocationSection | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\compressimages\CompressImagesScreen.kt |
| SaveLocationSection | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\convertimages\ConvertImagesScreen.kt |
| SaveLocationSection | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\resizeimages\ResizeImagesScreen.kt |
| SaveLocationSection | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\imagestopdf\ImagesToPdfScreen.kt |
| SaveLocationSection | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\pdftoimages\PdfToImagesScreen.kt |
| SaveLocationSection | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\splitpdf\SplitPdfScreen.kt |
| SaveLocationUtils | class          | app\src\main\java\com\example\pdf_img_tools_app\utils\SaveLocationUtils.kt |
| SectionHeader    | function       | app\src\main\java\com\example\pdf_img_tools_app\features\home\HomeScreen.kt |
| SelectedFilesBottomSheet | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\mergepdf\MergePdfScreen.kt |
| SelectedFilesSection | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\mergepdf\MergePdfScreen.kt |
| SelectedImagesBottomSheet | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\compressimages\CompressImagesScreen.kt |
| SelectedImagesBottomSheet | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\imagestopdf\ImagesToPdfScreen.kt |
| SettingOption    | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\imagestopdf\ImagesToPdfScreen.kt |
| Show             | class          | app\src\main\java\com\example\pdf_img_tools_app\utils\UiMessageBus.kt |
| ShowError        | class          | app\src\main\java\com\example\pdf_img_tools_app\features\image\imageresizer\ImageResizerViewModel.kt |
| ShowSuccess      | class          | app\src\main\java\com\example\pdf_img_tools_app\features\image\imageresizer\ImageResizerViewModel.kt |
| SingleFilePicker | function       | app\src\main\java\com\example\pdf_img_tools_app\ui\components\SingleFilePicker.kt |
| SmartMessageDisplay | function       | app\src\main\java\com\example\pdf_img_tools_app\ui\components\SmartMessageDisplay.kt |
| SplitButton      | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\splitpdf\SplitPdfScreen.kt |
| SplitPdfScreen   | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\splitpdf\SplitPdfScreen.kt |
| SplitPdfUiState  | class          | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\splitpdf\SplitPdfUiState.kt |
| SplitPdfViewModel | class          | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\splitpdf\SplitPdfViewModel.kt |
| Theme.Pdf_img_tools_app | resource:style | app\src\main\res\values\themes.xml |
| ThemeOption      | function       | app\src\main\java\com\example\pdf_img_tools_app\core\ui\components\ThemeSelector.kt |
| ThemeSelector    | function       | app\src\main\java\com\example\pdf_img_tools_app\core\ui\components\ThemeSelector.kt |
| ThemeSelectorPreview | function       | app\src\main\java\com\example\pdf_img_tools_app\core\ui\components\ThemeSelector.kt |
| ToolCard         | function       | app\src\main\java\com\example\pdf_img_tools_app\ui\components\ToolCard.kt |
| ToolItem         | class          | app\src\main\java\com\example\pdf_img_tools_app\model\ToolItem.kt |
| ToolProgressIndicator | function       | app\src\main\java\com\example\pdf_img_tools_app\core\ui\components\ToolProgressIndicator.kt |
| ToolRepository   | class          | app\src\main\java\com\example\pdf_img_tools_app\data\repository\ToolRepository.kt |
| UiEvent          | class          | app\src\main\java\com\example\pdf_img_tools_app\features\image\imageresizer\ImageResizerViewModel.kt |
| UiMessageBus     | class          | app\src\main\java\com\example\pdf_img_tools_app\utils\UiMessageBus.kt |
| UiMessageData    | class          | app\src\main\java\com\example\pdf_img_tools_app\model\UiMessageData.kt |
| UiMessageDisplay | function       | app\src\main\java\com\example\pdf_img_tools_app\ui\components\UiMessageDisplay.kt |
| addFile          | function       | app\src\main\java\com\example\pdf_img_tools_app\core\FileArchiverViewModel.kt |
| addImageToMediaStore | function       | app\src\main\java\com\example\pdf_img_tools_app\service\ImageResizeService.kt |
| addImages        | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\compressimages\CompressImagesViewModel.kt |
| addImages        | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\resizeimages\BatchImageResizeViewModel.kt |
| addImages        | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\imagestopdf\ImagesToPdfViewModel.kt |
| addPdfFiles      | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\mergepdf\MergePdfViewModel.kt |
| addition_isCorrect | function       | app\src\test\java\com\example\pdf_img_tools_app\ExampleUnitTest.kt |
| app_name         | resource:string | app\src\main\res\values\strings.xml |
| applyCanvasTransformations | function       | app\src\main\java\com\example\pdf_img_tools_app\service\ImageResizeService.kt |
| black            | resource:color | app\src\main\res\values\colors.xml |
| calculateDimensions | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\resizeimages\BatchImageResizeViewModel.kt |
| calculateInSampleSize | function       | app\src\main\java\com\example\pdf_img_tools_app\service\ImageResizeService.kt |
| calculateTargetSize | function       | app\src\main\java\com\example\pdf_img_tools_app\service\ImageService.kt |
| cancelCompression | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\compressimages\CompressImagesViewModel.kt |
| cancelCompression | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\compresspdf\CompressPdfViewModel.kt |
| cancelMerge      | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\mergepdf\MergePdfViewModel.kt |
| cancelProcessing | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\convertimages\ConvertImagesViewModel.kt |
| cancelProcessing | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\imagestopdf\ImagesToPdfViewModel.kt |
| cancelProcessing | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\pdftoimages\PdfToImagesViewModel.kt |
| changeSaveMode   | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\compresspdf\CompressPdfViewModel.kt |
| changeSaveMode   | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\mergepdf\MergePdfViewModel.kt |
| class            | class          | app\src\main\java\com\example\pdf_img_tools_app\core\ui\theme\Theme.kt |
| class            | class          | app\src\main\java\com\example\pdf_img_tools_app\features\image\resizeimages\BatchImageResizeViewModel.kt |
| class            | class          | app\src\main\java\com\example\pdf_img_tools_app\model\ImageResizeTemplate.kt |
| class            | class          | app\src\main\java\com\example\pdf_img_tools_app\model\ResizeMode.kt |
| class            | class          | app\src\main\java\com\example\pdf_img_tools_app\model\SaveLocationType.kt |
| class            | class          | app\src\main\java\com\example\pdf_img_tools_app\model\SaveMode.kt |
| class            | class          | app\src\main\java\com\example\pdf_img_tools_app\model\ToolItem.kt |
| class            | class          | app\src\main\java\com\example\pdf_img_tools_app\model\UiMessageData.kt |
| class            | class          | app\src\main\java\com\example\pdf_img_tools_app\service\ImageService.kt |
| class            | class          | app\src\main\java\com\example\pdf_img_tools_app\service\ImageService.kt |
| class            | class          | app\src\main\java\com\example\pdf_img_tools_app\service\PdfService.kt |
| class            | class          | app\src\main\java\com\example\pdf_img_tools_app\utils\DisplayMethod.kt |
| class            | class          | app\src\main\java\com\example\pdf_img_tools_app\utils\NotificationUtils.kt |
| clearAll         | function       | app\src\main\java\com\example\pdf_img_tools_app\core\CommonToolState.kt |
| clearAllImages   | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\compressimages\CompressImagesViewModel.kt |
| clearAllImages   | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\imagestopdf\ImagesToPdfViewModel.kt |
| clearAllImages   | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\pdftoimages\PdfToImagesViewModel.kt |
| clearAllMessages | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\UiMessageBus.kt |
| clearAllPdfs     | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\mergepdf\MergePdfViewModel.kt |
| clearFiles       | function       | app\src\main\java\com\example\pdf_img_tools_app\core\FileArchiverViewModel.kt |
| clearMessages    | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\UiMessageBus.kt |
| clearOutputDetails | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\compressimages\CompressImagesViewModel.kt |
| clearOutputDetails | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\convertimages\ConvertImagesViewModel.kt |
| clearOutputDetails | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\compresspdf\CompressPdfViewModel.kt |
| clearOutputDetails | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\imagestopdf\ImagesToPdfViewModel.kt |
| clearOutputDetails | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\mergepdf\MergePdfViewModel.kt |
| clearPdfFile     | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\pdftoimages\PdfToImagesViewModel.kt |
| clearPdfFile     | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\splitpdf\SplitPdfViewModel.kt |
| clearProcessedImages | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\resizeimages\BatchImageResizeViewModel.kt |
| clearScope       | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\UiMessageBus.kt |
| clearSelectedFile | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\compresspdf\CompressPdfViewModel.kt |
| clearSelectedImage | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\convertimages\ConvertImagesViewModel.kt |
| clearSelectedImage | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\imageresizer\ImageResizerViewModel.kt |
| clearSelectedImages | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\resizeimages\BatchImageResizeViewModel.kt |
| completeArchiving | function       | app\src\main\java\com\example\pdf_img_tools_app\core\CommonToolState.kt |
| completeProcessing | function       | app\src\main\java\com\example\pdf_img_tools_app\core\CommonToolState.kt |
| compressImages   | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\compressimages\CompressImagesViewModel.kt |
| compressImages   | function       | app\src\main\java\com\example\pdf_img_tools_app\service\ImageService.kt |
| compressPdf      | function       | app\src\main\java\com\example\pdf_img_tools_app\service\PdfService.kt |
| compressSingleImageInternal | function       | app\src\main\java\com\example\pdf_img_tools_app\service\ImageService.kt |
| convertImage     | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\convertimages\ConvertImagesViewModel.kt |
| convertImageFormat | function       | app\src\main\java\com\example\pdf_img_tools_app\service\ImageService.kt |
| convertImagesToPdf | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\imagestopdf\ImagesToPdfViewModel.kt |
| convertPdfToImages | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\pdftoimages\PdfToImagesViewModel.kt |
| copyFile         | function       | app\src\main\java\com\example\pdf_img_tools_app\service\ImageResizeService.kt |
| copyStream       | function       | app\src\main\java\com\example\pdf_img_tools_app\service\ImageService.kt |
| createAndSaveZipFile | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\ArchiveUtils.kt |
| createArchive    | function       | app\src\main\java\com\example\pdf_img_tools_app\core\FileArchiverViewModel.kt |
| createImagePreview | function       | app\src\main\java\com\example\pdf_img_tools_app\service\ImageResizeService.kt |
| createOutputFile | function       | app\src\main\java\com\example\pdf_img_tools_app\service\ImageResizeService.kt |
| createOutputFile | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\FileUtils.kt |
| createOutputFile | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\FileUtils.kt |
| createOutputFileInAppDir | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\FileUtils.kt |
| createTempFile   | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\FileUtils.kt |
| createZipArchive | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\FileUtils.kt |
| createZipFile    | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\compressimages\CompressImagesViewModel.kt |
| createZipFile    | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\ArchiveUtils.kt |
| defining         | class          | app\src\main\java\com\example\pdf_img_tools_app\model\ResizeMode.kt |
| detectPdfHasImages | function       | app\src\main\java\com\example\pdf_img_tools_app\service\PdfService.kt |
| determineDisplayMethod | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\MessageDisplayManager.kt |
| dismissLargeFileWarning | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\compresspdf\CompressPdfViewModel.kt |
| dismissMessage   | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\UiMessageBus.kt |
| error            | function       | app\src\main\java\com\example\pdf_img_tools_app\model\UiMessageData.kt |
| for              | class          | app\src\main\java\com\example\pdf_img_tools_app\core\CommonToolState.kt |
| for              | class          | app\src\main\java\com\example\pdf_img_tools_app\data\repository\ToolRepository.kt |
| for              | class          | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\splitpdf\SplitPdfViewModel.kt |
| for              | class          | app\src\main\java\com\example\pdf_img_tools_app\service\PdfService.kt |
| for              | class          | app\src\main\java\com\example\pdf_img_tools_app\utils\ArchiveUtils.kt |
| formatFileSize   | function       | app\src\main\java\com\example\pdf_img_tools_app\core\ui\components\CommonUIComponents.kt |
| formatFileSize   | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\FileUtils.kt |
| formatMessageForDisplay | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\MessageDisplayManager.kt |
| formatSuccessMessage | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\imageresizer\ImageResizerViewModel.kt |
| formatTimeRemaining | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\compresspdf\CompressPdfViewModel.kt |
| fromDisplayName  | function       | app\src\main\java\com\example\pdf_img_tools_app\model\ImageResizeTemplate.kt |
| fromDisplayName  | function       | app\src\main\java\com\example\pdf_img_tools_app\service\ImageService.kt |
| fromMimeType     | function       | app\src\main\java\com\example\pdf_img_tools_app\service\ImageService.kt |
| getAllTools      | function       | app\src\main\java\com\example\pdf_img_tools_app\data\repository\ToolRepository.kt |
| getBitmapFromUri | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\FileUtils.kt |
| getColorScheme   | function       | app\src\main\java\com\example\pdf_img_tools_app\core\ui\theme\Theme.kt |
| getDefaultDisplayMethod | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\MessageDisplayManager.kt |
| getDirectoryName | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\FileUtils.kt |
| getFileDetails   | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\FileUtils.kt |
| getFileName      | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\FileUtils.kt |
| getFileNameFromUri | function       | app\src\main\java\com\example\pdf_img_tools_app\service\ImageResizeService.kt |
| getFilePath      | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\FileUtils.kt |
| getFileSize      | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\FileUtils.kt |
| getFileSizeFromUri | function       | app\src\main\java\com\example\pdf_img_tools_app\service\ImageResizeService.kt |
| getFormatNames   | function       | app\src\main\java\com\example\pdf_img_tools_app\service\ImageService.kt |
| getIconForMimeType | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\FileUtils.kt |
| getImageDetails  | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\resizeimages\BatchImageResizeViewModel.kt |
| getImageDimensions | function       | app\src\main\java\com\example\pdf_img_tools_app\service\ImageResizeService.kt |
| getImageDimensions | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\FileUtils.kt |
| getImageTools    | function       | app\src\main\java\com\example\pdf_img_tools_app\data\repository\ToolRepository.kt |
| getMimeType      | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\FileUtils.kt |
| getOutputFilename | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\resizeimages\BatchImageResizeViewModel.kt |
| getPageCount     | function       | app\src\main\java\com\example\pdf_img_tools_app\service\PdfService.kt |
| getPageCount     | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\FileUtils.kt |
| getPathFromUri   | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\FileUtils.kt |
| getPdfTools      | function       | app\src\main\java\com\example\pdf_img_tools_app\data\repository\ToolRepository.kt |
| getProcessedFormatsString | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\resizeimages\BatchImageResizeViewModel.kt |
| getResizeDimensionsString | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\resizeimages\BatchImageResizeViewModel.kt |
| getSaveLocationUri | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\SaveLocationUtils.kt |
| getSelectedFilesCount | function       | app\src\main\java\com\example\pdf_img_tools_app\core\FileArchiverViewModel.kt |
| getSelectedFormatsString | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\resizeimages\BatchImageResizeViewModel.kt |
| getTemplateNames | function       | app\src\main\java\com\example\pdf_img_tools_app\model\ImageResizeTemplate.kt |
| getThumbnail     | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\FileUtils.kt |
| getTotalOriginalSize | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\resizeimages\BatchImageResizeViewModel.kt |
| getTotalSelectedSize | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\resizeimages\BatchImageResizeViewModel.kt |
| has              | class          | app\src\main\java\com\example\pdf_img_tools_app\utils\FileUtils.kt |
| hasTransparency  | function       | app\src\main\java\com\example\pdf_img_tools_app\service\PdfService.kt |
| imagesToPdf      | function       | app\src\main\java\com\example\pdf_img_tools_app\service\PdfService.kt |
| info             | function       | app\src\main\java\com\example\pdf_img_tools_app\model\UiMessageData.kt |
| isBlackBoxProblem | function       | app\src\main\java\com\example\pdf_img_tools_app\service\PdfService.kt |
| isSaveLocationValid | function       | app\src\main\java\com\example\pdf_img_tools_app\core\CommonToolState.kt |
| isSupportedFormat | function       | app\src\main\java\com\example\pdf_img_tools_app\service\ImageResizeService.kt |
| isWebpTypeSupported | function       | app\src\main\java\com\example\pdf_img_tools_app\service\ImageService.kt |
| mergePdfFiles    | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\mergepdf\MergePdfViewModel.kt |
| mergePdfFiles    | function       | app\src\main\java\com\example\pdf_img_tools_app\service\PdfService.kt |
| onCreate         | function       | app\src\main\java\com\example\pdf_img_tools_app\MainActivity.kt |
| onEndPageChanged | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\splitpdf\SplitPdfViewModel.kt |
| onFilePicked     | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\compresspdf\CompressPdfViewModel.kt |
| onFilePicked     | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\splitpdf\SplitPdfViewModel.kt |
| onStartPageChanged | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\splitpdf\SplitPdfViewModel.kt |
| optimizeMetadataOnly | function       | app\src\main\java\com\example\pdf_img_tools_app\service\PdfService.kt |
| optimizePageResources | function       | app\src\main\java\com\example\pdf_img_tools_app\service\PdfService.kt |
| pdfToImages      | function       | app\src\main\java\com\example\pdf_img_tools_app\service\PdfService.kt |
| purple_200       | resource:color | app\src\main\res\values\colors.xml |
| purple_500       | resource:color | app\src\main\res\values\colors.xml |
| purple_700       | resource:color | app\src\main\res\values\colors.xml |
| rasterizeAndCompressPdf | function       | app\src\main\java\com\example\pdf_img_tools_app\service\PdfService.kt |
| rememberCommonToolState | function       | app\src\main\java\com\example\pdf_img_tools_app\core\CommonToolState.kt |
| removeFile       | function       | app\src\main\java\com\example\pdf_img_tools_app\core\FileArchiverViewModel.kt |
| removeImage      | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\compressimages\CompressImagesViewModel.kt |
| removeImage      | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\resizeimages\BatchImageResizeViewModel.kt |
| removeImage      | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\imagestopdf\ImagesToPdfViewModel.kt |
| removeImage      | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\pdftoimages\PdfToImagesViewModel.kt |
| removePdf        | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\mergepdf\MergePdfViewModel.kt |
| removeProcessedImage | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\resizeimages\BatchImageResizeViewModel.kt |
| removeSelectedPdfs | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\mergepdf\MergePdfViewModel.kt |
| representing     | class          | app\src\main\java\com\example\pdf_img_tools_app\features\image\compressimages\CompressImagesUiState.kt |
| representing     | class          | app\src\main\java\com\example\pdf_img_tools_app\features\image\convertimages\ConvertImagesUiState.kt |
| representing     | class          | app\src\main\java\com\example\pdf_img_tools_app\features\image\resizeimages\ResizeImagesUiState.kt |
| representing     | class          | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\compresspdf\CompressPdfUiState.kt |
| representing     | class          | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\imagestopdf\ImagesToPdfUiState.kt |
| representing     | class          | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\mergepdf\MergePdfUiState.kt |
| representing     | class          | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\pdftoimages\PdfToImagesUiState.kt |
| representing     | class          | app\src\main\java\com\example\pdf_img_tools_app\model\ResizedImage.kt |
| representing     | class          | app\src\main\java\com\example\pdf_img_tools_app\model\UiMessageData.kt |
| representing     | class          | app\src\main\java\com\example\pdf_img_tools_app\utils\UiMessageBus.kt |
| resetOutput      | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\splitpdf\SplitPdfViewModel.kt |
| resetResize      | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\imageresizer\ImageResizerViewModel.kt |
| resizeBitmapHelper | function       | app\src\main\java\com\example\pdf_img_tools_app\core\ui\components\ImageCanvas.kt |
| resizeImage      | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\imageresizer\ImageResizerViewModel.kt |
| resizeImage      | function       | app\src\main\java\com\example\pdf_img_tools_app\service\ImageResizeService.kt |
| resizeImage      | function       | app\src\main\java\com\example\pdf_img_tools_app\service\ImageService.kt |
| resizeImages     | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\resizeimages\BatchImageResizeViewModel.kt |
| saveFileToDirectory | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\FileUtils.kt |
| saveFileToDownloads | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\FileUtils.kt |
| saveMultipleToLocation | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\SaveLocationUtils.kt |
| saveState        | function       | app\src\main\java\com\example\pdf_img_tools_app\core\ui\components\ImageCanvas.kt |
| saveToExternalStorage | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\FileUtils.kt |
| saveToLocation   | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\SaveLocationUtils.kt |
| scaleBitmap      | function       | app\src\main\java\com\example\pdf_img_tools_app\service\ImageResizeService.kt |
| selectImage      | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\convertimages\ConvertImagesViewModel.kt |
| setAppTheme      | function       | app\src\main\java\com\example\pdf_img_tools_app\core\ui\theme\Theme.kt |
| setErrorMessage  | function       | app\src\main\java\com\example\pdf_img_tools_app\core\CommonToolState.kt |
| setFormat        | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\imageresizer\ImageResizerViewModel.kt |
| setPdfFile       | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\pdftoimages\PdfToImagesViewModel.kt |
| setResizedImage  | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\imageresizer\ImageResizerViewModel.kt |
| setSelectedImage | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\imageresizer\ImageResizerViewModel.kt |
| setShowProcessedImagesSheet | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\resizeimages\BatchImageResizeViewModel.kt |
| setShowSelectedImagesSheet | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\resizeimages\BatchImageResizeViewModel.kt |
| setTemplate      | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\imageresizer\ImageResizerViewModel.kt |
| shareFile        | function       | app\src\main\java\com\example\pdf_img_tools_app\ui\components\OutputFileDetails.kt |
| showDialog       | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\UiMessageBus.kt |
| showError        | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\UiMessageBus.kt |
| showInfo         | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\UiMessageBus.kt |
| showMessage      | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\UiMessageBus.kt |
| showMessage      | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\UiMessageBus.kt |
| showSnackbar     | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\UiMessageBus.kt |
| showSuccess      | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\UiMessageBus.kt |
| showToast        | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\MessageDisplayManager.kt |
| showToast        | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\NotificationUtils.kt |
| showToast        | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\UiMessageBus.kt |
| showWarning      | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\UiMessageBus.kt |
| smartCompressPdf | function       | app\src\main\java\com\example\pdf_img_tools_app\service\PdfService.kt |
| splitPdf         | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\splitpdf\SplitPdfViewModel.kt |
| splitPdf         | function       | app\src\main\java\com\example\pdf_img_tools_app\service\PdfService.kt |
| startArchiving   | function       | app\src\main\java\com\example\pdf_img_tools_app\core\CommonToolState.kt |
| startCompression | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\compresspdf\CompressPdfViewModel.kt |
| startProcessing  | function       | app\src\main\java\com\example\pdf_img_tools_app\core\CommonToolState.kt |
| success          | function       | app\src\main\java\com\example\pdf_img_tools_app\model\UiMessageData.kt |
| teal_200         | resource:color | app\src\main\res\values\colors.xml |
| teal_700         | resource:color | app\src\main\res\values\colors.xml |
| to               | class          | app\src\main\java\com\example\pdf_img_tools_app\core\ui\theme\Theme.kt |
| to               | class          | app\src\main\java\com\example\pdf_img_tools_app\model\ImageCanvasState.kt |
| toggleAllImagesBottomSheet | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\compressimages\CompressImagesViewModel.kt |
| toggleBottomSheet | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\pdftoimages\PdfToImagesViewModel.kt |
| toggleConfirmMergeDialog | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\mergepdf\MergePdfViewModel.kt |
| toggleFormatMenu | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\convertimages\ConvertImagesViewModel.kt |
| toggleImageSelection | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\pdftoimages\PdfToImagesViewModel.kt |
| toggleImagesBottomSheet | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\imagestopdf\ImagesToPdfViewModel.kt |
| toggleItemSelection | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\mergepdf\MergePdfViewModel.kt |
| toggleMaintainAspectRatio | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\imageresizer\ImageResizerViewModel.kt |
| toggleOutputFileSheet | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\mergepdf\MergePdfViewModel.kt |
| toggleSaveLocationSelector | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\splitpdf\SplitPdfViewModel.kt |
| toggleSelectedFilesSheet | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\mergepdf\MergePdfViewModel.kt |
| toggleSelectedImagesBottomSheet | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\compressimages\CompressImagesViewModel.kt |
| updateCompressionFormat | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\compressimages\CompressImagesViewModel.kt |
| updateCompressionQuality | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\compressimages\CompressImagesViewModel.kt |
| updateDpi        | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\pdftoimages\PdfToImagesViewModel.kt |
| updateHeight     | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\imageresizer\ImageResizerViewModel.kt |
| updateImageAlignment | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\imagestopdf\ImagesToPdfViewModel.kt |
| updateImageDetails | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\compressimages\CompressImagesViewModel.kt |
| updateImageDetails | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\imagestopdf\ImagesToPdfViewModel.kt |
| updateInputFile  | function       | app\src\main\java\com\example\pdf_img_tools_app\core\CommonToolState.kt |
| updateMessage    | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\UiMessageBus.kt |
| updateOutputFormat | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\pdftoimages\PdfToImagesViewModel.kt |
| updatePaperSize  | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\imagestopdf\ImagesToPdfViewModel.kt |
| updateProgress   | function       | app\src\main\java\com\example\pdf_img_tools_app\core\CommonToolState.kt |
| updateQuality    | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\convertimages\ConvertImagesViewModel.kt |
| updateQuality    | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\compresspdf\CompressPdfViewModel.kt |
| updateResizeSettings | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\resizeimages\BatchImageResizeViewModel.kt |
| updateSaveLocation | function       | app\src\main\java\com\example\pdf_img_tools_app\core\CommonToolState.kt |
| updateSaveLocation | function       | app\src\main\java\com\example\pdf_img_tools_app\core\FileArchiverViewModel.kt |
| updateSaveLocation | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\splitpdf\SplitPdfViewModel.kt |
| updateSaveMode   | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\compressimages\CompressImagesViewModel.kt |
| updateSaveMode   | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\convertimages\ConvertImagesViewModel.kt |
| updateSaveMode   | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\imagestopdf\ImagesToPdfViewModel.kt |
| updateSaveMode   | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\pdftoimages\PdfToImagesViewModel.kt |
| updateSaveMode   | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\splitpdf\SplitPdfViewModel.kt |
| updateSavePath   | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\compressimages\CompressImagesViewModel.kt |
| updateSavePath   | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\convertimages\ConvertImagesViewModel.kt |
| updateSavePath   | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\compresspdf\CompressPdfViewModel.kt |
| updateSavePath   | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\imagestopdf\ImagesToPdfViewModel.kt |
| updateSavePath   | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\mergepdf\MergePdfViewModel.kt |
| updateSavePath   | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\pdftoimages\PdfToImagesViewModel.kt |
| updateSaveSettings | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\resizeimages\BatchImageResizeViewModel.kt |
| updateSelectedFormat | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\convertimages\ConvertImagesViewModel.kt |
| updateWidth      | function       | app\src\main\java\com\example\pdf_img_tools_app\features\image\imageresizer\ImageResizerViewModel.kt |
| useAppContext    | function       | app\src\androidTest\java\com\example\pdf_img_tools_app\ExampleInstrumentedTest.kt |
| validatePageInputs | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\splitpdf\SplitPdfViewModel.kt |
| validateSaveLocation | function       | app\src\main\java\com\example\pdf_img_tools_app\utils\SaveLocationUtils.kt |
| viewFile         | function       | app\src\main\java\com\example\pdf_img_tools_app\core\ui\components\CommonUIComponents.kt |
| viewFile         | function       | app\src\main\java\com\example\pdf_img_tools_app\ui\components\OutputFileDetails.kt |
| viewImage        | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\imagestopdf\ImagesToPdfScreen.kt |
| viewImage        | function       | app\src\main\java\com\example\pdf_img_tools_app\features\pdf\pdftoimages\PdfToImagesScreen.kt |
| viewImage        | function       | app\src\main\java\com\example\pdf_img_tools_app\ui\components\OutputFileDetails.kt |
| viewPdf          | function       | app\src\main\java\com\example\pdf_img_tools_app\ui\components\OutputFileDetails.kt |
| warning          | function       | app\src\main\java\com\example\pdf_img_tools_app\model\UiMessageData.kt |
| white            | resource:color | app\src\main\res\values\colors.xml |
| with             | class          | app\src\main\java\com\example\pdf_img_tools_app\service\ImageService.kt |
| with             | class          | app\src\main\java\com\example\pdf_img_tools_app\service\PdfService.kt |

## 📄 Included Files (Full Content)

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

### `.windsurf\rules\rules.md`

```md
---
trigger: always_on
---

📌 Important: My Android project uses a feature-based architecture. You must follow this structure, avoid unsafe changes, use reusable components, and write organized, maintainable code.

---

🗂️ PROJECT STRUCTURE — MUST BE FOLLOWED

- All tools/screens are grouped under `features/` by type (e.g., pdf, image).
- Each feature folder contains:
  - One screen Composable (e.g., MergePdfScreen.kt)
  - One ViewModel (e.g., MergePdfViewModel.kt)
  - Optional UI state/event class
- Shared UI components (e.g., FilePickerHandler, OutputFileDetails) go in:
  - `core/ui/components/`
- Shared utilities (e.g., UriUtils, FileUtils) go in:
  - `core/utils/` or `service/`
- Navigation is centralized in:
  - `navigation/` or `core/AppNavigation.kt`

✅ Always:
- Follow this structure when creating or modifying anything.
- Colocate ViewModels, UI states, and screens inside each feature folder.
- Keep shared logic in `core/` only if reused across multiple features.
- Maintain this organization at all times unless I explicitly ask to change it.

🚫 Never:
- Create global `viewmodel/` or `screens/` folders.
- Scatter or misplace files outside their correct feature or shared context.
- Modify unrelated features when working on a specific one.

---

♻️ REUSE EXISTING COMPONENTS — NO DUPLICATION

✅ When implementing UI or logic:
- Always check if reusable components already exist in `core/ui/components/` or `core/utils/`.
- Reuse shared Composables (e.g., FilePickerHandler, OutputFileDetails) when applicable.
- If a component is reusable, do not reimplement it — **import and use the existing one**.

🚫 Never:
- Create duplicate versions of existing shared components or utility functions.
- Rewrite logic that already exists elsewhere in a reusable form.

---

🧼 ORGANIZATION & CLEAN CODE — BEST PRACTICES REQUIRED

✅ Code must follow clean, organized structure:
- Group related functions inside their correct files (e.g., business logic in ViewModel, UI in Composables).
- Use proper naming conventions for functions, classes, and states.
- Use sealed classes or data classes for UI state when needed.
- Keep Composables lightweight and readable — split large blocks if necessary.
- Maintain proper file separation (e.g., don’t mix Composables and ViewModel logic).

🚫 Never:
- Write disorganized, overly nested, or hard-to-maintain code.
- Put UI logic inside ViewModel or business logic inside screen files.
- Leave unused code or commented-out blocks.

---

🛠️ SAFE CODE MODIFICATION RULES (Fixes, New Features, Refactors)

✅ What You CAN Do:
- Fix only the specific issue or build error described.
- Add new functionality within the correct feature folder.
- Reorganize files if asked — only update package imports.
- Keep existing UI layout and behavior untouched unless explicitly asked to change it.

🚫 What You MUST NOT Do:
- Modify or break functionality in unrelated files.
- Change or optimize working code outside the scope.
- Alter UI appearance or navigation without permission.
- Introduce new states or flows without clear instruction.

🎯 GOAL:
Make safe, isolated, and correct changes. Preserve all unrelated functionality and UI. Respect the established project structure, reuse existing code, and maintain high coding standards at all times.

If in doubt — ask before assuming.
```

### `app\src\androidTest\java\com\example\pdf_img_tools_app\ExampleInstrumentedTest.kt`

```kt
package com.example.pdf_img_tools_app

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
        assertEquals("com.example.pdf_img_tools_app", appContext.packageName)
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

    <application
        android:allowBackup="true"
        android:dataExtractionRules="@xml/data_extraction_rules"
        android:fullBackupContent="@xml/backup_rules"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/Theme.Pdf_img_tools_app"
        android:requestLegacyExternalStorage="true"
        android:enableOnBackInvokedCallback="true"
        tools:targetApi="31">
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
    </application>

</manifest>```

### `app\src\main\java\com\example\pdf_img_tools_app\MainActivity.kt`

```kt
package com.example.pdf_img_tools_app

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
import com.example.pdf_img_tools_app.core.AppNavigation
import com.example.pdf_img_tools_app.core.ui.theme.Pdf_img_tools_appTheme
import com.tom_roush.pdfbox.android.PDFBoxResourceLoader

// Local composition provider for dark theme state
val LocalDarkTheme = staticCompositionLocalOf { false }

class MainActivity : ComponentActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {

        super.onCreate(savedInstanceState)

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

### `app\src\main\java\com\example\pdf_img_tools_app\config\FeatureFlags.kt`

```kt
// FeatureFlags.kt
package com.example.pdf_img_tools_app.config


object FeatureFlags {
    // PDF Tools
    const val ENABLE_COMPRESS_PDF = true
    const val ENABLE_MERGE_PDFS = true
    const val ENABLE_SPLIT_PDF = true
    const val ENABLE_PDF_TO_IMAGES = true
    const val ENABLE_IMAGES_TO_PDF = true

    // Image Tools
    const val ENABLE_COMPRESS_IMAGES = true
    const val ENABLE_RESIZE_IMAGES = true
    const val ENABLE_CONVERT_IMAGES = true
    const val ENABLE_IMAGE_RESIZER = false  // disabled for v1

    // Future Enhancements
    const val ENABLE_BATCH_PDF_OPERATIONS = false
    const val ENABLE_WATERMARKING = false
}```

### `app\src\main\java\com\example\pdf_img_tools_app\core\AppNavigation.kt`

```kt
package com.example.pdf_img_tools_app.core

import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.navigation.NavHostController
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import com.example.pdf_img_tools_app.features.home.HomeScreen
import com.example.pdf_img_tools_app.features.image.imageresizer.ImageResizerScreen
import com.example.pdf_img_tools_app.features.image.compressimages.CompressImagesScreen
import com.example.pdf_img_tools_app.features.image.convertimages.ConvertImagesScreen
import com.example.pdf_img_tools_app.features.image.resizeimages.ResizeImagesScreen
import com.example.pdf_img_tools_app.features.pdf.compresspdf.CompressPdfScreen
import com.example.pdf_img_tools_app.features.pdf.mergepdf.MergePdfScreen
import com.example.pdf_img_tools_app.features.pdf.splitpdf.SplitPdfScreen
import com.example.pdf_img_tools_app.features.pdf.pdftoimages.PdfToImagesScreen
import com.example.pdf_img_tools_app.features.pdf.imagestopdf.ImagesToPdfScreen

/**
 * Defines the navigation routes for the app
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
}

/**
 * App navigation component
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
        composable(AppDestinations.RESIZE_IMAGES) {
            ResizeImagesScreen(
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

        composable(AppDestinations.IMAGE_RESIZER) {
            ImageResizerScreen(
                navController = navController,
                isDarkTheme = isDarkTheme,
                onThemeToggle = onThemeToggle
            )
        }
    }
}```

### `app\src\main\java\com\example\pdf_img_tools_app\core\CommonToolState.kt`

```kt
package com.example.pdf_img_tools_app.core

import android.content.Context
import android.net.Uri
import androidx.compose.runtime.Composable
import androidx.compose.runtime.MutableState
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import com.example.pdf_img_tools_app.model.SaveLocationType
import com.example.pdf_img_tools_app.utils.FileDetails
import com.example.pdf_img_tools_app.utils.FileUtils

/**
 * Common state class for tool screens
 * Provides a consistent way to manage processing state, error messages,
 * progress reporting, and file selection
 */
class CommonToolState {
    // Processing state
    val isProcessing = mutableStateOf(false)
    val processingProgress = mutableStateOf(-1f)
    
    // Error message
    val errorMessage = mutableStateOf<String?>(null)
    
    // File selection state
    val inputFileUri = mutableStateOf<Uri?>(null)
    val inputFileDetails = mutableStateOf<FileDetails?>(null)
    
    // Output file details
    val outputFileDetails = mutableStateOf<FileDetails?>(null)
    
    // Save location
    val saveLocationType = mutableStateOf(SaveLocationType.DOWNLOADS)
    val customSaveLocationUri = mutableStateOf<Uri?>(null)
    val customSaveLocationName = mutableStateOf("")
    
    // Archive dialog
    val showArchiveDialog = mutableStateOf(false)
    val isArchiving = mutableStateOf(false)
    val archiveProgress = mutableStateOf(-1f)
    
    // Function to update the selected input file
    fun updateInputFile(uri: Uri?, context: Context) {
        inputFileUri.value = uri
        outputFileDetails.value = null
        errorMessage.value = null
        
        if (uri != null) {
            inputFileDetails.value = FileUtils.getFileDetails(context, uri)
        } else {
            inputFileDetails.value = null
        }
    }
    
    // Start processing
    fun startProcessing() {
        isProcessing.value = true
        processingProgress.value = 0f
        errorMessage.value = null
    }
    
    // Update progress
    fun updateProgress(progress: Float) {
        processingProgress.value = progress.coerceIn(0f, 1f)
    }
    
    // Complete processing
    fun completeProcessing(success: Boolean = true, message: String? = null) {
        if (!success && message != null) {
            errorMessage.value = message
        }
        isProcessing.value = false
        processingProgress.value = -1f
    }
    
    // Set error message
    fun setErrorMessage(message: String?) {
        errorMessage.value = message
    }
    
    // Clear all state
    fun clearAll() {
        isProcessing.value = false
        processingProgress.value = -1f
        errorMessage.value = null
        inputFileUri.value = null
        inputFileDetails.value = null
        outputFileDetails.value = null
    }
    
    // Start archiving
    fun startArchiving() {
        isArchiving.value = true
        archiveProgress.value = 0f
        errorMessage.value = null
    }
    
    // Complete archiving
    fun completeArchiving(success: Boolean = true, message: String? = null) {
        if (!success && message != null) {
            errorMessage.value = message
        }
        isArchiving.value = false
        archiveProgress.value = -1f
    }
    
    // Check if save location is valid
    fun isSaveLocationValid(): Boolean {
        return when (saveLocationType.value) {
            SaveLocationType.DOWNLOADS -> true
            SaveLocationType.CUSTOM -> customSaveLocationUri.value != null
            else -> false
        }
    }
    
    // Update save location
    fun updateSaveLocation(type: SaveLocationType, uri: Uri? = null, name: String? = null) {
        saveLocationType.value = type
        if (uri != null) {
            customSaveLocationUri.value = uri
        }
        if (name != null) {
            customSaveLocationName.value = name
        }
    }
}

/**
 * Composable function to remember a CommonToolState
 */
@Composable
fun rememberCommonToolState(): CommonToolState {
    return remember { CommonToolState() }
} ```

### `app\src\main\java\com\example\pdf_img_tools_app\core\FileArchiverViewModel.kt`

```kt
package com.example.pdf_img_tools_app.core

import android.content.Context
import android.net.Uri
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.pdf_img_tools_app.model.SaveLocationType
import com.example.pdf_img_tools_app.utils.ArchiveUtils
import com.example.pdf_img_tools_app.utils.FileUtils
import kotlinx.coroutines.launch

/**
 * ViewModel for file archiving functionality
 */
class FileArchiverViewModel : ViewModel() {
    
    // Use CommonToolState for state management
    val state = CommonToolState()
    
    // Selected files to archive
    private val selectedFiles = mutableListOf<Pair<Uri, String>>()
    
    // Add a file to be archived
    fun addFile(uri: Uri, filename: String) {
        selectedFiles.add(Pair(uri, filename))
    }
    
    // Remove a file from the archive list
    fun removeFile(uri: Uri) {
        selectedFiles.removeIf { it.first == uri }
    }
    
    // Clear all selected files
    fun clearFiles() {
        selectedFiles.clear()
    }
    
    // Get selected files count
    fun getSelectedFilesCount(): Int = selectedFiles.size
    
    // Create archive
    fun createArchive(context: Context, archiveName: String) {
        if (selectedFiles.isEmpty()) {
            state.setErrorMessage("No files selected to archive")
            return
        }
        
        if (!state.isSaveLocationValid()) {
            state.setErrorMessage("Please select a valid save location")
            return
        }
        
        viewModelScope.launch {
            state.startArchiving()
            
            val archiveUri = ArchiveUtils.createAndSaveZipFile(
                context = context,
                files = selectedFiles,
                fileName = archiveName,
                saveLocationType = state.saveLocationType.value,
                customSaveLocationUri = state.customSaveLocationUri.value,
                progressCallback = { progress ->
                    state.archiveProgress.value = progress
                }
            )
            
            if (archiveUri != null) {
                // Get file details for the created archive
                val fileDetails = FileUtils.getFileDetails(context, archiveUri)
                state.outputFileDetails.value = fileDetails
                state.completeArchiving(true)
            } else {
                state.completeArchiving(false, "Failed to create archive")
            }
        }
    }
    
    // Update save location settings
    fun updateSaveLocation(
        type: SaveLocationType,
        customUri: Uri? = null,
        customName: String? = null
    ) {
        state.updateSaveLocation(type, customUri, customName)
    }
} ```

### `app\src\main\java\com\example\pdf_img_tools_app\core\ui\components\CheckerboardBackground.kt`

```kt
package com.example.pdf_img_tools_app.ui.components

import androidx.compose.foundation.Canvas
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp

/**
 * Creates a checkerboard pattern background commonly used for transparent images
 * This helps users to visualize transparent areas of images clearly
 */

@Composable
fun CheckerboardBackground(
    modifier: Modifier = Modifier,
    tileSize: Dp = 12.dp,  // Size of each tile in the pattern
    darkColor: Color = Color(0xFFCCCCCC),  // Dark tile color
    lightColor: Color = Color(0xFFEEEEEE)  // Light tile color
) {
    Box(modifier = modifier) {
        Canvas(modifier = Modifier.fillMaxSize()) {
            val width = size.width
            val height = size.height
            
            // Convert Dp to pixels
            val tileSizePx = tileSize.toPx()
            
            val horizontalCount = (width / tileSizePx).toInt() + 1
            val verticalCount = (height / tileSizePx).toInt() + 1
            
            for (i in 0 until horizontalCount) {
                for (j in 0 until verticalCount) {
                    val isLightTile = (i + j) % 2 == 0
                    val color = if (isLightTile) lightColor else darkColor
                    
                    drawRect(
                        color = color,
                        topLeft = androidx.compose.ui.geometry.Offset(
                            x = i * tileSizePx,
                            y = j * tileSizePx
                        ),
                        size = androidx.compose.ui.geometry.Size(
                            width = tileSizePx,
                            height = tileSizePx
                        )
                    )
                }
            }
        }
    }
}
```

### `app\src\main\java\com\example\pdf_img_tools_app\core\ui\components\CommonUIComponents.kt`

```kt
package com.example.pdf_img_tools_app.ui.components

import android.annotation.SuppressLint
import android.content.Context
import android.content.Intent
import android.net.Uri
import android.widget.Toast

// This DetailRow implementation has been removed to avoid conflicts with DetailRow.kt
// Please use the DetailRow from DetailRow.kt instead

/**
 * Function to view a file using the system viewer
 */
fun viewFile(context: Context, uri: Uri, mimeType: String) {
    try {
        val intent = Intent(Intent.ACTION_VIEW).apply {
            setDataAndType(uri, mimeType)
            addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION)
        }
        if (context is android.app.Activity) {
            context.startActivity(intent)
        } else {
            intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
            context.startActivity(intent)
        }
    } catch (e: Exception) {
        Toast.makeText(context, "Cannot open file: ${e.message}", Toast.LENGTH_SHORT).show()
    }
}

/**
 * Formats file size to a human-readable string
 */

@SuppressLint("DefaultLocale")
fun formatFileSize(sizeBytes: Long): String {
    return when {
        sizeBytes < 1024 -> "$sizeBytes B"
        sizeBytes < 1024 * 1024 -> "${sizeBytes / 1024} KB"
        sizeBytes < 1024 * 1024 * 1024 -> String.format("%.2f MB", sizeBytes / (1024.0 * 1024.0))
        else -> String.format("%.2f GB", sizeBytes / (1024.0 * 1024.0 * 1024.0))
    }
}
```

### `app\src\main\java\com\example\pdf_img_tools_app\core\ui\components\DetailRow.kt`

```kt
package com.example.pdf_img_tools_app.ui.components

import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp

/**
 * A reusable detail row for displaying labeled information with an icon
 */
@Composable
fun DetailRow(
    icon: ImageVector,
    label: String,
    value: String,
    modifier: Modifier = Modifier
) {
    Row(
        verticalAlignment = Alignment.CenterVertically,
        modifier = modifier.fillMaxWidth()
    ) {
        Icon(
            imageVector = icon,
            contentDescription = null,
            tint = MaterialTheme.colorScheme.onSurfaceVariant,
            modifier = Modifier.size(18.dp)
        )
        
        Spacer(modifier = Modifier.width(8.dp))
        
        Text(
            text = label,
            style = MaterialTheme.typography.bodyMedium,
            fontWeight = FontWeight.Medium,
            color = MaterialTheme.colorScheme.onSurfaceVariant
        )
        
        Spacer(modifier = Modifier.width(4.dp))
        
        Text(
            text = value,
            style = MaterialTheme.typography.bodyMedium,
            maxLines = 1,
            overflow = TextOverflow.Ellipsis
        )
    }
} ```

### `app\src\main\java\com\example\pdf_img_tools_app\core\ui\components\ImageCanvas.kt`

```kt
package com.example.pdf_img_tools_app.ui.components

import android.graphics.Bitmap
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.gestures.detectDragGestures
import androidx.compose.foundation.gestures.detectTapGestures
import androidx.compose.foundation.gestures.detectTransformGestures
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.AspectRatio
import androidx.compose.material.icons.filled.Check
import androidx.compose.material.icons.filled.Crop
import androidx.compose.material.icons.filled.FlipToBack
import androidx.compose.material.icons.filled.FlipToFront
import androidx.compose.material.icons.filled.Grid4x4
import androidx.compose.material.icons.filled.Refresh
import androidx.compose.material.icons.filled.Redo
import androidx.compose.material.icons.filled.RotateRight
import androidx.compose.material.icons.filled.Undo
import com.example.pdf_img_tools_app.ui.components.ImageCanvasState
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Rect
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.*
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.graphics.drawscope.translate
import androidx.compose.ui.graphics.drawscope.rotate
import androidx.compose.ui.graphics.drawscope.scale as drawScaleTransform
import androidx.compose.ui.input.pointer.pointerInput
import androidx.compose.ui.layout.onSizeChanged
import androidx.compose.ui.platform.LocalDensity
import androidx.compose.ui.semantics.contentDescription
import androidx.compose.ui.semantics.semantics
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.text.drawText
import androidx.compose.ui.text.rememberTextMeasurer
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.compose.ui.unit.toSize
import kotlin.math.max
import kotlin.math.min
import kotlin.math.roundToInt

/**
 * A comprehensive image canvas component with advanced manipulation features and fixed-size canvas based on target dimensions.
 *
 * @param bitmap The image bitmap to display and manipulate
 * @param modifier Modifier to be applied to the canvas
 * @param useTransparentBackground Whether to use a transparent background (for PNG) or white (for JPG)
 * @param targetWidth The target width for resizing (in pixels)
 * @param targetHeight The target height for resizing (in pixels)
 * @param maintainAspectRatio Whether to maintain aspect ratio when resizing
 * @param onDimensionsChanged Callback when the image dimensions change due to resizing
 * @param onResize Callback when the image is resized to the canvas size
 */
@Composable
fun ImageCanvas(
    bitmap: Bitmap?,
    modifier: Modifier = Modifier,
    useTransparentBackground: Boolean = false,
    showGrid: Boolean = false,
    targetWidth: Int = 0,
    targetHeight: Int = 0,
    maintainAspectRatio: Boolean = true,
    onToggleAspectRatio: () -> Unit = {},
    onDimensionsChanged: (Int, Int) -> Unit = { _, _ -> },
    onSaveState: (ImageCanvasState) -> Unit = {},
    initialState: ImageCanvasState? = null,
    onShowGridChange: (Boolean) -> Unit = {},
    onResize: (Bitmap) -> Unit = {}
) {
    // Fallback UI if bitmap is null
    if (bitmap == null) {
        Box(
            modifier = modifier.fillMaxSize(),
            contentAlignment = Alignment.Center
        ) {
            Text(
                text = "No image loaded",
                color = MaterialTheme.colorScheme.onSurface,
                fontSize = 16.sp,
                modifier = Modifier.semantics { contentDescription = "No image loaded" }
            )
        }
        return
    }

    // Convert bitmap to ImageBitmap for Compose rendering, downscaling if necessary
    val imageBitmap = remember(bitmap) {
        try {
            if (bitmap.width > 2048 || bitmap.height > 2048) {
                val scaleFactor = min(2048f / bitmap.width, 2048f / bitmap.height)
                Bitmap.createScaledBitmap(
                    bitmap,
                    (bitmap.width * scaleFactor).toInt(),
                    (bitmap.height * scaleFactor).toInt(),
                    true
                ).asImageBitmap()
            } else {
                bitmap.asImageBitmap()
            }
        } catch (e: Exception) {
            // Handle potential OutOfMemoryError or other bitmap issues
            bitmap.asImageBitmap()
        }
    }
    val density = LocalDensity.current
    val textMeasurer = rememberTextMeasurer()

    // Aspect ratio selection
    val aspectRatios = listOf(
        Pair("1:1", 1f),
        Pair("4:3", 4f / 3f),
        Pair("16:9", 16f / 9f)
    )
    var selectedAspectRatio by remember { mutableStateOf(aspectRatios[0].second) }

    // Canvas size
    var canvasWidth by remember { mutableStateOf(0f) }
    var canvasHeight by remember { mutableStateOf(0f) }

    // Canvas state
    var scale by remember { mutableStateOf(initialState?.scale ?: 1f) }
    var offset by remember { mutableStateOf(initialState?.offset ?: Offset.Zero) }
    var rotation by remember { mutableStateOf(initialState?.rotation ?: 0f) }
    var isFlippedHorizontally by remember {
        mutableStateOf(
            initialState?.isFlippedHorizontally ?: false
        )
    }
    var isFlippedVertically by remember {
        mutableStateOf(
            initialState?.isFlippedVertically ?: false
        )
    }

    // Undo/redo state
    val undoStack = remember { mutableStateListOf<ImageCanvasState>() }
    val redoStack = remember { mutableStateListOf<ImageCanvasState>() }

    // Keep track of the history for undo/redo operations
    fun saveState() {
        val currentState = ImageCanvasState(
            scale = scale,
            offset = offset,
            rotation = rotation,
            isFlippedHorizontally = isFlippedHorizontally,
            isFlippedVertically = isFlippedVertically
        )
        undoStack.add(currentState)
        if (undoStack.size > 50) undoStack.removeAt(0) // Limit to 50 states
        redoStack.clear()
        onSaveState(currentState)
    }

    // Cropping state
    var isCropping by remember { mutableStateOf(false) }
    var cropRect by remember { mutableStateOf<Rect?>(null) }
    var dragStartPosition by remember { mutableStateOf(Offset.Zero) }
    var isDraggingCropRect by remember { mutableStateOf(false) }
    var draggedCorner by remember { mutableStateOf<Offset?>(null) }

    // Initialize crop rect if needed
    LaunchedEffect(bitmap, isCropping, selectedAspectRatio) {
        if (isCropping && cropRect == null && bitmap != null) {
            // Initialize with default crop rect matching the selected aspect ratio
            val maxWidth = min(canvasWidth, bitmap.width * scale)
            val maxHeight = min(canvasHeight, bitmap.height * scale)
            val canvasAspect = selectedAspectRatio
            val width = if (maxWidth / maxHeight > canvasAspect) {
                maxHeight * canvasAspect
            } else {
                maxWidth
            }
            val height = width / canvasAspect
            val left = (canvasWidth - width) / 2f
            val top = (canvasHeight - height) / 2f
            cropRect = Rect(left, top, left + width, top + height)
        }
    }

    // Real dimensions after transformations
    val originalWidth = bitmap.width
    val originalHeight = bitmap.height
    var displayedWidth by remember { mutableStateOf(max(originalWidth, 1)) }
    var displayedHeight by remember { mutableStateOf(max(originalHeight, 1)) }

    // Update dimensions when scale changes
    LaunchedEffect(scale) {
        displayedWidth = max((originalWidth * scale).roundToInt(), 1)
        displayedHeight = max((originalHeight * scale).roundToInt(), 1)
        onDimensionsChanged(displayedWidth, displayedHeight)
    }

    // Cache grid path for performance
    val gridPath = remember(imageBitmap, scale) {
        Path().apply {
            val width = imageBitmap.width.toFloat()
            val height = imageBitmap.height.toFloat()
            // Add vertical and horizontal lines for rule of thirds
            for (i in 1..2) {
                moveTo(width * i / 3, 0f)
                lineTo(width * i / 3, height)
                moveTo(0f, height * i / 3)
                lineTo(width, height * i / 3)
            }
        }
    }

    // Calculate canvas size based on target dimensions or aspect ratio
    val maxCanvasWidth = with(density) { 600.dp.toPx() } // Maximum width constraint
    val maxCanvasHeight = with(density) { 600.dp.toPx() } // Maximum height constraint

    // Dynamic canvas based on target dimensions if provided
    LaunchedEffect(targetWidth, targetHeight, bitmap) {
        if (targetWidth > 0 && targetHeight > 0) {
            // Use target dimensions to determine canvas size with proper scaling
            val targetAspect = targetWidth.toFloat() / targetHeight.toFloat()

            // Adjust canvas size based on target dimensions while respecting max constraints
            if (targetAspect > 1f) {
                // Landscape: prioritize width
                canvasWidth = maxCanvasWidth
                canvasHeight = maxCanvasWidth / targetAspect
                if (canvasHeight > maxCanvasHeight) {
                    canvasHeight = maxCanvasHeight
                    canvasWidth = maxCanvasHeight * targetAspect
                }
            } else {
                // Portrait or square: prioritize height
                canvasHeight = maxCanvasHeight
                canvasWidth = maxCanvasHeight * targetAspect
                if (canvasWidth > maxCanvasWidth) {
                    canvasWidth = maxCanvasWidth
                    canvasHeight = maxCanvasWidth / targetAspect
                }
            }

            // Update selected aspect ratio to match target dimensions
            selectedAspectRatio = targetAspect

        } else {
            // Fallback to default aspect ratio if no target dimensions are provided
            val canvasAspect = selectedAspectRatio
            if (canvasAspect > 1f) {
                // Landscape: prioritize width
                canvasWidth = maxCanvasWidth
                canvasHeight = maxCanvasWidth / canvasAspect
                if (canvasHeight > maxCanvasHeight) {
                    canvasHeight = maxCanvasHeight
                    canvasWidth = maxCanvasHeight * canvasAspect
                }
            } else {
                // Portrait or square: prioritize height
                canvasHeight = maxCanvasHeight
                canvasWidth = maxCanvasHeight * canvasAspect
                if (canvasWidth > maxCanvasWidth) {
                    canvasWidth = maxCanvasWidth
                    canvasHeight = maxCanvasWidth / canvasAspect
                }
            }
        }

        // Ensure canvas dimensions are positive
        canvasWidth = max(canvasWidth, 1f)
        canvasHeight = max(canvasHeight, 1f)

        // Initialize scale and offset to fit image in canvas
        if (initialState == null) {
            val imageAspect = imageBitmap.width.toFloat() / imageBitmap.height.toFloat()
            val canvasAspect = canvasWidth / canvasHeight.toFloat()

            scale = if (imageAspect > canvasAspect) {
                canvasWidth / imageBitmap.width.toFloat()
            } else {
                canvasHeight / imageBitmap.height.toFloat()
            } * 0.9f

            offset = Offset(
                (canvasWidth - imageBitmap.width * scale) / 2f,
                (canvasHeight - imageBitmap.height * scale) / 2f
            )
        }
    }

    // Main image canvas
    Box(modifier = modifier) {
        if (canvasWidth <= 0f || canvasHeight <= 0f) {
            // Skip rendering if canvas dimensions are invalid
            return@Box
        }

        Canvas(
            modifier = Modifier
                .size(with(density) { canvasWidth.toDp() }, with(density) { canvasHeight.toDp() })
                .align(Alignment.Center)
                .background(if (useTransparentBackground) Color.Transparent else Color.White)
                .pointerInput(isCropping) {
                    if (isCropping) {
                        // Handle crop rectangle interaction
                        detectTapGestures { tapPosition ->
                            // Initialize crop rectangle if not already set
                            if (cropRect == null) {
                                val maxWidth = min(canvasWidth, imageBitmap.width * scale)
                                val maxHeight = min(canvasHeight, imageBitmap.height * scale)
                                val canvasAspect = selectedAspectRatio
                                val width = if (maxWidth / maxHeight > canvasAspect) {
                                    maxHeight * canvasAspect
                                } else {
                                    maxWidth
                                }
                                val height = width / canvasAspect
                                val left = (canvasWidth - width) / 2f
                                val top = (canvasHeight - height) / 2f
                                cropRect = Rect(left, top, left + width, top + height)
                            }
                        }
                    }
                }
                .pointerInput(isCropping) {
                    if (isCropping) {
                        // Handle dragging/resizing of crop rect
                        detectDragGestures(
                            onDragStart = { position ->
                                cropRect?.let { rect ->
                                    val corners = listOf(
                                        rect.topLeft,
                                        rect.topRight,
                                        rect.bottomLeft,
                                        rect.bottomRight
                                    )
                                    draggedCorner = corners.find { corner ->
                                        (corner - position).getDistance() < 20f
                                    }
                                    isDraggingCropRect =
                                        draggedCorner != null || rect.contains(position)
                                    dragStartPosition = position
                                }
                            },
                            onDrag = { change, dragAmount ->
                                change.consume()
                                cropRect?.let { rect ->
                                    if (isDraggingCropRect) {
                                        if (draggedCorner != null) {
                                            // Resize crop rectangle
                                            val newRect = when (draggedCorner) {
                                                rect.topLeft -> Rect(
                                                    left = (rect.left + dragAmount.x).coerceAtLeast(
                                                        offset.x
                                                    ),
                                                    top = (rect.top + dragAmount.y).coerceAtLeast(
                                                        offset.y
                                                    ),
                                                    right = rect.right,
                                                    bottom = rect.bottom
                                                )

                                                rect.topRight -> Rect(
                                                    left = rect.left,
                                                    top = (rect.top + dragAmount.y).coerceAtLeast(
                                                        offset.y
                                                    ),
                                                    right = (rect.right + dragAmount.x).coerceAtMost(
                                                        offset.x + imageBitmap.width * scale
                                                    ),
                                                    bottom = rect.bottom
                                                )

                                                rect.bottomLeft -> Rect(
                                                    left = (rect.left + dragAmount.x).coerceAtLeast(
                                                        offset.x
                                                    ),
                                                    top = rect.top,
                                                    right = rect.right,
                                                    bottom = (rect.bottom + dragAmount.y).coerceAtMost(
                                                        offset.y + imageBitmap.height * scale
                                                    )
                                                )

                                                rect.bottomRight -> Rect(
                                                    left = rect.left,
                                                    top = rect.top,
                                                    right = (rect.right + dragAmount.x).coerceAtMost(
                                                        offset.x + imageBitmap.width * scale
                                                    ),
                                                    bottom = (rect.bottom + dragAmount.y).coerceAtMost(
                                                        offset.y + imageBitmap.height * scale
                                                    )
                                                )

                                                else -> rect
                                            }
                                            // Enforce minimum size and aspect ratio
                                            val canvasAspect = selectedAspectRatio
                                            val minSize = 50f
                                            val newWidth = newRect.width.coerceAtLeast(minSize)
                                            val newHeight = newWidth / canvasAspect.toFloat()
                                            cropRect = Rect(
                                                newRect.left,
                                                newRect.top,
                                                newRect.left + newWidth,
                                                newRect.top + newHeight
                                            )
                                        } else {
                                            // Move crop rectangle
                                            val newRect = rect.translate(dragAmount)
                                            val imageBounds = Rect(
                                                offset.x,
                                                offset.y,
                                                offset.x + imageBitmap.width * scale,
                                                offset.y + imageBitmap.height * scale
                                            )
                                            cropRect = Rect(
                                                newRect.left.coerceIn(
                                                    imageBounds.left,
                                                    imageBounds.right - newRect.width
                                                ),
                                                newRect.top.coerceIn(
                                                    imageBounds.top,
                                                    imageBounds.bottom - newRect.height
                                                ),
                                                newRect.right.coerceIn(
                                                    newRect.left + 50f,
                                                    imageBounds.right
                                                ),
                                                newRect.bottom.coerceIn(
                                                    newRect.top + 50f / selectedAspectRatio.toFloat(),
                                                    imageBounds.bottom
                                                )
                                            )
                                        }
                                    }
                                }
                            },
                            onDragEnd = {
                                isDraggingCropRect = false
                                draggedCorner = null
                            }
                        )
                    }
                }
                .pointerInput(Unit) {
                    // Handle dragging of image if not in crop mode
                    detectDragGestures(
                        onDragStart = { dragStartPosition = it },
                        onDrag = { change, dragAmount ->
                            change.consume()
                            if (!isCropping) {
                                offset += dragAmount
                                saveState()
                            }
                        }
                    )
                }
                .pointerInput(Unit) {
                    detectTransformGestures(
                        onGesture = { _, pan, zoom, _ ->
                            if (!isCropping) {
                                // Handle panning
                                offset += pan

                                // Handle zooming
                                val prevScale = scale
                                scale = (scale * zoom).coerceIn(0.1f, 3f)

                                // Adjust offset to zoom toward pointer
                                val focusPoint = Offset(canvasWidth / 2, canvasHeight / 2)
                                val scaleFactor = scale / prevScale
                                val newOffset = (offset - focusPoint) * scaleFactor + focusPoint
                                offset = newOffset

                                saveState()
                            }
                        }
                    )
                }
                .semantics { contentDescription = "Image editing canvas" }
        ) {
            // Draw background
            drawRect(
                color = if (useTransparentBackground) Color.Transparent else Color.White,
                size = size
            )

            // Draw image with transformations
            translate(offset.x, offset.y) {
                rotate(
                    rotation,
                    Offset(imageBitmap.width * scale / 2, imageBitmap.height * scale / 2)
                ) {
                    // Apply scale and flip transformations manually
                    val scaleX = scale * (if (isFlippedHorizontally) -1f else 1f)
                    val scaleY = scale * (if (isFlippedVertically) -1f else 1f)
                    val pivotX = imageBitmap.width / 2f
                    val pivotY = imageBitmap.height / 2f

                    // Apply scaling matrix with pivot
                    drawScaleTransform(scaleX, scaleY) {
                        drawImage(
                            image = imageBitmap,
                            topLeft = Offset(
                                x = if (isFlippedHorizontally) -imageBitmap.width.toFloat() else 0f,
                                y = if (isFlippedVertically) -imageBitmap.height.toFloat() else 0f
                            )
                        )
                    }
                }
            }

            // Draw grid overlay
            if (showGrid) {
                translate(offset.x, offset.y) {
                    rotate(
                        rotation,
                        Offset(imageBitmap.width * scale / 2, imageBitmap.height * scale / 2)
                    ) {
                        drawScaleTransform(scale, scale) {
                            drawPath(
                                path = gridPath,
                                color = Color.White.copy(alpha = 0.7f),
                                style = Stroke(
                                    width = 1f / scale,
                                    pathEffect = PathEffect.dashPathEffect(
                                        floatArrayOf(
                                            10f / scale,
                                            10f / scale
                                        )
                                    )
                                )
                            )
                        }
                    }
                }
            }

            // Draw crop rectangle if in cropping mode
            cropRect?.let { rect ->
                if (isCropping) {
                    drawRect(
                        color = Color.White,
                        topLeft = rect.topLeft,
                        size = rect.size,
                        style = Stroke(width = 2f)
                    )

                    // Draw handles at corners
                    val handleRadius = 10f
                    val handleColor = Color.White
                    val corners = listOf(
                        rect.topLeft,
                        rect.topRight,
                        rect.bottomLeft,
                        rect.bottomRight
                    )

                    corners.forEach { corner ->
                        drawCircle(
                            color = handleColor,
                            radius = handleRadius,
                            center = corner,
                            style = Stroke(width = 2f)
                        )
                    }

                    // Draw semi-transparent overlay outside crop area
                    val outsidePath = Path().apply {
                        addRect(Rect(Offset.Zero, Size(size.width, size.height)))
                        addRect(rect)
                        fillType = PathFillType.EvenOdd
                    }

                    drawPath(
                        path = outsidePath,
                        color = Color.Black.copy(alpha = 0.5f)
                    )
                }
            }

            // Display dimensions only if valid
            if (displayedWidth > 0 && displayedHeight > 0) {
                val dimensionsText = "${displayedWidth}×${displayedHeight}px"
                val textStyle = TextStyle(
                    color = Color.White,
                    fontSize = 14.sp,
                    background = Color.Black.copy(alpha = 0.7f),
                    textAlign = TextAlign.Left
                )

                // Measure the text to get its size
                val textLayoutResult = textMeasurer.measure(dimensionsText, textStyle)

                // Create a background for the text
                drawRect(
                    color = Color.Black.copy(alpha = 0.7f),
                    topLeft = Offset(10f, 10f),
                    size = Size(
                        textLayoutResult.size.width.toFloat() + 10f,
                        textLayoutResult.size.height.toFloat() + 6f
                    ),
                    alpha = 0.7f
                )

                // Draw the text
                drawText(
                    textMeasurer = textMeasurer,
                    text = dimensionsText,
                    topLeft = Offset(15f, 13f),
                    style = textStyle.copy(background = Color.Transparent)
                )
            }
        }

        // Control panel
        Column(
            modifier = Modifier
                .align(Alignment.BottomEnd)
                .padding(8.dp)
                .clip(RoundedCornerShape(8.dp))
                .background(MaterialTheme.colorScheme.tertiary)
                .padding(8.dp)
        ) {
            // Aspect ratio selector
            Row(
                verticalAlignment = Alignment.CenterVertically
            ) {
                Text(
                    text = "Aspect Ratio:",
                    color = MaterialTheme.colorScheme.onTertiary,
                    fontSize = 12.sp
                )
                Spacer(modifier = Modifier.width(8.dp))
                DropdownMenu(
                    expanded = false,
                    onDismissRequest = { /* Handled by button click */ },
                    modifier = Modifier.background(MaterialTheme.colorScheme.surface)
                ) {
                    var expanded by remember { mutableStateOf(false) }
                    Box {
                        Button(onClick = { expanded = true }) {
                            Text(
                                text = aspectRatios.find { it.second == selectedAspectRatio }?.first
                                    ?: "Custom"
                            )
                        }
                    }

                    // Rotate button
                    IconButton(
                        onClick = {
                            rotation = (rotation + 90f) % 360f
                            saveState()
                        },
                        modifier = Modifier.semantics {
                            contentDescription = "Rotate image 90 degrees clockwise"
                        }
                    ) {
                        Icon(
                            imageVector = Icons.Default.RotateRight,
                            contentDescription = null,
                            tint = MaterialTheme.colorScheme.onSurfaceVariant
                        )
                    }

                    // Crop toggle
                    IconButton(
                        onClick = {
                            isCropping = !isCropping
                            if (!isCropping && cropRect != null) {
                                // Reset crop rect when exiting crop mode
                                cropRect = null
                            }
                            saveState()
                        },
                        modifier = Modifier.semantics {
                            contentDescription =
                                if (isCropping) "Exit crop mode" else "Enter crop mode"
                        }
                    ) {
                        Icon(
                            imageVector = Icons.Default.Crop,
                            contentDescription = null,
                            tint = if (isCropping) MaterialTheme.colorScheme.primary else MaterialTheme.colorScheme.onSurfaceVariant
                        )
                    }

                    // Confirm resize button (visible only in crop mode)
                    if (isCropping) {
                        IconButton(
                            onClick = {
                                cropRect?.let { rect ->
                                    try {
                                        // Local helper function to resize bitmap
                                        fun resizeBitmapHelper(
                                            bitmap: Bitmap,
                                            cropRect: Rect,
                                            scale: Float,
                                            offset: Offset,
                                            canvasWidth: Float,
                                            canvasHeight: Float
                                        ): Bitmap {
                                            val scaledRect = Rect(
                                                ((cropRect.left - offset.x) / scale).coerceIn(
                                                    0f,
                                                    bitmap.width.toFloat()
                                                ),
                                                ((cropRect.top - offset.y) / scale).coerceIn(
                                                    0f,
                                                    bitmap.height.toFloat()
                                                ),
                                                ((cropRect.right - offset.x) / scale).coerceIn(
                                                    0f,
                                                    bitmap.width.toFloat()
                                                ),
                                                ((cropRect.bottom - offset.y) / scale).coerceIn(
                                                    0f,
                                                    bitmap.height.toFloat()
                                                )
                                            )
                                            // Crop the bitmap to the selected rectangle
                                            val croppedBitmap = Bitmap.createBitmap(
                                                bitmap,
                                                scaledRect.left.toInt(),
                                                scaledRect.top.toInt(),
                                                scaledRect.width.toInt(),
                                                scaledRect.height.toInt()
                                            )
                                            // Resize to match canvas dimensions
                                            return Bitmap.createScaledBitmap(
                                                croppedBitmap,
                                                canvasWidth.toInt(),
                                                canvasHeight.toInt(),
                                                true
                                            )
                                        }

                                        val resizedBitmap = resizeBitmapHelper(
                                            bitmap,
                                            rect,
                                            scale,
                                            offset,
                                            canvasWidth,
                                            canvasHeight
                                        )
                                        onResize(resizedBitmap)
                                        isCropping = false
                                        cropRect = null
                                        // Reset transformations
                                        scale = 1f
                                        offset = Offset(
                                            (canvasWidth - resizedBitmap.width.toFloat()) / 2f,
                                            (canvasHeight - resizedBitmap.height.toFloat()) / 2f
                                        )
                                        rotation = 0f
                                        isFlippedHorizontally = false
                                        isFlippedVertically = false
                                        saveState()
                                    } catch (e: Exception) {
                                        // Handle resizing errors
                                    }
                                }
                            },
                            modifier = Modifier.semantics { contentDescription = "Confirm resize" }
                        ) {
                            Icon(
                                imageVector = Icons.Default.Check,
                                contentDescription = null,
                                tint = MaterialTheme.colorScheme.primary
                            )
                        }
                    }

                    // Grid toggle
                    IconButton(
                        onClick = { onShowGridChange(!showGrid) },
                        modifier = Modifier.semantics {
                            contentDescription = if (showGrid) "Hide grid" else "Show grid"
                        }
                    ) {
                        Icon(
                            imageVector = Icons.Default.Grid4x4,
                            contentDescription = null,
                            tint = if (showGrid) MaterialTheme.colorScheme.primary else MaterialTheme.colorScheme.onSurfaceVariant
                        )
                    }

                    // Flip horizontal
                    IconButton(
                        onClick = {
                            isFlippedHorizontally = !isFlippedHorizontally
                            saveState()
                        },
                        modifier = Modifier.semantics {
                            contentDescription = "Flip image horizontally"
                        }
                    ) {
                        Icon(
                            imageVector = Icons.Default.FlipToBack,
                            contentDescription = null,
                            tint = MaterialTheme.colorScheme.onSurfaceVariant
                        )
                    }

                    // Flip vertical
                    IconButton(
                        onClick = {
                            isFlippedVertically = !isFlippedVertically
                            saveState()
                        },
                        modifier = Modifier.semantics {
                            contentDescription = "Flip image vertically"
                        }
                    ) {
                        Icon(
                            imageVector = Icons.Default.FlipToFront,
                            contentDescription = null,
                            tint = MaterialTheme.colorScheme.onSurfaceVariant
                        )
                    }

                    // Reset button
                    IconButton(
                        onClick = {
                            scale = 1f
                            offset = Offset(
                                (canvasWidth - imageBitmap.width) / 2f,
                                (canvasHeight - imageBitmap.height) / 2f
                            )
                            rotation = 0f
                            isFlippedHorizontally = false
                            isFlippedVertically = false
                            isCropping = false
                            cropRect = null
                            saveState()
                        },
                        modifier = Modifier.semantics {
                            contentDescription = "Reset all transformations"
                        }
                    ) {
                        Icon(
                            imageVector = Icons.Default.Refresh,
                            contentDescription = null,
                            tint = MaterialTheme.colorScheme.onSurfaceVariant
                        )
                    }

                    // Undo button
                    IconButton(
                        onClick = {
                            if (undoStack.isNotEmpty()) {
                                val state = undoStack.removeAt(undoStack.lastIndex)
                                redoStack.add(
                                    ImageCanvasState(
                                        scale = scale,
                                        offset = offset,
                                        rotation = rotation,
                                        isFlippedHorizontally = isFlippedHorizontally,
                                        isFlippedVertically = isFlippedVertically
                                    )
                                )
                                scale = state.scale
                                offset = state.offset
                                rotation = state.rotation
                                isFlippedHorizontally = state.isFlippedHorizontally
                                isFlippedVertically = state.isFlippedVertically
                            }
                        },
                        enabled = undoStack.isNotEmpty(),
                        modifier = Modifier.semantics { contentDescription = "Undo last action" }
                    ) {
                        Icon(
                            imageVector = Icons.Default.Undo,
                            contentDescription = null,
                            tint = if (undoStack.isNotEmpty()) MaterialTheme.colorScheme.onSurfaceVariant else MaterialTheme.colorScheme.onSurfaceVariant.copy(
                                alpha = 0.5f
                            )
                        )
                    }

                    // Redo button
                    IconButton(
                        onClick = {
                            if (redoStack.isNotEmpty()) {
                                val state = redoStack.removeAt(redoStack.lastIndex)
                                undoStack.add(
                                    ImageCanvasState(
                                        scale = scale,
                                        offset = offset,
                                        rotation = rotation,
                                        isFlippedHorizontally = isFlippedHorizontally,
                                        isFlippedVertically = isFlippedVertically
                                    )
                                )
                                scale = state.scale
                                offset = state.offset
                                rotation = state.rotation
                                isFlippedHorizontally = state.isFlippedHorizontally
                                isFlippedVertically = state.isFlippedVertically
                            }
                        },
                        enabled = redoStack.isNotEmpty(),
                        modifier = Modifier.semantics {
                            contentDescription = "Redo last undone action"
                        }
                    ) {
                        Icon(
                            imageVector = Icons.Default.Redo,
                            contentDescription = null,
                            tint = if (redoStack.isNotEmpty()) MaterialTheme.colorScheme.onSurfaceVariant else MaterialTheme.colorScheme.onSurfaceVariant.copy(
                                alpha = 0.5f
                            )
                        )
                    }
                }
            }
        }
    }
}
```

### `app\src\main\java\com\example\pdf_img_tools_app\core\ui\components\ProcessingIndicator.kt`

```kt
package com.example.pdf_img_tools_app.ui.components

import androidx.compose.animation.core.*
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Cancel
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.window.Dialog
import androidx.compose.ui.window.DialogProperties

/**
 * A processing indicator that shows a progress bar with percentage and a message.
 * 
 * @param isVisible Whether the indicator is visible
 * @param progress The current progress as a float between 0 and 1
 * @param message The message to display
 * @param timeRemaining Estimated time remaining (optional)
 * @param onDismissRequest Optional callback to dismiss the indicator
 * @param onCancel Optional callback to cancel the operation
 */
@Composable
fun ProcessingIndicator(
    isVisible: Boolean,
    progress: Float = -1f, // -1 means indeterminate
    message: String = "Processing...",
    timeRemaining: String? = null,
    onDismissRequest: (() -> Unit)? = null,
    onCancel: (() -> Unit)? = null
) {
    if (!isVisible) return
    
    // Pulsating animation for the background - using primaryContainer for better semantics
    val infiniteTransition = rememberInfiniteTransition(label = "processing_background")
    val color by infiniteTransition.animateValue(
        initialValue = MaterialTheme.colorScheme.primaryContainer.copy(alpha = 0.3f),
        targetValue = MaterialTheme.colorScheme.primaryContainer.copy(alpha = 0.5f),
        typeConverter = ColorConverter,
        animationSpec = infiniteRepeatable(
            animation = tween(1000),
            repeatMode = RepeatMode.Reverse
        ),
        label = "background_pulse"
    )
    
    Dialog(
        onDismissRequest = { onDismissRequest?.invoke() },
        properties = DialogProperties(dismissOnBackPress = false, dismissOnClickOutside = false)
    ) {
        Box(
            contentAlignment = Alignment.Center,
            modifier = Modifier
                .clip(RoundedCornerShape(16.dp))
                .background(MaterialTheme.colorScheme.surfaceVariant)
                .padding(24.dp)
        ) {
            Column(
                horizontalAlignment = Alignment.CenterHorizontally,
                verticalArrangement = Arrangement.Center,
                modifier = Modifier.width(300.dp)
            ) {
                // Title
                Text(
                    text = message,
                    style = MaterialTheme.typography.titleMedium,
                    fontWeight = FontWeight.SemiBold,
                    textAlign = TextAlign.Center
                )
                
                Spacer(modifier = Modifier.height(16.dp))
                
                // Progress bar with background effect
                Box(
                    modifier = Modifier
                        .fillMaxWidth()
                        .height(12.dp)
                        .clip(RoundedCornerShape(8.dp))
                        .background(color)
                ) {
                    if (progress >= 0) {
                        // Determinate progress bar
                        Box(
                            modifier = Modifier
                                .fillMaxWidth(progress.coerceIn(0f, 1f))
                                .fillMaxHeight()
                                .clip(RoundedCornerShape(8.dp))
                                .background(MaterialTheme.colorScheme.primary)
                        )
                    } else {
                        // Indeterminate progress bar
                        val infiniteProgress by infiniteTransition.animateFloat(
                            initialValue = 0f,
                            targetValue = 1f,
                            animationSpec = infiniteRepeatable(
                                animation = tween(1500),
                                repeatMode = RepeatMode.Restart
                            ),
                            label = "progress_animation"
                        )
                        
                        Box(
                            modifier = Modifier
                                .fillMaxWidth(0.3f)
                                .fillMaxHeight()
                                .offset(x = (infiniteProgress * 210).dp)
                                .clip(RoundedCornerShape(8.dp))
                                .background(MaterialTheme.colorScheme.primary)
                        )
                    }
                }
                
                Spacer(modifier = Modifier.height(8.dp))
                
                // Percentage text - show only for determinate progress
                if (progress >= 0) {
                    Row(
                        horizontalArrangement = Arrangement.Center,
                        modifier = Modifier.fillMaxWidth()
                    ) {
                        Text(
                            text = "${(progress * 100).toInt()}%",
                            style = MaterialTheme.typography.bodyMedium,
                            fontWeight = FontWeight.Bold,
                        )
                        
                        // Show time remaining if available
                        timeRemaining?.let {
                            Spacer(modifier = Modifier.width(8.dp))
                            Text(
                                text = "• $it remaining",
                                style = MaterialTheme.typography.bodyMedium,
                                color = MaterialTheme.colorScheme.onSurfaceVariant.copy(alpha = 0.7f)
                            )
                        }
                    }
                }
                
                // Cancel button if onCancel is provided
                if (onCancel != null) {
                    Spacer(modifier = Modifier.height(16.dp))
                    TextButton(
                        onClick = { onCancel() },
                        colors = ButtonDefaults.textButtonColors(
                            contentColor = MaterialTheme.colorScheme.error
                        )
                    ) {
                        Icon(
                            imageVector = Icons.Default.Cancel,
                            contentDescription = "Cancel",
                            modifier = Modifier.size(16.dp)
                        )
                        Spacer(modifier = Modifier.width(4.dp))
                        Text("Cancel")
                    }
                }
            }
        }
    }
}

/**
 * Color converter for animateValue
 */
private object ColorConverter : TwoWayConverter<Color, AnimationVector4D> {
    override val convertToVector: (Color) -> AnimationVector4D = { color ->
        AnimationVector4D(color.red, color.green, color.blue, color.alpha)
    }
    
    override val convertFromVector: (AnimationVector4D) -> Color = { vector ->
        Color(vector.v1, vector.v2, vector.v3, vector.v4)
    }
}

/**
 * Simple overlay to indicate processing is happening in the background
 */
@Composable
fun ProcessingOverlay(
    isVisible: Boolean,
    message: String = "Processing..."
) {
    if (!isVisible) return
    
    Box(
        modifier = Modifier
            .fillMaxWidth()
            .padding(16.dp)
            .clip(RoundedCornerShape(8.dp))
            .background(MaterialTheme.colorScheme.surfaceVariant)
            .padding(16.dp),
        contentAlignment = Alignment.Center
    ) {
        Row(
            verticalAlignment = Alignment.CenterVertically,
            horizontalArrangement = Arrangement.spacedBy(16.dp)
        ) {
            CircularProgressIndicator(
                modifier = Modifier.size(24.dp),
                color = MaterialTheme.colorScheme.primary,
                strokeWidth = 2.dp
            )
            
            Text(
                text = message,
                style = MaterialTheme.typography.bodyMedium,
                fontWeight = FontWeight.Medium,
                color = MaterialTheme.colorScheme.onSurfaceVariant
            )
        }
    }
}```

### `app\src\main\java\com\example\pdf_img_tools_app\core\ui\components\ThemeSelector.kt`

```kt
package com.example.pdf_img_tools_app.core.ui.components

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.unit.dp
import com.example.pdf_img_tools_app.core.ui.theme.Amber500
import com.example.pdf_img_tools_app.core.ui.theme.AppTheme
import com.example.pdf_img_tools_app.core.ui.theme.Blue500
import com.example.pdf_img_tools_app.core.ui.theme.Green500
import com.example.pdf_img_tools_app.core.ui.theme.Purple500
import com.example.pdf_img_tools_app.core.ui.theme.Sky500
import com.example.pdf_img_tools_app.core.ui.theme.setAppTheme

/**
 * A component that allows users to select different color themes based on Tailwind colors
 */
@Composable
fun ThemeSelector(
    currentTheme: AppTheme,
    modifier: Modifier = Modifier
) {
    Card(
        modifier = modifier.fillMaxWidth(),
        shape = RoundedCornerShape(12.dp),
        elevation = CardDefaults.cardElevation(defaultElevation = 2.dp),
        colors = CardDefaults.cardColors(
            containerColor = MaterialTheme.colorScheme.surface,
            contentColor = MaterialTheme.colorScheme.onSurface
        )
    ) {
        Column(
            modifier = Modifier.padding(16.dp)
        ) {
            Text(
                text = "Theme Color",
                style = MaterialTheme.typography.titleMedium
            )
            
            Spacer(modifier = Modifier.height(12.dp))
            
            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.SpaceEvenly
            ) {
                // Default Theme
                ThemeOption(
                    colorName = "Default",
                    color = Sky500,
                    isSelected = currentTheme == AppTheme.DEFAULT,
                    onClick = { setAppTheme(AppTheme.DEFAULT) }
                )
                
                // Blue Theme
                ThemeOption(
                    colorName = "Blue",
                    color = Blue500,
                    isSelected = currentTheme == AppTheme.BLUE,
                    onClick = { setAppTheme(AppTheme.BLUE) }
                )
                
                // Green Theme
                ThemeOption(
                    colorName = "Green",
                    color = Green500,
                    isSelected = currentTheme == AppTheme.GREEN,
                    onClick = { setAppTheme(AppTheme.GREEN) }
                )
                
                // Purple Theme
                ThemeOption(
                    colorName = "Purple",
                    color = Purple500,
                    isSelected = currentTheme == AppTheme.PURPLE,
                    onClick = { setAppTheme(AppTheme.PURPLE) }
                )
                
                // Amber Theme
                ThemeOption(
                    colorName = "Amber",
                    color = Amber500,
                    isSelected = currentTheme == AppTheme.AMBER,
                    onClick = { setAppTheme(AppTheme.AMBER) }
                )
            }
        }
    }
}

@Composable
private fun ThemeOption(
    colorName: String,
    color: androidx.compose.ui.graphics.Color,
    isSelected: Boolean,
    onClick: () -> Unit
) {
    Column(
        horizontalAlignment = Alignment.CenterHorizontally,
        modifier = Modifier
            .padding(8.dp)
            .clickable(onClick = onClick)
    ) {
        Box(
            modifier = Modifier
                .size(48.dp)
                .clip(CircleShape)
                .background(color)
                .then(
                    if (isSelected) {
                        Modifier.border(2.dp, MaterialTheme.colorScheme.primary, CircleShape)
                    } else {
                        Modifier.border(1.dp, MaterialTheme.colorScheme.outline, CircleShape)
                    }
                )
        )
        
        Spacer(modifier = Modifier.height(4.dp))
        
        Text(
            text = colorName,
            style = MaterialTheme.typography.bodySmall,
            color = if (isSelected) MaterialTheme.colorScheme.primary else MaterialTheme.colorScheme.onSurfaceVariant
        )
    }
}

/**
 * Preview of ThemeSelector
 */
@Composable
fun ThemeSelectorPreview() {
    ThemeSelector(
        currentTheme = AppTheme.DEFAULT,
        modifier = Modifier.padding(16.dp)
    )
} ```

### `app\src\main\java\com\example\pdf_img_tools_app\core\ui\components\ToolProgressIndicator.kt`

```kt
package com.example.pdf_img_tools_app.ui.components

import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.StrokeCap
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp

/**
 * A reusable progress indicator that can be integrated into tool buttons
 * Supports both determinate (with percentage) and indeterminate progress
 * 
 * @param isVisible Whether the progress indicator is visible
 * @param progress The current progress (0f to 1f), -1f for indeterminate
 * @param icon Optional icon to show alongside progress
 * @param text Text to display
 * @param onCancel Optional callback for cancellation
 */
@Composable
fun ToolProgressIndicator(
    isVisible: Boolean,
    progress: Float = -1f, // -1 means indeterminate
    icon: ImageVector? = null,
    text: String = "",
    errorMessage: String? = null,
    onCancel: (() -> Unit)? = null,
    modifier: Modifier = Modifier
) {
    if (!isVisible) return
    
    Box(
        contentAlignment = Alignment.Center,
        modifier = modifier
            .fillMaxWidth()
            .clip(RoundedCornerShape(12.dp))
            .background(MaterialTheme.colorScheme.primaryContainer)
            .padding(16.dp)
    ) {
        Column(
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.Center,
            modifier = Modifier.fillMaxWidth()
        ) {
            // Icon and text
            if (icon != null || text.isNotEmpty()) {
                Row(
                    verticalAlignment = Alignment.CenterVertically,
                    horizontalArrangement = Arrangement.Center,
                    modifier = Modifier.fillMaxWidth()
                ) {
                    icon?.let {
                        Icon(
                            imageVector = it,
                            contentDescription = null,
                            tint = MaterialTheme.colorScheme.onPrimaryContainer,
                            modifier = Modifier.size(20.dp)
                        )
                        Spacer(modifier = Modifier.width(8.dp))
                    }
                    
                    if (text.isNotEmpty()) {
                        Text(
                            text = text,
                            style = MaterialTheme.typography.bodyMedium,
                            fontWeight = FontWeight.Medium,
                            color = MaterialTheme.colorScheme.onPrimaryContainer
                        )
                    }
                }
                
                Spacer(modifier = Modifier.height(16.dp))
            }
            
            // Progress indicator
            if (progress >= 0) {
                // Determinate progress
                Column(
                    horizontalAlignment = Alignment.CenterHorizontally,
                    modifier = Modifier.fillMaxWidth()
                ) {
                    // Progress bar
                    LinearProgressIndicator(
                        progress = { progress },
                        modifier = Modifier
                            .fillMaxWidth()
                            .height(8.dp)
                            .clip(RoundedCornerShape(4.dp)),
                        color = MaterialTheme.colorScheme.primary,
                        trackColor = MaterialTheme.colorScheme.onPrimaryContainer.copy(alpha = 0.1f),
                        strokeCap = StrokeCap.Round
                    )
                    
                    Spacer(modifier = Modifier.height(4.dp))
                    
                    // Percentage text
                    Text(
                        text = "${(progress * 100).toInt()}%",
                        style = MaterialTheme.typography.bodySmall,
                        fontWeight = FontWeight.Bold,
                        color = MaterialTheme.colorScheme.onPrimaryContainer
                    )
                }
            } else {
                // Indeterminate progress
                LinearProgressIndicator(
                    modifier = Modifier
                        .fillMaxWidth()
                        .height(8.dp)
                        .clip(RoundedCornerShape(4.dp)),
                    color = MaterialTheme.colorScheme.primary,
                    trackColor = MaterialTheme.colorScheme.onPrimaryContainer.copy(alpha = 0.1f),
                    strokeCap = StrokeCap.Round
                )
            }
            
            // Error message if present
            errorMessage?.let {
                if (it.isNotEmpty()) {
                    Spacer(modifier = Modifier.height(8.dp))
                    Text(
                        text = it,
                        style = MaterialTheme.typography.bodySmall,
                        color = MaterialTheme.colorScheme.error,
                        textAlign = TextAlign.Center
                    )
                }
            }
            
            // Cancel button
            if (onCancel != null) {
                Spacer(modifier = Modifier.height(12.dp))
                OutlinedButton(
                    modifier = Modifier.fillMaxWidth(),
                    onClick = { onCancel() },
                    border = BorderStroke(2.dp, MaterialTheme.colorScheme.primary),
                    colors = ButtonDefaults.outlinedButtonColors(
                        containerColor = MaterialTheme.colorScheme.background
                    ),
                ) {
                    Spacer(modifier = Modifier.width(4.dp))
                    Text("Cancel")
                }
            }
        }
    }
}

```

### `app\src\main\java\com\example\pdf_img_tools_app\core\ui\theme\Color.kt`

```kt
package com.example.pdf_img_tools_app.core.ui.theme

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

### `app\src\main\java\com\example\pdf_img_tools_app\core\ui\theme\Shape.kt`

```kt
package com.example.pdf_img_tools_app.core.ui.theme

import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Shapes
import androidx.compose.ui.unit.dp

// Updated shapes for a sharper, sleeker look
val Shapes = Shapes(
    small = RoundedCornerShape(2.dp),    // Sharper small corners
    medium = RoundedCornerShape(4.dp),   // Sharper medium corners (Buttons, Cards)
    large = RoundedCornerShape(8.dp)     // Sharper large corners
) 
```

### `app\src\main\java\com\example\pdf_img_tools_app\core\ui\theme\Theme.kt`

```kt
package com.example.pdf_img_tools_app.core.ui.theme

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

// Theme enum to allow easy switching between different Tailwind-based themes
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
    background = Slate50, // Page background
    onBackground = Slate900, // Default text

    // Cards, menus, and sheets
    surface = Slate200, // Default surface color
    onSurface = Slate600, // Text/icons on surfaces

    surfaceVariant = White, // For lower elevation components
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

// Helper function to set the current app theme
fun setAppTheme(theme: AppTheme) {
    currentTheme = theme
}
```

### `app\src\main\java\com\example\pdf_img_tools_app\core\ui\theme\Type.kt`

```kt
package com.example.pdf_img_tools_app.core.ui.theme

import androidx.compose.material3.Typography
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.sp

// Set of Material typography styles to start with
val Typography = Typography(
    bodyLarge = TextStyle(
        fontFamily = FontFamily.Default,
        fontWeight = FontWeight.Normal,
        fontSize = 16.sp,
        lineHeight = 24.sp,
        letterSpacing = 0.5.sp
    )
    /* Other default text styles to override
    titleLarge = TextStyle(
        fontFamily = FontFamily.Default,
        fontWeight = FontWeight.Normal,
        fontSize = 22.sp,
        lineHeight = 28.sp,
        letterSpacing = 0.sp
    ),
    labelSmall = TextStyle(
        fontFamily = FontFamily.Default,
        fontWeight = FontWeight.Medium,
        fontSize = 11.sp,
        lineHeight = 16.sp,
        letterSpacing = 0.5.sp
    )
    */
)
```

### `app\src\main\java\com\example\pdf_img_tools_app\data\repository\ToolRepository.kt`

```kt
package com.example.pdf_img_tools_app.data.repository
import  com.example.pdf_img_tools_app.config.FeatureFlags

import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.rounded.Cached
import androidx.compose.material.icons.rounded.Compress
import androidx.compose.material.icons.rounded.MergeType
import androidx.compose.material.icons.rounded.Photo
import androidx.compose.material.icons.rounded.PhotoSizeSelectLarge
import androidx.compose.material.icons.rounded.PictureAsPdf
import androidx.compose.material.icons.rounded.Transform
import androidx.compose.material.icons.rounded.UnfoldLess
import androidx.compose.material.icons.rounded.ViewColumn
import com.example.pdf_img_tools_app.model.ToolCategory
import com.example.pdf_img_tools_app.model.ToolItem
import com.example.pdf_img_tools_app.navigation.AppDestinations

/**
 * Repository class for tool items
 */

class ToolRepository {
    /**
     * Get all tool items
     */
    fun getAllTools(): List<ToolItem> = pdfTools + imageTools
    
    /**
     * Get PDF tool items
     */
    fun getPdfTools(): List<ToolItem> = pdfTools
    
    /**
     * Get Image tool items
     */
    fun getImageTools(): List<ToolItem> = imageTools
    
    companion object {
        /**
         * PDF tools list
         */
        private val pdfTools = buildList{
            if (FeatureFlags.ENABLE_COMPRESS_PDF) {
                add(
                    ToolItem(
                        id = "compress_pdf",
                        name = "compress PDF",
                        description = "Reduce PDF file size while preserving quality",
                        icon = Icons.Rounded.Compress,
                        route = AppDestinations.COMPRESS_PDF,
                        category = ToolCategory.PDF
                    )
                )
            }
            if (FeatureFlags.ENABLE_MERGE_PDFS) {
                add(
                    ToolItem(
                        id = "merge_pdfs",
                        name = "Merge PDF",
                        description = "Combine multiple PDFs into one",
                        icon = Icons.Rounded.MergeType,
                        route = AppDestinations.MERGE_PDF,
                        category = ToolCategory.PDF
                    )
                )
            }
            if (FeatureFlags.ENABLE_SPLIT_PDF) {
                add(
                    ToolItem(
                        id = "split_pdf",
                        name = "Split PDF",
                        description = "Extract selected pages or ranges",
                        icon = Icons.Rounded.ViewColumn,
                        route = AppDestinations.SPLIT_PDF,
                        category = ToolCategory.PDF
                    )
                )
            }
            if (FeatureFlags.ENABLE_PDF_TO_IMAGES) {
                add(
                    ToolItem(
                        id = "pdf_to_images",
                        name = "Pdf to Images",
                        description = "Convert PDF pages to JPG or PNG",
                        icon = Icons.Rounded.Photo,
                        route = AppDestinations.PDF_TO_IMAGES,
                        category = ToolCategory.PDF
                    )
                )
            }
            if (FeatureFlags.ENABLE_IMAGES_TO_PDF) {
                add(
                    ToolItem(
                        id = "images_to_pdf",
                        name = "Images to PDF",
                        description = "Combine images into one PDF",
                        icon = Icons.Rounded.PictureAsPdf,
                        route = AppDestinations.IMAGES_TO_PDF,
                        category = ToolCategory.PDF
                    )
                )

            }
        }
        

        /**
         * Image tools list
         */
        private val imageTools = buildList {

            if (FeatureFlags.ENABLE_COMPRESS_IMAGES) {
                add(
                    ToolItem(
                        id = "compress_images",
                        name = "Compress Images",
                        description = "Reduce image size with adjustable quality",
                        icon = Icons.Rounded.UnfoldLess,
                        route = AppDestinations.COMPRESS_IMAGES,
                        category = ToolCategory.IMAGE
                    )
                )
            }
            if (FeatureFlags.ENABLE_RESIZE_IMAGES) {
                add(
                    ToolItem(
                        id = "resize_images",
                        name = "Batch Images Resizer",
                        description = "Change width and height while preserving aspect ratio",
                        icon = Icons.Rounded.Transform,
                        route = AppDestinations.RESIZE_IMAGES,
                        category = ToolCategory.IMAGE
                    )
                )
            }

            if (FeatureFlags.ENABLE_CONVERT_IMAGES) {
                add(
                    ToolItem(
                        id = "convert_images",
                        name = "Convert Image Format",
                        description = "Convert between JPG, PNG, and WebP",
                        icon = Icons.Rounded.Cached,
                        route = AppDestinations.CONVERT_IMAGES,
                        category = ToolCategory.IMAGE
                    )
                )
            }

            if (FeatureFlags.ENABLE_IMAGE_RESIZER) {
                add(
                    ToolItem(
                        id = "image_resizer",
                        name = "Image Resizer",
                        description = "Professional tool to resize a single image with templates",
                        icon = Icons.Rounded.PhotoSizeSelectLarge,
                        route = AppDestinations.IMAGE_RESIZER,
                        category = ToolCategory.IMAGE
                    )
                )
            }

        }
    }
} ```

### `app\src\main\java\com\example\pdf_img_tools_app\features\home\HomeScreen.kt`

```kt
package com.example.pdf_img_tools_app.features.home

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.HorizontalDivider
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.navigation.NavController
import com.example.pdf_img_tools_app.data.repository.ToolRepository
import com.example.pdf_img_tools_app.model.ToolItem
import com.example.pdf_img_tools_app.ui.components.BaseToolScreen
import com.example.pdf_img_tools_app.ui.components.ToolCard

/**
 * Home screen displaying all tool categories
 */

@Composable
fun HomeScreen(
    navController: NavController,
    isDarkTheme: Boolean,
    onThemeToggle: () -> Unit,
    modifier: Modifier = Modifier
){
    // Remember data sources to ensure stable references
    val toolRepository = remember { ToolRepository() }
    val pdfTools = remember { toolRepository.getPdfTools() }
    val imageTools = remember { toolRepository.getImageTools() }
    
    // Define scope key for this screen's messages
    val messageScope = "home"
    
    BaseToolScreen(
        title = "Toolkit",
        navController = navController,
        isDarkTheme = isDarkTheme,
        onThemeToggle = onThemeToggle,
        messageScope = messageScope,
        modifier = modifier,
        contentScrollable = true,
        showBackButton = false
    ) {
        // Content within BaseToolScreen
        Column(modifier = Modifier.fillMaxSize().padding(vertical = 0.dp)){

            Box(
                modifier = Modifier
                    .fillMaxWidth()
                    .background(
                        color = MaterialTheme.colorScheme.surface,
                        shape = MaterialTheme.shapes.extraLarge
                    )
            ){
                Column {
                    // PDF Tools Section
                    SectionHeader(
                        title = "Pdf tools",
                        color = MaterialTheme.colorScheme.onSurface,
                    )

                    HorizontalDivider(color = MaterialTheme.colorScheme.outline)

                    // Use a fixed layout for grid display instead of LazyVerticalGrid
                    FixedToolsGrid(
                        tools = pdfTools,
                        navController = navController, 
                        isDarkTheme = isDarkTheme,
                    )
                }
            }

            Spacer(modifier = Modifier.height(16.dp))

            Box(
                modifier = Modifier
                    .fillMaxWidth()
                    .background(
                        color = MaterialTheme.colorScheme.surface,
                        shape = MaterialTheme.shapes.extraLarge
                    )
            ){
                Column {
                    // Image Tools Section
                    SectionHeader(
                        title = "Image tools",
                        color = MaterialTheme.colorScheme.onSurface
                    )

                    HorizontalDivider(color = MaterialTheme.colorScheme.outline)

                    // Use a fixed layout for grid display
                    FixedToolsGrid(
                        tools = imageTools,
                        navController = navController,
                        isDarkTheme = isDarkTheme
                    )
                }
            }
        }
    }
}

/**
 * Section header with accent color
 */

@Composable
fun SectionHeader(
    title: String,
    color: androidx.compose.ui.graphics.Color,
    modifier: Modifier = Modifier.padding(12.dp)
) {
    Text(
        text = title,
        style = MaterialTheme.typography.titleMedium,
        color = color,
        fontWeight = FontWeight.Normal,
        modifier = modifier.padding(all = 8.dp).fillMaxWidth()
    )
}

/**
 * A fixed grid layout that displays tools in rows with 2 items per row
 */
@Composable
fun FixedToolsGrid(
    tools: List<ToolItem>,
    navController: NavController,
    isDarkTheme: Boolean,
    modifier: Modifier = Modifier // Add padding to control spacing
){
    Column(modifier = modifier.fillMaxWidth().padding(14.dp)) { // Add horizontal padding
        // Group tools into pairs and render each pair as a row
        tools.chunked(2).forEach { rowItems ->
            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(vertical = 6.dp), // Adjust vertical padding for rows
                horizontalArrangement = Arrangement.spacedBy(8.dp)
            ){
                rowItems.forEach { tool ->
                    Box(
                        modifier = Modifier.weight(1f)
                    ){
                        ToolCard(
                            toolItem = tool,
                            onClick = { navController.navigate(tool.route) },
                            isDarkTheme = isDarkTheme,
                        )
                    }
                }

                // If there's only one item in the row, add an empty spacer for the second slot
                if (rowItems.size == 1) {
                    Spacer(modifier = Modifier.weight(1f))
                }
            }
        }
    }
} ```

### `app\src\main\java\com\example\pdf_img_tools_app\features\image\compressimages\CompressImagesScreen.kt`

```kt
package com.example.pdf_img_tools_app.features.image.compressimages

import android.net.Uri
import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.selection.selectable
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Compress
import androidx.compose.material.icons.rounded.FileOpen
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.HorizontalDivider
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.RadioButton
import androidx.compose.material3.Slider
import androidx.compose.material3.SliderDefaults
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation.NavController
import com.example.pdf_img_tools_app.ui.components.BaseToolScreen
import com.example.pdf_img_tools_app.ui.components.FileBottomSheet
import com.example.pdf_img_tools_app.ui.components.FilePickerHandler
import com.example.pdf_img_tools_app.ui.components.OutputFileDetails
import com.example.pdf_img_tools_app.ui.components.ProgressToolButton
import com.example.pdf_img_tools_app.ui.components.ReusableSaveLocationSelector
import com.example.pdf_img_tools_app.ui.components.viewImage
import com.example.pdf_img_tools_app.utils.FileDetails

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

    BaseToolScreen(
        title = "Compress Images",
        navController = navController,
        isDarkTheme = isDarkTheme,
        onThemeToggle = onThemeToggle,
        contentScrollable = true,
        messageScope = "compress_images",
        modifier = modifier
    ) {
        Card(
            modifier = Modifier
                .fillMaxWidth()
                .padding(vertical = 8.dp),
            colors = CardDefaults.cardColors(
                containerColor = MaterialTheme.colorScheme.surface,
                contentColor = MaterialTheme.colorScheme.onSurface
            ),
            elevation = CardDefaults.cardElevation(defaultElevation = 1.dp),
            shape = RoundedCornerShape(24.dp)
        ) {
            Column(
                verticalArrangement = Arrangement.spacedBy(16.dp),
                modifier = Modifier.padding(24.dp)
            ) {
                HeaderSection()
                HorizontalDivider(color = MaterialTheme.colorScheme.outline)
                FileSelectionSection(uiState, viewModel, context, isDarkTheme)
                CompressionSettingsSection(uiState, viewModel, formatOptions)
                if (uiState.selectedImageUris.isNotEmpty()) {
                    SaveLocationSection(uiState, viewModel)
                }
                CompressButton(uiState, viewModel, context)
                OutputDetailsSection(uiState, viewModel, context, isDarkTheme)
            }
        }
        SelectedImagesBottomSheet(uiState, viewModel, context, isDarkTheme)
    }
}

@Composable
private fun HeaderSection() {
    Row(verticalAlignment = Alignment.CenterVertically) {
        Icon(Icons.Default.Compress, contentDescription = null, tint = MaterialTheme.colorScheme.primary, modifier = Modifier.size(32.dp))
        Spacer(modifier = Modifier.width(8.dp))
        Column {
            Text(text = "Compress Images", style = MaterialTheme.typography.titleMedium, color = MaterialTheme.colorScheme.primary)
            Text(text = "Reduce image file size by compressing", style = MaterialTheme.typography.bodySmall)
        }
    }
}

@Composable
private fun FileSelectionSection(uiState: CompressImagesUiState, viewModel: CompressImagesViewModel, context: android.content.Context, isDarkTheme: Boolean) {
    Column {
        Text(
            text = "Select Images",
            style = MaterialTheme.typography.bodyMedium,
            fontWeight = FontWeight.SemiBold
        )
        Spacer(modifier = Modifier.height(4.dp))
        Text(
            text = "Select one or more image files to compress",
            style = MaterialTheme.typography.bodySmall,
        )
        Spacer(modifier = Modifier.height(16.dp))
        FilePickerHandler(
            single = false,
            supportedMimeTypes = listOf("image/*"),
            onPicked = { uris -> viewModel.addImages(context, uris) }
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
                modifier = Modifier.fillMaxWidth()
            ) {
                Icon(
                    Icons.Rounded.FileOpen,
                    contentDescription = null,
                    modifier = Modifier.padding(end = 8.dp)
                )
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
            Text(
                text = "Selected Images Details",
                style = MaterialTheme.typography.bodyMedium,
                fontWeight = FontWeight.SemiBold,
            )
            Spacer(modifier = Modifier.height(16.dp))
            OutputFileDetails(
                file = summaryDetails,
                showSize = true,
                showFormat = true,
                onOpen = { viewModel.toggleSelectedImagesBottomSheet(true) },
                onDelete = { viewModel.clearAllImages() },
                isDarkTheme = isDarkTheme
            )
        }
    }
}

@Composable
private fun CompressionSettingsSection(uiState: CompressImagesUiState, viewModel: CompressImagesViewModel, formatOptions: List<String>) {
    Column {
        Text(
            text = "Compression Settings",
            style = MaterialTheme.typography.bodyMedium,
            fontWeight = FontWeight.SemiBold
        )
        Spacer(modifier = Modifier.height(8.dp))
        Text(text = "Output Format", style = MaterialTheme.typography.bodyMedium)
        Row(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.spacedBy(16.dp)
        ) {
            formatOptions.forEach { format ->
                Row(
                    modifier = Modifier
                        .selectable(
                            selected = (format == uiState.compressionFormat),
                            onClick = { viewModel.updateCompressionFormat(format) })
                        .padding(8.dp),
                    verticalAlignment = Alignment.CenterVertically
                ) {
                    RadioButton(
                        selected = (format == uiState.compressionFormat),
                        onClick = { viewModel.updateCompressionFormat(format) })
                    Text(
                        text = format,
                        style = MaterialTheme.typography.bodyMedium,
                        modifier = Modifier.padding(start = 4.dp)
                    )
                }
            }
        }
        Spacer(modifier = Modifier.height(8.dp))
        Text(
            text = "Compression Quality: ${uiState.compressionQuality.toInt()}%",
            style = MaterialTheme.typography.bodyMedium
        )
        Slider(
            value = uiState.compressionQuality,
            onValueChange = { viewModel.updateCompressionQuality(it) },
            valueRange = 10f..100f,
            steps = 17,
            colors = SliderDefaults.colors(
                thumbColor = MaterialTheme.colorScheme.primary,
                activeTrackColor = MaterialTheme.colorScheme.primary,
                activeTickColor = MaterialTheme.colorScheme.onPrimary,
            ),
        )
    }
}

@Composable
private fun SaveLocationSection(uiState: CompressImagesUiState, viewModel: CompressImagesViewModel) {
    ReusableSaveLocationSelector(
        visible = true,
        defaultSaveLocation = uiState.savePath,
        onSaveLocationChanged = { viewModel.updateSavePath(it) },
        saveModeEnabled = true,
        initialSaveMode = uiState.saveMode,
        onSaveModeChanged = { viewModel.updateSaveMode(it) }
    )
}

@Composable
private fun CompressButton(uiState: CompressImagesUiState, viewModel: CompressImagesViewModel, context: android.content.Context) {
    ProgressToolButton(
        onClick = { viewModel.compressImages(context, "compress_images") },
        isProcessing = uiState.isProcessing,
        progress = uiState.processingProgress,
        enabled = !uiState.isProcessing && uiState.selectedImageUris.isNotEmpty(),
        text = "Compress Images",
        icon = Icons.Default.Compress,
        errorMessage = if (uiState.isProcessing) null else uiState.errorMessage,
        onCancel = if (uiState.isProcessing) { { viewModel.cancelCompression() } } else null
    )
}

@Composable
private fun OutputDetailsSection(uiState: CompressImagesUiState, viewModel: CompressImagesViewModel, context: android.content.Context, isDarkTheme: Boolean) {
    if (uiState.outputDetailsList.isNotEmpty()) {
        val compressedTotal = uiState.outputDetailsList.sumOf { it.size }
        val summaryDetails = uiState.outputDetailsList.firstOrNull()?.copy(
            name = "${uiState.outputDetailsList.size} Images",
            size = compressedTotal
        )
        summaryDetails?.let {
            Text(
                text = "Selected Images Details",
                style = MaterialTheme.typography.bodyMedium,
                fontWeight = FontWeight.SemiBold,
            )
            OutputFileDetails(
                file = it,
                showSize = true,
                showFormat = true,
                onOpen = { viewModel.toggleAllImagesBottomSheet(true) },
                onDelete = { viewModel.clearOutputDetails() },
                isDarkTheme = isDarkTheme
            )
        }
    }
}

@Composable
private fun SelectedImagesBottomSheet(uiState: CompressImagesUiState, viewModel: CompressImagesViewModel, context: android.content.Context, isDarkTheme: Boolean) {
    FileBottomSheet(
        show = uiState.showSelectedImagesBottomSheet && uiState.selectedImageUris.isNotEmpty(),
        onDismiss = { viewModel.toggleSelectedImagesBottomSheet(false) },
        fileUris = uiState.selectedImageUris,
        title = "Selected Images",
        onFileRemove = { uri -> viewModel.removeImage(context, uri) },
        onClearAll = { viewModel.clearAllImages() },
        onFileView = { uri, mimeType -> viewImage(context, uri, mimeType ?: "image/*") },
        isDarkTheme = isDarkTheme
    )
}```

### `app\src\main\java\com\example\pdf_img_tools_app\features\image\compressimages\CompressImagesUiState.kt`

```kt
package com.example.pdf_img_tools_app.features.image.compressimages

import android.net.Uri
import com.example.pdf_img_tools_app.model.SaveMode
import com.example.pdf_img_tools_app.utils.FileDetails

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
)
```

### `app\src\main\java\com\example\pdf_img_tools_app\features\image\compressimages\CompressImagesViewModel.kt`

```kt
package com.example.pdf_img_tools_app.features.image.compressimages

import android.content.Context
import android.net.Uri
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.pdf_img_tools_app.model.SaveMode
import com.example.pdf_img_tools_app.service.ImageFormat
import com.example.pdf_img_tools_app.service.ImageService
import com.example.pdf_img_tools_app.utils.FileDetails
import com.example.pdf_img_tools_app.utils.FileUtils
import com.example.pdf_img_tools_app.utils.SaveLocationUtils
import com.example.pdf_img_tools_app.utils.UiMessageBus
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.Job
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import java.io.File
import java.io.FileOutputStream
import java.util.zip.ZipEntry
import java.util.zip.ZipOutputStream

/**
 * ViewModel for the Compress Images screen that handles business logic and state management
 */
class CompressImagesViewModel : ViewModel() {
    
    // The UI state exposed to the UI layer
    var uiState by mutableStateOf(CompressImagesUiState())
        private set
    
    // Reference to the current compression job
    private var compressionJob: Job? = null
    
    /**
     * Add images to the list
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
     * Clear all selected images
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
     * Update details for all selected images
     */
    private fun updateImageDetails(context: Context) {
        viewModelScope.launch {
            val detailsMap = mutableMapOf<Uri, FileDetails>()
            
            for (uri in uiState.selectedImageUris) {
                val details = FileUtils.getFileDetails(context, uri)
                if (details != null) {
                    detailsMap[uri] = details
                }
            }
            
            uiState = uiState.copy(imageDetailsMap = detailsMap)
        }
    }
    
    /**
     * Update the compression quality
     */
    fun updateCompressionQuality(quality: Float) {
        uiState = uiState.copy(compressionQuality = quality)
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
    fun updateSaveMode(saveMode: SaveMode) {
        uiState = uiState.copy(saveMode = saveMode)
    }
    
    /**
     * Update the compression format
     */
    fun updateCompressionFormat(format: String) {
        uiState = uiState.copy(compressionFormat = format)
    }
    
    /**
     * Toggle the selected images bottom sheet visibility
     */
    fun toggleSelectedImagesBottomSheet(show: Boolean) {
        uiState = uiState.copy(showSelectedImagesBottomSheet = show)
    }
    
    /**
     * Toggle the output images bottom sheet visibility
     */
    fun toggleAllImagesBottomSheet(show: Boolean) {
        uiState = uiState.copy(showAllImagesBottomSheet = show)
    }
    
    /**
     * Cancel the current compression job
     */
    fun cancelCompression() {
        compressionJob?.cancel()
        compressionJob = null
        
        uiState = uiState.copy(
            isProcessing = false,
            processingProgress = -1f
        )
    }
    
    /**
     * Clear output details
     */
    fun clearOutputDetails() {
        uiState = uiState.copy(outputDetailsList = emptyList())
    }
    
    /**
     * Compress the selected images
     */
    fun compressImages(context: Context, messageScope: String) {
        if (uiState.selectedImageUris.isEmpty()) {
            uiState = uiState.copy(errorMessage = "Please select at least one image")
            return
        }
        
        // Validate save location
        if (!SaveLocationUtils.validateSaveLocation(uiState.savePath)) {
            UiMessageBus.showError("Please specify a valid save location", messageScope)
            return
        }
        
        // Start processing
        uiState = uiState.copy(
            isProcessing = true,
            processingProgress = 0f,
            errorMessage = null,
            outputDetailsList = emptyList()
        )
        
        compressionJob = viewModelScope.launch {
            try {
                val imageService = ImageService(context)
                val totalImages = uiState.selectedImageUris.size
                var processedImages = 0
                val compressionQualityInt = uiState.compressionQuality.toInt()
                val outputDetails = mutableListOf<FileDetails>()
                
                // Process each image
                for (uri in uiState.selectedImageUris) {
                    if (!uiState.isProcessing) break // Check if cancelled
                    
                    val originalDetails = uiState.imageDetailsMap[uri]
                    if (originalDetails == null) {
                        processedImages++
                        uiState = uiState.copy(
                            processingProgress = processedImages.toFloat() / totalImages
                        )
                        continue
                    }
                    
                    try {
                        // Create a temporary file for the compressed image
                        val originalFileName = originalDetails.name
                        val fileExtension = if (uiState.compressionFormat == "JPEG") ".jpg" else ".png"
                        val tempFile = FileUtils.createTempFile(context, "compressed_${originalFileName}", fileExtension)
                        
                        if (tempFile == null) {
                            UiMessageBus.showError("Failed to create temporary file", messageScope)
                            processedImages++
                            uiState = uiState.copy(
                                processingProgress = processedImages.toFloat() / totalImages
                            )
                            continue
                        }
                        
                        // Compress the image
                        val imageFormat = ImageFormat.fromDisplayName(uiState.compressionFormat)
                        val result = imageService.convertImageFormat(
                            inputUri = uri,
                            outputFile = tempFile,
                            format = imageFormat,
                            quality = compressionQualityInt
                        )
                        
                        result.fold(
                            onSuccess = {
                                // Generate output filename
                                val outputFileName = "compressed_${originalFileName}${fileExtension}"
                                
                                // Save to chosen location
                                val savedUri = SaveLocationUtils.saveToLocation(
                                    sourceFile = tempFile,
                                    outputFileName = outputFileName,
                                    savePath = uiState.savePath,
                                    context = context,
                                    mimeType = "image/${uiState.compressionFormat.lowercase()}",
                                    saveMode = uiState.saveMode
                                )
                                
                                if (savedUri != null) {
                                    val fileDetails = FileUtils.getFileDetails(context, savedUri)
                                    if (fileDetails != null) {
                                        outputDetails.add(fileDetails)
                                    }
                                }
                                
                                // Clean up temp file
                                tempFile.delete()
                            },
                            onFailure = { error ->
                                UiMessageBus.showError(
                                    "Error compressing ${originalDetails.name}: ${error.message ?: "Unknown error"}",
                                    messageScope
                                )
                                tempFile.delete()
                            }
                        )
                    } catch (e: Exception) {
                        UiMessageBus.showError(
                            "Error compressing ${originalDetails.name}: ${e.message ?: "Unknown error"}",
                            messageScope
                        )
                    } finally {
                        processedImages++
                        uiState = uiState.copy(
                            processingProgress = processedImages.toFloat() / totalImages
                        )
                    }
                }
                
                // Update the UI with output details
                if (outputDetails.isNotEmpty()) {
                    uiState = uiState.copy(outputDetailsList = outputDetails)
                    
                    val originalTotal = uiState.imageDetailsMap.values.sumOf { it.size }
                    val compressedTotal = outputDetails.sumOf { it.size }
                    
                    if (compressedTotal < originalTotal) {
                        val savedPercentage = 100 - (compressedTotal * 100 / originalTotal)
                        UiMessageBus.showSuccess(
                            "Compressed ${outputDetails.size} images (${savedPercentage}% smaller)",
                            messageScope
                        )
                    } else {
                        UiMessageBus.showSuccess(
                            "Compressed ${outputDetails.size} images",
                            messageScope
                        )
                    }
                    
                    // If saveMode is ZIP_ARCHIVE, create a zip file with all the compressed images
                    if (uiState.saveMode == SaveMode.ZIP_ARCHIVE && outputDetails.size > 1) {
                        createZipFile(context, outputDetails, messageScope)
                    }
                } else {
                    UiMessageBus.showError("No images were compressed", messageScope)
                }
            } catch (e: Exception) {
                UiMessageBus.showError(
                    "Error: ${e.message ?: "Unknown error"}",
                    messageScope
                )
            } finally {
                uiState = uiState.copy(
                    isProcessing = false,
                    processingProgress = -1f
                )
                compressionJob = null
            }
        }
    }
    
    /**
     * Create a ZIP file containing all compressed images
     */
    private suspend fun createZipFile(context: Context, fileDetails: List<FileDetails>, messageScope: String) {
        try {
            // Create a temporary zip file
            val tempZipFile = FileUtils.createTempFile(context, "compressed_images", ".zip")
            if (tempZipFile == null) {
                UiMessageBus.showError("Failed to create ZIP file", messageScope)
                return
            }
            
            // Create a ZIP file with all the compressed images
            withContext(Dispatchers.IO) {
                ZipOutputStream(FileOutputStream(tempZipFile)).use { zipOut ->
                    for (fileDetail in fileDetails) {
                        try {
                            val inputStream = context.contentResolver.openInputStream(fileDetail.uri)
                            inputStream?.use { input ->
                                val zipEntry = ZipEntry(fileDetail.name)
                                zipOut.putNextEntry(zipEntry)
                                input.copyTo(zipOut)
                                zipOut.closeEntry()
                            }
                        } catch (e: Exception) {
                            UiMessageBus.showError(
                                "Error adding ${fileDetail.name} to ZIP: ${e.message ?: "Unknown error"}",
                                messageScope
                            )
                        }
                    }
                }
            }
            
            // Save the ZIP file to the chosen location
            val zipFileName = "compressed_images_${System.currentTimeMillis()}.zip"
            val savedUri = SaveLocationUtils.saveToLocation(
                context = context,
                sourceFile = tempZipFile,
                outputFileName = zipFileName,
                mimeType = "application/zip",
                savePath = uiState.savePath,
                saveMode = SaveMode.SEPARATELY
            )
            
            if (savedUri != null) {
                val zipDetails = FileUtils.getFileDetails(context, savedUri)
                if (zipDetails != null) {
                    UiMessageBus.showSuccess(
                        "Created ZIP file with ${fileDetails.size} compressed images",
                        messageScope
                    )
                }
            } else {
                UiMessageBus.showError("Failed to save ZIP file", messageScope)
            }
            
            // Clean up temp file
            tempZipFile.delete()
        } catch (e: Exception) {
            UiMessageBus.showError(
                "Error creating ZIP file: ${e.message ?: "Unknown error"}",
                messageScope
            )
        }
    }
}
```

### `app\src\main\java\com\example\pdf_img_tools_app\features\image\convertimages\ConvertImagesScreen.kt`

```kt
package com.example.pdf_img_tools_app.features.image.convertimages

import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.KeyboardArrowDown
import androidx.compose.material.icons.filled.KeyboardArrowUp
import androidx.compose.material.icons.filled.Transform
import androidx.compose.material.icons.rounded.Cached
import androidx.compose.material.icons.rounded.FileOpen
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.Divider
import androidx.compose.material3.DropdownMenu
import androidx.compose.material3.DropdownMenuItem
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.ExposedDropdownMenuBox
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Slider
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation.NavController
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.material3.HorizontalDivider
import androidx.compose.material3.SliderDefaults
import com.example.pdf_img_tools_app.service.ImageFormat
import com.example.pdf_img_tools_app.ui.components.BaseToolScreen
import com.example.pdf_img_tools_app.ui.components.FilePickerHandler
import com.example.pdf_img_tools_app.ui.components.OutputFileDetails
import com.example.pdf_img_tools_app.ui.components.ProgressToolButton
import com.example.pdf_img_tools_app.ui.components.ReusableSaveLocationSelector
import com.example.pdf_img_tools_app.ui.components.viewImage


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

    BaseToolScreen(
        title = "Convert Images",
        navController = navController,
        isDarkTheme = isDarkTheme,
        onThemeToggle = onThemeToggle,
        contentScrollable = true,
        messageScope = "convert_images",
        modifier = modifier
    ) {
        Card(
            modifier = Modifier
                .fillMaxWidth()
                .padding(vertical = 8.dp),
            colors = CardDefaults.cardColors(
                containerColor = MaterialTheme.colorScheme.surface,
                contentColor = MaterialTheme.colorScheme.onSurface
            ),
            elevation = CardDefaults.cardElevation(defaultElevation = 1.dp),
            shape = RoundedCornerShape(24.dp)
        ) {
            Column(
                verticalArrangement = Arrangement.spacedBy(16.dp),
                modifier = Modifier.padding(24.dp)
            ) {
                HeaderSection()
                HorizontalDivider(color = MaterialTheme.colorScheme.outline)
                FileSelectionSection(uiState, viewModel, context, isDarkTheme)
                ConversionSettingsSection(uiState, viewModel)
                if (uiState.originalImageDetails != null) {
                    SaveLocationSection(uiState, viewModel)
                }
                ConvertButton(uiState, viewModel, context)
                OutputDetailsSection(uiState, viewModel, context, isDarkTheme)
            }
        }
    }
}


@Composable
private fun HeaderSection() {
    Row(verticalAlignment = Alignment.CenterVertically) {
        Icon(Icons.Rounded.Cached, contentDescription = null, tint = MaterialTheme.colorScheme.primary, modifier = Modifier.size(32.dp))
        Spacer(modifier = Modifier.width(8.dp))
        Column {
            Text("Convert Image Format", style = MaterialTheme.typography.titleMedium, color = MaterialTheme.colorScheme.primary)
            Text("Change image file format and quality", style = MaterialTheme.typography.bodySmall)
        }
    }
}

@Composable
private fun FileSelectionSection(uiState: ConvertImagesUiState, viewModel: ConvertImagesViewModel, context: android.content.Context, isDarkTheme: Boolean) {
    Column {
        Text(
            text = "Select Image",
            style = MaterialTheme.typography.bodyMedium,
            fontWeight = FontWeight.SemiBold,
        )
        Spacer(modifier = Modifier.height(4.dp))
        Text(
            text = "Select image for change format Ex: 'jpg' to 'png'",
            style = MaterialTheme.typography.bodySmall,
        )
        Spacer(modifier = Modifier.height(16.dp))
        FilePickerHandler(
            single = true,
            supportedMimeTypes = listOf("image/*"),
            onPicked = { uris -> uris.firstOrNull()?.let { viewModel.selectImage(context, it) } }
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
                modifier = Modifier.fillMaxWidth().padding(vertical = 0.dp)
            ) {
                Icon(
                    Icons.Rounded.FileOpen,
                    contentDescription = null,
                    modifier = Modifier.padding(end = 8.dp)
                )
                Text(text = "Select Image")
            }
        }
        uiState.originalImageDetails?.let { details ->
            Spacer(modifier = Modifier.height(16.dp))
            Text(
                text = "Selected Images Details",
                style = MaterialTheme.typography.bodyMedium,
                fontWeight = FontWeight.SemiBold,
            )
            Spacer(modifier = Modifier.height(16.dp))
            OutputFileDetails(
                file = details,
                showName = true,
                showSize = true,
                showFormat = true,
                showDimensions = true,
                onOpen = { viewImage(context, details.uri, details.mimeType) },
                onDelete = { viewModel.clearSelectedImage() },
                isDarkTheme = isDarkTheme
            )
        }
    }
}

@Composable
private fun ConversionSettingsSection(uiState: ConvertImagesUiState, viewModel: ConvertImagesViewModel) {
    Column {
        Text(
            text = "Conversion Settings",
            style = MaterialTheme.typography.bodyMedium,
            fontWeight = FontWeight.SemiBold
        )
        Spacer(modifier = Modifier.height(8.dp))
        FormatDropdown(uiState, viewModel)
        if (uiState.selectedFormat.supportsQuality) {
            Spacer(modifier = Modifier.height(16.dp))
            QualitySlider(uiState, viewModel)
        }
    }
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
private fun FormatDropdown(uiState: ConvertImagesUiState, viewModel: ConvertImagesViewModel) {
    Column {
        Text(text = "Output Format", style = MaterialTheme.typography.bodyMedium)
        Spacer(modifier = Modifier.padding(bottom = 8.dp))
        ExposedDropdownMenuBox(
            expanded = uiState.formatMenuExpanded,
            onExpandedChange = { viewModel.toggleFormatMenu(!uiState.formatMenuExpanded) },
            modifier = Modifier.fillMaxWidth() // Ensure the dropdown box respects the card's width
        ) {
            OutlinedTextField(
                readOnly = true,
                value = uiState.selectedFormat.displayName, // Display the selected format
                onValueChange = {},
                trailingIcon = {
                    Icon(
                        if (uiState.formatMenuExpanded) Icons.Default.KeyboardArrowUp else Icons.Default.KeyboardArrowDown,
                        contentDescription = null
                    )
                },
                modifier = Modifier
                    .menuAnchor()
                    .fillMaxWidth()
            )
            DropdownMenu(
                expanded = uiState.formatMenuExpanded,
                onDismissRequest = { viewModel.toggleFormatMenu(false) },
                modifier = Modifier
                    // Match the width of the text field
                    .padding(horizontal = 16.dp) // Add padding to prevent overflow
            ) {
                ImageFormat.values().forEach { format ->
                    DropdownMenuItem(
                        text = { Text(format.displayName) },
                        onClick = {
                            viewModel.updateSelectedFormat(format) // Update the selected format
                            viewModel.toggleFormatMenu(false) // Close the dropdown
                        },
                    )
                }
            }
        }
    }
}

@Composable
private fun QualitySlider(uiState: ConvertImagesUiState, viewModel: ConvertImagesViewModel) {
    Column {
        Text("Quality: ${uiState.quality.toInt()}%", style = MaterialTheme.typography.bodyMedium)
        Spacer(modifier = Modifier.height(8.dp))
        Slider(
            value = uiState.quality,
            onValueChange = { viewModel.updateQuality(it) },
            valueRange = 10f..100f,
            steps = 8,
            modifier = Modifier.padding(vertical = 8.dp),
            colors = SliderDefaults.colors(
                thumbColor = MaterialTheme.colorScheme.primary,
                activeTrackColor = MaterialTheme.colorScheme.primary,
                activeTickColor = MaterialTheme.colorScheme.onPrimary,
            )
        )
    }
}

@Composable
private fun SaveLocationSection(uiState: ConvertImagesUiState, viewModel: ConvertImagesViewModel) {
    ReusableSaveLocationSelector(
        visible = true,
        defaultSaveLocation = uiState.savePath,
        onSaveLocationChanged = { viewModel.updateSavePath(it) },
        saveModeEnabled = true,
        initialSaveMode = uiState.saveMode,
        onSaveModeChanged = { viewModel.updateSaveMode(it) }
    )
}

@Composable
private fun ConvertButton(uiState: ConvertImagesUiState, viewModel: ConvertImagesViewModel, context: android.content.Context) {
    ProgressToolButton(
        onClick = { viewModel.convertImage(context, "convert_images") },
        isProcessing = uiState.isProcessing,
        progress = uiState.processingProgress,
        enabled = !uiState.isProcessing && uiState.selectedImageUri != null,
        text = "Convert Image",
        icon = Icons.Default.Transform
    )
}

@Composable
private fun OutputDetailsSection(uiState: ConvertImagesUiState, viewModel: ConvertImagesViewModel, context: android.content.Context, isDarkTheme: Boolean) {
    uiState.outputDetails?.let { details ->
        Text(
            text = "Compressed Images Details",
            style = MaterialTheme.typography.bodyMedium,
            fontWeight = FontWeight.SemiBold,
        )
        OutputFileDetails(
            file = details,
            showName = true,
            showSize = true,
            showFormat = true,
            showDimensions = true,
            onOpen = { viewImage(context, details.uri, details.mimeType) },
            onDelete = { viewModel.clearOutputDetails() },
            isDarkTheme = isDarkTheme
        )
    }
}```

### `app\src\main\java\com\example\pdf_img_tools_app\features\image\convertimages\ConvertImagesUiState.kt`

```kt
package com.example.pdf_img_tools_app.features.image.convertimages

import android.net.Uri
import com.example.pdf_img_tools_app.model.SaveMode
import com.example.pdf_img_tools_app.service.ImageFormat
import com.example.pdf_img_tools_app.utils.FileDetails

/**
 * Data class representing the UI state for the Convert Images screen
 */
data class ConvertImagesUiState(
    val selectedImageUri: Uri? = null,
    val originalImageDetails: FileDetails? = null,
    val formatMenuExpanded: Boolean = false,
    val selectedFormat: ImageFormat = ImageFormat.JPG,
    val quality: Float = 90f,
    val isProcessing: Boolean = false,
    val processingProgress: Float = -1f,
    val outputDetails: FileDetails? = null,
    val savePath: String = "Downloads",
    val saveMode: SaveMode = SaveMode.SEPARATELY,
    val errorMessage: String? = null
)
```

### `app\src\main\java\com\example\pdf_img_tools_app\features\image\convertimages\ConvertImagesViewModel.kt`

```kt
package com.example.pdf_img_tools_app.features.image.convertimages

import android.content.Context
import android.net.Uri
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.pdf_img_tools_app.model.SaveMode
import com.example.pdf_img_tools_app.service.ImageFormat
import com.example.pdf_img_tools_app.service.ImageService
import com.example.pdf_img_tools_app.utils.FileDetails
import com.example.pdf_img_tools_app.utils.FileUtils
import com.example.pdf_img_tools_app.utils.SaveLocationUtils
import com.example.pdf_img_tools_app.utils.UiMessageBus
import kotlinx.coroutines.launch
import java.io.File
import java.io.IOException
import java.text.SimpleDateFormat
import java.util.Date
import java.util.Locale

/**
 * ViewModel for the Convert Images screen that handles business logic and state management
 */
class ConvertImagesViewModel : ViewModel() {
    
    // The UI state exposed to the UI layer
    var uiState by mutableStateOf(ConvertImagesUiState())
        private set
    
    /**
     * Select an image to convert
     */
    fun selectImage(context: Context, uri: Uri) {
        // Update image details
        val details = FileUtils.getFileDetails(context, uri)
        
        uiState = uiState.copy(
            selectedImageUri = uri,
            originalImageDetails = details,
            outputDetails = null
        )
    }
    
    /**
     * Update the selected format
     */
    fun updateSelectedFormat(format: ImageFormat) {
        uiState = uiState.copy(selectedFormat = format)
    }
    
    /**
     * Toggle the format menu expansion state
     */
    fun toggleFormatMenu(expanded: Boolean) {
        uiState = uiState.copy(formatMenuExpanded = expanded)
    }
    
    /**
     * Update the quality value
     */
    fun updateQuality(quality: Float) {
        uiState = uiState.copy(quality = quality)
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
    fun updateSaveMode(saveMode: SaveMode) {
        uiState = uiState.copy(saveMode = saveMode)
    }
    
    /**
     * Clear output details
     */
    fun clearOutputDetails() {
        uiState = uiState.copy(outputDetails = null)
    }
    
    /**
     * Clear selected image
     */
    fun clearSelectedImage() {
        uiState = uiState.copy(
            selectedImageUri = null,
            originalImageDetails = null
        )
    }
    
    /**
     * Cancel the current processing
     */
    fun cancelProcessing() {
        uiState = uiState.copy(
            isProcessing = false,
            processingProgress = -1f
        )
    }
    
    /**
     * Convert the selected image
     */
    fun convertImage(context: Context, messageScope: String) {
        val selectedUri = uiState.selectedImageUri
        if (selectedUri == null) {
            uiState = uiState.copy(errorMessage = "Please select an image first")
            return
        }
        
        // Validate save location
        if (!SaveLocationUtils.validateSaveLocation(uiState.savePath)) {
            UiMessageBus.showError("Please specify a valid save location", messageScope)
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
                // Get image details
                val details = uiState.originalImageDetails ?: FileUtils.getFileDetails(context, selectedUri)
                if (details == null) {
                    UiMessageBus.showError("Could not get image details", messageScope)
                    uiState = uiState.copy(isProcessing = false)
                    return@launch
                }
                
                // Create output filename
                val originalExtension = details.name.substringAfterLast('.', "")
                val newExtension = uiState.selectedFormat.extension
                val outputFileName = details.name.replace(originalExtension, newExtension)
                
                // Create a temporary file for output
                val tempOutputFile = FileUtils.createTempFile(
                    context, 
                    "converted_${System.currentTimeMillis()}", 
                    ".${newExtension}"
                )
                
                if (tempOutputFile == null) {
                    UiMessageBus.showError("Could not create temporary file", messageScope)
                    uiState = uiState.copy(isProcessing = false)
                    return@launch
                }
                
                // Convert image
                val imageService = ImageService(context)
                val result = imageService.convertImageFormat(
                    inputUri = selectedUri,
                    outputFile = tempOutputFile,
                    format = uiState.selectedFormat,
                    quality = uiState.quality.toInt()
                )
                
                result.fold(
                    onSuccess = {
                        // Generate a filename with date
                        val dateFormat = SimpleDateFormat("yyyyMMdd_HHmmss", Locale.getDefault())
                        val dateString = dateFormat.format(Date())
                        val safeOutputFileName = "converted_${dateString}.${newExtension}"
                        
                        // Save to chosen location
                        val savedUri = SaveLocationUtils.saveToLocation(
                            context = context,
                            sourceFile = tempOutputFile,
                            outputFileName = safeOutputFileName,
                            mimeType = "image/${newExtension}",
                            savePath = uiState.savePath,
                            saveMode = uiState.saveMode
                        )
                        
                        if (savedUri != null) {
                            val outputDetails = FileUtils.getFileDetails(context, savedUri)
                            uiState = uiState.copy(outputDetails = outputDetails)
                            
                            // Calculate size change for user feedback
                            val originalSize = details.size
                            val convertedSize = outputDetails?.size ?: 0L
                            if (originalSize > 0 && convertedSize > 0) {
                                val sizeChange = (1 - (convertedSize.toFloat() / originalSize)).coerceIn(-1f, 1f)
                                val sizeChangeText = if (sizeChange >= 0) {
                                    "${(sizeChange * 100).toInt()}% smaller"
                                } else {
                                    "${(-sizeChange * 100).toInt()}% larger"
                                }
                                
                                UiMessageBus.showSuccess(
                                    "Image converted successfully: $sizeChangeText",
                                    messageScope
                                )
                            } else {
                                UiMessageBus.showSuccess(
                                    "Image converted successfully",
                                    messageScope
                                )
                            }
                        } else {
                            UiMessageBus.showError("Failed to save converted image", messageScope)
                        }
                        
                        // Clean up temp file
                        tempOutputFile.delete()
                    },
                    onFailure = { error ->
                        UiMessageBus.showError(
                            "Error: ${error.message ?: "Unknown error"}",
                            messageScope
                        )
                        tempOutputFile.delete()
                    }
                )
            } catch (e: IOException) {
                UiMessageBus.showError("IO Error: ${e.message}", messageScope)
            } catch (e: Exception) {
                UiMessageBus.showError("Error: ${e.message}", messageScope)
            } finally {
                uiState = uiState.copy(
                    isProcessing = false,
                    processingProgress = -1f
                )
            }
        }
    }
}
```

### `app\src\main\java\com\example\pdf_img_tools_app\features\image\imageresizer\ImageResizerScreen.kt`

```kt
package com.example.pdf_img_tools_app.features.image.imageresizer

import android.Manifest
import android.annotation.SuppressLint
import android.net.Uri
import android.os.Build
import com.example.pdf_img_tools_app.ui.components.CheckerboardBackground
import com.example.pdf_img_tools_app.ui.components.DetailRow
import com.example.pdf_img_tools_app.ui.components.ImageCanvas
import com.example.pdf_img_tools_app.ui.components.ImageCanvasState
import com.example.pdf_img_tools_app.ui.components.formatFileSize
import com.example.pdf_img_tools_app.ui.components.viewFile
import com.example.pdf_img_tools_app.service.ImageFormat
// FileExtraDetails import removed
import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.aspectRatio
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Add
import androidx.compose.material.icons.filled.Close
import androidx.compose.material.icons.filled.Done
import androidx.compose.material.icons.filled.PhotoCamera
import androidx.compose.material.icons.filled.Save
import androidx.compose.material.icons.outlined.Image
import androidx.compose.material3.Button
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.DropdownMenuItem
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.ExposedDropdownMenuBox
import androidx.compose.material3.ExposedDropdownMenuDefaults
import androidx.compose.material3.ModalBottomSheet
import androidx.compose.material3.rememberModalBottomSheetState
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Scaffold
import com.example.pdf_img_tools_app.ui.components.SmartMessageDisplay
import androidx.compose.material3.Switch
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.rememberCoroutineScope
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.asImageBitmap
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation.NavController
import com.example.pdf_img_tools_app.features.image.imageresizer.ImageResizerViewModel
import com.google.accompanist.permissions.ExperimentalPermissionsApi
import com.google.accompanist.permissions.isGranted
import com.google.accompanist.permissions.rememberPermissionState
import com.google.accompanist.permissions.shouldShowRationale
import com.example.pdf_img_tools_app.ui.components.OutputFileDetails
import com.example.pdf_img_tools_app.utils.FileDetails
import com.example.pdf_img_tools_app.ui.components.AppTopBar
import com.example.pdf_img_tools_app.model.SaveLocationType
import com.example.pdf_img_tools_app.utils.UiMessageBus
import kotlinx.coroutines.launch
import androidx.compose.runtime.DisposableEffect
import com.example.pdf_img_tools_app.ui.components.BaseToolScreen

@SuppressLint("UnusedMaterial3ScaffoldPaddingParameter")
@OptIn(ExperimentalMaterial3Api::class, ExperimentalPermissionsApi::class)
@Composable
fun ImageResizerScreen(
    navController: NavController,
    isDarkTheme: Boolean,
    onThemeToggle: () -> Unit,
    modifier: Modifier = Modifier
) {
    val context = LocalContext.current
    val viewModel: ImageResizerViewModel = viewModel()
    val coroutineScope = rememberCoroutineScope()
    
    // Define scope key for this screen's messages
    val messageScope = "image_resizer"
    val scrollState = rememberScrollState()
    
    // Preview image bottom sheet state
    var showPreviewSheet by remember { mutableStateOf(false) }
    
    // Permission state for storage access (only needed for API < 29)
    val storagePermissionState = if (Build.VERSION.SDK_INT < Build.VERSION_CODES.Q) {
        rememberPermissionState(Manifest.permission.WRITE_EXTERNAL_STORAGE)
    } else null
    
    // Image picker launcher
    val imagePickerLauncher = rememberLauncherForActivityResult(
        contract = ActivityResultContracts.GetContent()
    ) { uri: Uri? ->
        uri?.let {
            viewModel.setSelectedImage(context, it)
        }
    }
    
    // Using coroutineScope instead of LaunchedEffect to handle events
    val scope = rememberCoroutineScope()
    
    // Register an event collector when the component is first created
    DisposableEffect(Unit) {
        val job = scope.launch {
            viewModel.eventFlow.collect { event ->
                when (event) {
                    is ImageResizerViewModel.UiEvent.ShowError -> {
                        UiMessageBus.showError(event.message, messageScope)
                    }
                    is ImageResizerViewModel.UiEvent.ShowSuccess -> {
                        UiMessageBus.showSuccess(event.message, messageScope)
                    }
                }
            }
        }
        
        // Clean up when the component is disposed
        onDispose {
            job.cancel()
        }
    }
    
    // ViewModel properties for save location
    val saveLocationType = SaveLocationType.DOWNLOADS
    val customSaveLocationUri: Uri? = null
    val isProcessing = false
    val processingProgress = 0f
    
    // Enhanced FileBottomSheet for image preview with metadata
    if (showPreviewSheet && (viewModel.previewResizedBitmap != null || viewModel.previewBitmap != null)) {
        val previewImageUri = if (viewModel.resizeComplete && viewModel.resizedImage?.resizedImageFile != null) {
            Uri.fromFile(viewModel.resizedImage?.resizedImageFile)
        } else {
            viewModel.selectedImageUri
        }
        
        if (previewImageUri != null) {
            ModalBottomSheet(
                onDismissRequest = { showPreviewSheet = false },
                sheetState = rememberModalBottomSheetState()
            ) {
                Column(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(16.dp),
                    horizontalAlignment = Alignment.CenterHorizontally
                ) {
                    // Title with close button
                    Row(
                        modifier = Modifier.fillMaxWidth(),
                        horizontalArrangement = Arrangement.SpaceBetween,
                        verticalAlignment = Alignment.CenterVertically
                    ) {
                        Text(
                            text = "Image Preview",
                            style = MaterialTheme.typography.titleMedium,
                            fontWeight = FontWeight.Bold
                        )
                        
                        IconButton(onClick = { showPreviewSheet = false }) {
                            Icon(Icons.Default.Close, contentDescription = "Close")
                        }
                    }
                    
                    Spacer(modifier = Modifier.height(16.dp))
                    
                    // Image preview at actual dimensions (constrained to screen)
                    val imageModifier = if (viewModel.resizeComplete && viewModel.resizedImage != null) {
                        // For resized images, respect the actual dimensions
                        val imageWidth = viewModel.resizedImage?.width ?: 0
                        val imageHeight = viewModel.resizedImage?.height ?: 0
                        val aspectRatio = if (imageHeight > 0) imageWidth.toFloat() / imageHeight.toFloat() else 1f
                        
                        Modifier
                            .fillMaxWidth(0.8f)
                            .aspectRatio(aspectRatio)
                            .clip(RoundedCornerShape(8.dp))
                            .border(1.dp, MaterialTheme.colorScheme.outline, RoundedCornerShape(8.dp))
                    } else {
                        Modifier
                            .fillMaxWidth(0.8f)
                            .aspectRatio(1f)
                            .clip(RoundedCornerShape(8.dp))
                            .border(1.dp, MaterialTheme.colorScheme.outline, RoundedCornerShape(8.dp))
                    }
                    
                    // Display the appropriate bitmap
                    val bitmap = if (viewModel.resizeComplete && viewModel.previewResizedBitmap != null) {
                        viewModel.previewResizedBitmap
                    } else {
                        viewModel.previewBitmap
                    }
                    
                    bitmap?.asImageBitmap()?.let {
                        Image(
                            bitmap = it,
                            contentDescription = "Preview Image",
                            modifier = imageModifier,
                            contentScale = ContentScale.Fit
                        )
                    }

                    Spacer(modifier = Modifier.height(8.dp))
                    
                    // Metadata display
                    if (viewModel.resizeComplete && viewModel.resizedImage != null) {
                        val resized = viewModel.resizedImage!!
                        
                        // File details card
                        Card(
                            modifier = Modifier.fillMaxWidth(),
                            colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surfaceVariant)
                        ) {
                            Column(modifier = Modifier.padding(16.dp)) {
                                Text(
                                    text = "Image Details",
                                    style = MaterialTheme.typography.titleSmall,
                                    fontWeight = FontWeight.Bold
                                )
                                
                                Spacer(modifier = Modifier.height(8.dp))
                                
                                // Dimensions
                                DetailRow(
                                    icon = Icons.Default.PhotoCamera,
                                    label = "Dimensions",
                                    value = "${resized.width} × ${resized.height} px"
                                )
                                
                                Spacer(modifier = Modifier.height(4.dp))
                                
                                // Format
                                DetailRow(
                                    icon = Icons.Default.PhotoCamera,
                                    label = "Format",
                                    value = resized.format.displayName
                                )
                                
                                Spacer(modifier = Modifier.height(4.dp))
                                
                                // Size
                                DetailRow(
                                    icon = Icons.Default.Save,
                                    label = "File Size",
                                    value = formatFileSize(resized.sizeAfter)
                                )
                                
                                Spacer(modifier = Modifier.height(4.dp))
                                
                                // Reduction
                                val reduction = if (resized.sizeBefore > 0) {
                                    val percent = (resized.sizeBefore - resized.sizeAfter).toFloat() / resized.sizeBefore * 100
                                    String.format("%.1f%% reduction", percent)
                                } else {
                                    "N/A"
                                }
                                
                                DetailRow(
                                    icon = Icons.Default.Save,
                                    label = "Size Reduction",
                                    value = reduction
                                )
                            }
                        }
                        
                        Spacer(modifier = Modifier.height(16.dp))
                        
                        // Action button to view in full screen
                        Button(
                            onClick = {
                                val uri = Uri.fromFile(resized.resizedImageFile)
                                val mimeType = "image/${resized.format.extension}"
                                viewFile(context, uri, mimeType)
                            },
                            modifier = Modifier.fillMaxWidth(0.8f)
                        ) {
                            Icon(
                                imageVector = Icons.Default.PhotoCamera,
                                contentDescription = null,
                                modifier = Modifier.padding(end = 8.dp)
                            )
                            Text("View Full Image")
                        }
                    }
                }
            }
        }
    }
    
    // Add error message state
    var errorMessage by remember { mutableStateOf<String?>(null) }
    
    BaseToolScreen(
        title = "Image Resizer",
        navController = navController,
        isDarkTheme = isDarkTheme,
        onThemeToggle = onThemeToggle,
        messageScope = messageScope,
        isLoading = viewModel.isLoading,
        contentScrollable = true,
        modifier = Modifier
    ) {
        Card(
            modifier = Modifier
                .fillMaxWidth().padding(vertical = 8.dp),
            colors = CardDefaults.cardColors(
                containerColor = MaterialTheme.colorScheme.surface,
                contentColor = MaterialTheme.colorScheme.onSurfaceVariant
            ),
            elevation = CardDefaults.cardElevation(defaultElevation = 1.dp),
            shape = RoundedCornerShape(24.dp)
        ){
            Column(
                modifier = Modifier
                    .fillMaxSize()
                    .padding(0.dp)
                    .background(MaterialTheme.colorScheme.surface, shape = MaterialTheme.shapes.extraLarge),
                verticalArrangement = Arrangement.spacedBy(16.dp)
            ){
                // BaseToolScreen already handles the SmartMessageDisplay component

                // Image selection area
                ImageSelectionArea(
                    previewBitmap = viewModel.previewBitmap,
                    isLoading = viewModel.isLoading,
                    onSelectImage = {
                        imagePickerLauncher.launch("image/*")
                    },
                    onClearImage = {
                        viewModel.clearSelectedImage()
                    },
                    viewModel = viewModel
                )

                // Always show resizing options
                ResizeOptionsArea(
                    width = viewModel.width,
                    onWidthChange = { viewModel.updateWidth(it) },
                    height = viewModel.height,
                    onHeightChange = { viewModel.updateHeight(it) },
                    templateOptions = viewModel.templateOptions,
                    selectedTemplate = viewModel.selectedTemplate.displayName,
                    onTemplateSelected = { viewModel.setTemplate(it) },
                    formatOptions = viewModel.formatOptions,
                    selectedFormat = viewModel.selectedFormat.displayName,
                    onFormatSelected = { viewModel.setFormat(it) },
                    maintainAspectRatio = viewModel.maintainAspectRatio,
                    onToggleAspectRatio = { viewModel.toggleMaintainAspectRatio() },
                    originalWidth = viewModel.originalWidth,
                    originalHeight = viewModel.originalHeight,
                    onResize = {
                        if (Build.VERSION.SDK_INT < Build.VERSION_CODES.Q &&
                            storagePermissionState != null &&
                            !storagePermissionState.status.isGranted
                        ) {
                            // Request permission for older Android versions
                            storagePermissionState.launchPermissionRequest()
                        } else {
                            viewModel.resizeImage(context)
                        }
                    },
                    isImageSelected = viewModel.selectedImageUri != null,
                    isResizing = viewModel.isLoading
                )

                Spacer(modifier = Modifier.height(16.dp))

                // Display error message if any
                errorMessage?.let {
                    Spacer(modifier = Modifier.height(16.dp))

                    UiMessageBus.showError(it, messageScope)
                    errorMessage = null  // Clear after showing

                    Spacer(modifier = Modifier.height(16.dp))
                }

                // Show permission rationale if needed
                if (Build.VERSION.SDK_INT < Build.VERSION_CODES.Q &&
                    storagePermissionState != null &&
                    !storagePermissionState.status.isGranted &&
                    storagePermissionState.status.shouldShowRationale
                ) {
                    Spacer(modifier = Modifier.height(16.dp))
                    PermissionRationaleCard()
                }

                // Always show the output file details section (but it will be empty if no resized image)
                if (viewModel.resizeComplete && viewModel.resizedImage != null && viewModel.resizedImage?.resizedImageFile != null) {
                    val resizedImageUri = Uri.fromFile(viewModel.resizedImage?.resizedImageFile)
                    val fileDetails = FileDetails(
                        uri = resizedImageUri,
                        name = viewModel.resizedImage?.resizedImageFile?.name ?: "Resized Image",
                        path = viewModel.resizedImage?.resizedImageFile?.parent,
                        size = viewModel.resizedImage?.sizeAfter ?: 0L,
                        mimeType = "image/jpeg", // Adjust based on actual format
                        dimensions = Pair(viewModel.resizedImage?.width ?: 0, viewModel.resizedImage?.height ?: 0)
                    )

                    val additionalDetails = mutableMapOf<String, String>()
                    viewModel.resizedImage?.let { resized ->
                        additionalDetails["Original Size"] = formatFileSize(resized.sizeBefore)
                    }

                    // Create label overrides map
                    val labelOverrides = mutableMapOf<String, String>(
                        "format" to "Format",
                        "size" to "Size",
                        "dimensions" to "Dimensions"
                    )
                    
                    // Add any additional details to the label map
                    additionalDetails.forEach { (key, _) ->
                        labelOverrides[key.lowercase()] = key
                    }
                    
                    // Get compression info if available
                    val compressionInfo = viewModel.resizedImage?.let { 
                        if (it.sizeBefore > 0 && it.sizeAfter > 0) {
                            Pair(it.sizeBefore, it.sizeAfter)
                        } else null
                    }
                    
                    OutputFileDetails(
                        modifier = Modifier.padding(8.dp),
                        file = fileDetails,
                        showName = true,
                        showSize = true,
                        showFormat = true,
                        showDimensions = true,
                        showCompression = compressionInfo != null,
                        compressionInfo = compressionInfo,
                        labelOverrides = labelOverrides,
                        onOpen = {
                            // Show the preview bottom sheet
                            showPreviewSheet = true
                        },
                        onShare = null,
                        onDelete = {
                            // Reset the resize process
                            viewModel.resetResize()
                        },
                        isDarkTheme = isDarkTheme
                    )
                }
            }
        }
    }
}

@Composable
fun ImageSelectionArea(
    previewBitmap: android.graphics.Bitmap?,
    isLoading: Boolean,
    onSelectImage: () -> Unit,
    onClearImage: () -> Unit,
    viewModel: ImageResizerViewModel
) {
    // State for the canvas
    var showGrid by remember { mutableStateOf(false) }
    var canvasState by remember { mutableStateOf<ImageCanvasState?>(null) }
    
    Card(
        modifier = Modifier.fillMaxWidth(),
        colors = CardDefaults.cardColors(containerColor = Color.Transparent),
//        shape = RoundedCornerShape(24.dp)
    ) {
        Column(
            modifier = Modifier
                .fillMaxWidth()
                .padding(0.dp),
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.SpaceBetween,
                verticalAlignment = Alignment.CenterVertically
            ) {
//                Text(
//                    text = "Image Editor",
//                    style = MaterialTheme.typography.titleMedium,
//                    fontWeight = FontWeight.SemiBold
//                )
            }
            
            Spacer(modifier = Modifier.height(0.dp))
            
            // Image container with ImageCanvas or placeholder
            Box(
                modifier = Modifier
                    .fillMaxWidth()
                    .height(380.dp)
                    .clip(RoundedCornerShape(topStart = 16.dp, topEnd = 16.dp))
                    .background(MaterialTheme.colorScheme.tertiary)
                    .clickable(enabled = previewBitmap == null) { onSelectImage() },
                contentAlignment = Alignment.Center
            ) {
                // Draw checkerboard for PNG transparency
                if (viewModel.selectedFormat == ImageFormat.PNG) {
                    CheckerboardBackground(
                        modifier = Modifier.fillMaxSize(),
                        tileSize = 8.dp
                    )
                }
                if (previewBitmap == null) {
                    // No image selected - show placeholder
                    Column(
                        horizontalAlignment = Alignment.CenterHorizontally
                    ) {
                        Icon(
                            imageVector = Icons.Outlined.Image,
                            contentDescription = null,
                            modifier = Modifier.size(26.dp),
                            tint = MaterialTheme.colorScheme.onTertiary
                        )
                        
                        Spacer(modifier = Modifier.height(8.dp))
                        
                        Text(
                            text = "Tap to select image",
                            color = MaterialTheme.colorScheme.onTertiary
                        )
                    }
                } else if (isLoading) {
                    // Loading indicator
                    CircularProgressIndicator()
                } else {
                    // Image canvas with manipulation features
                    ImageCanvas(
                        bitmap = previewBitmap,
                        modifier = Modifier.fillMaxSize(),
                        useTransparentBackground = viewModel.selectedFormat == ImageFormat.PNG,
                        showGrid = showGrid,
                        maintainAspectRatio = viewModel.maintainAspectRatio,
                        onToggleAspectRatio = viewModel::toggleMaintainAspectRatio,
                        onDimensionsChanged = { width, height ->
                            // Update dimensions in ViewModel
                            viewModel.updateWidth(width.toString())
                            viewModel.updateHeight(height.toString())
                        },
                        onSaveState = { state -> 
                            canvasState = state
                        },
                        initialState = canvasState,
                        onShowGridChange = { newShowGrid ->
                            showGrid = newShowGrid
                        },
                        targetWidth = viewModel.width.toIntOrNull() ?: 0,
                        targetHeight = viewModel.height.toIntOrNull() ?: 0
                    )
                }
            }
            
            Spacer(modifier = Modifier.height(16.dp))
            
            if (previewBitmap == null) {
                Button(
                    onClick = onSelectImage,
                    modifier = Modifier.fillMaxWidth().padding(start = 16.dp, end = 16.dp)
                ) {
                    Icon(
                        imageVector = Icons.Default.Add,
                        contentDescription = null,
                        modifier = Modifier.padding(end = 8.dp)
                    )
                    Text(text = "Select Image")
                }
            }
            else {
                // Display real-time dimensions
                Row(
                    modifier = Modifier.fillMaxWidth(),
                    horizontalArrangement = Arrangement.Center,
                    verticalAlignment = Alignment.CenterVertically
                ) {
//                    Text(
//                        text = "Dimensions: ${viewModel.width} × ${viewModel.height} px",
//                        style = MaterialTheme.typography.bodyMedium,
//                        color = MaterialTheme.colorScheme.onSurfaceVariant
//                    )

                    // Clear button
                    Button(
                        onClick = onClearImage,
                        modifier = Modifier.fillMaxWidth().padding(start = 16.dp, end = 16.dp)
                    ) {
                        Text(text = "Clear")
                    }
                }
           }
        }
    }
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun ResizeOptionsArea(
    width: String,
    onWidthChange: (String) -> Unit,
    height: String,
    onHeightChange: (String) -> Unit,
    templateOptions: List<String>,
    selectedTemplate: String,
    onTemplateSelected: (String) -> Unit,
    formatOptions: List<String>,
    selectedFormat: String,
    onFormatSelected: (String) -> Unit,
    maintainAspectRatio: Boolean,
    onToggleAspectRatio: () -> Unit,
    originalWidth: Int,
    originalHeight: Int,
    onResize: () -> Unit,
    isImageSelected: Boolean,
    isResizing: Boolean
) {
    Card(
        modifier = Modifier
            .fillMaxWidth(),
        colors = CardDefaults.cardColors(containerColor = Color.Transparent),
//        shape = RoundedCornerShape(24.dp)
    ) {
        Column(
            modifier = Modifier
                .fillMaxWidth()
                .padding(24.dp)
        ) {
            Text(
                text = "Resize Options",
                style = MaterialTheme.typography.titleMedium,
                fontWeight = FontWeight.SemiBold
            )
            
            Spacer(modifier = Modifier.height(8.dp))
            
            // Original dimensions
            if (isImageSelected) {
                Text(
                    text = "Original Size: ${originalWidth}x${originalHeight}",
                    style = MaterialTheme.typography.bodySmall,
                    color = MaterialTheme.colorScheme.onSurfaceVariant
                )
            } else {
                Text(
                    text = "Select an image to see original dimensions",
                    style = MaterialTheme.typography.bodySmall,
                    color = MaterialTheme.colorScheme.onSurfaceVariant
                )
            }
            
            Spacer(modifier = Modifier.height(16.dp))
            
            // Template selector
            var isExpanded by remember { mutableStateOf(false) }
            
            Text(
                text = "Preset templates",
                style = MaterialTheme.typography.bodyMedium
            )
            
            Spacer(modifier = Modifier.height(8.dp))
            
            ExposedDropdownMenuBox(
                expanded = isExpanded,
                onExpandedChange = { isExpanded = it }
            ) {
                OutlinedTextField(
                    value = selectedTemplate,
                    onValueChange = {},
                    readOnly = true,
                    trailingIcon = { ExposedDropdownMenuDefaults.TrailingIcon(expanded = isExpanded) },
                    modifier = Modifier
                        .fillMaxWidth()
                        .menuAnchor()
                )
                
                ExposedDropdownMenu(
                    expanded = isExpanded,
                    onDismissRequest = { isExpanded = false }
                ) {
                    templateOptions.forEach { option ->
                        DropdownMenuItem(
                            text = { Text(text = option) },
                            onClick = {
                                onTemplateSelected(option)
                                isExpanded = false
                            }
                        )
                    }
                }
            }
            
            Spacer(modifier = Modifier.height(16.dp))

            Text(
                text = "Custom dimensions",
                style = MaterialTheme.typography.bodyMedium
            )
            
            // Width and height inputs
            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.spacedBy(8.dp)
            ) {
                // Width input
                OutlinedTextField(
                    value = width,
                    onValueChange = onWidthChange,
                    label = { Text("Width (px)") },
                    keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number),
                    modifier = Modifier.weight(1f)
                )
                
                // Height input
                OutlinedTextField(
                    value = height,
                    onValueChange = onHeightChange,
                    label = { Text("Height (px)") },
                    keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number),
                    modifier = Modifier.weight(1f)
                )
            }
            
            Spacer(modifier = Modifier.height(16.dp))
            
            // Format selection dropdown
            Text(
                text = "Output Format",
                style = MaterialTheme.typography.bodyMedium
            )
            
            Spacer(modifier = Modifier.height(8.dp))
            
            var isFormatExpanded by remember { mutableStateOf(false) }
            
            ExposedDropdownMenuBox(
                expanded = isFormatExpanded,
                onExpandedChange = { isFormatExpanded = it }
            ) {
                OutlinedTextField(
                    value = selectedFormat,
                    onValueChange = {},
                    readOnly = true,
                    trailingIcon = { ExposedDropdownMenuDefaults.TrailingIcon(expanded = isFormatExpanded) },
                    modifier = Modifier
                        .fillMaxWidth()
                        .menuAnchor()
                )
                
                ExposedDropdownMenu(
                    expanded = isFormatExpanded,
                    onDismissRequest = { isFormatExpanded = false }
                ) {
                    formatOptions.forEach { option ->
                        DropdownMenuItem(
                            text = { Text(text = option) },
                            onClick = {
                                onFormatSelected(option)
                                isFormatExpanded = false
                            }
                        )
                    }
                }
            }
            
            Spacer(modifier = Modifier.height(16.dp))
            
            // Maintain aspect ratio toggle
            Row(
                modifier = Modifier.fillMaxWidth(),
                verticalAlignment = Alignment.CenterVertically
            ) {
                Text(
                    text = "Maintain aspect ratio",
                    modifier = Modifier.weight(1f)
                )
                
                Switch(
                    checked = maintainAspectRatio,
                    onCheckedChange = { onToggleAspectRatio() }
                )
            }
            
            Spacer(modifier = Modifier.height(16.dp))
            
            // Resize button
            Button(
                onClick = onResize,
                modifier = Modifier.fillMaxWidth(),
                enabled = isImageSelected && !isResizing
            ) {
                if (isResizing) {
                    CircularProgressIndicator(
                        modifier = Modifier.size(24.dp),
                        color = MaterialTheme.colorScheme.onPrimary,
                        strokeWidth = 2.dp
                    )
                    Spacer(modifier = Modifier.width(8.dp))
                    Text("Resizing...")
                } else {
                    Icon(
                        imageVector = Icons.Default.Done,
                        contentDescription = null,
                        modifier = Modifier.padding(end = 8.dp)
                    )
                    Text(text = "Resize Image")
                }
            }
        }
    }
}

@Composable
fun PermissionRationaleCard() {
    Card(
        modifier = Modifier.fillMaxWidth(),
        elevation = CardDefaults.cardElevation(defaultElevation = 4.dp),
        colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.errorContainer)
    ) {
        Column(
            modifier = Modifier
                .fillMaxWidth()
                .padding(16.dp)
        ) {
            Text(
                text = "Permission Required",
                style = MaterialTheme.typography.titleMedium,
                color = MaterialTheme.colorScheme.onErrorContainer
            )
            
            Spacer(modifier = Modifier.height(8.dp))
            
            Text(
                text = "Storage permission is required to save resized images on your device.",
                color = MaterialTheme.colorScheme.onErrorContainer
            )
        }
    }
}


```

### `app\src\main\java\com\example\pdf_img_tools_app\features\image\imageresizer\ImageResizerViewModel.kt`

```kt
package com.example.pdf_img_tools_app.features.image.imageresizer

import android.content.Context
import android.graphics.Bitmap
import android.net.Uri
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.pdf_img_tools_app.service.ImageFormat
import com.example.pdf_img_tools_app.model.ImageResizeTemplate
import com.example.pdf_img_tools_app.model.ResizedImage
import com.example.pdf_img_tools_app.service.ImageResizeService
import kotlinx.coroutines.Job
import kotlinx.coroutines.flow.MutableSharedFlow
import kotlinx.coroutines.flow.asSharedFlow
import kotlinx.coroutines.launch
import java.io.File
import java.io.FileOutputStream
import java.text.DecimalFormat

/**
 * ViewModel for the Image Resizer feature
 */
class ImageResizerViewModel : ViewModel() {

    // UI State
    var selectedImageUri by mutableStateOf<Uri?>(null)
        private set

    var previewBitmap by mutableStateOf<Bitmap?>(null)
        private set

    var previewResizedBitmap by mutableStateOf<Bitmap?>(null)
        private set

    var selectedTemplate by mutableStateOf(ImageResizeTemplate.CUSTOM)
        private set

    var width by mutableStateOf("")
        private set

    var height by mutableStateOf("")
        private set

    var maintainAspectRatio by mutableStateOf(true)
        private set

    var originalWidth by mutableStateOf(0)
        private set

    var originalHeight by mutableStateOf(0)
        private set

    var originalAspectRatio by mutableStateOf(1.0f)
        private set

    var isLoading by mutableStateOf(false)
        private set

    var resizeComplete by mutableStateOf(false)
        private set

    var resizedImage by mutableStateOf<ResizedImage?>(null)
        private set

    // Image format selection
    var selectedFormat by mutableStateOf<ImageFormat>(ImageFormat.JPG)
        private set

    // Format options
    val formatOptions = ImageFormat.getFormatNames()

    // Event flow for one-time events
    private val _eventFlow = MutableSharedFlow<UiEvent>()
    val eventFlow = _eventFlow.asSharedFlow()

    // Template options
    val templateOptions = ImageResizeTemplate.getTemplateNames()

    // Current resizing job
    private var resizeJob: Job? = null

    /**
     * Sets the selected image URI and loads preview
     */
    fun setSelectedImage(context: Context, uri: Uri) {
        // Cancel any ongoing job before starting a new one
        resizeJob?.cancel()

        resizeJob = viewModelScope.launch {
            isLoading = true

            try {
                val imageResizeService = ImageResizeService(context)

                // Check if format is supported
                if (!imageResizeService.isSupportedFormat(uri)) {
                    _eventFlow.emit(UiEvent.ShowError("Unsupported image format. Please select a JPG, PNG, or WebP image."))
                    return@launch
                }

                // Load preview bitmap
                val bitmap = imageResizeService.createImagePreview(uri)
                if (bitmap == null || bitmap.width <= 0 || bitmap.height <= 0) {
                    _eventFlow.emit(UiEvent.ShowError("Invalid image: Image dimensions are invalid."))
                    return@launch
                }

                previewBitmap = bitmap
                selectedImageUri = uri

                // Get original dimensions
                val dimensions = imageResizeService.getImageDimensions(uri)
                originalWidth = dimensions.first
                originalHeight = dimensions.second

                // Validate dimensions
                if (originalWidth <= 0 || originalHeight <= 0) {
                    _eventFlow.emit(UiEvent.ShowError("Invalid image: Image dimensions are invalid."))
                    clearSelectedImage()
                    return@launch
                }

                // Calculate aspect ratio
                originalAspectRatio = originalWidth.toFloat() / originalHeight.toFloat()

                // Set initial width and height to match original
                width = originalWidth.toString()
                height = originalHeight.toString()

                // Reset resize state
                resizeComplete = false
                resizedImage = null
            } catch (e: Exception) {
                _eventFlow.emit(UiEvent.ShowError("Failed to load image: ${e.message ?: "Unknown error"}"))
                clearSelectedImage()
            } finally {
                isLoading = false
            }
        }
    }

    /**
     * Sets the resized image from ImageCanvas
     */
    fun setResizedImage(context: Context, bitmap: Bitmap) {
        if (bitmap.width <= 0 || bitmap.height <= 0) {
            viewModelScope.launch {
                _eventFlow.emit(UiEvent.ShowError("Invalid resized image: Image dimensions are invalid."))
            }
            return
        }

        viewModelScope.launch {
            try {
                isLoading = true

                // Save the resized bitmap to a temporary file
                val outputFile = File.createTempFile("resized_", ".${selectedFormat.extension}", context.cacheDir)
                FileOutputStream(outputFile).use { outputStream ->
                    val compressFormat = when (selectedFormat) {
                        ImageFormat.PNG -> Bitmap.CompressFormat.PNG
                        ImageFormat.JPG -> Bitmap.CompressFormat.JPEG
                        else -> Bitmap.CompressFormat.JPEG // Default to JPEG for any other format
                    }
                    bitmap.compress(compressFormat, 90, outputStream)
                }

                // Calculate sizes
                val sizeAfter = outputFile.length()
                val sizeBefore = selectedImageUri?.let { uri ->
                    context.contentResolver.openInputStream(uri)?.use { inputStream ->
                        inputStream.available().toLong()
                    } ?: 0L
                } ?: 0L

                // Update state
                previewResizedBitmap = bitmap
                resizedImage = ResizedImage(
                    resizedImageFile = outputFile,
                    width = bitmap.width,
                    height = bitmap.height,
                    format = selectedFormat,
                    sizeBefore = sizeBefore,
                    sizeAfter = sizeAfter
                )
                resizeComplete = true

                // Update dimensions in UI
                width = bitmap.width.toString()
                height = bitmap.height.toString()

                // Show success message
                val message = formatSuccessMessage(resizedImage!!)
                _eventFlow.emit(UiEvent.ShowSuccess(message))
            } catch (e: Exception) {
                _eventFlow.emit(UiEvent.ShowError("Failed to process resized image: ${e.message ?: "Unknown error"}"))
            } finally {
                isLoading = false
            }
        }
    }

    /**
     * Sets the selected template and updates width/height
     */
    fun setTemplate(templateName: String) {
        val template = ImageResizeTemplate.fromDisplayName(templateName)
        selectedTemplate = template

        if (template != ImageResizeTemplate.CUSTOM) {
            width = template.width.toString()
            height = template.height.toString()
        }
    }

    /**
     * Updates the width and maintains aspect ratio if enabled
     */
    fun updateWidth(newWidth: String) {
        width = newWidth

        if (maintainAspectRatio && newWidth.isNotEmpty()) {
            try {
                val widthValue = newWidth.toInt()
                if (widthValue > 0 && originalAspectRatio > 0) {
                    val calculatedHeight = (widthValue / originalAspectRatio).toInt()
                    height = calculatedHeight.toString()
                }
            } catch (e: NumberFormatException) {
                // Do nothing for invalid input
            }
        }
    }

    /**
     * Updates the height and maintains aspect ratio if enabled
     */
    fun updateHeight(newHeight: String) {
        height = newHeight

        if (maintainAspectRatio && newHeight.isNotEmpty()) {
            try {
                val heightValue = newHeight.toInt()
                if (heightValue > 0 && originalAspectRatio > 0) {
                    val calculatedWidth = (heightValue * originalAspectRatio).toInt()
                    width = calculatedWidth.toString()
                }
            } catch (e: NumberFormatException) {
                // Do nothing for invalid input
            }
        }
    }

    /**
     * Toggles the maintain aspect ratio option
     */
    fun toggleMaintainAspectRatio() {
        maintainAspectRatio = !maintainAspectRatio
    }

    /**
     * Sets the selected output format
     */
    fun setFormat(formatName: String) {
        selectedFormat = ImageFormat.fromDisplayName(formatName)
    }

    /**
     * Performs image resizing operation
     */
    fun resizeImage(context: Context) {
        // Cancel any ongoing resize operation
        resizeJob?.cancel()

        // Validate inputs
        if (selectedImageUri == null) {
            viewModelScope.launch {
                _eventFlow.emit(UiEvent.ShowError("Please select an image first"))
            }
            return
        }

        val widthValue = width.toIntOrNull()
        val heightValue = height.toIntOrNull()

        if (widthValue == null || heightValue == null || widthValue <= 0 || heightValue <= 0) {
            viewModelScope.launch {
                _eventFlow.emit(UiEvent.ShowError("Invalid dimensions. Please enter valid width and height"))
            }
            return
        }

        // Start resizing
        resizeJob = viewModelScope.launch {
            isLoading = true

            try {
                val imageResizeService = ImageResizeService(context)

                selectedImageUri?.let { uri ->
                    val result = imageResizeService.resizeImage(uri, widthValue, heightValue, selectedFormat)

                    if (result.resizedImageFile != null && result.width > 0 && result.height > 0) {
                        // Load preview of resized image
                        val resizedUri = Uri.fromFile(result.resizedImageFile)
                        val resizedBitmap = imageResizeService.createImagePreview(resizedUri)
                        if (resizedBitmap == null || resizedBitmap.width <= 0 || resizedBitmap.height <= 0) {
                            _eventFlow.emit(UiEvent.ShowError("Failed to load resized image preview."))
                            return@let
                        }

                        // Update state
                        previewResizedBitmap = resizedBitmap
                        resizedImage = result
                        resizeComplete = true

                        // Update dimensions
                        width = result.width.toString()
                        height = result.height.toString()

                        // Show success message
                        val message = formatSuccessMessage(result)
                        _eventFlow.emit(UiEvent.ShowSuccess(message))
                    } else {
                        _eventFlow.emit(UiEvent.ShowError("Failed to resize image: Invalid output dimensions."))
                    }
                }
            } catch (e: Exception) {
                _eventFlow.emit(UiEvent.ShowError("Error during image resize: ${e.message ?: "Unknown error"}"))
            } finally {
                isLoading = false
            }
        }
    }

    /**
     * Resets the resizing process
     */
    fun resetResize() {
        previewResizedBitmap = null
        resizeComplete = false
        resizedImage = null
        // Reset to original dimensions
        width = originalWidth.toString()
        height = originalHeight.toString()
    }

    /**
     * Clear the selected image
     */
    fun clearSelectedImage() {
        selectedImageUri = null
        previewBitmap = null
        previewResizedBitmap = null
        resizeComplete = false
        resizedImage = null
        width = ""
        height = ""
        originalWidth = 0
        originalHeight = 0
        originalAspectRatio = 1.0f
    }

    /**
     * Formats a user-friendly success message with size reduction info
     */
    private fun formatSuccessMessage(resizedImage: ResizedImage): String {
        val sizeBefore = resizedImage.sizeBefore
        val sizeAfter = resizedImage.sizeAfter

        val percentReduction = if (sizeBefore > 0) {
            val reduction = (sizeBefore - sizeAfter).toFloat() / sizeBefore.toFloat() * 100
            DecimalFormat("#.##").format(reduction)
        } else {
            "0"
        }

        return "Image resized successfully!\n" +
                "Size reduced by $percentReduction%\n" +
                "Saved to Pictures/ImageResizer"
    }

    /**
     * Events emitted by this ViewModel
     */
    sealed class UiEvent {
        data class ShowError(val message: String) : UiEvent()
        data class ShowSuccess(val message: String) : UiEvent()
    }
}```

### `app\src\main\java\com\example\pdf_img_tools_app\features\image\resizeimages\BatchImageResizeViewModel.kt`

```kt
package com.example.pdf_img_tools_app.features.image.resizeimages


import android.content.Context
import android.net.Uri
import androidx.compose.runtime.State
import androidx.compose.runtime.mutableStateOf
import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import com.example.pdf_img_tools_app.service.ImageFormat
import com.example.pdf_img_tools_app.service.ImageService
import com.example.pdf_img_tools_app.utils.FileDetails
import com.example.pdf_img_tools_app.utils.FileUtils
import com.example.pdf_img_tools_app.utils.SaveLocationUtils
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import com.example.pdf_img_tools_app.model.SaveMode as FileSaveMode
import java.io.File
import java.util.UUID

/**
 * Resize modes supported by the batch image resizer
 */
enum class ResizeMode(val displayName: String) {
    FIXED_DIMENSIONS("Fixed Dimensions"),
    PERCENTAGE("Scale by Percentage"),
    PRESET_SMALL("Small (240×240)"),
    PRESET_MEDIUM("Medium (800×600)"),
    PRESET_LARGE("Large (1920×1080)")
}

/**
 * ViewModel for the batch image resize tool
 */
class BatchImageResizeViewModel(private val context: Context) : ViewModel() {

    /**
     * Factory for creating BatchImageResizeViewModel instances
     */
    class Factory(private val context: Context) : ViewModelProvider.Factory {
        @Suppress("UNCHECKED_CAST")
        override fun <T : ViewModel> create(modelClass: Class<T>): T {
            if (modelClass.isAssignableFrom(BatchImageResizeViewModel::class.java)) {
                return BatchImageResizeViewModel(context) as T
            }
            throw IllegalArgumentException("Unknown ViewModel class")
        }
    }

    // UI state
    private val _uiState = mutableStateOf(ResizeImagesUiState())
    val uiState: State<ResizeImagesUiState> = _uiState

    // Processing state flows for collecting in Composables
    private val _isProcessing = MutableStateFlow(false)
    val isProcessing: StateFlow<Boolean> = _isProcessing.asStateFlow()

    private val _progress = MutableStateFlow(0f)
    val progress: StateFlow<Float> = _progress.asStateFlow()

    // Image service instance
    private val imageService = ImageService(context)

    /**
     * Add images to the selection
     */
    fun addImages(uris: List<Uri>) {
        _uiState.value = _uiState.value.copy(
            selectedImages = _uiState.value.selectedImages + uris
        )
    }

    /**
     * Remove an image from selection
     */
    fun removeImage(uri: Uri) {
        _uiState.value = _uiState.value.copy(
            selectedImages = _uiState.value.selectedImages.filter { it != uri }
        )
    }

    /**
     * Clear all selected images
     */
    fun clearSelectedImages() {
        _uiState.value = _uiState.value.copy(
            selectedImages = emptyList()
        )
    }

    /**
     * Get details of a selected image
     */
    fun getImageDetails(uri: Uri): FileDetails? {
        return FileUtils.getFileDetails(context, uri)
    }

    /**
     * Remove a processed image
     */
    fun removeProcessedImage(details: FileDetails) {
        _uiState.value = _uiState.value.copy(
            processedImages = _uiState.value.processedImages.filter { it != details }
        )
    }

    /**
     * Clear all processed images
     */
    fun clearProcessedImages() {
        _uiState.value = _uiState.value.copy(
            processedImages = emptyList()
        )
    }

    /**
     * Show or hide the selected images bottom sheet
     */
    fun setShowSelectedImagesSheet(show: Boolean) {
        _uiState.value = _uiState.value.copy(
            showSelectedImagesSheet = show
        )
    }

    /**
     * Show or hide the processed images bottom sheet
     */
    fun setShowProcessedImagesSheet(show: Boolean) {
        _uiState.value = _uiState.value.copy(
            showProcessedImagesSheet = show
        )
    }

    /**
     * Update resize settings
     */
    fun updateResizeSettings(
        targetWidth: String? = null,
        targetHeight: String? = null,
        scalePercentage: String? = null,
        preserveAspectRatio: Boolean? = null,
        resizeMode: ResizeMode? = null,
        outputFormat: ImageFormat? = null,
        outputQuality: Int? = null,
        filenamePattern: String? = null
    ) {
        _uiState.value = _uiState.value.copy(
            targetWidth = targetWidth ?: _uiState.value.targetWidth,
            targetHeight = targetHeight ?: _uiState.value.targetHeight,
            scalePercentage = scalePercentage ?: _uiState.value.scalePercentage,
            preserveAspectRatio = preserveAspectRatio ?: _uiState.value.preserveAspectRatio,
            resizeMode = resizeMode ?: _uiState.value.resizeMode,
            outputFormat = outputFormat ?: _uiState.value.outputFormat,
            outputQuality = outputQuality ?: _uiState.value.outputQuality,
            filenamePattern = filenamePattern ?: _uiState.value.filenamePattern
        )
    }

    /**
     * Update save location settings
     */
    fun updateSaveSettings(savePath: String? = null, saveMode: FileSaveMode? = null) {
        _uiState.value = _uiState.value.copy(
            savePath = savePath ?: _uiState.value.savePath,
            saveMode = saveMode ?: _uiState.value.saveMode
        )
    }

    /**
     * Resize all selected images with current settings
     */
    suspend fun resizeImages(savePath: String, saveMode: FileSaveMode): Result<List<FileDetails>> {
        val selectedImages = _uiState.value.selectedImages
        if (selectedImages.isEmpty()) {
            return Result.failure(Exception("No images selected"))
        }

        // Update state to indicate processing
        _uiState.value = _uiState.value.copy(
            isProcessing = true,
            progress = 0f,
            savePath = savePath,
            saveMode = saveMode
        )
        _isProcessing.value = true
        _progress.value = 0f

        try {
            val results = mutableListOf<FileDetails>()
            val totalImages = selectedImages.size

            // Create a temp directory for processing
            val tempDir = File(context.cacheDir, "resize_temp_${System.currentTimeMillis()}")
            if (!tempDir.exists()) tempDir.mkdirs()

            // Make sure the save path is valid
            if (!SaveLocationUtils.validateSaveLocation(savePath)) {
                throw IllegalStateException("Invalid save location")
            }

            // Track files created during processing for cleanup
            val processedFiles = mutableListOf<File>()

            selectedImages.forEachIndexed { index, imageUri ->
                // Update progress
                val currentProgress = index.toFloat() / totalImages
                _uiState.value = _uiState.value.copy(progress = currentProgress)
                _progress.value = currentProgress

                // Get original file details
                val sourceDetails = FileUtils.getFileDetails(context, imageUri)

                // Calculate dimensions based on resize mode
                val dimensions = calculateDimensions(imageUri, sourceDetails)

                // Generate output filename
                val outputFilename = if (sourceDetails != null) {
                    getOutputFilename(sourceDetails.name)
                } else {
                    "resized_${System.currentTimeMillis()}.${_uiState.value.outputFormat.extension}"
                }

                // Create a temporary file for processing
                val tempOutputFile = File(tempDir, "temp_${System.currentTimeMillis()}.${_uiState.value.outputFormat.extension}")
                processedFiles.add(tempOutputFile)

                // Perform the resize operation
                val result = try {
                    imageService.resizeImage(
                        inputUri = imageUri,
                        outputFile = tempOutputFile,
                        targetWidth = dimensions.first,
                        targetHeight = dimensions.second,
                        preserveAspectRatio = _uiState.value.preserveAspectRatio,
                        format = _uiState.value.outputFormat,
                        quality = _uiState.value.outputQuality
                    )

                    // If successful, save to the final location using SaveLocationUtils
                    val finalUri = SaveLocationUtils.saveToLocation(
                        context = context,
                        sourceFile = tempOutputFile,
                        outputFileName = outputFilename,
                        mimeType = "image/${_uiState.value.outputFormat.extension}",
                        savePath = savePath,
                        saveMode = saveMode
                    )

                    // If we got a URI back, add it to the results
                    if (finalUri != null) {
                        val fileDetails = FileUtils.getFileDetails(context, finalUri)
                        if (fileDetails != null) {
                            // Add the dimensions which might not be in the file details
                            val fileDetailsWithDimensions = fileDetails.copy(
                                dimensions = if (dimensions.first > 0 && dimensions.second > 0) {
                                    Pair(dimensions.first, dimensions.second)
                                } else null
                            )

                            results.add(fileDetailsWithDimensions)

                            // Update processed images in UI state
                            _uiState.value = _uiState.value.copy(
                                processedImages = _uiState.value.processedImages + fileDetailsWithDimensions
                            )
                        }
                    }

                    true
                } catch (e: Exception) {
                    false
                }
            }

            // Clean up temp files
            processedFiles.forEach { it.delete() }
            tempDir.delete()

            return Result.success(results)
        } catch (e: Exception) {
            // Update error state
            _uiState.value = _uiState.value.copy(
                errorMessage = e.message
            )
            return Result.failure(e)
        } finally {
            // Update processing state when complete
            _uiState.value = _uiState.value.copy(
                isProcessing = false,
                progress = 1f
            )
            _isProcessing.value = false
            _progress.value = 1f
        }
    }

    /**
     * Calculate dimensions based on the selected resize mode
     */
    private fun calculateDimensions(imageUri: Uri, sourceDetails: FileDetails?): Pair<Int, Int> {
        val sourceWidth = sourceDetails?.dimensions?.first ?: 0
        val sourceHeight = sourceDetails?.dimensions?.second ?: 0

        return when (_uiState.value.resizeMode) {
            ResizeMode.FIXED_DIMENSIONS -> {
                val w = _uiState.value.targetWidth.toIntOrNull() ?: 0
                val h = _uiState.value.targetHeight.toIntOrNull() ?: 0
                Pair(w, h)
            }
            ResizeMode.PERCENTAGE -> {
                val scale = _uiState.value.scalePercentage.toFloatOrNull() ?: 50f
                val percentage = scale / 100f
                val w = (sourceWidth * percentage).toInt()
                val h = (sourceHeight * percentage).toInt()
                Pair(w, h)
            }
            ResizeMode.PRESET_SMALL -> {
                Pair(240, 240)
            }
            ResizeMode.PRESET_MEDIUM -> {
                Pair(800, 600)
            }
            ResizeMode.PRESET_LARGE -> {
                Pair(1920, 1080)
            }
        }
    }

    /**
     * Apply the filename pattern to generate output filename
     */
    private fun getOutputFilename(originalFilename: String): String {
        val nameWithoutExt = originalFilename.substringBeforeLast(".")

        return _uiState.value.filenamePattern
            .replace("{filename}", nameWithoutExt)
            .replace("{uuid}", UUID.randomUUID().toString().substring(0, 8))
            .plus(".${_uiState.value.outputFormat.extension}")
    }

    /**
     * Get the total size of all selected images
     */
    fun getTotalSelectedSize(): Long {
        return _uiState.value.selectedImages.sumOf { uri ->
            FileUtils.getFileDetails(context, uri)?.size ?: 0L
        }
    }

    /**
     * Get a string representation of all formats in selected images
     */
    fun getSelectedFormatsString(): String {
        val formats = _uiState.value.selectedImages.mapNotNull { uri ->
            FileUtils.getFileDetails(context, uri)?.mimeType?.substringAfterLast("/")
        }.distinct()

        return if (formats.isEmpty()) {
            "Unknown"
        } else {
            formats.joinToString(", ").uppercase()
        }
    }

    /**
     * Get a string representation of the formats of processed images
     */
    fun getProcessedFormatsString(): String {
        return if (_uiState.value.processedImages.isEmpty()) {
            _uiState.value.outputFormat.name
        } else {
            _uiState.value.outputFormat.name
        }
    }

    /**
     * Get the total original size of images before processing
     */
    fun getTotalOriginalSize(): Long {
        return _uiState.value.selectedImages.sumOf { uri ->
            FileUtils.getFileDetails(context, uri)?.size ?: 0L
        }
    }

    /**
     * Get a human-readable string describing the resize dimensions
     */
    fun getResizeDimensionsString(): String {
        return when (_uiState.value.resizeMode) {
            ResizeMode.FIXED_DIMENSIONS -> {
                val w = _uiState.value.targetWidth.toIntOrNull() ?: 0
                val h = _uiState.value.targetHeight.toIntOrNull() ?: 0
                "${w}×${h} px"
            }
            ResizeMode.PERCENTAGE -> {
                val scale = _uiState.value.scalePercentage.toFloatOrNull() ?: 50f
                "${scale}% of original"
            }
            ResizeMode.PRESET_SMALL -> "240×240 px"
            ResizeMode.PRESET_MEDIUM -> "800×600 px"
            ResizeMode.PRESET_LARGE -> "1920×1080 px"
        }
    }
}
```

### `app\src\main\java\com\example\pdf_img_tools_app\features\image\resizeimages\ResizeImagesScreen.kt`

```kt
package com.example.pdf_img_tools_app.features.image.resizeimages

import android.net.Uri
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.CropRotate
import androidx.compose.material.icons.rounded.Transform
import androidx.compose.material3.*
import androidx.compose.material3.CardDefaults
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation.NavController
import com.example.pdf_img_tools_app.service.ImageFormat
import com.example.pdf_img_tools_app.ui.components.BaseToolScreen
import com.example.pdf_img_tools_app.ui.components.FileBottomSheet
import com.example.pdf_img_tools_app.ui.components.FilePickerHandler
import com.example.pdf_img_tools_app.ui.components.OutputFileDetails
import com.example.pdf_img_tools_app.ui.components.ReusableSaveLocationSelector
import com.example.pdf_img_tools_app.ui.components.ProgressToolButton
import com.example.pdf_img_tools_app.model.SaveMode
import com.example.pdf_img_tools_app.ui.components.viewImage
import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material.icons.rounded.FileOpen
import com.example.pdf_img_tools_app.utils.FileDetails
import com.example.pdf_img_tools_app.utils.UiMessageBus
import androidx.compose.runtime.collectAsState
import androidx.compose.ui.text.font.FontWeight
import kotlinx.coroutines.launch
import androidx.core.net.toUri

/**
 * Screen for batch resizing multiple images
 */
@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun ResizeImagesScreen(
    navController: NavController,
    isDarkTheme: Boolean,
    onThemeToggle: () -> Unit,
    modifier: Modifier = Modifier
) {
    val context = LocalContext.current
    val viewModel: BatchImageResizeViewModel = viewModel(factory = BatchImageResizeViewModel.Factory(context))
    val coroutineScope = rememberCoroutineScope()
    val messageScope = "resize_images"
    val uiState by viewModel.uiState
    val isProcessing = viewModel.isProcessing.collectAsState(initial = false).value
    val progress = viewModel.progress.collectAsState(initial = 0f).value
    var savePath by remember { mutableStateOf(uiState.savePath) }
    var saveMode by remember { mutableStateOf(uiState.saveMode) }
    var showSelectedImagesSheet by remember { mutableStateOf(false) }
    var showProcessedImagesSheet by remember { mutableStateOf(false) }
    var errorMessage by remember { mutableStateOf<String?>(null) }

    BaseToolScreen(
        title = "Batch Image Resizer",
        navController = navController,
        isDarkTheme = isDarkTheme,
        onThemeToggle = onThemeToggle,
        messageScope = messageScope,
        modifier = Modifier
    ) {
        Card(
            modifier = Modifier.fillMaxWidth().padding(vertical = 8.dp),
            colors = CardDefaults.cardColors(
                containerColor = MaterialTheme.colorScheme.surface,
                contentColor = MaterialTheme.colorScheme.onSurface
            ),
            elevation = CardDefaults.cardElevation(defaultElevation = 2.dp),
            shape = RoundedCornerShape(24.dp)
        ) {
            Column(
                modifier = Modifier
                    .fillMaxSize()
                    .background(
                        color = MaterialTheme.colorScheme.surface,
                        shape = MaterialTheme.shapes.extraLarge
                    )
                    .padding(24.dp),
                verticalArrangement = Arrangement.spacedBy(16.dp)
            ) {
                HeaderSection()
                HorizontalDivider(color = MaterialTheme.colorScheme.outline)
                FileSelectionSection(
                    uiState = uiState,
                    viewModel = viewModel,
                    isDarkTheme = isDarkTheme,
                    showSelectedImagesSheet = showSelectedImagesSheet,
                    onShowSheet = { showSelectedImagesSheet = it }
                )
                ResizeOptionsSection(uiState, viewModel)
                OutputOptionsSection(uiState, viewModel)
                SaveLocationSection(
                    selectedImages = uiState.selectedImages,
                    savePath = savePath,
                    saveMode = saveMode,
                    onSavePathChange = { savePath = it },
                    onSaveModeChange = { saveMode = it }
                )
                ProcessButtonSection(
                    selectedImages = uiState.selectedImages,
                    isProcessing = isProcessing,
                    onProcess = {
                        errorMessage = null
                        coroutineScope.launch {
                            if (viewModel.uiState.value.processedImages.isNotEmpty()) {
                                viewModel.clearProcessedImages()
                            }
                            viewModel.resizeImages(savePath, saveMode).onSuccess { results ->
                                if (results.isNotEmpty()) {
                                    UiMessageBus.showSuccess(
                                        "${results.size} images resized successfully!",
                                        messageScope
                                    )
                                    showProcessedImagesSheet = true
                                } else {
                                    UiMessageBus.showError(
                                        "No images were successfully resized.",
                                        messageScope
                                    )
                                }
                            }.onFailure { error ->
                                errorMessage = error.message
                                UiMessageBus.showError(
                                    "Batch resize failed: ${error.message}",
                                    messageScope
                                )
                            }
                        }
                    }
                )
                if (errorMessage != null && !isProcessing) {
                    Column {
                        Spacer(modifier = Modifier.height(8.dp))
                        Text(
                            text = errorMessage ?: "",
                            color = MaterialTheme.colorScheme.error,
                            style = MaterialTheme.typography.bodySmall
                        )
                    }
                }
                ProcessedImagesSection(
                    processedImages = uiState.processedImages,
                    isDarkTheme = isDarkTheme,
                    showProcessedImagesSheet = showProcessedImagesSheet,
                    onShowSheet = { showProcessedImagesSheet = it },
                    savePath = savePath,
                    resizeMode = uiState.resizeMode,
                    viewModel = viewModel
                )
            }
        }
    }

    // Bottom sheets
    if (showSelectedImagesSheet) {
        FileBottomSheet(
            show = showSelectedImagesSheet,
            onDismiss = { showSelectedImagesSheet = false },
            fileUris = uiState.selectedImages,
            title = "Selected Images",
            onFileRemove = { uri -> viewModel.removeImage(uri) },
            onClearAll = { viewModel.clearSelectedImages() },
            onFileView = { uri, mimeType ->
                try {
                    viewImage(context, uri, mimeType)
                } catch (e: Exception) {
                    UiMessageBus.showError("Could not open file: ${e.message}", messageScope)
                }
            },
            showImagePreview = true,
            showDimensions = true,
            isDarkTheme = isDarkTheme
        )
    }

    if (showProcessedImagesSheet) {
        FileBottomSheet(
            show = showProcessedImagesSheet,
            onDismiss = { showProcessedImagesSheet = false },
            fileUris = uiState.processedImages.mapNotNull { it.uri },
            title = "Processed Images",
            onFileRemove = { uri ->
                uiState.processedImages.find { it.uri == uri }?.let {
                    viewModel.removeProcessedImage(it)
                }
            },
            onClearAll = { viewModel.clearProcessedImages() },
            onFileView = { uri, mimeType ->
                try {
                    viewImage(context, uri, mimeType)
                } catch (e: Exception) {
                    UiMessageBus.showError("Could not open file: ${e.message}", messageScope)
                }
            },
            showImagePreview = true,
            showDimensions = true,
            isDarkTheme = isDarkTheme
        )
    }
}

// --- Section composables below ---

@Composable
private fun HeaderSection() {
    Row {
        Icon(
            imageVector = Icons.Rounded.Transform,
            contentDescription = null,
            tint = MaterialTheme.colorScheme.primary,
            modifier = Modifier.size(36.dp)
        )
        Spacer(modifier = Modifier.width(8.dp))
        Column {
            Text(
                text = "Batch Image Resizer",
                style = MaterialTheme.typography.titleMedium,
                color = MaterialTheme.colorScheme.primary,
            )
            Spacer(modifier = Modifier.height(2.dp))
            Text(
                text = "Convert multiple images into a single PDF document",
                style = MaterialTheme.typography.bodySmall,
            )
        }
    }
}

@Composable
private fun FileSelectionSection(
    uiState: ResizeImagesUiState,
    viewModel: BatchImageResizeViewModel,
    isDarkTheme: Boolean,
    showSelectedImagesSheet: Boolean,
    onShowSheet: (Boolean) -> Unit
) {
    Column {
        Text(
            text = "Select Images",
            style = MaterialTheme.typography.titleMedium,
        )
        Spacer(modifier = Modifier.height(4.dp))
        Text(
            text = "Select multiple images just hold and select.",
            style = MaterialTheme.typography.bodySmall,
        )
        Spacer(modifier = Modifier.height(16.dp))
        FilePickerHandler(
            single = false,
            supportedMimeTypes = listOf("image/*"),
            onPicked = { uris ->
                if (uris.isNotEmpty()) {
                    viewModel.addImages(uris)
                    onShowSheet(true)
                }
            }
        ) { launchPicker, _ ->
            OutlinedButton(
                onClick = launchPicker,
                shape = RoundedCornerShape(14.dp),
                colors = ButtonDefaults.outlinedButtonColors(
                    containerColor = MaterialTheme.colorScheme.primaryContainer,
                    contentColor = MaterialTheme.colorScheme.onPrimaryContainer
                ),
                contentPadding = PaddingValues(24.dp),
                border = BorderStroke(
                    1.dp,
                    MaterialTheme.colorScheme.onPrimaryContainer
                ),
                modifier = Modifier.fillMaxWidth(),
            ) {
                Icon(
                    Icons.Rounded.FileOpen,
                    contentDescription = null,
                    modifier = Modifier.size(ButtonDefaults.IconSize)
                )
                Spacer(modifier = Modifier.size(ButtonDefaults.IconSpacing))
                Text(text = "Select Images")
            }
        }
        if (uiState.selectedImages.isNotEmpty()) {
            val selectedImageUri = uiState.selectedImages.firstOrNull() ?: "content://placeholder/selected".toUri()
            val selectedSummary = FileDetails(
                name = "${uiState.selectedImages.size} Images Selected",
                uri = selectedImageUri,
                size = viewModel.getTotalSelectedSize(),
                mimeType = "image/*",
                path = "Various locations"
            )
            val labelOverrides = mapOf(
                "format" to "Type",
                "size" to "Total Size",
                "source" to "Source"
            )
            Spacer(modifier = Modifier.height(16.dp))

            Text(
                text = "Selected Images Details",
                style = MaterialTheme.typography.bodyMedium,
                fontWeight = FontWeight.SemiBold,
            )
            Spacer(modifier = Modifier.height(16.dp))

            OutputFileDetails(
                file = selectedSummary,
                showName = true,
                showSize = true,
                showFormat = true,
                showDimensions = false,
                labelOverrides = labelOverrides,
                onOpen = { onShowSheet(true) },
                onShare = null,
                onDelete = { viewModel.clearSelectedImages() },
                isDarkTheme = isDarkTheme
            )
        }
    }
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
private fun ResizeOptionsSection(
    uiState: ResizeImagesUiState,
    viewModel: BatchImageResizeViewModel
) {
    val resizeMode = uiState.resizeMode
    val resizeModeOptions = listOf(
        "Custom" to ResizeMode.FIXED_DIMENSIONS,
        "Percent" to ResizeMode.PERCENTAGE,
        "Small" to ResizeMode.PRESET_SMALL,
        "Medium" to ResizeMode.PRESET_MEDIUM,
        "Large" to ResizeMode.PRESET_LARGE
    )
    var isResizeModeExpanded by remember { mutableStateOf(false) }
    val currentModeLabel = resizeModeOptions.find { it.second == uiState.resizeMode }?.first ?: "Fixed"

    Column(modifier = Modifier.padding(top = 8.dp)) {
        Text(
            text = "Resize Options",
            style = MaterialTheme.typography.titleMedium,
        )
        Spacer(modifier = Modifier.height(4.dp))
        Text("Select resize mode", style = MaterialTheme.typography.bodySmall)
        Spacer(modifier = Modifier.height(8.dp))

        ExposedDropdownMenuBox(
            expanded = isResizeModeExpanded,
            onExpandedChange = { isResizeModeExpanded = it }
        ) {
            OutlinedTextField(
                value = currentModeLabel,
                onValueChange = {},
                readOnly = true,
                label = { Text("Resize Mode") },
                trailingIcon = { ExposedDropdownMenuDefaults.TrailingIcon(expanded = isResizeModeExpanded) },
                modifier = Modifier.fillMaxWidth().menuAnchor(),
                colors = TextFieldDefaults.colors(
                    focusedContainerColor = MaterialTheme.colorScheme.surfaceTint,
                    unfocusedContainerColor = MaterialTheme.colorScheme.surfaceTint,
                    focusedIndicatorColor = MaterialTheme.colorScheme.onTertiary,
                    unfocusedIndicatorColor = MaterialTheme.colorScheme.onSurface,
                    cursorColor = MaterialTheme.colorScheme.tertiary,
                    focusedLabelColor = MaterialTheme.colorScheme.onTertiary,
                    unfocusedLabelColor = MaterialTheme.colorScheme.onSurface,
                    focusedTextColor = MaterialTheme.colorScheme.onTertiaryContainer,
                    unfocusedTextColor = MaterialTheme.colorScheme.onSurface
                )
            )
            ExposedDropdownMenu(
                expanded = isResizeModeExpanded,
                onDismissRequest = { isResizeModeExpanded = false }
            ) {
                resizeModeOptions.forEach { (label, mode) ->
                    DropdownMenuItem(
                        text = { Text(text = label) },
                        onClick = {
                            viewModel.updateResizeSettings(resizeMode = mode)
                            isResizeModeExpanded = false
                        }
                    )
                }
            }
        }
        Spacer(modifier = Modifier.height(16.dp))

        when (resizeMode) {
            ResizeMode.FIXED_DIMENSIONS -> {
                Row(
                    horizontalArrangement = Arrangement.spacedBy(8.dp),
                    modifier = Modifier.fillMaxWidth()
                ) {
                    OutlinedTextField(
                        value = uiState.targetWidth,
                        onValueChange = { viewModel.updateResizeSettings(targetWidth = it) },
                        label = { Text("Width (px)") },
                        keyboardOptions = KeyboardOptions.Default.copy(keyboardType = KeyboardType.Number),
                        singleLine = true,
                        modifier = Modifier.weight(1f),
                        colors = TextFieldDefaults.colors(
                            focusedContainerColor = MaterialTheme.colorScheme.surfaceTint,
                            unfocusedContainerColor = MaterialTheme.colorScheme.surfaceTint,
                            focusedIndicatorColor = MaterialTheme.colorScheme.onTertiary,
                            unfocusedIndicatorColor = MaterialTheme.colorScheme.onSurface,
                            cursorColor = MaterialTheme.colorScheme.tertiary,
                            focusedLabelColor = MaterialTheme.colorScheme.onTertiary,
                            unfocusedLabelColor = MaterialTheme.colorScheme.onSurface,
                            focusedTextColor = MaterialTheme.colorScheme.onTertiaryContainer,
                            unfocusedTextColor = MaterialTheme.colorScheme.onSurface
                        )
                    )
                    OutlinedTextField(
                        value = uiState.targetHeight,
                        onValueChange = { viewModel.updateResizeSettings(targetHeight = it) },
                        label = { Text("Height (px)") },
                        keyboardOptions = KeyboardOptions.Default.copy(keyboardType = KeyboardType.Number),
                        singleLine = true,
                        modifier = Modifier.weight(1f),
                        colors = TextFieldDefaults.colors(
                            focusedContainerColor = MaterialTheme.colorScheme.surfaceTint,
                            unfocusedContainerColor = MaterialTheme.colorScheme.surfaceTint,
                            focusedIndicatorColor = MaterialTheme.colorScheme.onTertiary,
                            unfocusedIndicatorColor = MaterialTheme.colorScheme.onSurface,
                            cursorColor = MaterialTheme.colorScheme.tertiary,
                            focusedLabelColor = MaterialTheme.colorScheme.onTertiary,
                            unfocusedLabelColor = MaterialTheme.colorScheme.onSurface,
                            focusedTextColor = MaterialTheme.colorScheme.onTertiaryContainer,
                            unfocusedTextColor = MaterialTheme.colorScheme.onSurface
                        )
                    )
                }
                Row(
                    verticalAlignment = Alignment.CenterVertically,
                    modifier = Modifier.padding(top = 8.dp)
                ) {
                    Checkbox(
                        checked = uiState.preserveAspectRatio,
                        onCheckedChange = {
                            viewModel.updateResizeSettings(
                                preserveAspectRatio = it
                            )
                        },
                    )
                    Column {
                        Text(
                            text = "Preserve aspect ratio",
                            style = MaterialTheme.typography.titleMedium
                        )
                        Text(
                            text = "Prevents the image from appearing stretched or squished.",
                            style = MaterialTheme.typography.bodySmall
                        )
                    }
                }
            }
            ResizeMode.PERCENTAGE -> {
                OutlinedTextField(
                    value = uiState.scalePercentage,
                    onValueChange = { viewModel.updateResizeSettings(scalePercentage = it) },
                    label = { Text("Scale Percentage") },
                    trailingIcon = { Text("%") },
                    keyboardOptions = KeyboardOptions.Default.copy(keyboardType = KeyboardType.Number),
                    singleLine = true,
                    modifier = Modifier.fillMaxWidth(),
                    colors = TextFieldDefaults.colors(
                        focusedContainerColor = MaterialTheme.colorScheme.surfaceTint,
                        unfocusedContainerColor = MaterialTheme.colorScheme.surfaceTint,
                        focusedIndicatorColor = MaterialTheme.colorScheme.onTertiary,
                        unfocusedIndicatorColor = MaterialTheme.colorScheme.onSurface,
                        cursorColor = MaterialTheme.colorScheme.tertiary,
                        focusedLabelColor = MaterialTheme.colorScheme.onTertiary,
                        unfocusedLabelColor = MaterialTheme.colorScheme.onSurface,
                        focusedTextColor = MaterialTheme.colorScheme.onTertiaryContainer,
                        unfocusedTextColor = MaterialTheme.colorScheme.onSurface
                    )
                )
            }
            else -> {
                val presetText = when (resizeMode) {
                    ResizeMode.PRESET_SMALL -> "240×240 px"
                    ResizeMode.PRESET_MEDIUM -> "800×600 px"
                    ResizeMode.PRESET_LARGE -> "1920×1080 px"
                    else -> ""
                }
                Box(
                    modifier = Modifier.fillMaxWidth()
                        .background(
                            color = MaterialTheme.colorScheme.surfaceVariant,
                            shape = RoundedCornerShape(8.dp)
                        ).padding(16.dp)
                ) {
                    Text(
                        text = "Selected preset $presetText",
                        style = MaterialTheme.typography.bodyMedium,
                        color = MaterialTheme.colorScheme.onSurfaceVariant,
                        modifier = Modifier.padding(vertical = 2.dp)
                    )
                }
                Row(
                    verticalAlignment = Alignment.CenterVertically,
                    modifier = Modifier.padding(top = 8.dp)
                ) {
                    Checkbox(
                        checked = uiState.preserveAspectRatio,
                        onCheckedChange = {
                            viewModel.updateResizeSettings(
                                preserveAspectRatio = it
                            )
                        },
                    )
                    Text("Preserve aspect ratio")
                }
            }
        }
    }
}

@Composable
private fun OutputOptionsSection(
    uiState: ResizeImagesUiState,
    viewModel: BatchImageResizeViewModel
) {
    Column(modifier = Modifier.padding(top = 8.dp)) {
        Text(
            text = "Output Options",
            style = MaterialTheme.typography.titleMedium,
        )
        Spacer(modifier = Modifier.height(4.dp))
        Text(text = "Select output format", style = MaterialTheme.typography.bodySmall)
        Spacer(modifier = Modifier.height(8.dp))
        Row(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.spacedBy(8.dp)
        ) {
            listOf(
                "JPEG" to ImageFormat.JPG,
                "PNG" to ImageFormat.PNG,
                "WebP" to ImageFormat.WEBP_LOSSY
            ).forEach { (label, format) ->
                OutlinedButton(
                    onClick = { viewModel.updateResizeSettings(outputFormat = format) },
                    colors = ButtonDefaults.outlinedButtonColors(
                        containerColor = if (uiState.outputFormat == format) MaterialTheme.colorScheme.tertiaryContainer else MaterialTheme.colorScheme.surface,
                        contentColor = if (uiState.outputFormat == format) MaterialTheme.colorScheme.onTertiaryContainer else MaterialTheme.colorScheme.onSurface
                    ),
                    border = BorderStroke(
                        width = 1.dp,
                        color = if (uiState.outputFormat == format) MaterialTheme.colorScheme.tertiary else MaterialTheme.colorScheme.onSurface
                    ),
                    modifier = Modifier.weight(1f)
                ) {
                    Text(label)
                }
            }
        }
        Spacer(modifier = Modifier.height(16.dp))
        Text(text = "Select filename pattern", style = MaterialTheme.typography.bodySmall)
        Spacer(modifier = Modifier.height(8.dp))
        OutlinedTextField(
            value = uiState.filenamePattern,
            onValueChange = { viewModel.updateResizeSettings(filenamePattern = it) },
            label = { Text(text = "Filename Pattern") },
            placeholder = { Text(text = "resized_{filename}") },
            singleLine = true,
            supportingText = {
                Text(
                    text = "Note: Use {filename} for original name, {uuid} for unique ID",
                    modifier = Modifier.padding(top = 8.dp)
                )
            },
            modifier = Modifier.fillMaxWidth(),
            colors = TextFieldDefaults.colors(
                focusedContainerColor = MaterialTheme.colorScheme.surfaceTint,
                unfocusedContainerColor = MaterialTheme.colorScheme.surfaceTint,
                focusedIndicatorColor = MaterialTheme.colorScheme.onTertiary,
                unfocusedIndicatorColor = MaterialTheme.colorScheme.onSurface,
                cursorColor = MaterialTheme.colorScheme.tertiary,
                focusedLabelColor = MaterialTheme.colorScheme.onTertiary,
                unfocusedLabelColor = MaterialTheme.colorScheme.onSurface,
                focusedTextColor = MaterialTheme.colorScheme.onTertiaryContainer,
                unfocusedTextColor = MaterialTheme.colorScheme.onSurface
            )
        )
    }
}

@Composable
private fun SaveLocationSection(
    selectedImages: List<Uri>,
    savePath: String,
    saveMode: SaveMode,
    onSavePathChange: (String) -> Unit,
    onSaveModeChange: (SaveMode) -> Unit
) {
    ReusableSaveLocationSelector(
        visible = selectedImages.isNotEmpty(),
        defaultSaveLocation = savePath,
        onSaveLocationChanged = onSavePathChange,
        saveModeEnabled = true,
        initialSaveMode = SaveMode.valueOf(saveMode.name),
        onSaveModeChanged = { onSaveModeChange(SaveMode.valueOf(it.name)) },
        modifier = Modifier.fillMaxWidth()
    )
}

@Composable
private fun ProcessButtonSection(
    selectedImages: List<Uri>,
    isProcessing: Boolean,
    onProcess: () -> Unit
) {
    ProgressToolButton(
        onClick = onProcess,
        enabled = !isProcessing && selectedImages.isNotEmpty(),
        text = "Resize ${selectedImages.size} ${if (selectedImages.size == 1) "Image" else "Images"}",
        isProcessing = isProcessing,
        modifier = Modifier.fillMaxWidth(),
        icon = Icons.Default.CropRotate,
    )
}

@Composable
private fun ProcessedImagesSection(
    processedImages: List<FileDetails>,
    isDarkTheme: Boolean,
    showProcessedImagesSheet: Boolean,
    onShowSheet: (Boolean) -> Unit,
    savePath: String,
    resizeMode: ResizeMode,
    viewModel: BatchImageResizeViewModel
) {
    if (processedImages.isNotEmpty()) {
        val processedUri = processedImages.firstOrNull()?.uri
            ?: "content://placeholder/processed".toUri()
        val processedSummary = FileDetails(
            name = "${processedImages.size} Images Resized",
            uri = processedUri,
            size = processedImages.sumOf { it.size },
            mimeType = "image/*",
            path = savePath
        )
        val additionalDetails = mapOf(
            "Format" to viewModel.getProcessedFormatsString(),
            "Resize Mode" to resizeMode.displayName,
            "Dimensions" to viewModel.getResizeDimensionsString()
        )
        val totalOriginalSize = viewModel.getTotalOriginalSize()
        val totalProcessedSize = processedImages.sumOf { it.size }
        val compressionInfo = if (totalOriginalSize > 0) Pair( totalOriginalSize, totalProcessedSize) else null
        val labelMap = mutableMapOf<String, String>(
            "format" to "Output Format",
            "size" to "Total Size"
        )
        additionalDetails.forEach { (key, _) ->
            labelMap[key.lowercase()] = key
        }
        Text(
            text = "Resized Images Details",
            style = MaterialTheme.typography.bodyMedium,
            fontWeight = FontWeight.SemiBold,
        )
        OutputFileDetails(
            file = processedSummary,
            showSize = true,
            showFormat = true,
            showDimensions = true,
            showCompression = compressionInfo != null,
            compressionInfo = compressionInfo,
            labelOverrides = labelMap,
            onOpen = { onShowSheet(true) },
            onShare = null,
            onDelete = { viewModel.clearProcessedImages() },
            isDarkTheme = isDarkTheme
        )
    }
}```

### `app\src\main\java\com\example\pdf_img_tools_app\features\image\resizeimages\ResizeImagesUiState.kt`

```kt
package com.example.pdf_img_tools_app.features.image.resizeimages

import android.net.Uri
import com.example.pdf_img_tools_app.model.SaveMode
import com.example.pdf_img_tools_app.service.ImageFormat
import com.example.pdf_img_tools_app.utils.FileDetails

/**
 * Data class representing the UI state for the Resize Images screen
 */
data class ResizeImagesUiState(
    // Selected and processed images
    val selectedImages: List<Uri> = emptyList(),
    val processedImages: List<FileDetails> = emptyList(),
    
    // Processing state
    val isProcessing: Boolean = false,
    val progress: Float = 0f,
    
    // Resize parameters
    val targetWidth: String = "",
    val targetHeight: String = "",
    val scalePercentage: String = "50",
    val preserveAspectRatio: Boolean = true,
    val resizeMode: ResizeMode = ResizeMode.FIXED_DIMENSIONS,
    
    // Output options
    val outputFormat: ImageFormat = ImageFormat.JPG,
    val outputQuality: Int = 90,
    val filenamePattern: String = "resized_{filename}",
    
    // Save location options
    val savePath: String = "Downloads",
    val saveMode: SaveMode = SaveMode.SEPARATELY,
    
    // UI state
    val showSelectedImagesSheet: Boolean = false,
    val showProcessedImagesSheet: Boolean = false,
    
    // Error handling
    val errorMessage: String? = null
)
```

### `app\src\main\java\com\example\pdf_img_tools_app\features\pdf\compresspdf\CompressPdfScreen.kt`

```kt
package com.example.pdf_img_tools_app.features.pdf.compresspdf

import android.content.Context
import androidx.navigation.NavController
import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Compress
import androidx.compose.material.icons.filled.Warning
import androidx.compose.material.icons.rounded.Compress
import androidx.compose.material.icons.rounded.FileOpen
import androidx.compose.material3.AlertDialog
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.HorizontalDivider
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.Slider
import androidx.compose.material3.SliderDefaults
import androidx.compose.material3.SnackbarHostState
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.lifecycle.viewmodel.compose.viewModel
import com.example.pdf_img_tools_app.ui.components.BaseToolScreen
import com.example.pdf_img_tools_app.ui.components.FilePickerHandler
import com.example.pdf_img_tools_app.ui.components.OutputFileDetails
import com.example.pdf_img_tools_app.ui.components.ProgressToolButton
import com.example.pdf_img_tools_app.ui.components.ReusableSaveLocationSelector
import com.example.pdf_img_tools_app.ui.components.shareFile
import com.example.pdf_img_tools_app.ui.components.viewPdf
import com.example.pdf_img_tools_app.utils.FileDetails
import com.example.pdf_img_tools_app.utils.FileUtils

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

    BaseToolScreen(
        title = "Compress PDF",
        navController = navController,
        isDarkTheme = isDarkTheme,
        onThemeToggle = onThemeToggle,
        contentScrollable = true,
        messageScope = "compress_pdf",
        modifier = modifier
    ) {
        Card(
            modifier = Modifier
                .fillMaxWidth()
                .padding(vertical = 8.dp),
            colors = CardDefaults.cardColors(
                containerColor = MaterialTheme.colorScheme.surface,
                contentColor = MaterialTheme.colorScheme.onSurface
            ),
            elevation = CardDefaults.cardElevation(defaultElevation = 1.dp),
            shape = RoundedCornerShape(24.dp)
        ) {
            Column(
                modifier = Modifier.padding(24.dp),
                verticalArrangement = Arrangement.spacedBy(16.dp)
            ) {
                HeaderSection()
                HorizontalDivider(color = MaterialTheme.colorScheme.outline)
                FileSelectionSection(uiState, context, viewModel)
                CompressionQualitySection(uiState, viewModel)
                if (uiState.selectedPdfUri != null) {
                    ReusableSaveLocationSelector(
                        visible = true,
                        defaultSaveLocation = uiState.savePath,
                        onSaveLocationChanged = { viewModel.updateSavePath(it) },
                        saveModeEnabled = false,
                        initialSaveMode = uiState.saveMode,
                        onSaveModeChanged = { viewModel.changeSaveMode(it) },
                        modifier = Modifier.fillMaxWidth()
                    )
                }

                ProgressToolButton(
                    onClick = { viewModel.startCompression(context, "compress_pdf") },
                    isProcessing = uiState.isProcessing,
                    progress = uiState.progress,
                    enabled = !uiState.isProcessing && uiState.selectedPdfUri != null,
                    text = "Compress PDF",
                    icon = Icons.Default.Compress,
                    errorMessage = if (uiState.isProcessing) null else uiState.errorMessage,
                    onCancel = if (uiState.isProcessing) { { viewModel.cancelCompression() } } else null
                )
                uiState.outputDetails?.let { details ->
                    Text(
                        text = "Compressed PDF File Details",
                        style = MaterialTheme.typography.bodyMedium,
                        fontWeight = FontWeight.SemiBold,
                    )
                    OutputFileDetails(
                        file = details,
                        showCompression = true,
                        compressionInfo = uiState.selectedPdfUri?.let { uri ->
                            val originalSize = FileUtils.getFileSize(context, uri)
                            if (originalSize > 0 && details.size > 0) Pair(originalSize, details.size) else null
                        },
                        onOpen = { viewPdf(context, details.uri) },
                        onShare = { shareFile(context, details.uri, details.mimeType) },
                        onDelete = { viewModel.clearOutputDetails() },
                        isDarkTheme = isDarkTheme,
                    )
                }
            }
        }
    }

    // Small components below
    if (uiState.showLargeFileWarning) {
        AlertDialog(
            onDismissRequest = { viewModel.dismissLargeFileWarning() },
            icon = { Icon(Icons.Filled.Warning, contentDescription = null, tint = MaterialTheme.colorScheme.error) },
            title = { Text("Large File Detected") },
            text = { Text("This file is quite large. Compression may take several minutes.") },
            confirmButton = { TextButton(onClick = { viewModel.dismissLargeFileWarning() }) { Text("Understand") } }
        )
    }
}

@Composable
private fun HeaderSection() {
    Row(verticalAlignment = Alignment.CenterVertically) {
        Icon(Icons.Rounded.Compress, contentDescription = null, tint = MaterialTheme.colorScheme.primary, modifier = Modifier.size(32.dp))
        Spacer(modifier = Modifier.width(8.dp))
        Column {
            Text("Compress PDF", style = MaterialTheme.typography.titleMedium, color = MaterialTheme.colorScheme.primary)
            Spacer(modifier = Modifier.height(2.dp))
            Text("Reduce PDF file size while preserving quality", style = MaterialTheme.typography.bodySmall)
        }
    }
}

@Composable
private fun FileSelectionSection(uiState: CompressPdfUiState, context: Context, viewModel: CompressPdfViewModel) {
    Column {
        Text("Select PDF File", style = MaterialTheme.typography.bodyMedium, fontWeight = FontWeight.SemiBold)
        Spacer(modifier = Modifier.height(4.dp))
        Text("Select a single PDF file.", style = MaterialTheme.typography.bodySmall)
        Spacer(modifier = Modifier.height(16.dp))
        if (uiState.selectedPdfUri == null) {
            FilePickerHandler(
                single = true,
                supportedMimeTypes = listOf("application/pdf"),
                onPicked = { uris -> if (uris.isNotEmpty()) viewModel.onFilePicked(context, uris.first()) }
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
                    modifier = Modifier.fillMaxWidth()
                ) {
                    Icon(Icons.Rounded.FileOpen, contentDescription = null, modifier = Modifier.size(ButtonDefaults.IconSize))
                    Spacer(modifier = Modifier.size(ButtonDefaults.IconSpacing))
                    Text("Select PDF File")
                }
            }
        } else {
            Text(
                text = "Selected PDF File Details",
                style = MaterialTheme.typography.bodyMedium,
                fontWeight = FontWeight.SemiBold,
            )
            Spacer(modifier = Modifier.height(16.dp))
            OutputFileDetails(
                file = FileDetails(
                    name = FileUtils.getFileName(context, uiState.selectedPdfUri) ?: "Unknown",
                    size = uiState.fileSize,
                    mimeType = "application/pdf",
                    uri = uiState.selectedPdfUri,
                    pageCount = uiState.pdfPageCount.takeIf { it > 0 }
                ),
                showSize = true,
                showFormat = true,
                showPages = true,
                onDelete = { viewModel.clearSelectedFile() },
                onOpen = { viewPdf(context, uiState.selectedPdfUri) },
            )
        }

    }
}

@Composable
private fun CompressionQualitySection(uiState: CompressPdfUiState, viewModel: CompressPdfViewModel) {
    Text("Compression quality ${uiState.compressionQuality.toInt()}%", style = MaterialTheme.typography.bodyMedium, fontWeight = FontWeight.SemiBold)
    Column(modifier = Modifier.fillMaxWidth()) {
        Slider(
            value = uiState.compressionQuality,
            onValueChange = { viewModel.updateQuality(it) },
            valueRange = 10f..100f,
            steps = 9,
            modifier = Modifier.fillMaxWidth(),
            colors = SliderDefaults.colors(
                thumbColor = MaterialTheme.colorScheme.primary,
                activeTrackColor = MaterialTheme.colorScheme.primary,
                activeTickColor = MaterialTheme.colorScheme.onPrimary,
            ),
        )
        Row(modifier = Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.SpaceBetween) {
            Text("Smaller size", style = MaterialTheme.typography.bodySmall)
            Text("Better quality", style = MaterialTheme.typography.bodySmall)
        }
    }
}```

### `app\src\main\java\com\example\pdf_img_tools_app\features\pdf\compresspdf\CompressPdfUiState.kt`

```kt
package com.example.pdf_img_tools_app.features.pdf.compresspdf

import android.net.Uri
import com.example.pdf_img_tools_app.model.SaveMode
import com.example.pdf_img_tools_app.utils.FileDetails

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
)
```

### `app\src\main\java\com\example\pdf_img_tools_app\features\pdf\compresspdf\CompressPdfViewModel.kt`

```kt
package com.example.pdf_img_tools_app.features.pdf.compresspdf

import android.content.Context
import android.net.Uri
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.pdf_img_tools_app.model.SaveMode
import com.example.pdf_img_tools_app.service.PdfService
import com.example.pdf_img_tools_app.utils.FileUtils
import com.example.pdf_img_tools_app.utils.SaveLocationUtils
import com.example.pdf_img_tools_app.utils.UiMessageBus
import kotlinx.coroutines.Job
import kotlinx.coroutines.launch
import java.io.FileOutputStream

/**
 * ViewModel for the Compress PDF screen that handles business logic and state management
 */
class CompressPdfViewModel : ViewModel() {
    
    // The UI state exposed to the UI layer
    var uiState by mutableStateOf(CompressPdfUiState())
        private set
    
    // Private properties
    private var compressionJob: Job? = null
    private var startTime: Long = 0
    
    /**
     * Handles when a PDF file is picked from the file picker
     */
    fun onFilePicked(context: Context, uri: Uri) {
        val fileSize = FileUtils.getFileSize(context, uri)
        
        uiState = uiState.copy(
            selectedPdfUri = uri,
            outputDetails = null,
            fileSize = fileSize,
            showLargeFileWarning = fileSize > 10 * 1024 * 1024 // Show warning for files > 10MB
        )
        
        // Extract page count using PdfService
        viewModelScope.launch {
            try {
                val pdfService = PdfService(context)
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
        uiState = uiState.copy(saveMode = saveMode)
    }
    
    /**
     * Updates the save path
     */
    fun updateSavePath(path: String) {
        uiState = uiState.copy(savePath = path)
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
        uiState = uiState.copy(
            selectedPdfUri = null,
            outputDetails = null,
            pdfPageCount = 0
        )
    }
    
    /**
     * Clears the output details
     */
    fun clearOutputDetails() {
        uiState = uiState.copy(
            outputDetails = null,
            pdfPageCount = 0
        )
    }
    
    /**
     * Starts the PDF compression process
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
        
        // Cancel any existing job
        compressionJob?.cancel()
        
        // Start new compression job
        compressionJob = viewModelScope.launch {
            uiState = currentState.copy(
                isProcessing = true,
                progress = 0f
            )
            startTime = System.currentTimeMillis()
            
            try {
                val pdfService = PdfService(context)
                
                // 1. Create temp file for processing
                val tempInputFile = FileUtils.createTempFile(context, "pdf_input", ".pdf")
                if (tempInputFile == null) {
                    UiMessageBus.showError("Failed to create temporary file", messageScope)
                    uiState = uiState.copy(isProcessing = false)
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
                        val originalFileName = FileUtils.getFileName(context, selectedUri)
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
                            val details = FileUtils.getFileDetails(context, finalUri)
                            
                            uiState = uiState.copy(outputDetails = details)
                            
                            // Get compression ratio
                            val originalSize = FileUtils.getFileSize(context, selectedUri)
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
            } finally {
                uiState = uiState.copy(
                    isProcessing = false,
                    progress = -1f,
                    estimatedTimeRemaining = null
                )
                compressionJob = null
            }
        }
    }
    
    /**
     * Cancels the ongoing compression job
     */
    fun cancelCompression() {
        compressionJob?.cancel()
        compressionJob = null
        uiState = uiState.copy(
            isProcessing = false,
            progress = -1f,
            estimatedTimeRemaining = null
        )
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
}
```

### `app\src\main\java\com\example\pdf_img_tools_app\features\pdf\imagestopdf\ImagesToPdfScreen.kt`

```kt
package com.example.pdf_img_tools_app.features.pdf.imagestopdf

import android.content.ActivityNotFoundException
import android.content.Context
import android.content.Intent
import android.net.Uri
import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.selection.selectable
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.PictureAsPdf
import androidx.compose.material.icons.rounded.FileOpen
import androidx.compose.material.icons.rounded.PictureAsPdf
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Card
import androidx.compose.material3.DropdownMenuItem
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.ExposedDropdownMenuBox
import androidx.compose.material3.ExposedDropdownMenuDefaults
import androidx.compose.material3.HorizontalDivider
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Text
import androidx.compose.material3.TextField
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation.NavController
import com.example.pdf_img_tools_app.ui.components.BaseToolScreen
import com.example.pdf_img_tools_app.ui.components.FileBottomSheet
import com.example.pdf_img_tools_app.ui.components.FilePickerHandler
import com.example.pdf_img_tools_app.ui.components.OutputFileDetails
import com.example.pdf_img_tools_app.ui.components.ProgressToolButton
import com.example.pdf_img_tools_app.ui.components.ReusableSaveLocationSelector
import com.example.pdf_img_tools_app.ui.components.shareFile
import com.example.pdf_img_tools_app.ui.components.viewPdf
import com.example.pdf_img_tools_app.utils.FileDetails
import androidx.core.net.toUri

// Helper function to view an image
private fun viewImage(context: Context, imageUri: Uri, mimeType: String?) {
    val intent = Intent(Intent.ACTION_VIEW)
    intent.setDataAndType(imageUri, mimeType ?: "image/*")
    intent.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION)
    try {
        context.startActivity(intent)
    } catch (e: ActivityNotFoundException) {
        android.util.Log.e("ImagesToPdfScreen", "No app found to view this image")
    }
}

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

    BaseToolScreen(
        title = "Images to PDF",
        navController = navController,
        isDarkTheme = isDarkTheme,
        onThemeToggle = onThemeToggle,
        contentScrollable = true,
        messageScope = "images_to_pdf",
        modifier = modifier
    ) {
        Card(
            modifier = Modifier
                .fillMaxWidth()
                .padding(vertical = 8.dp),
            colors = CardDefaults.cardColors(
                containerColor = MaterialTheme.colorScheme.surface,
                contentColor = MaterialTheme.colorScheme.onSurface
            ),
            elevation = CardDefaults.cardElevation(defaultElevation = 1.dp),
            shape = RoundedCornerShape(24.dp)
        ) {
            Column(
                verticalArrangement = Arrangement.spacedBy(16.dp),
                modifier = Modifier.padding(24.dp)
            ) {
                HeaderSection()
                HorizontalDivider(color = MaterialTheme.colorScheme.outline)
                FileSelectionSection(uiState, context, viewModel, isDarkTheme)
                PdfSettingsSection(uiState, viewModel)
                if (uiState.selectedImageUris.isNotEmpty()){
                    SaveLocationSection(uiState, viewModel)
                }

                ConvertButton(uiState, viewModel, context)
                OutputDetailsSection(uiState, context, viewModel, isDarkTheme)
            }
        }
        SelectedImagesBottomSheet(uiState, context, viewModel, isDarkTheme)
    }
}

@Composable
private fun HeaderSection() {
    Row(verticalAlignment = Alignment.CenterVertically) {
        Icon(Icons.Rounded.PictureAsPdf, contentDescription = null, tint = MaterialTheme.colorScheme.primary, modifier = Modifier.size(32.dp))
        Spacer(modifier = Modifier.width(8.dp))
        Column {
            Text("Images to PDF", style = MaterialTheme.typography.titleMedium, color = MaterialTheme.colorScheme.primary)
            Spacer(modifier = Modifier.height(2.dp))
            Text("Convert image files to a PDF document", style = MaterialTheme.typography.bodySmall)
        }
    }
}

@Composable
private fun FileSelectionSection(uiState: ImagesToPdfUiState, context: Context, viewModel: ImagesToPdfViewModel, isDarkTheme: Boolean) {
    Column {
        Text(
            "Select Images",
            style = MaterialTheme.typography.bodyMedium,
            fontWeight = FontWeight.SemiBold
        )
        Spacer(modifier = Modifier.height(4.dp))
        Text(
            "Select one or more image files to convert",
            style = MaterialTheme.typography.bodySmall,
        )
        Spacer(modifier = Modifier.height(16.dp))
        FilePickerHandler(
            single = false,
            supportedMimeTypes = listOf("image/*"),
            onPicked = { uris -> viewModel.addImages(context, uris) }
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
                modifier = Modifier.fillMaxWidth().padding(vertical = 0.dp)
            ) {
                Icon(
                    Icons.Rounded.FileOpen,
                    contentDescription = null,
                    modifier = Modifier.size(ButtonDefaults.IconSize)
                )
                Spacer(modifier = Modifier.size(ButtonDefaults.IconSpacing))
                Text(text = "Select Images")
            }
        }
        if (uiState.selectedImageUris.isNotEmpty()) {
            val totalSize = uiState.imageDetailsMap.values.sumOf { it.size }
            val summaryDetails = FileDetails(
                name = "${uiState.selectedImageUris.size} Images Selected",
                uri = uiState.selectedImageUris.firstOrNull()
                    ?: "content://placeholder/images_pdf".toUri(),
                size = totalSize,
                mimeType = "image/*",
                path = "Various locations"
            )

            Spacer(modifier = Modifier.height(16.dp))

            Text(
                text = "Selected Images Details",
                style = MaterialTheme.typography.bodyMedium,
                fontWeight = FontWeight.SemiBold,
            )
            Spacer(modifier = Modifier.height(16.dp))
            OutputFileDetails(
                file = summaryDetails,
                showSize = true,
                showFormat = true,
                onOpen = { viewModel.toggleImagesBottomSheet(true) },
                onDelete = { viewModel.clearAllImages() },
                isDarkTheme = isDarkTheme
            )
        }
    }
}

@Composable
private fun PdfSettingsSection(uiState: ImagesToPdfUiState, viewModel: ImagesToPdfViewModel) {
    Column {
        Text(
            "PDF Settings",
            style = MaterialTheme.typography.bodyMedium,
            fontWeight = FontWeight.SemiBold
        )
        Spacer(modifier = Modifier.height(16.dp))
        SettingOption(
            "Paper Size",
            listOf("A4", "LETTER", "LEGAL"),
            uiState.paperSize
        ) { viewModel.updatePaperSize(it) }
        Spacer(modifier = Modifier.height(16.dp))
        SettingOption(
            "Image Alignment",
            listOf("FIT_PAGE", "CENTER", "ACTUAL_SIZE"),
            uiState.imageAlignment
        ) { viewModel.updateImageAlignment(it) }
    }
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
private fun SettingOption(title: String, options: List<String>, selectedOption: String, onOptionSelected: (String) -> Unit) {
    var expanded by remember { mutableStateOf(false) }

    Column(modifier = Modifier.fillMaxWidth()) {
        Text(title, style = MaterialTheme.typography.bodyMedium)
        Spacer(modifier = Modifier.height(8.dp))
        ExposedDropdownMenuBox(
            expanded = expanded,
            onExpandedChange = { expanded = !expanded },
            modifier = Modifier.fillMaxWidth()
        ) {
            OutlinedTextField(
                value = selectedOption.replace('_', ' '),
                onValueChange = {},
                readOnly = true,
                trailingIcon = { ExposedDropdownMenuDefaults.TrailingIcon(expanded = expanded) },
                modifier = Modifier
                    .menuAnchor()
                    .fillMaxWidth()
            )
            ExposedDropdownMenu(
                expanded = expanded,
                onDismissRequest = { expanded = false }
            ) {
                options.forEach { option ->
                    DropdownMenuItem(
                        text = { Text(option.replace('_', ' ')) },
                        onClick = {
                            onOptionSelected(option)
                            expanded = false
                        }
                    )
                }
            }
        }
    }
}

@Composable
private fun SaveLocationSection(uiState: ImagesToPdfUiState, viewModel: ImagesToPdfViewModel) {
    ReusableSaveLocationSelector(
        visible = true,
        defaultSaveLocation = uiState.savePath,
        onSaveLocationChanged = { viewModel.updateSavePath(it) },
        saveModeEnabled = true,
        initialSaveMode = uiState.saveMode,
        onSaveModeChanged = { viewModel.updateSaveMode(it) },
        modifier = Modifier.fillMaxWidth()
    )
}

@Composable
private fun ConvertButton(uiState: ImagesToPdfUiState, viewModel: ImagesToPdfViewModel, context: Context) {
    ProgressToolButton(
        onClick = { viewModel.convertImagesToPdf(context, "images_to_pdf") },
        isProcessing = uiState.isProcessing,
        progress = uiState.processingProgress,
        enabled = !uiState.isProcessing && uiState.selectedImageUris.isNotEmpty(),
        text = "Create PDF",
        icon = Icons.Default.PictureAsPdf,
        errorMessage = if (uiState.isProcessing) null else uiState.errorMessage,
        onCancel = if (uiState.isProcessing) { { viewModel.cancelProcessing() } } else null
    )
}

@Composable
private fun OutputDetailsSection(uiState: ImagesToPdfUiState, context: Context, viewModel: ImagesToPdfViewModel, isDarkTheme: Boolean) {
    uiState.outputDetails?.let { details ->
        Text(
            text = "Converted PDF File Details",
            style = MaterialTheme.typography.bodyMedium,
            fontWeight = FontWeight.SemiBold,
        )
        OutputFileDetails(
            file = details,
            showSize = true,
            showFormat = true,
            showPages = true,
            onOpen = { viewPdf(context, details.uri) },
            onShare = { shareFile(context, details.uri, details.mimeType) },
            onDelete = { viewModel.clearOutputDetails() },
            isDarkTheme = isDarkTheme
        )
    }
}

@Composable
private fun SelectedImagesBottomSheet(uiState: ImagesToPdfUiState, context: Context, viewModel: ImagesToPdfViewModel, isDarkTheme: Boolean) {
    FileBottomSheet(
        show = uiState.showSelectedImagesBottomSheet && uiState.selectedImageUris.isNotEmpty(),
        onDismiss = { viewModel.toggleImagesBottomSheet(false) },
        fileUris = uiState.selectedImageUris,
        title = "Selected Images",
        showDimensions = true,
        onFileRemove = { uri -> viewModel.removeImage(context, uri) },
        onClearAll = { viewModel.clearAllImages() },
        onFileView = { uri, mimeType -> viewImage(context, uri, mimeType ?: "image/*") },
        isDarkTheme = isDarkTheme
    )
}```

### `app\src\main\java\com\example\pdf_img_tools_app\features\pdf\imagestopdf\ImagesToPdfUiState.kt`

```kt
package com.example.pdf_img_tools_app.features.pdf.imagestopdf

import android.net.Uri
import com.example.pdf_img_tools_app.model.SaveMode
import com.example.pdf_img_tools_app.utils.FileDetails

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
)
```

### `app\src\main\java\com\example\pdf_img_tools_app\features\pdf\imagestopdf\ImagesToPdfViewModel.kt`

```kt
package com.example.pdf_img_tools_app.features.pdf.imagestopdf

import android.content.Context
import android.net.Uri
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.pdf_img_tools_app.model.SaveMode
import com.example.pdf_img_tools_app.service.PdfService
import com.example.pdf_img_tools_app.utils.FileDetails
import com.example.pdf_img_tools_app.utils.FileUtils
import com.example.pdf_img_tools_app.utils.SaveLocationUtils
import com.example.pdf_img_tools_app.utils.UiMessageBus
import kotlinx.coroutines.launch
import java.io.File
import java.text.SimpleDateFormat
import java.util.Date
import java.util.Locale

/**
 * ViewModel for the Images to PDF screen that handles business logic and state management
 */
class ImagesToPdfViewModel : ViewModel() {
    
    // The UI state exposed to the UI layer
    var uiState by mutableStateOf(ImagesToPdfUiState())
        private set
    
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
     * Clear all selected images
     */
    fun clearAllImages() {
        uiState = uiState.copy(
            selectedImageUris = emptyList(),
            imageDetailsMap = emptyMap(),
            outputDetails = null,
            showSelectedImagesBottomSheet = false
        )
    }
    
    /**
     * Update details for all selected images
     */
    private fun updateImageDetails(context: Context) {
        viewModelScope.launch {
            val detailsMap = mutableMapOf<Uri, FileDetails>()
            
            for (uri in uiState.selectedImageUris) {
                val details = FileUtils.getFileDetails(context, uri)
                if (details != null) {
                    detailsMap[uri] = details
                }
            }
            
            uiState = uiState.copy(imageDetailsMap = detailsMap)
        }
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
    fun updateSaveMode(saveMode: SaveMode) {
        uiState = uiState.copy(saveMode = saveMode)
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
     * Cancel the current processing
     */
    fun cancelProcessing() {
        uiState = uiState.copy(
            isProcessing = false,
            processingProgress = -1f
        )
    }
    
    /**
     * Clear output details
     */
    fun clearOutputDetails() {
        uiState = uiState.copy(outputDetails = null)
    }
    
    /**
     * Convert images to PDF
     */
    fun convertImagesToPdf(context: Context, messageScope: String) {
        if (uiState.selectedImageUris.isEmpty()) {
            uiState = uiState.copy(errorMessage = "Please select at least one image")
            return
        }
        
        // Validate save location
        if (!SaveLocationUtils.validateSaveLocation(uiState.savePath)) {
            UiMessageBus.showError("Please specify a valid save location", messageScope)
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
                // Create temporary output file
                val tempOutputFile = FileUtils.createTempFile(context, "images_to_pdf", ".pdf")
                if (tempOutputFile == null) {
                    UiMessageBus.showError("Failed to create temporary file", messageScope)
                    uiState = uiState.copy(isProcessing = false)
                    return@launch
                }
                
                val pdfService = PdfService(context)
                
                // Convert images to PDF
                val result = pdfService.imagesToPdf(
                    imageUris = uiState.selectedImageUris,
                    outputFile = tempOutputFile,
                    paperSize = uiState.paperSize,
                    imageAlignment = uiState.imageAlignment,
                    onProgressUpdate = { progress ->
                        uiState = uiState.copy(processingProgress = progress)
                    }
                )
                
                result.fold(
                    onSuccess = {
                        // Generate a filename with date
                        val dateFormat = SimpleDateFormat("yyyyMMdd_HHmmss", Locale.getDefault())
                        val dateString = dateFormat.format(Date())
                        val outputFileName = "images_to_pdf_${dateString}.pdf"
                        
                        // Save to chosen location
                        val savedUri = SaveLocationUtils.saveToLocation(
                            context = context,
                            sourceFile = tempOutputFile,
                            outputFileName = outputFileName,
                            mimeType = "application/pdf",
                            savePath = uiState.savePath,
                            saveMode = uiState.saveMode
                        )
                        
                        if (savedUri != null) {
                            val fileDetails = FileUtils.getFileDetails(context, savedUri)
                            uiState = uiState.copy(
                                outputDetails = fileDetails,
                                pdfPageCount = uiState.selectedImageUris.size
                            )
                            
                            UiMessageBus.showSuccess(
                                "${uiState.selectedImageUris.size} images converted to PDF successfully!",
                                messageScope
                            )
                        } else {
                            UiMessageBus.showError("Failed to save PDF file", messageScope)
                        }
                        
                        // Clean up temp file
                        tempOutputFile.delete()
                    },
                    onFailure = { error ->
                        UiMessageBus.showError(
                            "Error: ${error.message ?: "Unknown error"}",
                            messageScope
                        )
                        tempOutputFile.delete()
                    }
                )
            } catch (e: Exception) {
                UiMessageBus.showError(
                    "Error: ${e.message ?: "Unknown error"}",
                    messageScope
                )
            } finally {
                uiState = uiState.copy(
                    isProcessing = false,
                    processingProgress = -1f
                )
            }
        }
    }
}
```

### `app\src\main\java\com\example\pdf_img_tools_app\features\pdf\mergepdf\MergePdfScreen.kt`

```kt
package com.example.pdf_img_tools_app.features.pdf.mergepdf

import android.content.Context
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.PictureAsPdf
import androidx.compose.material3.AlertDialog
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.rememberCoroutineScope
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp
import androidx.navigation.NavController
import androidx.lifecycle.viewmodel.compose.viewModel
import com.example.pdf_img_tools_app.ui.components.BaseToolScreen
import com.example.pdf_img_tools_app.ui.components.FilePickerHandler
import androidx.compose.material.icons.rounded.FileOpen
import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.layout.PaddingValues
import com.example.pdf_img_tools_app.ui.components.OutputFileDetails
import com.example.pdf_img_tools_app.ui.components.ReusableSaveLocationSelector
import com.example.pdf_img_tools_app.ui.components.viewPdf
import com.example.pdf_img_tools_app.ui.components.shareFile
import com.example.pdf_img_tools_app.utils.FileDetails
import com.example.pdf_img_tools_app.ui.components.FileBottomSheet
// No need to import FileExtraDetails anymore
import com.example.pdf_img_tools_app.utils.FileUtils
import com.example.pdf_img_tools_app.ui.components.ProgressToolButton
import kotlinx.coroutines.launch
import androidx.compose.material.icons.filled.MergeType
import androidx.compose.material.icons.rounded.Merge
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.FilledTonalButton
import androidx.compose.material3.HorizontalDivider
import androidx.compose.ui.text.font.FontWeight
import androidx.core.net.toUri
import kotlinx.coroutines.CoroutineScope

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

    BaseToolScreen(
        title = "Merge PDFs",
        navController = navController,
        isDarkTheme = isDarkTheme,
        onThemeToggle = onThemeToggle,
        contentScrollable = false,
        modifier = modifier
    ) {
        Card(
            modifier = Modifier
                .fillMaxWidth()
                .padding(vertical = 8.dp),
            shape = RoundedCornerShape(24.dp),
            colors = CardDefaults.cardColors(
                containerColor = MaterialTheme.colorScheme.surface,
                contentColor = MaterialTheme.colorScheme.onSurface
            )
        ) {
            Column(
                modifier = Modifier
                    .fillMaxWidth()
                    .verticalScroll(rememberScrollState())
                    .padding(24.dp),
                verticalArrangement = Arrangement.spacedBy(16.dp)
            ) {
                HeaderSection()
                FilePickerSection(viewModel)
                SelectedFilesSection(context, uiState, viewModel, isDarkTheme)
                if(uiState.selectedPdfUris.isNotEmpty()) {
                    ReusableSaveLocationSelector(
                        visible = true,
                        defaultSaveLocation = uiState.savePath,
                        onSaveLocationChanged = { viewModel.updateSavePath(it) },
                        saveModeEnabled = false,
                        initialSaveMode = uiState.saveMode,
                        onSaveModeChanged = { viewModel.changeSaveMode(it) },
                        modifier = Modifier.fillMaxWidth()
                    )
                }
                ProgressToolButton(
                    onClick = { viewModel.toggleConfirmMergeDialog(true) },
                    enabled = uiState.selectedPdfUris.size >= 2 && !uiState.isProcessing,
                    isProcessing = uiState.isProcessing,
                    progress = uiState.processingProgress,
                    text = "Merge PDFs",
                    icon = Icons.Default.MergeType,
                    onCancel = if (uiState.isProcessing) {
                        { viewModel.cancelMerge() }
                    } else null
                )
                uiState.outputDetails?.let { details ->
                    OutputFileDetailsSection(context, details, viewModel, isDarkTheme)
                }
            }
        }
        if (uiState.showSelectedFilesSheet) {
            SelectedFilesBottomSheet(context, uiState, viewModel, isDarkTheme)
        }
        if (uiState.showConfirmMergeDialog) {
            ConfirmMergeDialog(uiState, viewModel, coroutineScope, context)
        }
    }
}

@Composable
private fun HeaderSection() {
    Row {
        Icon(
            imageVector = Icons.Rounded.Merge,
            contentDescription = null,
            tint = MaterialTheme.colorScheme.primary,
            modifier = Modifier.size(32.dp)
        )
        Spacer(modifier = Modifier.width(8.dp))
        Column {
            Text(
                text = "Merge PDFs",
                style = MaterialTheme.typography.titleMedium,
                color = MaterialTheme.colorScheme.primary
            )
            Spacer(modifier = Modifier.height(2.dp))
            Text(
                text = "Combine multiple PDF files into a single document",
                style = MaterialTheme.typography.bodySmall
            )
        }
    }
    HorizontalDivider(color = MaterialTheme.colorScheme.outline)
}

@Composable
private fun FilePickerSection(viewModel: MergePdfViewModel) {
    Column {
        Text(
            text = "Select files",
            style = MaterialTheme.typography.bodyMedium,
            fontWeight = FontWeight.SemiBold,
        )
        Spacer(modifier = Modifier.height(4.dp))
        Text(
            text = "Select multiple files from phone hold and select",
            style = MaterialTheme.typography.bodySmall
        )
        Spacer(modifier = Modifier.height(16.dp))
        FilePickerHandler(
            single = false,
            supportedMimeTypes = listOf("application/pdf"),
            onPicked = { uris -> viewModel.addPdfFiles(uris) }
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
                modifier = Modifier.fillMaxWidth()
            ) {
                Icon(Icons.Rounded.FileOpen, contentDescription = null, modifier = Modifier.size(ButtonDefaults.IconSize))
                Spacer(modifier = Modifier.size(ButtonDefaults.IconSpacing))
                Text("Select PDF Files")
            }
        }
    }
}

@Composable
private fun SelectedFilesSection(
    context: Context,
    uiState: MergePdfUiState,
    viewModel: MergePdfViewModel,
    isDarkTheme: Boolean
) {
    if (uiState.selectedPdfUris.isNotEmpty()) {
        val totalSize = uiState.selectedPdfUris.sumOf { FileUtils.getFileSize(context, it) }
        val firstPdfUri = uiState.selectedPdfUris.firstOrNull() ?: "content://placeholder/merge_pdf".toUri()
        val summaryDetails = FileDetails(
            name = "${uiState.selectedPdfUris.size} PDFs Selected",
            uri = firstPdfUri,
            size = totalSize,
            mimeType = "application/pdf",
            path = "Various locations"
        )
        Text(
            text = "Selected Pdf Files Detail",
            style = MaterialTheme.typography.bodyMedium,
            fontWeight = FontWeight.SemiBold,
        )
        OutputFileDetails(
            file = summaryDetails,
            showSize = true,
            showFormat = true,
            showPages = true,
            showCompression = false,
            labelOverrides = mapOf("format" to "Type", "pages" to "Pages"),
            onOpen = { viewModel.toggleSelectedFilesSheet(true) },
//            onShare = { shareFile(context, summaryDetails.uri, summaryDetails.mimeType) },
            onDelete = { viewModel.clearAllPdfs() },
            isDarkTheme = isDarkTheme
        )
    }
}

@Composable
private fun OutputFileDetailsSection(
    context: Context,
    details: FileDetails,
    viewModel: MergePdfViewModel,
    isDarkTheme: Boolean
) {
    Text(
        text = "Merged Pdf File Details",
        style = MaterialTheme.typography.bodyMedium,
        fontWeight = FontWeight.SemiBold,
    )
    OutputFileDetails(
        file = details,
        showName = true,
        showSize = true,
        showFormat = true,
        showPages = true,
        showCompression = false,
        labelOverrides = mapOf("size" to "Size", "format" to "Type", "pages" to "Pages"),
        onOpen = { viewPdf(context, details.uri) },
        onShare = { shareFile(context, details.uri, details.mimeType) },
        onDelete = { viewModel.clearOutputDetails() },
        isDarkTheme = isDarkTheme
    )
}

@Composable
private fun SelectedFilesBottomSheet(
    context: Context,
    uiState: MergePdfUiState,
    viewModel: MergePdfViewModel,
    isDarkTheme: Boolean
) {
    FileBottomSheet(
        show = uiState.showSelectedFilesSheet,
        onDismiss = { viewModel.toggleSelectedFilesSheet(false) },
        fileUris = uiState.selectedPdfUris,
        title = "Selected PDFs",
        onFileRemove = { viewModel.removePdf(it) },
        onClearAll = { viewModel.clearAllPdfs() },
        isDarkTheme = isDarkTheme,
        fileTypeIcon = Icons.Default.PictureAsPdf,
        useCheckboxes = true,
        showIndexNumbers = true,
        showFileSize = true,
        showDimensions = false
    )
}

@Composable
private fun ConfirmMergeDialog(
    uiState: MergePdfUiState,
    viewModel: MergePdfViewModel,
    coroutineScope: CoroutineScope,
    context: Context
) {
    AlertDialog(
        onDismissRequest = { viewModel.toggleConfirmMergeDialog(false) },
        title = { Text("Confirm Merge") },
        text = { Text("Merge ${uiState.selectedPdfUris.size} PDF files into a single document?") },
        confirmButton = {
            TextButton(onClick = {
                viewModel.toggleConfirmMergeDialog(false)
                coroutineScope.launch { viewModel.mergePdfFiles(context) }
            }) {
                Text("Merge")
            }
        },
        dismissButton = {
            TextButton(onClick = { viewModel.toggleConfirmMergeDialog(false) }) {
                Text("Cancel")
            }
        }
    )
}```

### `app\src\main\java\com\example\pdf_img_tools_app\features\pdf\mergepdf\MergePdfUiState.kt`

```kt
package com.example.pdf_img_tools_app.features.pdf.mergepdf

import android.net.Uri
import com.example.pdf_img_tools_app.model.SaveMode
import com.example.pdf_img_tools_app.utils.FileDetails

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
    val errorMessage: String? = null
)
```

### `app\src\main\java\com\example\pdf_img_tools_app\features\pdf\mergepdf\MergePdfViewModel.kt`

```kt
package com.example.pdf_img_tools_app.features.pdf.mergepdf

import android.content.Context
import android.net.Uri
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.pdf_img_tools_app.model.SaveMode
import com.example.pdf_img_tools_app.service.PdfService
import com.example.pdf_img_tools_app.utils.FileDetails
import com.example.pdf_img_tools_app.utils.FileUtils
import com.example.pdf_img_tools_app.utils.SaveLocationUtils
import com.example.pdf_img_tools_app.utils.UiMessageBus
import kotlinx.coroutines.launch
import java.io.File

/**
 * ViewModel for the Merge PDF screen that handles business logic and state management
 */
class MergePdfViewModel : ViewModel() {
    
    // The UI state exposed to the UI layer
    var uiState by mutableStateOf(MergePdfUiState())
        private set
    
    /**
     * Add PDFs to the list of files to merge
     */
    fun addPdfFiles(uris: List<Uri>) {
        if (uris.isNotEmpty()) {
            uiState = uiState.copy(
                selectedPdfUris = uiState.selectedPdfUris + uris,
                outputDetails = null
            )
        }
    }
    
    /**
     * Remove a single PDF from the list
     */
    fun removePdf(uri: Uri) {
        uiState = uiState.copy(
            selectedPdfUris = uiState.selectedPdfUris.filter { it != uri }
        )
    }
    
    /**
     * Remove multiple PDFs from the list
     */
    fun removeSelectedPdfs() {
        uiState = uiState.copy(
            selectedPdfUris = uiState.selectedPdfUris.filter { it !in uiState.selectedItemsToRemove },
            selectedItemsToRemove = emptyList()
        )
    }
    
    /**
     * Clear all selected PDFs
     */
    fun clearAllPdfs() {
        uiState = uiState.copy(
            selectedPdfUris = emptyList(),
            outputDetails = null
        )
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
        uiState = uiState.copy(savePath = path)
    }
    
    /**
     * Changes the save mode
     */
    fun changeSaveMode(saveMode: SaveMode) {
        uiState = uiState.copy(saveMode = saveMode)
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
        uiState = uiState.copy(
            isProcessing = false,
            processingProgress = -1f
        )
    }
    
    /**
     * Merge selected PDF files
     */
    fun mergePdfFiles(context: Context, messageScope: String = "merge_pdf") {
        if (uiState.selectedPdfUris.size < 2) {
            UiMessageBus.showError("Please select at least 2 PDF files to merge", messageScope)
            return
        }
        
        // Validate save location
        if (!SaveLocationUtils.validateSaveLocation(uiState.savePath)) {
            UiMessageBus.showError("Please specify a valid save location", messageScope)
            return
        }
        
        // Start merging process
        uiState = uiState.copy(
            isProcessing = true,
            processingProgress = 0f,
            showConfirmMergeDialog = false
        )
        
        viewModelScope.launch {
            try {
                val pdfService = PdfService(context)
                
                // Create temporary output file
                val tempOutputFile = FileUtils.createTempFile(context, "merged_pdf", ".pdf")
                if (tempOutputFile == null) {
                    UiMessageBus.showError("Failed to create temporary file", messageScope)
                    uiState = uiState.copy(isProcessing = false)
                    return@launch
                }
                
                val mergeResult = pdfService.mergePdfFiles(
                    context = context,
                    pdfUris = uiState.selectedPdfUris,
                    outputFile = tempOutputFile,
                    onProgressUpdate = { current, total ->
                        uiState = uiState.copy(
                            processingProgress = current.toFloat() / total.toFloat()
                        )
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
                            UiMessageBus.showSuccess(
                                "${uiState.selectedPdfUris.size} PDFs merged successfully!",
                                messageScope
                            )
                            // Get details of the FINAL saved file
                            val details = FileUtils.getFileDetails(context, savedFileUri)
                            
                            uiState = uiState.copy(
                                outputDetails = details,
                                totalPageCount = updatedTotalPageCount
                            )
                        } else {
                            UiMessageBus.showError(
                                "Failed to save merged file",
                                messageScope
                            )
                        }
                        
                        // Clean up
                        tempOutputFile.delete()
                    },
                    onFailure = { error ->
                        UiMessageBus.showError(
                            "Failed to merge PDFs: ${error.message}",
                            messageScope
                        )
                    }
                )
            } catch (e: Exception) {
                UiMessageBus.showError(
                    "Error: ${e.message}",
                    messageScope
                )
            } finally {
                uiState = uiState.copy(
                    isProcessing = false,
                    processingProgress = -1f
                )
            }
        }
    }
}
```

### `app\src\main\java\com\example\pdf_img_tools_app\features\pdf\pdftoimages\PdfToImagesScreen.kt`

```kt
package com.example.pdf_img_tools_app.features.pdf.pdftoimages

import android.annotation.SuppressLint
import android.content.ActivityNotFoundException
import android.content.Context
import android.content.Intent
import android.net.Uri
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.selection.selectable
import androidx.compose.foundation.selection.toggleable
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Image
import androidx.compose.material3.Card
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.ExposedDropdownMenuBox
import androidx.compose.material3.ExposedDropdownMenuDefaults
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.DropdownMenu
import androidx.compose.material3.DropdownMenuItem
import androidx.compose.material3.HorizontalDivider
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.RadioButton
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation.NavController
import com.example.pdf_img_tools_app.ui.components.BaseToolScreen
import com.example.pdf_img_tools_app.ui.components.FileBottomSheet
import com.example.pdf_img_tools_app.ui.components.OutputFileDetails
import com.example.pdf_img_tools_app.ui.components.ProgressToolButton
import com.example.pdf_img_tools_app.ui.components.ReusableSaveLocationSelector
import com.example.pdf_img_tools_app.ui.components.SingleFilePicker
import com.example.pdf_img_tools_app.ui.components.shareFile
import com.example.pdf_img_tools_app.ui.components.viewPdf
import com.example.pdf_img_tools_app.utils.FileDetails

// Define the helper function outside the Composable
private fun viewImage(context: Context, imageUri: Uri, mimeType: String?) {
    val intent = Intent(Intent.ACTION_VIEW)
    intent.setDataAndType(imageUri, mimeType ?: "image/*") // Use fallback mime type
    intent.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION)
    try {
        context.startActivity(intent)
    } catch (e: ActivityNotFoundException) {
        android.util.Log.e("PdfToImagesScreen", "No app found to view this image")
    }
}

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

    BaseToolScreen(
        title = "PDF to Images",
        navController = navController,
        isDarkTheme = isDarkTheme,
        onThemeToggle = onThemeToggle,
        contentScrollable = true,
        messageScope = "pdf_to_images",
        modifier = modifier
    ) {
        Card(
            modifier = Modifier
                .fillMaxWidth().padding(vertical = 8.dp),
            colors = CardDefaults.cardColors(
                containerColor = MaterialTheme.colorScheme.surface,
                contentColor = MaterialTheme.colorScheme.onSurface
            ),
            elevation = CardDefaults.cardElevation(defaultElevation = 2.dp),
            shape = RoundedCornerShape(24.dp)
        ) {
            Column(
                modifier = Modifier.padding(24.dp),
                verticalArrangement = Arrangement.spacedBy(16.dp),
            ) {
                HeaderSection()
                HorizontalDivider(color = MaterialTheme.colorScheme.outline)
                FileSelectionSection(uiState, context, viewModel, isDarkTheme)
                ImageFormatSection(uiState, imageFormats, viewModel)
                DpiSelectionSection(uiState, dpiOptions, viewModel)
                if (uiState.selectedPdfUri != null) {
                    SaveLocationSection(uiState, viewModel)
                }
                ConvertButton(uiState, viewModel, context)
                OutputSummary(uiState, context, viewModel, isDarkTheme)
            }
        }
        OutputImagesBottomSheet(uiState, context, viewModel, isDarkTheme)
    }
}

@Composable
private fun HeaderSection() {
    Row(verticalAlignment = Alignment.CenterVertically) {
        Icon(Icons.Default.Image, contentDescription = null, tint = MaterialTheme.colorScheme.primary, modifier = Modifier.size(32.dp))
        Spacer(modifier = Modifier.width(8.dp))
        Column {
            Text("PDF to Images", style = MaterialTheme.typography.titleMedium, color = MaterialTheme.colorScheme.primary)
            Text("Convert PDF pages to image files", style = MaterialTheme.typography.bodySmall)
        }
    }
}

@Composable
private fun FileSelectionSection(uiState: PdfToImagesUiState, context: Context, viewModel: PdfToImagesViewModel, isDarkTheme: Boolean) {
    Column {
        Text(
            text = "Select PDF File",
            style = MaterialTheme.typography.bodyMedium,
            fontWeight = FontWeight.SemiBold
        )
        Spacer(modifier = Modifier.height(4.dp))
        Text(
            text = "Select a pdf file to remove pages into images format.",
            style = MaterialTheme.typography.bodySmall,
        )
        Spacer(modifier = Modifier.height(16.dp))
        SingleFilePicker(
            onFileSelected = { uri -> viewModel.setPdfFile(context, uri) },
            supportedMimeTypes = listOf("application/pdf"),
            buttonText = "Select PDF File"
        )

        uiState.originalFileDetails?.let {
            Spacer(modifier = Modifier.height(16.dp))
            Text(
                text = "Selected PDF File Details",
                style = MaterialTheme.typography.bodyMedium,
                fontWeight = FontWeight.SemiBold,
            )
            Spacer(modifier = Modifier.height(16.dp))
            OutputFileDetails(
                file = it,
                showName = true,
                showSize = true,
                showFormat = true,
                showPages = true,
                onOpen = { viewPdf(context, uiState.selectedPdfUri) },
//            onShare = { shareFile(context, uiState.selectedPdfUri, "application/pdf") },
                onDelete = { viewModel.clearPdfFile() },
                isDarkTheme = isDarkTheme
            )
        }
    }
}

@SuppressLint("UnrememberedMutableState")
@OptIn(ExperimentalMaterial3Api::class)
@Composable
private fun ImageFormatSection(
    uiState: PdfToImagesUiState,
    formats: List<String>,
    viewModel: PdfToImagesViewModel
) {
    Column {
        var expanded = remember { mutableStateOf(false) }

        Text("Image Format", style = MaterialTheme.typography.bodyMedium)
        Spacer(modifier = Modifier.height(8.dp))

        ExposedDropdownMenuBox(
            expanded = expanded.value,
            onExpandedChange = { expanded.value = !expanded.value }
        ) {
            OutlinedTextField(
                value = uiState.outputFormat,
                onValueChange = {},
                readOnly = true,
                label = { Text("Select Format") },
                trailingIcon = { ExposedDropdownMenuDefaults.TrailingIcon(expanded = expanded.value) },
                modifier = Modifier.fillMaxWidth().menuAnchor()
            )
            ExposedDropdownMenu(
                expanded = expanded.value,
                onDismissRequest = { expanded.value = false }) {
                formats.forEach { format ->
                    DropdownMenuItem(text = { Text(format) }, onClick = {
                        viewModel.updateOutputFormat(format)
                        expanded.value = false
                    })
                }
            }
        }
    }
}

@SuppressLint("UnrememberedMutableState")
@OptIn(ExperimentalMaterial3Api::class)
@Composable
private fun DpiSelectionSection(
    uiState: PdfToImagesUiState,
    dpiOptions: List<Int>,
    viewModel: PdfToImagesViewModel
) {
    Column {
        var expanded = remember { mutableStateOf(false) }

        Text("Image Quality (DPI)", style = MaterialTheme.typography.bodyMedium)
        Spacer(modifier = Modifier.height(8.dp))

        ExposedDropdownMenuBox(
            expanded = expanded.value,
            onExpandedChange = { expanded.value = !expanded.value }
        ) {
            OutlinedTextField(
                value = uiState.dpi.toString(),
                onValueChange = {},
                readOnly = true,
                label = { Text("Select DPI") },
                trailingIcon = { ExposedDropdownMenuDefaults.TrailingIcon(expanded = expanded.value) },
                modifier = Modifier
                    .fillMaxWidth()
                    .menuAnchor()
            )
            ExposedDropdownMenu(
                expanded = expanded.value,
                onDismissRequest = { expanded.value = false }) {
                dpiOptions.forEach { dpi ->
                    DropdownMenuItem(text = { Text("$dpi") }, onClick = {
                        viewModel.updateDpi(dpi)
                        expanded.value = false
                    })
                }
            }
        }
    }
}

@Composable
private fun SaveLocationSection(uiState: PdfToImagesUiState, viewModel: PdfToImagesViewModel) {
    ReusableSaveLocationSelector(
        visible = true,
        defaultSaveLocation = uiState.savePath,
        onSaveLocationChanged = { viewModel.updateSavePath(it) },
        saveModeEnabled = true,
        initialSaveMode = uiState.saveMode,
        onSaveModeChanged = { viewModel.updateSaveMode(it) },
        modifier = Modifier.fillMaxWidth()
    )
}

@Composable
private fun ConvertButton(uiState: PdfToImagesUiState, viewModel: PdfToImagesViewModel, context: Context) {
    ProgressToolButton(
        onClick = { viewModel.convertPdfToImages(context, "pdf_to_images") },
        isProcessing = uiState.isProcessing,
        progress = uiState.processingProgress,
        enabled = !uiState.isProcessing && uiState.selectedPdfUri != null,
        text = "Convert PDF To Images",
        icon = Icons.Default.Image,
        errorMessage = if (uiState.isProcessing) null else uiState.errorMessage,
        onCancel = if (uiState.isProcessing) { { viewModel.cancelProcessing() } } else null
    )
}

@Composable
private fun OutputSummary(uiState: PdfToImagesUiState, context: Context, viewModel: PdfToImagesViewModel, isDarkTheme: Boolean) {
    if (uiState.outputImages.isNotEmpty()) {
        val totalSize = uiState.outputImages.sumOf { it.size }
        val summaryFileDetails = FileDetails(
            uri = uiState.outputImages.firstOrNull()?.uri ?: Uri.EMPTY,
            name = "${uiState.outputImages.size} Extracted Images",
            size = totalSize,
            mimeType = "image/*",
            path = uiState.savePath
        )
        Text(
            text = "Converted Images Details",
            style = MaterialTheme.typography.bodyMedium,
            fontWeight = FontWeight.SemiBold,
        )
        OutputFileDetails(
            file = summaryFileDetails,
            showSize = true,
            showFormat = true,
            onOpen = { viewModel.toggleBottomSheet(true) },
            onShare = { shareFile(context, summaryFileDetails.uri, "image/*") },
            onDelete = { viewModel.clearAllImages() },
            isDarkTheme = isDarkTheme
        )
    }
}

@Composable
private fun OutputImagesBottomSheet(uiState: PdfToImagesUiState, context: Context, viewModel: PdfToImagesViewModel, isDarkTheme: Boolean) {
    FileBottomSheet(
        show = uiState.showBottomSheet && uiState.outputImages.isNotEmpty(),
        onDismiss = { viewModel.toggleBottomSheet(false) },
        fileUris = uiState.outputImages.map { it.uri },
        title = "All Images",
        onFileRemove = { uri -> viewModel.removeImage(uri) },
        onClearAll = { viewModel.clearAllImages() },
        onFileView = { uri, mimeType -> viewImage(context, uri, mimeType ?: "image/*") },
        isDarkTheme = isDarkTheme
    )
}```

### `app\src\main\java\com\example\pdf_img_tools_app\features\pdf\pdftoimages\PdfToImagesUiState.kt`

```kt
package com.example.pdf_img_tools_app.features.pdf.pdftoimages

import android.net.Uri
import com.example.pdf_img_tools_app.model.SaveMode
import com.example.pdf_img_tools_app.utils.FileDetails

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
)
```

### `app\src\main\java\com\example\pdf_img_tools_app\features\pdf\pdftoimages\PdfToImagesViewModel.kt`

```kt
package com.example.pdf_img_tools_app.features.pdf.pdftoimages

import android.content.Context
import android.net.Uri
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.pdf_img_tools_app.model.SaveMode
import com.example.pdf_img_tools_app.service.PdfService
import com.example.pdf_img_tools_app.utils.FileDetails
import com.example.pdf_img_tools_app.utils.FileUtils
import com.example.pdf_img_tools_app.utils.SaveLocationUtils
import com.example.pdf_img_tools_app.utils.UiMessageBus
import kotlinx.coroutines.launch
import java.io.File

/**
 * ViewModel for the PDF to Images screen that handles business logic and state management
 */
class PdfToImagesViewModel : ViewModel() {
    
    // The UI state exposed to the UI layer
    var uiState by mutableStateOf(PdfToImagesUiState())
        private set
    
    /**
     * Set the selected PDF file
     */
    fun setPdfFile(context: Context, uri: Uri) {
        uiState = uiState.copy(
            selectedPdfUri = uri,
            outputImages = emptyList(),
            originalFileDetails = FileUtils.getFileDetails(context, uri)
        )
        
        // Load page count in background
        viewModelScope.launch {
            try {
                val pdfService = PdfService(context)
                val pageCount = pdfService.getPageCount(context, uri)
                uiState = uiState.copy(pdfPageCount = pageCount)
            } catch (e: Exception) {
                // Handle error silently
                uiState = uiState.copy(pdfPageCount = 0)
            }
        }
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
        uiState = uiState.copy(savePath = path)
    }
    
    /**
     * Update the save mode
     */
    fun updateSaveMode(saveMode: SaveMode) {
        uiState = uiState.copy(saveMode = saveMode)
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
     * Toggle the bottom sheet visibility
     */
    fun toggleBottomSheet(show: Boolean) {
        uiState = uiState.copy(showBottomSheet = show)
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
     * Clear all output images
     */
    fun clearAllImages() {
        uiState = uiState.copy(
            outputImages = emptyList(),
            selectedImageIndices = emptySet(),
            showBottomSheet = false
        )
    }
    
    /**
     * Clear the selected PDF file
     */
    fun clearPdfFile() {
        uiState = uiState.copy(
            selectedPdfUri = null,
            originalFileDetails = null,
            pdfPageCount = 0
        )
    }
    
    /**
     * Cancel the current processing
     */
    fun cancelProcessing() {
        uiState = uiState.copy(
            isProcessing = false,
            processingProgress = -1f
        )
    }
    
    /**
     * Convert PDF to images
     */
    fun convertPdfToImages(context: Context, messageScope: String) {
        if (uiState.selectedPdfUri == null) {
            uiState = uiState.copy(errorMessage = "Please select a PDF file first")
            return
        }
        
        // Validate save location
        if (!SaveLocationUtils.validateSaveLocation(uiState.savePath)) {
            UiMessageBus.showError("Please specify a valid save location", messageScope)
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
                val pdfService = PdfService(context)
                val uri = uiState.selectedPdfUri ?: return@launch
                
                // Create temp directory for extracted images
                val tempDir = File(context.cacheDir, "pdf_images_${System.currentTimeMillis()}")
                if (!tempDir.exists()) {
                    tempDir.mkdirs()
                }
                
                // Convert PDF to images
                val result = pdfService.pdfToImages(
                    inputUri = uri,
                    outputDir = tempDir,
                    format = uiState.outputFormat,
                    dpi = uiState.dpi.toFloat()
                )
                
                result.fold(
                    onSuccess = { imageFiles ->
                        // Save images to the desired location
                        val savedImages = mutableListOf<FileDetails>()
                        
                        imageFiles.forEachIndexed { index, imageFile -> 
                            val fileName = "page_${index + 1}.${uiState.outputFormat.lowercase()}"
                            val mimeType = when (uiState.outputFormat.uppercase()) {
                                "PNG" -> "image/png"
                                "JPEG" -> "image/jpeg"
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
                                val imageDetails = FileUtils.getFileDetails(context, savedUri)
                                savedImages.add(imageDetails)
                            }
                            
                            // Delete the temp file
                            imageFile.delete()
                        }
                        
                        if (savedImages.isNotEmpty()) {
                            uiState = uiState.copy(outputImages = savedImages)
                            UiMessageBus.showSuccess(
                                "Extracted ${savedImages.size} images from PDF",
                                messageScope
                            )
                        } else {
                            UiMessageBus.showError("Failed to save any images", messageScope)
                        }
                        
                        // Clean up temp directory
                        tempDir.deleteRecursively()
                    },
                    onFailure = { error ->
                        UiMessageBus.showError("Failed to convert PDF: ${error.message}", messageScope)
                        tempDir.deleteRecursively()
                    }
                )
            } catch (e: Exception) {
                UiMessageBus.showError("Error: ${e.message}", messageScope)
            } finally {
                uiState = uiState.copy(
                    isProcessing = false,
                    processingProgress = -1f
                )
            }
        }
    }
}
```

### `app\src\main\java\com\example\pdf_img_tools_app\features\pdf\splitpdf\SplitPdfScreen.kt`

```kt
package com.example.pdf_img_tools_app.features.pdf.splitpdf

import android.net.Uri
import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ContentCut
import androidx.compose.material.icons.rounded.FileOpen
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.HorizontalDivider
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation.NavController
import com.example.pdf_img_tools_app.ui.components.BaseToolScreen
import com.example.pdf_img_tools_app.ui.components.FilePickerHandler
import com.example.pdf_img_tools_app.ui.components.OutputFileDetails
import com.example.pdf_img_tools_app.ui.components.ProgressToolButton
import com.example.pdf_img_tools_app.ui.components.ReusableSaveLocationSelector
import com.example.pdf_img_tools_app.ui.components.shareFile
import com.example.pdf_img_tools_app.ui.components.viewPdf


/**
 * Screen for splitting PDF files by page range
 */
@Composable
fun SplitPdfScreen(
    navController: NavController,
    isDarkTheme: Boolean,
    onThemeToggle: () -> Unit
) {
    val context = LocalContext.current
    val viewModel: SplitPdfViewModel = viewModel { SplitPdfViewModel(context) }
    val uiState by viewModel.uiState.collectAsState()

    BaseToolScreen(
        title = "Split PDF",
        navController = navController,
        isDarkTheme = isDarkTheme,
        onThemeToggle = onThemeToggle,
        messageScope = "split_pdf"
    ) {
        Card(
            modifier = Modifier
                .fillMaxWidth()
                .padding(vertical = 8.dp),
            colors = CardDefaults.cardColors(
                containerColor = MaterialTheme.colorScheme.surface,
                contentColor = MaterialTheme.colorScheme.onSurface
            ),
            elevation = CardDefaults.cardElevation(defaultElevation = 1.dp),
            shape = RoundedCornerShape(24.dp)
        ) {
            Column(
                modifier = Modifier.padding(24.dp),
                verticalArrangement = Arrangement.spacedBy(16.dp),
            ) {
                HeaderSection()
                HorizontalDivider(color = MaterialTheme.colorScheme.outline)
                FileSelectionSection(uiState, viewModel, isDarkTheme)
                PageRangeSection(uiState, viewModel)
                if(uiState.selectedPdfUri != null){
                    SaveLocationSection(uiState, viewModel)
                }
                SplitButton(uiState, viewModel)
                ErrorMessage(uiState)
                OutputDetailsSection(uiState, viewModel, context, isDarkTheme)
            }
        }
    }
}

@Composable
private fun HeaderSection() {
    Row(verticalAlignment = Alignment.CenterVertically) {
        Icon(Icons.Filled.ContentCut, contentDescription = null, tint = MaterialTheme.colorScheme.primary, modifier = Modifier.size(32.dp))
        Spacer(modifier = Modifier.width(8.dp))
        Column {
            Text("Split PDF", style = MaterialTheme.typography.titleMedium, color = MaterialTheme.colorScheme.primary)
            Text("Split PDF files by page range", style = MaterialTheme.typography.bodySmall)
        }
    }
}

@Composable
private fun FileSelectionSection(
    uiState: SplitPdfUiState,
    viewModel: SplitPdfViewModel,
    isDarkTheme: Boolean
) {
    Column {
        val context = LocalContext.current // Ensure this is inside a @Composable function
        Text(
            "Select PDF File",
            style = MaterialTheme.typography.bodyMedium,
            fontWeight = FontWeight.SemiBold
        )
        Text(
            "Select a single PDF file to split.",
            style = MaterialTheme.typography.bodySmall,
            modifier = Modifier.padding(vertical = 4.dp)
        )
        Spacer(modifier = Modifier.height(16.dp))
        if (uiState.selectedPdfUri == null) {
            FilePickerHandler(
                single = true,
                supportedMimeTypes = listOf("application/pdf"),
                onPicked = { uris -> uris.firstOrNull()?.let { viewModel.onFilePicked(it) } }
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
                    modifier = Modifier.fillMaxWidth()
                ) {
                    Icon(
                        Icons.Rounded.FileOpen,
                        contentDescription = null,
                        modifier = Modifier.padding(end = 8.dp)
                    )
                    Text("Select PDF File")
                }
            }
        } else {
            uiState.selectedPdfDetails?.let {
                Text(
                    text = "Selected PDF File Details",
                    style = MaterialTheme.typography.bodyMedium,
                    fontWeight = FontWeight.SemiBold,
                )
                Spacer(modifier = Modifier.height(16.dp))
                OutputFileDetails(
                    file = it,
                    showName = true,
                    showSize = true,
                    showFormat = true,
                    showPages = true,
                    onOpen = { viewPdf(context, it.uri) }, // Use context here
                    onDelete = { viewModel.clearPdfFile() },
                    isDarkTheme = isDarkTheme,
                )
            }
        }
    }
}

@Composable
private fun PageRangeSection(
    uiState: SplitPdfUiState,
    viewModel: SplitPdfViewModel
) {
    Column() {
        Text(
            text = "Page Range",
            style = MaterialTheme.typography.bodyMedium,
            fontWeight = FontWeight.SemiBold
        )
        Text(
            "Enter the valid page ranges to split the PDF.",
            style = MaterialTheme.typography.bodySmall,
            modifier = Modifier.padding(vertical = 4.dp)
        )
        Row(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.spacedBy(16.dp)
        ) {
            OutlinedTextField(
                value = uiState.startPage,
                onValueChange = { viewModel.onStartPageChanged(it) },
                label = { Text("Start Page") },
                keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number),
                isError = !uiState.isStartPageValid,
                modifier = Modifier.weight(1f).padding(bottom = 8.dp)
            )
            OutlinedTextField(
                value = uiState.endPage,
                onValueChange = { viewModel.onEndPageChanged(it) },
                label = { Text("End Page") },
                keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number),
                isError = !uiState.isEndPageValid,
                modifier = Modifier.weight(1f).padding(bottom = 8.dp)
            )
        }
        if (!uiState.isRangeValid) {
            Text(
                text = "Start page must be less than or equal to end page",
                color = MaterialTheme.colorScheme.error,
                style = MaterialTheme.typography.bodySmall,
                modifier = Modifier.padding(vertical = 8.dp)
            )
        }

        Text(
            "Valid range: 1 - ${uiState.pdfPageCount}",
            style = MaterialTheme.typography.bodySmall,
            modifier = Modifier.padding(top = 4.dp)
        )
    }
}

@Composable
private fun SaveLocationSection(
    uiState: SplitPdfUiState,
    viewModel: SplitPdfViewModel
) {
    ReusableSaveLocationSelector(
        visible = true,
        defaultSaveLocation = uiState.savePath,
        onSaveLocationChanged = { viewModel.updateSaveLocation(it) },
        saveModeEnabled = true,
        initialSaveMode = uiState.saveMode,
        onSaveModeChanged = { viewModel.updateSaveMode(it) },
    )
}

@Composable
private fun SplitButton(
    uiState: SplitPdfUiState,
    viewModel: SplitPdfViewModel
) {
    ProgressToolButton(
        text = "Split PDF",
        onClick = { viewModel.splitPdf("split_pdf") },
        isProcessing = uiState.isProcessing,
        progress = uiState.processingProgress,
        icon = Icons.Filled.ContentCut,
        enabled = uiState.selectedPdfUri != null && uiState.isRangeValid
    )
}

@Composable
private fun ErrorMessage(
    uiState: SplitPdfUiState
) {
    uiState.errorMessage?.let {
        Text(
            it,
            color = MaterialTheme.colorScheme.error,
            style = MaterialTheme.typography.bodyMedium,
            modifier = Modifier.padding(top = 16.dp)
        )
    }
}

@Composable
private fun OutputDetailsSection(
    uiState: SplitPdfUiState,
    viewModel: SplitPdfViewModel,
    context: android.content.Context,
    isDarkTheme: Boolean
) {
    uiState.outputDetails?.forEach { details ->
        Text(
            text = "Splitted PDF File Details",
            style = MaterialTheme.typography.bodyMedium,
            fontWeight = FontWeight.SemiBold,
        )

        OutputFileDetails(
            file = details,
            showName = true,
            showSize = true,
            showFormat = true,
            showPages = true,
            onOpen =  { viewPdf(context, details.uri) },
            onShare = { shareFile(context, details.uri, details.mimeType) },
            onDelete = { viewModel.resetOutput() },
            isDarkTheme = isDarkTheme,
        )
    }
}

```

### `app\src\main\java\com\example\pdf_img_tools_app\features\pdf\splitpdf\SplitPdfUiState.kt`

```kt
package com.example.pdf_img_tools_app.features.pdf.splitpdf

import android.net.Uri
import com.example.pdf_img_tools_app.model.SaveMode
import com.example.pdf_img_tools_app.utils.FileDetails

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
)
```

### `app\src\main\java\com\example\pdf_img_tools_app\features\pdf\splitpdf\SplitPdfViewModel.kt`

```kt
package com.example.pdf_img_tools_app.features.pdf.splitpdf

import android.content.Context
import android.net.Uri
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.pdf_img_tools_app.model.SaveMode
import com.example.pdf_img_tools_app.service.PdfService
import com.example.pdf_img_tools_app.utils.FileDetails
import com.example.pdf_img_tools_app.utils.FileUtils
import com.example.pdf_img_tools_app.utils.SaveLocationUtils
import com.example.pdf_img_tools_app.utils.UiMessageBus
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.update
import kotlinx.coroutines.launch
import java.io.File

/**
 * ViewModel for the Split PDF feature
 */
class SplitPdfViewModel(private val context: Context) : ViewModel() {
    
    private val _uiState = MutableStateFlow(SplitPdfUiState())
    val uiState: StateFlow<SplitPdfUiState> = _uiState.asStateFlow()
    
    private val pdfService = PdfService(context)
    
    /**
     * Handle when a PDF file is picked
     */
    fun onFilePicked(uri: Uri) {
        viewModelScope.launch {
            // Reset any previous state
            _uiState.update { it.copy(
                selectedPdfUri = uri,
                startPage = "1",
                endPage = "",
                isStartPageValid = true,
                isEndPageValid = true,
                isRangeValid = true,
                errorMessage = null,
                outputDetails = null,
                isProcessing = false,
                processingProgress = 0f,
                showSaveLocationSelector = true
            )}
            
            // Get PDF information
            val fileName = FileUtils.getFileName(context, uri)
            val fileSize = FileUtils.getFileSize(context, uri) ?: 0L
            val mimeType = FileUtils.getMimeType(context, uri) ?: "application/pdf"
            
            // Get page count
            val pageCount = pdfService.getPageCount(context, uri) ?: 0
            
            // Create FileDetails object for the selected PDF
            val fileDetails = FileDetails(
                uri = uri,
                name = fileName,
                size = fileSize,
                mimeType = mimeType,
                pageCount = pageCount
            )
            
            _uiState.update { it.copy(
                pdfFileName = fileName,
                pdfFileSize = fileSize,
                pdfPageCount = pageCount,
                endPage = pageCount.toString(), // Set default end page to last page
                selectedPdfDetails = fileDetails,
                // Set default save location to Downloads folder
                savePath = "Downloads"
            )}
        }
    }
    
    /**
     * Update the save location
     */
    fun updateSaveLocation(path: String) {
        _uiState.update { it.copy(savePath = path) }
    }
    
    /**
     * Update the save mode
     */
    fun updateSaveMode(saveMode: SaveMode) {
        _uiState.update { it.copy(saveMode = saveMode) }
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
     * Validate page inputs to ensure they are valid numbers within the PDF page range
     */
    private fun validatePageInputs() {
        val currentState = _uiState.value
        val pageCount = currentState.pdfPageCount
        
        if (pageCount == 0) return // Can't validate if we don't know the page count
        
        val startPageValue = currentState.startPage.toIntOrNull()
        val endPageValue = currentState.endPage.toIntOrNull()
        
        // Validate start page
        val isStartPageValid = startPageValue != null && startPageValue >= 1 && startPageValue <= pageCount
        
        // Validate end page
        val isEndPageValid = endPageValue != null && endPageValue >= 1 && endPageValue <= pageCount
        
        // Validate range (start page <= end page)
        val isRangeValid = startPageValue != null && endPageValue != null && startPageValue <= endPageValue
        
        _uiState.update { it.copy(
            isStartPageValid = isStartPageValid,
            isEndPageValid = isEndPageValid,
            isRangeValid = isRangeValid
        )}
    }
    
    /**
     * Split the PDF file based on the selected page range
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
        
        val startPage = currentState.startPage.toInt()
        val endPage = currentState.endPage.toInt()
        
        viewModelScope.launch {
            try {
                // Set processing state
                _uiState.update { it.copy(
                    isProcessing = true,
                    errorMessage = null
                )}
                
                // Create temp output directory for processing
                val tempOutputDir = File(context.cacheDir, "split_pdfs_temp")
                if (!tempOutputDir.exists()) {
                    tempOutputDir.mkdirs()
                }
                
                // Create page range for splitting
                val pageRange = listOf(Pair(startPage, endPage))
                
                // Call PDF service to split the PDF
                val result = pdfService.splitPdf(uri, tempOutputDir, pageRange)
                
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
                                    val details = FileUtils.getFileDetails(context, savedUri)
                                    if (details != null) {
                                        savedFiles.add(details)
                                    }
                                }
                                
                                // Delete the temp file regardless of whether save was successful
                                tempFile.delete()
                            } catch (e: Exception) {
                                // Log error but continue with other files
                                tempFile.delete()
                            }
                        }
                        
                        if (savedFiles.isNotEmpty()) {
                            UiMessageBus.showSuccess("PDF split successfully!", messageScope)
                            _uiState.update { it.copy(
                                isProcessing = false,
                                outputDetails = savedFiles,
                                processingProgress = 1f
                            )}
                        } else {
                            UiMessageBus.showError("Failed to save split PDF files", messageScope)
                            _uiState.update { it.copy(
                                isProcessing = false,
                                errorMessage = "Failed to save split PDF files",
                                processingProgress = 0f
                            )}
                        }
                    },
                    onFailure = { error ->
                        UiMessageBus.showError("Failed to split PDF: ${error.message}", messageScope)
                        _uiState.update { it.copy(
                            isProcessing = false,
                            errorMessage = "Failed to split PDF: ${error.message}",
                            processingProgress = 0f
                        )}
                    }
                )
            } catch (e: Exception) {
                UiMessageBus.showError("Error: ${e.message}", messageScope)
                _uiState.update { it.copy(
                    isProcessing = false,
                    errorMessage = "Error: ${e.message}",
                    processingProgress = 0f
                )}
            }
        }
    }
    
    /**
     * Clear output and reset to input state
     */
    fun resetOutput() {
        _uiState.update { it.copy(
            outputDetails = null,
            processingProgress = 0f,
            errorMessage = null
        )}
    }
    
    /**
     * Clear the selected PDF file
     */
    fun clearPdfFile() {
        _uiState.update { it.copy(
            selectedPdfUri = null,
            selectedPdfDetails = null,
            pdfPageCount = 0,
            pdfFileName = "",
            pdfFileSize = 0L,
            startPage = "",
            endPage = "",
            isStartPageValid = false,
            isEndPageValid = false,
            isRangeValid = false
        )}
    }
}
```

### `app\src\main\java\com\example\pdf_img_tools_app\model\ImageCanvasState.kt`

```kt
package com.example.pdf_img_tools_app.ui.components

import androidx.compose.ui.geometry.Offset

/**
 * Data class to store the state of the ImageCanvas for undo/redo operations
 */
data class ImageCanvasState(
    val scale: Float,
    val offset: Offset,
    val rotation: Float,
    val isFlippedHorizontally: Boolean,
    val isFlippedVertically: Boolean
)
```

### `app\src\main\java\com\example\pdf_img_tools_app\model\ImageResizeTemplate.kt`

```kt
package com.example.pdf_img_tools_app.model

/**
 * Predefined templates for image resizing
 */
enum class ImageResizeTemplate(val displayName: String, val width: Int, val height: Int) {
    INSTAGRAM_POST("Instagram Post", 1080, 1080),
    INSTAGRAM_STORY("Instagram Story", 1080, 1920),
    FACEBOOK_POST("Facebook Post", 1200, 630),
    TWITTER_POST("Twitter Post", 1200, 675),
    WHATSAPP_DP("WhatsApp Profile", 500, 500),
    LINKEDIN_COVER("LinkedIn Cover", 1584, 396),
    YOUTUBE_THUMBNAIL("YouTube Thumbnail", 1280, 720),
    PASSPORT_PHOTO("Passport Photo", 413, 531),
    CUSTOM("Custom Size", 0, 0); // Placeholder for custom dimensions

    companion object {
        fun getTemplateNames(): List<String> {
            return entries.map { it.displayName }
        }

        fun fromDisplayName(name: String): ImageResizeTemplate {
            return entries.find { it.displayName == name } ?: CUSTOM
        }
    }
}
```

### `app\src\main\java\com\example\pdf_img_tools_app\model\ResizedImage.kt`

```kt
package com.example.pdf_img_tools_app.model

import android.net.Uri
import com.example.pdf_img_tools_app.service.ImageFormat
import java.io.File

/**
 * Data class representing a resized image and its metadata
 */
data class ResizedImage(
    val originalUri: Uri? = null,         // Original image URI
    val resizedImageFile: File? = null,   // Resized image file
    val width: Int = 0,                   // Width of the resized image
    val height: Int = 0,                  // Height of the resized image
    val originalWidth: Int = 0,           // Original image width
    val originalHeight: Int = 0,          // Original image height
    val sizeBefore: Long = 0L,            // Size in bytes before resizing
    val sizeAfter: Long = 0L,             // Size in bytes after resizing
    val format: ImageFormat = ImageFormat.JPG  // Output format
)
```

### `app\src\main\java\com\example\pdf_img_tools_app\model\ResizeMode.kt`

```kt
package com.example.pdf_img_tools_app.model

/**
 * Enum class defining different image resize modes
 */
enum class ResizeMode {
    FIT,               // Resize to fit within dimensions, maintaining aspect ratio
    FILL,              // Resize to fill dimensions, may crop
    STRETCH,           // Stretch to exactly match dimensions, may distort
    MANUAL,            // Manual resizing with custom values
    FIXED_DIMENSIONS,  // Resize to fixed dimensions
    PERCENTAGE,        // Resize by percentage of original
    PRESET_SMALL,      // Small preset size (e.g., thumbnail)
    PRESET_MEDIUM,     // Medium preset size
    PRESET_LARGE       // Large preset size
}
```

### `app\src\main\java\com\example\pdf_img_tools_app\model\SaveLocationType.kt`

```kt
package com.example.pdf_img_tools_app.model

/**
 * Enum to represent different save location types
 */
enum class SaveLocationType {
    DOWNLOADS,  // Default Downloads folder
    CUSTOM      // Custom location selected by user
}
```

### `app\src\main\java\com\example\pdf_img_tools_app\model\SaveMode.kt`

```kt
package com.example.pdf_img_tools_app.model

/**
 * Enum to represent different save modes for PDF and image operations
 */
enum class SaveMode {
    SINGLE_FILE,     // Save as a single file
    MULTIPLE_FILES,  // Save as multiple files
    ZIP_ARCHIVE,     // Save as a zip archive
    FOLDER,          // Save to folder structure
    SEPARATELY,      // Save files separately
    AS_ARCHIVE       // Save as a single archive
}
```

### `app\src\main\java\com\example\pdf_img_tools_app\model\ToolItem.kt`

```kt
package com.example.pdf_img_tools_app.model

import androidx.compose.ui.graphics.vector.ImageVector

/**
 * Represents a tool in the app
 */
data class ToolItem(
    val id: String,
    val name: String,
    val description: String,
    val icon: ImageVector,
    val route: String,
    val category: ToolCategory
)

/**
 * Categories of tools in the app
 */
enum class ToolCategory {
    PDF,
    IMAGE
} ```

### `app\src\main\java\com\example\pdf_img_tools_app\model\UiMessageData.kt`

```kt
package com.example.pdf_img_tools_app.model

import java.util.UUID

/**
 * Enum representing the type of UI message
 */
enum class MessageType {
    INFO,
    SUCCESS,
    WARNING,
    ERROR
}

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
}
```

### `app\src\main\java\com\example\pdf_img_tools_app\navigation\AppDestinations.kt`

```kt
package com.example.pdf_img_tools_app.navigation

/**
 * Navigation destinations for the app
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
}
```

### `app\src\main\java\com\example\pdf_img_tools_app\service\ImageResizeService.kt`

```kt
package com.example.pdf_img_tools_app.service

import android.content.ContentValues
import android.content.Context
import android.graphics.Bitmap
import android.graphics.BitmapFactory
import android.graphics.Matrix
import android.net.Uri
import android.os.Build
import android.os.Environment
import android.provider.MediaStore
import androidx.core.content.FileProvider
import com.example.pdf_img_tools_app.model.ResizedImage
import com.example.pdf_img_tools_app.service.ImageFormat
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import java.io.File
import java.io.FileOutputStream
import java.io.InputStream
import java.io.OutputStream
import java.text.SimpleDateFormat
import java.util.Date
import java.util.Locale

/**
 * Service responsible for handling image resizing operations
 */
class ImageResizeService(private val context: Context) {

    companion object {
        private const val APP_FOLDER_NAME = "ImageResizer"
        private const val MAX_PREVIEW_DIMENSION = 1080 // Max dimension for preview to avoid OOM
        private const val QUALITY = 90 // JPEG quality for saving
        
        // Supported image formats
        private val SUPPORTED_FORMATS = listOf("jpg", "jpeg", "png", "webp")
    }

    /**
     * Resizes the image at the given URI to the specified dimensions and format
     * @param canvasState Optional canvas state to apply transformations from the UI preview
     */
    suspend fun resizeImage(
        imageUri: Uri, 
        targetWidth: Int, 
        targetHeight: Int,
        format: ImageFormat = ImageFormat.JPG,
        canvasState: com.example.pdf_img_tools_app.ui.components.ImageCanvasState? = null
    ): ResizedImage = withContext(Dispatchers.IO) {
        var inputStream: InputStream? = null
        var inputStream2: InputStream? = null
        var bitmap: Bitmap? = null
        var outputStream: FileOutputStream? = null
        
        try {
            // Get input stream from URI
            inputStream = context.contentResolver.openInputStream(imageUri)
            
            // Get original bitmap dimensions first (without loading the full bitmap)
            val options = BitmapFactory.Options().apply {
                inJustDecodeBounds = true
            }
            BitmapFactory.decodeStream(inputStream, null, options)
            inputStream?.close()
            
            val originalWidth = options.outWidth
            val originalHeight = options.outHeight
            val originalSizeBits = getFileSizeFromUri(imageUri)
            
            // Get input stream again
            inputStream2 = context.contentResolver.openInputStream(imageUri)
            
            // Sample down the bitmap if it's too large to prevent OutOfMemoryError
            val inSampleSize = calculateInSampleSize(originalWidth, originalHeight, targetWidth, targetHeight)
            
            // Load the bitmap with sampling
            val decodingOptions = BitmapFactory.Options().apply {
                this.inSampleSize = inSampleSize
                this.inPreferredConfig = Bitmap.Config.ARGB_8888
            }
            
            // Load bitmap with sampling
            bitmap = BitmapFactory.decodeStream(inputStream2, null, decodingOptions)
            inputStream2?.close()
            inputStream2 = null
            
            if (bitmap == null) {
                return@withContext ResizedImage(imageUri)
            }
            
            // Apply canvas transformations (scale, rotate, flip) to match what the user sees
            // Also pass the format to ensure the correct background is used (transparent for PNG, white for JPG)
            val transformedBitmap = applyCanvasTransformations(bitmap, canvasState, targetWidth, targetHeight, format)
            
            // If a new bitmap was created during transformation, recycle the old one
            if (transformedBitmap != bitmap) {
                bitmap.recycle()
                bitmap = transformedBitmap
            }
            
            // Save the resized image to file
            val outputFile = createOutputFile(format)
            outputStream = FileOutputStream(outputFile)
            
            // Use the specified output format
            val outputFormat = when (format) {
                ImageFormat.PNG -> Bitmap.CompressFormat.PNG
                else -> Bitmap.CompressFormat.JPEG
            }
            
            // For PNG format with transparency, ensure we have an alpha channel
            if (format == ImageFormat.PNG && bitmap.config != Bitmap.Config.ARGB_8888) {
                val newBitmap = bitmap.copy(Bitmap.Config.ARGB_8888, true)
                bitmap.recycle()
                bitmap = newBitmap
            }

            if (bitmap != null) {
                bitmap!!.compress(outputFormat, QUALITY, outputStream)
            }
            outputStream.flush()
            outputStream.close()
            
            // Add to media store if SDK >= Q (Android 10)
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
                addImageToMediaStore(outputFile, outputFormat)
            }
            
            // Get final bitmap dimensions and file size
            val finalWidth = bitmap?.width ?: 0
            val finalHeight = bitmap?.height ?: 0
            val finalSize = outputFile.length()
            
            // Recycle bitmap to free memory immediately
            bitmap?.recycle()
            bitmap = null // Explicitly set to null after recycling
            
            // Create and return ResizedImage object
            ResizedImage(
                originalUri = imageUri,
                resizedImageFile = outputFile,
                width = finalWidth,
                height = finalHeight,
                originalWidth = originalWidth,
                originalHeight = originalHeight,
                sizeBefore = originalSizeBits,
                sizeAfter = finalSize
            )
        } catch (e: Exception) {
            e.printStackTrace()
            return@withContext ResizedImage(imageUri)
        } finally {
            // Clean up resources in finally block
            try {
                inputStream?.close()
                inputStream2?.close()
                outputStream?.close()
                bitmap?.recycle()
            } catch (e: Exception) {
                e.printStackTrace()
            }
        }
    }

    /**
     * Creates a downsized preview bitmap to avoid OutOfMemoryError
     */
    suspend fun createImagePreview(imageUri: Uri): Bitmap? = withContext(Dispatchers.IO) {
        var inputStream: InputStream? = null
        var inputStream2: InputStream? = null
        
        try {
            inputStream = context.contentResolver.openInputStream(imageUri)
            
            // Get bitmap dimensions first
            val options = BitmapFactory.Options().apply {
                inJustDecodeBounds = true
            }
            BitmapFactory.decodeStream(inputStream, null, options)
            inputStream?.close()
            inputStream = null
            
            // Calculate sample size to load a preview version
            val largestDimension = maxOf(options.outWidth, options.outHeight)
            val inSampleSize = maxOf(1, largestDimension / MAX_PREVIEW_DIMENSION)
            
            // Load the preview bitmap
            inputStream2 = context.contentResolver.openInputStream(imageUri)
            val previewOptions = BitmapFactory.Options().apply {
                this.inSampleSize = inSampleSize
                this.inPreferredConfig = Bitmap.Config.RGB_565  // Use less memory for previews
            }
            
            val previewBitmap = BitmapFactory.decodeStream(inputStream2, null, previewOptions)
            inputStream2?.close()
            inputStream2 = null
            
            previewBitmap
        } catch (e: Exception) {
            e.printStackTrace()
            null
        } finally {
            try {
                inputStream?.close()
                inputStream2?.close()
            } catch (e: Exception) {
                e.printStackTrace()
            }
        }
    }
    
    /**
     * Checks if the file type is supported for resizing
     */
    fun isSupportedFormat(uri: Uri): Boolean {
        val fileName = getFileNameFromUri(uri)?.lowercase(Locale.ROOT) ?: return false
        return SUPPORTED_FORMATS.any { fileName.endsWith(".$it") }
    }
    
    /**
     * Calculates appropriate sample size for initial bitmap loading
     */
    private fun calculateInSampleSize(
        originalWidth: Int,
        originalHeight: Int,
        targetWidth: Int,
        targetHeight: Int
    ): Int {
        var inSampleSize = 1
        
        if (originalHeight > targetHeight || originalWidth > targetWidth) {
            val halfHeight = originalHeight / 2
            val halfWidth = originalWidth / 2
            
            // Calculate the largest inSampleSize value that is a power of 2 and keeps both
            // height and width larger than the requested height and width
            while ((halfHeight / inSampleSize) >= targetHeight && (halfWidth / inSampleSize) >= targetWidth) {
                inSampleSize *= 2
            }
        }
        
        return inSampleSize
    }
    
    /**
     * Scales bitmap to target dimensions
     */
    private fun scaleBitmap(bitmap: Bitmap, targetWidth: Int, targetHeight: Int): Bitmap {
        val width = bitmap.width
        val height = bitmap.height
        
        // If source dimensions match target dimensions, return original
        if (width == targetWidth && height == targetHeight) {
            return bitmap
        }
        
        // Create matrix for scaling
        val scaleMatrix = Matrix()
        val scaleX = targetWidth.toFloat() / width
        val scaleY = targetHeight.toFloat() / height
        scaleMatrix.setScale(scaleX, scaleY)
        
        // Create and return the scaled bitmap
        return Bitmap.createBitmap(bitmap, 0, 0, width, height, scaleMatrix, true)
    }
    
    /**
     * Applies canvas transformations (scale, translate, rotate, flip) to bitmap
     * to ensure the exported image matches EXACTLY what the user sees on screen
     * Creates a new bitmap with exact target dimensions and draws the transformed image onto it
     * with proper background (transparent for PNG, white for JPG)
     */
    private fun applyCanvasTransformations(
        bitmap: Bitmap, 
        canvasState: com.example.pdf_img_tools_app.ui.components.ImageCanvasState?, 
        targetWidth: Int, 
        targetHeight: Int,
        format: ImageFormat = ImageFormat.JPG
    ): Bitmap {
        // Create a new bitmap of the exact canvas dimensions
        val config = Bitmap.Config.ARGB_8888  // Always use ARGB_8888 for best quality
        val outputBitmap = Bitmap.createBitmap(targetWidth, targetHeight, config)
        
        // Create a canvas to draw on the new bitmap
        val canvas = android.graphics.Canvas(outputBitmap)
        
        // Fill with background color (white for JPG, transparent for PNG)
        if (format != ImageFormat.PNG) {
            canvas.drawColor(android.graphics.Color.WHITE)
        } else {
            // For PNG, we leave it transparent by default
            canvas.drawColor(android.graphics.Color.TRANSPARENT)
        }
        
        // Get original dimensions
        val originalWidth = bitmap.width
        val originalHeight = bitmap.height
        
        if (canvasState == null) {
            // If no canvas state provided, center the image at its original size
            val left = (targetWidth - originalWidth) / 2f
            val top = (targetHeight - originalHeight) / 2f
            
            // Draw the bitmap centered on the canvas
            canvas.drawBitmap(bitmap, left, top, null)
            return outputBitmap
        }
        
        // Create a transformation matrix that exactly matches what the user sees on screen
        val matrix = Matrix()
        
        // Apply scaling exactly as specified in canvas state
        val scaleX = if (canvasState.isFlippedHorizontally) -canvasState.scale else canvasState.scale
        val scaleY = if (canvasState.isFlippedVertically) -canvasState.scale else canvasState.scale
        matrix.setScale(scaleX, scaleY)
        
        // Apply rotation if needed
        if (canvasState.rotation != 0f) {
            // Rotate around the center of the bitmap
            val px = originalWidth / 2f
            val py = originalHeight / 2f
            matrix.preRotate(canvasState.rotation, px, py)
        }
        
        // Create the transformed bitmap using the matrix with the original dimensions
        val transformedBitmap = Bitmap.createBitmap(bitmap, 0, 0, originalWidth, originalHeight, matrix, true)
        
        // Apply the exact offset from the user's canvas
        // This ensures the image appears exactly where the user positioned it
        // The canvas offset represents the position in the canvas coordinate system
        val offsetX = canvasState.offset.x
        val offsetY = canvasState.offset.y
        
        // Calculate where to draw the bitmap based on its center position
        // First, find the center of the target canvas
        val targetCenterX = targetWidth / 2f
        val targetCenterY = targetHeight / 2f
        
        // Then calculate where to draw the top-left corner of the bitmap
        // to place its center at the target center plus the offset
        val drawX = targetCenterX - (transformedBitmap.width / 2f) + offsetX
        val drawY = targetCenterY - (transformedBitmap.height / 2f) + offsetY
        
        // Draw the transformed bitmap onto the canvas at the exact position
        canvas.drawBitmap(transformedBitmap, drawX, drawY, null)
        
        // Clean up if we created a new bitmap
        if (transformedBitmap != bitmap) {
            transformedBitmap.recycle()
        }
        
        return outputBitmap
    }
    
    /**
     * Creates an output file for saving a resized image
     */
    private fun createOutputFile(format: ImageFormat = ImageFormat.JPG): File {
        // Create app-specific folder if it doesn't exist
        val storageDir = File(Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_PICTURES), APP_FOLDER_NAME)
        if (!storageDir.exists()) {
            storageDir.mkdirs()
        }
        
        // Create unique filename based on timestamp with the correct extension
        val timestamp = SimpleDateFormat("yyyyMMdd_HHmmss", Locale.getDefault()).format(Date())
        return File(storageDir, "IMG_${timestamp}.${format.extension}")
    }
    
    /**
     * Gets file name from URI
     */
    private fun getFileNameFromUri(uri: Uri): String? {
        var result: String? = null
        
        if (uri.scheme == "content") {
            val projection = arrayOf(MediaStore.Images.Media.DISPLAY_NAME)
            context.contentResolver.query(uri, projection, null, null, null)?.use { cursor ->
                if (cursor.moveToFirst()) {
                    val nameIndex = cursor.getColumnIndex(MediaStore.Images.Media.DISPLAY_NAME)
                    if (nameIndex >= 0) {
                        result = cursor.getString(nameIndex)
                    }
                }
            }
        }
        
        if (result == null) {
            result = uri.path?.let { File(it).name }
        }
        
        return result
    }
    
    /**
     * Gets file size from URI
     */
    private fun getFileSizeFromUri(uri: Uri): Long {
        var fileSize: Long = 0
        
        try {
            context.contentResolver.query(uri, null, null, null, null)?.use { cursor ->
                if (cursor.moveToFirst()) {
                    val sizeIndex = cursor.getColumnIndex(MediaStore.Images.Media.SIZE)
                    if (sizeIndex != -1) {
                        fileSize = cursor.getLong(sizeIndex)
                    }
                }
            }
            
            // If we couldn't get the size through the ContentResolver
            if (fileSize == 0L) {
                context.contentResolver.openInputStream(uri)?.use { inputStream ->
                    fileSize = inputStream.available().toLong()
                }
            }
        } catch (e: Exception) {
            e.printStackTrace()
        }
        
        return fileSize
    }
    
    /**
     * Adds the saved image to the MediaStore on Android 10+ (API 29+)
     */
    private fun addImageToMediaStore(imageFile: File, format: Bitmap.CompressFormat) {
        val mimeType = when (format) {
            Bitmap.CompressFormat.JPEG -> "image/jpeg"
            Bitmap.CompressFormat.PNG -> "image/png"
            else -> if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R) {
                when (format) {
                    Bitmap.CompressFormat.WEBP_LOSSLESS, 
                    Bitmap.CompressFormat.WEBP_LOSSY -> "image/webp"
                    else -> "image/jpeg"
                }
            } else {
                "image/webp"
            }
        }
        
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
            val contentValues = ContentValues().apply {
                put(MediaStore.Images.Media.DISPLAY_NAME, imageFile.name)
                put(MediaStore.Images.Media.MIME_TYPE, mimeType)
                put(MediaStore.Images.Media.RELATIVE_PATH, "${Environment.DIRECTORY_PICTURES}/${APP_FOLDER_NAME}")
                put(MediaStore.Images.Media.IS_PENDING, 1)
            }
            
            val uri = context.contentResolver.insert(MediaStore.Images.Media.EXTERNAL_CONTENT_URI, contentValues)
            
            uri?.let { imageUri ->
                context.contentResolver.openOutputStream(imageUri)?.use { outputStream ->
                    copyFile(imageFile, outputStream)
                }
                
                // Now update the is_pending flag to publish
                contentValues.clear()
                contentValues.put(MediaStore.Images.Media.IS_PENDING, 0)
                context.contentResolver.update(imageUri, contentValues, null, null)
            }
        }
    }
    
    /**
     * Utility function to copy file content to output stream
     */
    private fun copyFile(sourceFile: File, outputStream: OutputStream) {
        sourceFile.inputStream().use { input ->
            val buffer = ByteArray(4 * 1024) // 4KB buffer
            var read: Int
            while (input.read(buffer).also { read = it } != -1) {
                outputStream.write(buffer, 0, read)
            }
            outputStream.flush()
        }
    }
    
    /**
     * Get original image dimensions without loading the entire bitmap
     */
    suspend fun getImageDimensions(imageUri: Uri): Pair<Int, Int> = withContext(Dispatchers.IO) {
        try {
            val inputStream = context.contentResolver.openInputStream(imageUri)
            
            val options = BitmapFactory.Options().apply {
                inJustDecodeBounds = true
            }
            
            BitmapFactory.decodeStream(inputStream, null, options)
            inputStream?.close()
            
            Pair(options.outWidth, options.outHeight)
        } catch (e: Exception) {
            e.printStackTrace()
            Pair(0, 0)
        }
    }
}
```

### `app\src\main\java\com\example\pdf_img_tools_app\service\ImageService.kt`

```kt
package com.example.pdf_img_tools_app.service

import android.content.Context
import android.graphics.Bitmap
import android.graphics.BitmapFactory
import android.graphics.Matrix
import android.net.Uri
import com.example.pdf_img_tools_app.utils.FileUtils
import id.zelory.compressor.Compressor
import id.zelory.compressor.constraint.quality
import id.zelory.compressor.constraint.resolution
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.async
import kotlinx.coroutines.awaitAll
import kotlinx.coroutines.coroutineScope
import kotlinx.coroutines.withContext
import java.io.ByteArrayOutputStream
import java.io.File
import java.io.FileOutputStream
import java.io.IOException
import java.io.InputStream
import java.io.OutputStream

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
        if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.R) 
            Bitmap.CompressFormat.WEBP_LOSSY 
        else
            @Suppress("DEPRECATION") Bitmap.CompressFormat.WEBP,
        "WebP (Lossy)", true
    ),
    WEBP_LOSSLESS("webp", "image/webp", 
        if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.R) 
            Bitmap.CompressFormat.WEBP_LOSSLESS 
        else 
            @Suppress("DEPRECATION") Bitmap.CompressFormat.WEBP,
        "WebP (Lossless)", true
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
            return android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.R
        }
    }
}

/**
 * Service for image operations
 */
class ImageService(private val context: Context) {

    /**
     * Compress multiple images concurrently, attempting to preserve original format or defaulting to JPG.
     * @param inputUris List of URIs for input images
     * @param quality Compression quality (0-100), primarily affects JPG/WEBP
     * @return Result containing a Map of original Uri to the compressed temporary File (or null if compression failed)
     */
    suspend fun compressImages(
        inputUris: List<Uri>,
        quality: Int = 80 
    ): Result<Map<Uri, File?>> = coroutineScope { 
        try {
            val results = inputUris.map { uri ->
                async(Dispatchers.IO) { 
                    // Pass null format to let internal function detect or default
                    uri to compressSingleImageInternal(uri, quality, null) 
                }
            }.awaitAll() 
            val resultMap = results.associate { it } 
            Result.success(resultMap)
        } catch (e: Exception) {
            Result.failure(e)
        }
    }

    /**
     * Internal function to compress a single image. Detects format or defaults to JPG.
     * Returns the temporary compressed file or null on failure.
     */
    private suspend fun compressSingleImageInternal(
        inputUri: Uri,
        quality: Int,
        // Format is optional: if null, detect from input; default to JPG if detection fails
        targetFormat: ImageFormat? = null 
    ): File? { 
        var tempInputFile: File? = null
        var tempCompressedFile: File? = null
        var finalTempFile: File? = null
        var success = false

        // Determine the output format
        val outputFormat = targetFormat ?: 
            FileUtils.getMimeType(context, inputUri)?.let { ImageFormat.fromMimeType(it) } ?: 
            ImageFormat.JPG // Default to JPG if detection fails

        try {
            context.contentResolver.openInputStream(inputUri)?.use { inputStream ->
                tempInputFile = FileUtils.createTempFile(context, "compress_in_", ".tmp")
                tempInputFile?.let { file ->
                    FileOutputStream(file).use { outputStream -> inputStream.copyTo(outputStream) }
                } ?: throw IOException("Failed to create temp input file for $inputUri")
            } ?: throw IOException("Cannot open input stream for $inputUri")

            tempCompressedFile = Compressor.compress(context, tempInputFile!!) { quality(quality) }

            val compressedBitmap = BitmapFactory.decodeFile(tempCompressedFile.path)
                ?: throw IOException("Failed to decode compressed bitmap for $inputUri")
            
            finalTempFile = FileUtils.createTempFile(context, "compress_out_", ".${outputFormat.extension}")
                 ?: throw IOException("Failed to create final temp output file for $inputUri")

            FileOutputStream(finalTempFile).use { os ->
                 // Use the determined output format for compression
                compressedBitmap.compress(outputFormat.compressFormat, quality, os)
            }
            compressedBitmap.recycle()
            success = true
            return finalTempFile

        } catch (e: Exception) {
            println("Error compressing image $inputUri: ${e.message}")
            // Ensure partial temp files are deleted on error before returning null
            finalTempFile?.delete()
            return null
        } finally {
            tempInputFile?.delete()
            if (tempCompressedFile != null && tempCompressedFile != finalTempFile && !success) {
                 tempCompressedFile.delete()
            }
        }
    }
    
    /**
     * Resize an image
     * @param format Optional: Output format. Defaults to JPG if null.
     */
    suspend fun resizeImage(
        inputUri: Uri,
        outputFile: File,
        targetWidth: Int,
        targetHeight: Int,
        preserveAspectRatio: Boolean = true,
        format: ImageFormat? = ImageFormat.JPG, // Make format optional, default JPG
        quality: Int = 90
    ): Result<File> = withContext(Dispatchers.IO) {
        var inputStream: InputStream? = null
        var bitmap: Bitmap? = null
        var resizedBitmap: Bitmap? = null
        
        try {
            // Open input stream only once and copy to temp file if needed
            inputStream = context.contentResolver.openInputStream(inputUri)
                ?: return@withContext Result.failure(Exception("Cannot open input file: $inputUri"))
            
            // First get the dimensions without loading the full bitmap
            val options = BitmapFactory.Options().apply { 
                inJustDecodeBounds = true 
            }
            BitmapFactory.decodeStream(inputStream, null, options)
            inputStream.close()
            
            val srcWidth = options.outWidth
            val srcHeight = options.outHeight
            
            if (srcWidth <= 0 || srcHeight <= 0) {
                return@withContext Result.failure(Exception("Could not decode image bounds for: $inputUri"))
            }
            
            // Calculate target size
            val (width, height) = calculateTargetSize(
                srcWidth, srcHeight, targetWidth, targetHeight, preserveAspectRatio
            )
            
            if (width <= 0 || height <= 0) {
                return@withContext Result.failure(Exception("Invalid target dimensions calculated: ${width}x${height}"))
            }
            
            // Reopen stream to load the actual bitmap
            inputStream = context.contentResolver.openInputStream(inputUri)
                ?: return@withContext Result.failure(Exception("Cannot reopen input file for decoding: $inputUri"))
            
            // Now load the full bitmap with calculated inSampleSize if needed
            options.apply {
                inJustDecodeBounds = false
                // Calculate inSampleSize for memory efficiency if image is large
                if (srcWidth > width * 2 && srcHeight > height * 2) {
                    inSampleSize = Math.min(srcWidth / width, srcHeight / height)
                }
            }
            
            bitmap = BitmapFactory.decodeStream(inputStream, null, options)
                ?: return@withContext Result.failure(Exception("Failed to decode bitmap from input: $inputUri"))
            
            // Create resized bitmap
            resizedBitmap = Bitmap.createScaledBitmap(bitmap, width, height, true)
            
            // Determine final output format (use provided or default to JPG)
            val outputFormat = format ?: ImageFormat.JPG
            
            // Save to output file
            FileOutputStream(outputFile).use { os ->
                resizedBitmap.compress(outputFormat.compressFormat, quality, os)
            }
            
            return@withContext Result.success(outputFile)
        } catch (e: Exception) {
            println("Error resizing image $inputUri: ${e.message}")
            return@withContext Result.failure(e)
        } finally {
            // Clean up resources in finally block
            try {
                inputStream?.close()
                bitmap?.recycle()
                if (resizedBitmap != bitmap) {
                    resizedBitmap?.recycle()
                }
            } catch (e: Exception) {
                // Ignore cleanup errors
            }
        }
    }
    
    /**
     * Convert image format
     */
    suspend fun convertImageFormat(
        inputUri: Uri,
        outputFile: File,
        format: ImageFormat, 
        quality: Int = 90
    ): Result<File> = withContext(Dispatchers.IO) {
        try {
             val bitmap = context.contentResolver.openInputStream(inputUri)?.use { inputStream ->
                  BitmapFactory.decodeStream(inputStream)
             } ?: return@withContext Result.failure(Exception("Cannot open input stream for conversion: $inputUri"))
            
             // Check for WebP format on older Android versions
             if (!ImageFormat.isWebpTypeSupported() && 
                 (format == ImageFormat.WEBP_LOSSY || format == ImageFormat.WEBP_LOSSLESS)) {
                 println("Warning: Using legacy WebP format on Android < 11")
             }
            
             FileOutputStream(outputFile).use { os ->
                  bitmap.compress(format.compressFormat, quality, os)
             }
             bitmap.recycle()
            
             return@withContext Result.success(outputFile)
        } catch (e: Exception) {
             println("Error converting image $inputUri: ${e.message}")
            return@withContext Result.failure(e)
        }
    }

    // --- Helpers --- 
     private fun copyStream(input: InputStream, output: OutputStream) { // Keep this if needed by other logic (though internal compress doesn't use it directly anymore)
         val buffer = ByteArray(1024)
         var bytesRead: Int
         while (input.read(buffer).also { bytesRead = it } != -1) {
             output.write(buffer, 0, bytesRead)
         }
     }
 
     private fun calculateTargetSize(
         srcWidth: Int,
         srcHeight: Int,
         targetWidth: Int,
         targetHeight: Int,
         preserveAspectRatio: Boolean
     ): Pair<Int, Int> {
         var width = if (targetWidth <= 0) srcWidth else targetWidth
         var height = if (targetHeight <= 0) srcHeight else targetHeight
         
         if (preserveAspectRatio && srcWidth > 0 && srcHeight > 0) { 
             val srcRatio = srcWidth.toFloat() / srcHeight.toFloat()
 
             if (targetWidth <= 0 && targetHeight > 0) { // Height is driving factor
                  width = (targetHeight * srcRatio).toInt()
                  height = targetHeight
             } else if (targetWidth > 0 && targetHeight <= 0) { // Width is driving factor
                  width = targetWidth
                  height = (targetWidth / srcRatio).toInt()
             } else if (targetWidth > 0 && targetHeight > 0) { // Both specified, fit within bounds
                  val targetRatio = targetWidth.toFloat() / targetHeight.toFloat()
                  if (targetRatio > srcRatio) { 
                       width = (targetHeight * srcRatio).toInt()
                       height = targetHeight
                  } else { 
                       height = (targetWidth / srcRatio).toInt()
                       width = targetWidth
                  }
             } 
             // else case: if both targetW and targetH are <= 0, initial width/height (srcW/srcH) are used
         } 
         // Ensure minimum dimensions
         return Pair(width.coerceAtLeast(1), height.coerceAtLeast(1))
    }
} ```

### `app\src\main\java\com\example\pdf_img_tools_app\service\PdfService.kt`

```kt
package com.example.pdf_img_tools_app.service

import android.content.Context
import android.graphics.Bitmap
import android.graphics.Canvas
import android.graphics.Color
import android.net.Uri
import android.util.Log
import com.tom_roush.pdfbox.android.PDFBoxResourceLoader
import com.tom_roush.pdfbox.io.MemoryUsageSetting
import com.tom_roush.pdfbox.multipdf.PDFMergerUtility
import com.tom_roush.pdfbox.pdmodel.PDDocument
import com.tom_roush.pdfbox.pdmodel.PDPage
import com.tom_roush.pdfbox.pdmodel.PDPageContentStream
import com.tom_roush.pdfbox.pdmodel.PDResources
import com.tom_roush.pdfbox.pdmodel.common.PDRectangle
import com.tom_roush.pdfbox.pdmodel.graphics.image.JPEGFactory
import com.tom_roush.pdfbox.pdmodel.graphics.image.LosslessFactory
import com.tom_roush.pdfbox.pdmodel.graphics.image.PDImageXObject
import com.tom_roush.pdfbox.rendering.ImageType
import com.tom_roush.pdfbox.rendering.PDFRenderer
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import java.io.File
import java.io.FileOutputStream
import java.io.InputStream
import kotlin.math.min

/**
 * Service for PDF operations using PdfBox-Android
 */
class PdfService(private val context: Context) {

    init {
        // Initialize PDFBox
        PDFBoxResourceLoader.init(context)
    }

    /**
     * Compress a PDF file
     * @param inputFile Input PDF file
     * @param compressionLevel JPEG quality for images (0-100)
     * @param compressionMode Determines how the PDF should be compressed
     * @param onProgressUpdate Callback for progress updates (0-1)
     * @return Success or error message
     */
    suspend fun compressPdf(
        inputFile: File,
        compressionLevel: Int = 80,
        compressionMode: CompressionMode = CompressionMode.AUTO,
        onProgressUpdate: ((Float) -> Unit)? = null
    ): Result<File> = withContext(Dispatchers.IO) {
        var sourceDoc: PDDocument? = null
        val outputFile = File.createTempFile("compressed_temp", ".pdf", context.cacheDir)

        try {
            // Set memory usage settings
            val memUsage = MemoryUsageSetting.setupMixed(50 * 1024 * 1024)
                .setTempDir(context.cacheDir)

            sourceDoc = PDDocument.load(inputFile, memUsage)
            val pageCount = sourceDoc.numberOfPages

            // Calculate file size in KB
            val fileSizeKB = inputFile.length() / 1024

            // Determine compression mode if AUTO was selected
            val resolvedMode = when (compressionMode) {
                CompressionMode.AUTO -> {
                    // For small files (under 300KB), use METADATA_ONLY to prevent size increase
                    if (fileSizeKB < 300) {
                        Log.d("PdfService", "Small file detected (${fileSizeKB}KB), using METADATA_ONLY mode")
                        CompressionMode.METADATA_ONLY
                    } else {
                        // Check if we can detect images in the PDF
                        val hasImages = detectPdfHasImages(sourceDoc)
                        if (hasImages) {
                            // If it has images, use SMART mode
                            Log.d("PdfService", "Images detected in file, using SMART mode")
                            CompressionMode.SMART
                        } else {
                            // If no images detected, just optimize metadata
                            Log.d("PdfService", "No images detected, using METADATA_ONLY mode")
                            CompressionMode.METADATA_ONLY
                        }
                    }
                }
                else -> compressionMode
            }

            // Apply compression based on resolved mode
            return@withContext when (resolvedMode) {
                CompressionMode.METADATA_ONLY -> {
                    optimizeMetadataOnly(sourceDoc, outputFile, onProgressUpdate)
                }
                CompressionMode.SMART -> {
                    smartCompressPdf(sourceDoc, outputFile, compressionLevel, onProgressUpdate)
                }
                CompressionMode.RASTERIZE -> {
                    rasterizeAndCompressPdf(sourceDoc, outputFile, compressionLevel, onProgressUpdate)
                }
                else -> {
                    // Should never reach here as AUTO is resolved above
                    optimizeMetadataOnly(sourceDoc, outputFile, onProgressUpdate)
                }
            }
        } catch (e: OutOfMemoryError) {
            return@withContext Result.failure(Exception("The PDF is too large to compress. Try using a lower quality setting.", e))
        } catch (e: Exception) {
            return@withContext Result.failure(e)
        } finally {
            try {
                sourceDoc?.close()
            } catch (e: Exception) {
                // Ignore cleanup errors
            }
        }
    }

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
    }

    /**
     * Detects if a PDF contains images
     */
    private fun detectPdfHasImages(doc: PDDocument): Boolean {
        try {
            // Sample a few pages to check for images
            val pagesToCheck = minOf(doc.numberOfPages, 5)
            for (i in 0 until pagesToCheck) {
                val page = doc.getPage(i)
                val resources = page.resources

                // Check for XObject images
                val xobjects = resources.xObjectNames
                if (xobjects != null) {
                    for (name in xobjects) {
                        val xobject = resources.getXObject(name)
                        if (xobject is PDImageXObject) {
                            return true
                        }
                    }
                }
            }
            return false
        } catch (e: Exception) {
            // If there's an error checking, assume it has images to be safe
            Log.e("PdfService", "Error detecting images: ${e.message}")
            return true
        }
    }

    /**
     * Simple metadata optimization without changing content
     * Used for already small/optimized files
     */
    private suspend fun optimizeMetadataOnly(
        sourceDoc: PDDocument,
        outputFile: File,
        onProgressUpdate: ((Float) -> Unit)?
    ): Result<File> = withContext(Dispatchers.IO) {
        try {
            // Progress update at beginning
            onProgressUpdate?.invoke(0.2f)

            // Remove unnecessary metadata safely
            try {
                // Some PDFs might not have document information
                if (sourceDoc.documentInformation != null) {
                    // Create an empty document information dictionary instead of setting to null
                    sourceDoc.documentInformation = PDDocument().documentInformation
                }

                // Remove metadata stream if it exists
                if (sourceDoc.documentCatalog != null && sourceDoc.documentCatalog.metadata != null) {
                    sourceDoc.documentCatalog.metadata = null
                }
            } catch (e: Exception) {
                // Ignore if metadata removal fails
                Log.e("PdfService", "Error removing metadata: ${e.message}")
            }

            // Progress update before saving
            onProgressUpdate?.invoke(0.8f)

            // Save with optimization flags
            sourceDoc.save(outputFile)
            onProgressUpdate?.invoke(1.0f)

            Log.d("PdfService", "Metadata-only optimization completed")
            return@withContext Result.success(outputFile)
        } catch (e: Exception) {
            Log.e("PdfService", "Error in metadata optimization: ${e.message}")
            return@withContext Result.failure(e)
        }
    }

    /**
     * Smart compression that preserves vector content while compressing images
     */
    private suspend fun smartCompressPdf(
        sourceDoc: PDDocument,
        outputFile: File,
        compressionLevel: Int,
        onProgressUpdate: ((Float) -> Unit)?
    ): Result<File> = withContext(Dispatchers.IO) {
        var tempDoc: PDDocument? = null

        try {
            // Create a new document to hold optimized content
            tempDoc = PDDocument()
            val pageCount = sourceDoc.numberOfPages

            // Copy each page with selective image optimization
            for (i in 0 until pageCount) {
                // Report progress
                onProgressUpdate?.invoke(i.toFloat() / pageCount * 0.8f)

                // Copy page structure from source, preserving all vectors and text
                val sourcePage = sourceDoc.getPage(i)
                val newPage = tempDoc.importPage(sourcePage)

                // Copy and compress images in resources
                // Note: This is a simplified approach - a real solution would need to
                // access and replace each image in the page's content stream
                optimizePageResources(tempDoc, newPage.resources, compressionLevel)
            }

            // Remove metadata safely
            try {
                // Some PDFs might not have document information
                if (tempDoc.documentInformation != null) {
                    // Create an empty document information dictionary instead of setting to null
                    tempDoc.documentInformation = PDDocument().documentInformation
                }

                // Remove metadata stream if it exists
                if (tempDoc.documentCatalog != null && tempDoc.documentCatalog.metadata != null) {
                    tempDoc.documentCatalog.metadata = null
                }
            } catch (e: Exception) {
                // Ignore if metadata removal fails
                Log.e("PdfService", "Error removing metadata: ${e.message}")
            }

            // Progress update before saving
            onProgressUpdate?.invoke(0.9f)

            // Save optimized document
            tempDoc.save(outputFile)
            tempDoc.close()

            onProgressUpdate?.invoke(1.0f)
            Log.d("PdfService", "Smart PDF compression completed")
            return@withContext Result.success(outputFile)
        } catch (e: Exception) {
            Log.e("PdfService", "Error in smart compression: ${e.message}")
            return@withContext Result.failure(e)
        } finally {
            tempDoc?.close()
        }
    }

    /**
     * Optimize page resources by compressing images
     */
    private fun optimizePageResources(doc: PDDocument, resources: PDResources, compressionLevel: Int) {
        try {
            val xobjectNames = resources.xObjectNames ?: return

            for (name in xobjectNames) {
                try {
                    val xobject = resources.getXObject(name)

                    // Process image XObjects only
                    if (xobject is PDImageXObject) {
                        // Skip if the image is already compressed enough
                        val imageBytes = xobject.image?.byteCount ?: 0
                        if (imageBytes < 5 * 1024) { // Skip small images < 5KB
                            continue
                        }

                        // Get image from XObject
                        val image = xobject.image
                        if (image != null) {
                            // Determine if image has transparency
                            val hasTransparency = hasTransparency(image)

                            // Create replacement image with compression
                            val replacement = if (hasTransparency) {
                                // Use lossless for transparency
                                LosslessFactory.createFromImage(doc, image)
                            } else {
                                // Use JPEG for non-transparent images
                                JPEGFactory.createFromImage(doc, image, compressionLevel / 100f)
                            }

                            // Replace original image with compressed one
                            resources.put(name, replacement)
                        }
                    }
                } catch (e: Exception) {
                    // Log error but continue with other images
                    Log.e("PdfService", "Error optimizing image: ${e.message}")
                }
            }
        } catch (e: Exception) {
            Log.e("PdfService", "Error optimizing resources: ${e.message}")
        }
    }

    /**
     * Full rasterization approach that converts each page to an image
     * Enhanced to properly handle transparency
     */
    private suspend fun rasterizeAndCompressPdf(
        sourceDoc: PDDocument,
        outputFile: File,
        compressionLevel: Int,
        onProgressUpdate: ((Float) -> Unit)?
    ): Result<File> = withContext(Dispatchers.IO) {
        var compressedDoc: PDDocument? = null

        try {
            compressedDoc = PDDocument()
            val renderer = PDFRenderer(sourceDoc)
            val pageCount = sourceDoc.numberOfPages

            // Adaptive DPI based on document size
            val dpi = when {
                pageCount > 50 -> 150f  // Lower DPI for many pages
                else -> 200f  // Higher DPI for better quality
            }

            for (i in 0 until pageCount) {
                // Report progress
                onProgressUpdate?.invoke(i.toFloat() / pageCount * 0.9f)

                try {
                    // Use ARGB to preserve transparency
                    val img = renderer.renderImageWithDPI(i, dpi, ImageType.ARGB)

                    // Create page with original dimensions to preserve aspect ratio
                    val srcPage = sourceDoc.getPage(i)
                    val pageRect = srcPage.cropBox
                    val page = PDPage(PDRectangle(
                        pageRect.width,
                        pageRect.height
                    ))
                    compressedDoc.addPage(page)

                    val contentStream = PDPageContentStream(compressedDoc, page)

                    // Check if the image has any transparent pixels
                    val hasTransparency = hasTransparency(img)

                    // Choose compression based on content
                    val pdImage = if (hasTransparency) {
                        // Use lossless compression for pages with transparency
                        LosslessFactory.createFromImage(compressedDoc, img)
                    } else {
                        // Use JPEG for pages without transparency
                        JPEGFactory.createFromImage(compressedDoc, img, compressionLevel / 100f)
                    }

                    // Draw image to fill the page
                    contentStream.drawImage(pdImage, 0f, 0f, page.mediaBox.width, page.mediaBox.height)
                    contentStream.close()

                    // Recycle bitmap
                    img.recycle()

                    // Force garbage collection after processing each page
                    System.gc()
                } catch (e: OutOfMemoryError) {
                    throw Exception("Page ${i+1} is too large to compress. Try a lower compression quality.")
                }
            }

            // Remove metadata safely
            try {
                // Some PDFs might not have document information
                if (compressedDoc.documentInformation != null) {
                    // Create an empty document information dictionary instead of setting to null
                    compressedDoc.documentInformation = PDDocument().documentInformation
                }

                // Remove metadata stream if it exists
                if (compressedDoc.documentCatalog != null && compressedDoc.documentCatalog.metadata != null) {
                    compressedDoc.documentCatalog.metadata = null
                }
            } catch (e: Exception) {
                // Ignore if metadata removal fails
                Log.e("PdfService", "Error removing metadata: ${e.message}")
            }

            // Final progress update
            onProgressUpdate?.invoke(0.95f)

            // Save the document
            FileOutputStream(outputFile).use { os ->
                compressedDoc.save(os)
            }
            compressedDoc.close()

            onProgressUpdate?.invoke(1.0f)
            Log.d("PdfService", "Rasterize and compress completed")
            return@withContext Result.success(outputFile)
        } catch (e: Exception) {
            Log.e("PdfService", "Error in rasterize compression: ${e.message}")
            return@withContext Result.failure(e)
        } finally {
            compressedDoc?.close()
        }
    }

    /**
     * Check if a bitmap has transparent pixels
     */
    private fun hasTransparency(bitmap: Bitmap): Boolean {
        try {
            // For efficiency, we'll check only a small sample of pixels
            val width = bitmap.width
            val height = bitmap.height

            // Check in 9 regions of the image (4 corners, 4 midpoints, and center)
            val samplePoints = listOf(
                Pair(0, 0),                          // Top-left
                Pair(width / 2, 0),                 // Top-center
                Pair(width - 1, 0),                 // Top-right
                Pair(0, height / 2),                // Middle-left
                Pair(width / 2, height / 2),        // Center
                Pair(width - 1, height / 2),        // Middle-right
                Pair(0, height - 1),                // Bottom-left
                Pair(width / 2, height - 1),        // Bottom-center
                Pair(width - 1, height - 1)         // Bottom-right
            )

            // Also check 20 random pixels for better sampling
            val random = java.util.Random()
            val randomPoints = (1..20).map {
                Pair(random.nextInt(width), random.nextInt(height))
            }

            // Combine fixed and random sample points
            val allPoints = samplePoints + randomPoints

            // Check alpha channel of each point
            for ((x, y) in allPoints) {
                val pixel = bitmap.getPixel(x, y)
                val alpha = Color.alpha(pixel)
                if (alpha < 255) {
                    return true
                }
            }

            return false
        } catch (e: Exception) {
            // If there's an error checking, assume no transparency to be safe
            Log.e("PdfService", "Error checking transparency: ${e.message}")
            return false
        }
    }

    /**
     * Result object for merge operations
     */
    data class MergeResult(
        val file: File,
        val totalPages: Int
    )

    /**
     * Merge multiple PDF files
     * @param context Context for accessing content resolver
     * @param pdfUris List of URIs to merge
     * @param outputFile Output file
     * @param onProgressUpdate Callback for progress updates
     * @return Success with MergeResult or failure
     */
    suspend fun mergePdfFiles(
        context: Context,
        pdfUris: List<Uri>,
        outputFile: File,
        onProgressUpdate: (Int, Int) -> Unit = { _, _ -> }
    ): Result<MergeResult> = withContext(Dispatchers.IO) {
        try {
            // Improved merger that handles transparency properly
            val merger = PDFMergerUtility()
            merger.destinationFileName = outputFile.absolutePath

            // Set memory usage settings with higher limit for complex PDFs
            val memUsage = MemoryUsageSetting.setupMixed(100 * 1024 * 1024)
                .setTempDir(context.cacheDir)

            // Track all open input streams to ensure proper closure
            val openStreams = mutableListOf<InputStream>()
            var totalPages = 0
            var currentFileIndex = 0

            for (uri in pdfUris) {
                try {
                    val inputStream = context.contentResolver.openInputStream(uri)
                        ?: continue

                    // Count pages for progress reporting
                    inputStream.use { stream ->
                        val tempDoc = PDDocument.load(stream)
                        totalPages += tempDoc.numberOfPages
                        tempDoc.close()
                    }

                    // Reopen stream for merger
                    val newStream = context.contentResolver.openInputStream(uri)
                        ?: continue

                    // Add to our list of streams to close later
                    openStreams.add(newStream)

                    // Add source to merger
                    merger.addSource(newStream)

                    // Report progress
                    currentFileIndex++
                    onProgressUpdate(currentFileIndex, pdfUris.size)
                } catch (e: Exception) {
                    // Log the error but continue with other files
                    Log.e("PdfService", "Error adding PDF: ${e.message}")
                }
            }

            try {
                // Merge documents with memory settings
                merger.mergeDocuments(memUsage)

                return@withContext Result.success(MergeResult(outputFile, totalPages))
            } finally {
                // Clean up all open streams
                openStreams.forEach { stream ->
                    try {
                        stream.close()
                    } catch (e: Exception) {
                        // Ignore closure errors
                    }
                }
            }
        } catch (e: Exception) {
            Log.e("PdfService", "PDF merge error: ${e.message}")
            return@withContext Result.failure(e)
        }
    }

    /**
     * Split a PDF file into multiple files based on page ranges
     * @param inputUri URI of the input PDF
     * @param outputDir Output directory
     * @param ranges List of page ranges to split (1-indexed, inclusive)
     * @return List of output PDF files
     */
    suspend fun splitPdf(
        inputUri: Uri,
        outputDir: File,
        ranges: List<Pair<Int, Int>>
    ): Result<List<File>> = withContext(Dispatchers.IO) {
        var sourceDoc: PDDocument? = null
        val outputFiles = mutableListOf<File>()

        try {
            // Set memory usage settings
            val memUsage = MemoryUsageSetting.setupMixed(50 * 1024 * 1024)
                .setTempDir(context.cacheDir)

            val inputStream = context.contentResolver.openInputStream(inputUri)
                ?: return@withContext Result.failure(Exception("Cannot open input file"))

            sourceDoc = PDDocument.load(inputStream, memUsage)

            for ((index, range) in ranges.withIndex()) {
                // Validate range
                if (range.first < 1 || range.second > sourceDoc.numberOfPages || range.first > range.second) {
                    return@withContext Result.failure(Exception("Invalid page range: ${range.first}-${range.second}"))
                }

                // Create a new document for this range
                val splitDoc = PDDocument()

                try {
                    // Using 0-indexed page numbers internally
                    for (i in range.first - 1 until range.second) {
                        // Import the page to avoid memory issues with direct copying
                        val page = sourceDoc.getPage(i)
                        val importedPage = splitDoc.importPage(page)
                        // Copy any annotations if needed
                        importedPage.annotations = page.annotations
                    }

                    // Save the split document
                    val outputFile = File(outputDir, "split_${index + 1}.pdf")
                    splitDoc.save(outputFile)
                    outputFiles.add(outputFile)

                    // Force garbage collection after each split
                    System.gc()
                } finally {
                    // Close the document to free resources immediately
                    try {
                        splitDoc.close()
                    } catch (e: Exception) {
                        // Ignore cleanup errors
                    }
                }
            }

            return@withContext Result.success(outputFiles)
        } catch (e: OutOfMemoryError) {
            return@withContext Result.failure(Exception("The PDF is too large to split. Try splitting into fewer ranges.", e))
        } catch (e: Exception) {
            return@withContext Result.failure(e)
        } finally {
            try {
                sourceDoc?.close()
            } catch (_: Exception) {
                // Ignore cleanup errors
            }
        }
    }

    /**
     * Convert PDF to images
     * @param inputUri URI of the input PDF
     * @param outputDir Output directory
     * @param dpi DPI for rendering
     * @param format Image format (jpg or png)
     * @return List of output image files
     */
    suspend fun pdfToImages(
        inputUri: Uri,
        outputDir: File,
        dpi: Float = 300f,
        format: String = "jpg"
    ): Result<List<File>> = withContext(Dispatchers.IO) {
        var doc: PDDocument? = null
        val imageFiles = mutableListOf<File>()

        try {
            // Set memory usage settings - increased for complex PDFs
            val memUsage = MemoryUsageSetting.setupMixed(200 * 1024 * 1024)
                .setTempDir(context.cacheDir)

            val inputStream = context.contentResolver.openInputStream(inputUri)
                ?: return@withContext Result.failure(Exception("Cannot open input file"))

            doc = PDDocument.load(inputStream, memUsage)
            val renderer = PDFRenderer(doc)

            // Determine compression format
            val compressFormat = if (format.equals("jpg", ignoreCase = true))
                Bitmap.CompressFormat.JPEG else Bitmap.CompressFormat.PNG

            // Higher quality for JPG to avoid artifacts in text
            val quality = if (format.equals("jpg", ignoreCase = true)) 95 else 100

            for (i in 0 until doc.numberOfPages) {
                try {
                    Log.d("PdfService", "Processing page ${i+1} of ${doc.numberOfPages}")

                    // Get page dimensions based on the PDF's cropbox
                    val page = doc.getPage(i)
                    val pageWidth = (page.cropBox.width * (dpi / 72f)).toInt()
                    val pageHeight = (page.cropBox.height * (dpi / 72f)).toInt()

                    // Ensure reasonable dimensions
                    if (pageWidth <= 0 || pageHeight <= 0 || pageWidth > 10000 || pageHeight > 10000) {
                        Log.e("PdfService", "Invalid page dimensions: $pageWidth x $pageHeight")
                        throw Exception("Invalid page dimensions")
                    }

                    Log.d("PdfService", "Page dimensions: $pageWidth x $pageHeight")

                    // Try multiple rendering approaches
                    var outputBitmap: Bitmap? = null
                    var renderedBitmap: Bitmap? = null

                    // --- APPROACH 1: ARGB rendering for best quality and handling of all content types ---
                    try {
                        // Start with ARGB to better handle transparency and different content types
                        // This improves handling of screenshots and poster-like images
                        Log.d("PdfService", "Starting with ARGB rendering for best quality")
                        outputBitmap = Bitmap.createBitmap(pageWidth, pageHeight, Bitmap.Config.ARGB_8888)
                        val canvas = Canvas(outputBitmap)
                        canvas.drawColor(Color.WHITE) // White background

                        // Render with ARGB for best quality
                        renderedBitmap = renderer.renderImageWithDPI(i, dpi, ImageType.ARGB)

                        // Special handling with an anti-aliasing paint to improve quality
                        val paint = android.graphics.Paint()
                        paint.isFilterBitmap = true
                        paint.isAntiAlias = true
                        canvas.drawBitmap(renderedBitmap, 0f, 0f, paint)

                        // Check if the rendered image contains mostly black pixels (possible failure)
                        if (isBlackBoxProblem(outputBitmap)) {
                            Log.d("PdfService", "Detected potential black box issue, trying alternative rendering")
                            throw Exception("Black box detected")
                        }
                    } catch (e: Exception) {
                        // Clean up failed bitmaps
                        renderedBitmap?.recycle()
                        outputBitmap?.recycle()

                        // --- APPROACH 2: RGB rendering with different settings ---
                        try {
                            Log.d("PdfService", "Trying RGB rendering approach")
                            outputBitmap = Bitmap.createBitmap(pageWidth, pageHeight, Bitmap.Config.ARGB_8888)
                            val canvas = Canvas(outputBitmap)
                            canvas.drawColor(Color.WHITE)

                            renderedBitmap = renderer.renderImageWithDPI(i, dpi, ImageType.RGB)

                            // Use a enhanced paint object with better quality settings
                            val paint = android.graphics.Paint()
                            paint.isFilterBitmap = true
                            paint.isAntiAlias = true
                            paint.isDither = true // Better color handling
                            canvas.drawBitmap(renderedBitmap, 0f, 0f, paint)
                        } catch (e: Exception) {
                            // Clean up failed bitmaps
                            renderedBitmap?.recycle()
                            outputBitmap?.recycle()

                            // --- APPROACH 3: Higher DPI rendering with improved post-processing ---
                            Log.d("PdfService", "Trying enhanced high DPI rendering approach")
                            val higherDpi = dpi * 1.8f // Use an even higher DPI for better quality

                            try {
                                outputBitmap = Bitmap.createBitmap(pageWidth, pageHeight, Bitmap.Config.ARGB_8888)
                                val canvas = Canvas(outputBitmap)
                                canvas.drawColor(Color.WHITE)

                                // Try rendering with ARGB first for best quality at higher resolution
                                renderedBitmap = renderer.renderImageWithDPI(i, higherDpi, ImageType.ARGB)

                                // Scale with high quality downsampling
                                val scaledBitmap = Bitmap.createScaledBitmap(renderedBitmap, pageWidth, pageHeight, true)
                                renderedBitmap.recycle()
                                renderedBitmap = scaledBitmap

                                // Draw with enhanced quality settings
                                val paint = android.graphics.Paint()
                                paint.isFilterBitmap = true
                                paint.isAntiAlias = true
                                paint.isDither = true
                                canvas.drawBitmap(renderedBitmap, 0f, 0f, paint)
                            } catch (e: Exception) {
                                // If all else fails, try one more approach with RGB
                                Log.d("PdfService", "Trying last resort approach")
                                renderedBitmap?.recycle()
                                outputBitmap?.recycle()

                                // Last resort approach - simple rendering at base DPI
                                outputBitmap = Bitmap.createBitmap(pageWidth, pageHeight, Bitmap.Config.ARGB_8888)
                                val canvas = Canvas(outputBitmap)
                                canvas.drawColor(Color.WHITE)

                                renderedBitmap = renderer.renderImageWithDPI(i, dpi, ImageType.RGB)
                                canvas.drawBitmap(renderedBitmap, 0f, 0f, null)
                            }
                        }
                    }

                    // Save the resulting image
                    val outputFile = File(outputDir, "page_${i + 1}.$format")
                    FileOutputStream(outputFile).use { os ->
                        outputBitmap?.compress(compressFormat, quality, os)
                    }

                    // Clean up bitmaps immediately
                    renderedBitmap?.recycle()
                    outputBitmap?.recycle()

                    imageFiles.add(outputFile)

                    // Force garbage collection after each page to prevent OOM
                    System.gc()
                } catch (e: OutOfMemoryError) {
                    Log.e("PdfService", "OOM when rendering page ${i+1}: ${e.message}")
                    throw Exception("Page ${i+1} is too large to convert. Try a lower DPI setting.")
                } catch (e: Exception) {
                    Log.e("PdfService", "Error rendering page ${i+1}: ${e.message}")
                    // Continue with other pages instead of failing completely
                    continue
                }
            }

            if (imageFiles.isEmpty()) {
                return@withContext Result.failure(Exception("Failed to convert any pages from the PDF"))
            }

            return@withContext Result.success(imageFiles)
        } catch (e: OutOfMemoryError) {
            return@withContext Result.failure(Exception("The PDF is too large to convert to images. Try a lower DPI setting.", e))
        } catch (e: Exception) {
            return@withContext Result.failure(e)
        } finally {
            try {
                doc?.close()
            } catch (e: Exception) {
                // Ignore cleanup errors
            }
        }
    }

    /**
     * Detect if an image has a significant amount of black pixels (potential rendering problem)
     * Improved to avoid falsely detecting legitimate black areas in screenshots and poster-like images
     */
    private fun isBlackBoxProblem(bitmap: Bitmap): Boolean {
        // Sample the image to check for large black areas
        val width = bitmap.width
        val height = bitmap.height

        // Increased sample points for better accuracy
        val samplePoints = 400
        val random = java.util.Random()

        var blackPixels = 0
        var nonBlackPixels = 0

        // Check random pixels throughout the image
        for (i in 0 until samplePoints) {
            val x = random.nextInt(width)
            val y = random.nextInt(height)
            val pixel = bitmap.getPixel(x, y)

            // Check if pixel is very dark (potential black box)
            val r = Color.red(pixel)
            val g = Color.green(pixel)
            val b = Color.blue(pixel)

            if (r < 10 && g < 10 && b < 10) {
                blackPixels++
            } else {
                nonBlackPixels++

                // If we have a significant number of non-black pixels,
                // it's probably legitimate content with some black areas
                if (nonBlackPixels > samplePoints * 0.15) {
                    return false
                }
            }
        }

        // Calculate percentage of black pixels
        val blackPercent = (blackPixels * 100) / samplePoints
        Log.d("PdfService", "Black pixel percentage: $blackPercent%")

        // More conservative threshold - if more than 85% of sampled pixels are black,
        // likely a rendering issue, otherwise it might be a screenshot with black elements
        return blackPercent > 85
    }

    /**
     * Get the number of pages in a PDF document
     * @param context Context for accessing content resolver
     * @param uri URI of the PDF document
     * @return Number of pages in the PDF, or 0 if there was an error
     */
    suspend fun getPageCount(context: Context, uri: Uri): Int = withContext(Dispatchers.IO) {
        var document: PDDocument? = null
        try {
            context.contentResolver.openInputStream(uri)?.use { inputStream ->
                document = PDDocument.load(inputStream)
                val pageCount = document?.numberOfPages ?: 0
                return@withContext pageCount
            }
            return@withContext 0
        } catch (e: Exception) {
            e.printStackTrace()
            return@withContext 0
        } finally {
            document?.close()
        }
    }

    /**
     * Convert images to PDF
     * @param imageUris List of image URIs
     * @param outputFile Output PDF file
     * @param paperSize Paper size (A4, LETTER, LEGAL)
     * @param imageAlignment Image alignment (FIT_PAGE, CENTER, ACTUAL_SIZE)
     * @param onProgressUpdate Callback for progress updates (0-1)
     * @return Success or error message
     */
    suspend fun imagesToPdf(
        imageUris: List<Uri>,
        outputFile: File,
        paperSize: String = "A4",
        imageAlignment: String = "FIT_PAGE",
        onProgressUpdate: ((Float) -> Unit)? = null
    ): Result<File> = withContext(Dispatchers.IO) {
        try {
            val doc = PDDocument()
            val totalImages = imageUris.size

            for ((index, uri) in imageUris.withIndex()) {
                // Report progress
                onProgressUpdate?.invoke(index.toFloat() / totalImages)

                try {
                    val inputStream = context.contentResolver.openInputStream(uri)
                        ?: continue

                    val bitmap = android.graphics.BitmapFactory.decodeStream(inputStream)
                    inputStream.close()

                    if (bitmap == null) {
                        continue // Skip invalid images
                    }

                    // Create a PDF page based on selected paper size
                    val width = bitmap.width
                    val height = bitmap.height
                    val aspectRatio = width.toFloat() / height.toFloat()

                    // Select page size based on paperSize parameter
                    val pageRect = when (paperSize) {
                        "LETTER" -> PDRectangle.LETTER
                        "LEGAL" -> PDRectangle.LEGAL
                        else -> PDRectangle.A4 // Default to A4
                    }
                    
                    val page: PDPage
                    if (aspectRatio > 1) {
                        // Landscape
                        // Create a landscape page by swapping width and height
                        page = PDPage(PDRectangle(pageRect.height, pageRect.width))
                    } else {
                        // Portrait
                        page = PDPage(pageRect)
                    }

                    doc.addPage(page)

                    // Create image and add to page
                    val pdImage = LosslessFactory.createFromImage(doc, bitmap)
                    val contentStream = PDPageContentStream(doc, page)

                    // Apply image alignment based on the imageAlignment parameter
                    val offsetX: Float
                    val offsetY: Float
                    val scaledWidth: Float
                    val scaledHeight: Float
                    
                    when (imageAlignment) {
                        "FIT_PAGE" -> {
                            // Calculate scale to fit the image within the page while maintaining aspect ratio
                            val scaleX = page.mediaBox.width / width
                            val scaleY = page.mediaBox.height / height
                            val scale = min(scaleX, scaleY)
                            
                            // Calculate position to center the image
                            scaledWidth = width * scale
                            scaledHeight = height * scale
                            offsetX = (page.mediaBox.width - scaledWidth) / 2
                            offsetY = (page.mediaBox.height - scaledHeight) / 2
                        }
                        "CENTER" -> {
                            // Center the image with proper scaling to fit page
                            // First check if image is larger than page in either dimension
                            if (width > page.mediaBox.width || height > page.mediaBox.height) {
                                // Scale down to fit within page
                                val scaleX = page.mediaBox.width / width
                                val scaleY = page.mediaBox.height / height
                                val scale = min(scaleX, scaleY)
                                
                                scaledWidth = width * scale
                                scaledHeight = height * scale
                            } else {
                                // Keep original size if smaller than page
                                scaledWidth = width.toFloat()
                                scaledHeight = height.toFloat()
                            }
                            // Center the image on the page
                            offsetX = (page.mediaBox.width - scaledWidth) / 2
                            offsetY = (page.mediaBox.height - scaledHeight) / 2
                        }
                        "ACTUAL_SIZE" -> {
                            // Use actual size but ensure it stays on the page
                            // Convert pixels to points (72 DPI standard for PDF)
                            val pdfPointWidth = min(width.toFloat(), page.mediaBox.width)
                            val pdfPointHeight = min(height.toFloat(), page.mediaBox.height)
                            
                            // Scale proportionally if image is larger than page
                            if (width > page.mediaBox.width || height > page.mediaBox.height) {
                                val scaleX = page.mediaBox.width / width
                                val scaleY = page.mediaBox.height / height
                                val scale = min(scaleX, scaleY) * 0.9f // 90% of available space for margin
                                
                                scaledWidth = width * scale
                                scaledHeight = height * scale
                            } else {
                                // Use actual size if smaller than page
                                scaledWidth = pdfPointWidth
                                scaledHeight = pdfPointHeight
                            }
                            
                            // Place at center of page
                            offsetX = (page.mediaBox.width - scaledWidth) / 2
                            offsetY = (page.mediaBox.height - scaledHeight) / 2
                        }
                        else -> {
                            // Default to FIT_PAGE
                            val scaleX = page.mediaBox.width / width
                            val scaleY = page.mediaBox.height / height
                            val scale = min(scaleX, scaleY)
                            
                            scaledWidth = width * scale
                            scaledHeight = height * scale
                            offsetX = (page.mediaBox.width - scaledWidth) / 2
                            offsetY = (page.mediaBox.height - scaledHeight) / 2
                        }
                    }

                    contentStream.drawImage(
                        pdImage,
                        offsetX,
                        offsetY,
                        scaledWidth,
                        scaledHeight
                    )

                    contentStream.close()
                    bitmap.recycle()

                    // Force garbage collection after each image to prevent OOM
                    System.gc()
                } catch (e: Exception) {
                    // Log error but continue with other images
                    e.printStackTrace()
                }
            }

            // Final progress update
            onProgressUpdate?.invoke(1.0f)

            doc.save(outputFile)
            doc.close()

            return@withContext Result.success(outputFile)
        } catch (e: Exception) {
            return@withContext Result.failure(e)
        }
    }
}
```

### `app\src\main\java\com\example\pdf_img_tools_app\ui\components\AppTopBar.kt`

```kt
package com.example.pdf_img_tools_app.ui.components

import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.filled.ArrowBack
import androidx.compose.material.icons.filled.DarkMode
import androidx.compose.material.icons.filled.LightMode
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
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun AppTopBar(
    title: String,
    showBackButton: Boolean = true,
    showThemeToggle: Boolean = true,
    onBackClick: () -> Unit = {},
    isDarkTheme: Boolean = false,
    onThemeToggleClick: () -> Unit = {}
) {
    val themeIcon = if (isDarkTheme) Icons.Default.LightMode else Icons.Default.DarkMode
    val themeDescription = if (isDarkTheme) "Switch to Light Mode" else "Switch to Dark Mode"

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
                IconButton(onClick = onBackClick) {
                    Icon(
                        imageVector = Icons.AutoMirrored.Filled.ArrowBack,
                        contentDescription = "Back"
                    )
                }
            }
        },
        actions = {
            if (showThemeToggle) {
                IconButton(onClick = onThemeToggleClick) {
                    Icon(
                        imageVector = themeIcon,
                        contentDescription = themeDescription
                    )
                }
            }
        }
    )
}
```

### `app\src\main\java\com\example\pdf_img_tools_app\ui\components\BaseToolScreen.kt`

```kt
package com.example.pdf_img_tools_app.ui.components

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
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.navigation.NavController

/**
 * Base screen layout for all tool screens with simplified layout to prevent measurement issues
 * Uses the SmartMessageDisplay component for displaying messages through the UiMessageBus
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
    content: @Composable () -> Unit
){
    val snackbarHostState = remember { SnackbarHostState() }

    Scaffold(
        topBar = {
            AppTopBar(
                title = title,
                showBackButton = showBackButton,
                onBackClick = { navController.popBackStack() },
                isDarkTheme = isDarkTheme,
                onThemeToggleClick = onThemeToggle
            )
        },
        snackbarHost = {
            SnackbarHost(hostState = snackbarHostState)
        },
        modifier = modifier,
    ) { innerPadding ->
        // Use a simple Box for content area
        Box(
            modifier = Modifier
                .fillMaxSize()
                .padding(innerPadding)
        ) {
            // Add SmartMessageDisplay at the top of the screen
            messageScope?.let { scope ->
                SmartMessageDisplay(
                    scope = scope,
                    snackbarHostState = snackbarHostState,
                    modifier = Modifier
                        .padding(horizontal = 16.dp)
                        .align(Alignment.TopCenter)
                )
            }
            if (isLoading) {
                // Center loading indicator
                CircularProgressIndicator(
                    modifier = Modifier
                        .size(48.dp)
                        .align(Alignment.Center),
                    color = MaterialTheme.colorScheme.primary,
                    strokeWidth = 4.dp
                )
            } else {
                // Content area with fixed size and optional scroll
                Box(
                    modifier = Modifier
                        .fillMaxSize()
                        .padding(horizontal = 12.dp)
                ){
                    if (contentScrollable) {
                        // Apply scrolling to content
                        Box(
                            modifier = Modifier
                                .fillMaxSize()
                                .verticalScroll(rememberScrollState())
                        ){
                            content()
                        }
                    }
                    else {
                        // No scrolling applied here
                        content()
                    }
                }
            }
        }
    }
}
```

### `app\src\main\java\com\example\pdf_img_tools_app\ui\components\FileBottomSheet.kt`

```kt
package com.example.pdf_img_tools_app.ui.components

import android.content.Context
import android.net.Uri
import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.itemsIndexed
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.CheckCircle
import androidx.compose.material.icons.filled.Clear
import androidx.compose.material.icons.filled.Close
import androidx.compose.material.icons.filled.Delete
import androidx.compose.material.icons.filled.RemoveRedEye
import androidx.compose.material.icons.outlined.Circle
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.Checkbox
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.FilledTonalButton
import androidx.compose.material3.HorizontalDivider
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.ModalBottomSheet
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.Text
import androidx.compose.material3.rememberModalBottomSheetState
import androidx.compose.runtime.Composable
import androidx.compose.runtime.mutableStateListOf
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.asImageBitmap
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import com.example.pdf_img_tools_app.utils.FileDetails
import com.example.pdf_img_tools_app.utils.FileUtils
import androidx.compose.ui.unit.sp

/**
 * Reusable bottom sheet component for displaying a list of files
 * 
 * @param show Whether to show the bottom sheet
 * @param onDismiss Callback when the bottom sheet is dismissed
 * @param fileUris List of file URIs to display
 * @param title Title for the bottom sheet
 * @param onFileRemove Callback when a file is removed
 * @param onClearAll Callback to clear all files
 * @param onFileView Callback to view a file (optional)
 * @param fileTypeIcon Icon to show for the file type (optional, defaults based on mime type)
 * @param isDarkTheme Whether dark theme is enabled
 * @param useCheckboxes Whether to use checkboxes for selection (true) or toggleable items (false)
 * @param showIndexNumbers Whether to show index numbers for the items
 * @param showFileSize Whether to show file size information
 * @param showDimensions Whether to show dimensions for image files
 * @param additionalItemContent Additional content to display for each item (optional)
 * @param showImagePreview Whether to show an image preview instead of a list for single image
 */

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun FileBottomSheet(
    show: Boolean,
    onDismiss: () -> Unit,
    fileUris: List<Uri>,
    title: String,
    onFileRemove: (Uri) -> Unit,
    onClearAll: () -> Unit,
    onFileView: ((Uri, String?) -> Unit)? = null,
    fileTypeIcon: ImageVector? = null,
    isDarkTheme: Boolean,
    useCheckboxes: Boolean = false,
    showIndexNumbers: Boolean = false,
    showFileSize: Boolean = true,
    showDimensions: Boolean = false,
    showImagePreview: Boolean = false,
    additionalItemContent: @Composable ((Uri, FileDetails?) -> Unit)? = null
) {
    if (!show) return
    
    val context = LocalContext.current
    val bottomSheetState = rememberModalBottomSheetState(skipPartiallyExpanded = true)
    val selectedItems = remember { mutableStateListOf<Uri>() }
    
    ModalBottomSheet(
        onDismissRequest = { 
            onDismiss()
            selectedItems.clear()
        },
        containerColor = MaterialTheme.colorScheme.surface,
        contentColor = MaterialTheme.colorScheme.onSurface,
        sheetState = bottomSheetState
    ) {
        Column(
            modifier = Modifier.fillMaxWidth()
        ) {
            // Header with title and close button
            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(start = 24.dp, end = 24.dp),
                horizontalArrangement = Arrangement.SpaceBetween,
                verticalAlignment = Alignment.CenterVertically
            ) {
                Text(
                    text = "$title (${fileUris.size})",
                    style = MaterialTheme.typography.titleMedium,
                    fontWeight = FontWeight.Normal
                )

                IconButton(onClick = { 
                    onDismiss()
                    selectedItems.clear()
                })
                {
                    Icon(
                        imageVector = Icons.Default.Close,
                        contentDescription = "Close"
                    )
                }
            }
            
            // Action buttons row (if selected items or files exist and not in image preview mode)
            if (fileUris.isNotEmpty() && !(showImagePreview && fileUris.size == 1)) {
                Row(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(all = 16.dp),
                    horizontalArrangement = Arrangement.spacedBy(8.dp)
                ) {
                    // Remove selected button
                    OutlinedButton(
                        onClick = {
                            if (selectedItems.isNotEmpty()) {
                                val itemsToRemove = selectedItems.toList() // Create a copy to avoid concurrent modification
                                itemsToRemove.forEach { onFileRemove(it) }
                                selectedItems.clear()
                            }
                        },
                        enabled = selectedItems.isNotEmpty(),
                        modifier = Modifier.weight(1f)
                    ) {
                        Icon(
                            imageVector = Icons.Default.Clear,
                            contentDescription = "Remove Selected"
                        )
                        Spacer(modifier = Modifier.width(4.dp))
                        Text("Remove Selected")
                    }
                    
                    // Clear all button
                    FilledTonalButton(
                        onClick = {
                            onClearAll()
                            selectedItems.clear()
                        },
                        modifier = Modifier.weight(1f),
                        colors = ButtonDefaults.filledTonalButtonColors(
                            containerColor = MaterialTheme.colorScheme.secondaryContainer,
                            contentColor = MaterialTheme.colorScheme.onSecondaryContainer
                        )
                    ) {
                        Icon(
                            imageVector = Icons.Default.Delete,
                            contentDescription = "Clear All",
                            modifier = Modifier.size(16.dp)
                        )
                        Spacer(modifier = Modifier.width(4.dp))
                        Text("Clear All")
                    }
                }
                
                Spacer(modifier = Modifier.height(8.dp))
            }

            HorizontalDivider(
                modifier = Modifier.fillMaxWidth(),
                color = MaterialTheme.colorScheme.outline
            )
            
            // If showing image preview for a single image
            if (showImagePreview && fileUris.size == 1) {
                val uri = fileUris[0]
                val fileDetails = FileUtils.getFileDetails(context, uri)
                
                Column(
                    modifier = Modifier
                        .weight(1f)
                        .fillMaxWidth()
                        .padding(16.dp),
                    horizontalAlignment = Alignment.CenterHorizontally
                ) {
                    // Image preview
                    Box(
                        modifier = Modifier
                            .weight(1f)
                            .fillMaxWidth()
                            .clip(RoundedCornerShape(12.dp))
                            .background(Color(0xFF121212).copy(alpha = 0.1f)),
                        contentAlignment = Alignment.Center
                    ) {
                        val bitmap = remember(uri) {
                            FileUtils.getBitmapFromUri(context, uri)
                        }
                        
                        if (bitmap != null) {
                            Image(
                                bitmap = bitmap.asImageBitmap(),
                                contentDescription = "Image Preview",
                                modifier = Modifier.fillMaxSize(),
                                contentScale = ContentScale.Fit
                            )
                        } else {
                            CircularProgressIndicator()
                        }
                    }
                    
                    Spacer(modifier = Modifier.height(16.dp))
                    
                    // File details
                    if (fileDetails != null) {
                        Card(
                            modifier = Modifier.fillMaxWidth(),
                            colors = CardDefaults.cardColors(
                                containerColor = MaterialTheme.colorScheme.surfaceVariant
                            )
                        ) {
                            Column(
                                modifier = Modifier.padding(16.dp)
                            ) {
                                Text(
                                    text = fileDetails.name ?: "Image",
                                    style = MaterialTheme.typography.titleMedium,
                                    maxLines = 1,
                                    overflow = TextOverflow.Ellipsis
                                )
                                
                                Spacer(modifier = Modifier.height(8.dp))
                                
                                if (showFileSize) {
                                    Text(
                                        text = "Size: ${FileUtils.formatFileSize(fileDetails.size)}",
                                        style = MaterialTheme.typography.bodyMedium
                                    )
                                }
                                
                                if (showDimensions && fileDetails.dimensions != null) {
                                    Text(
                                        text = "Dimensions: ${fileDetails.dimensions.first} x ${fileDetails.dimensions.second}",
                                        style = MaterialTheme.typography.bodyMedium
                                    )
                                }
                                
                                // Additional custom content if provided
                                additionalItemContent?.let { it(uri, fileDetails) }
                            }
                        }
                    }
                }
            } else {
                // Original file list
                LazyColumn(
                    modifier = Modifier
                        .weight(1f)
                        .fillMaxWidth(),
                    verticalArrangement = Arrangement.spacedBy(8.dp)
                ) {
                    itemsIndexed(fileUris) { index, uri ->
                        val fileDetails = FileUtils.getFileDetails(context, uri)
                        val isSelected = selectedItems.contains(uri)
                        
                        FileListItem(
                            uri = uri,
                            fileDetails = fileDetails,
                            index = if (showIndexNumbers) index + 1 else null,
                            isSelected = isSelected,
                            onToggleSelection = {
                                if (isSelected) {
                                    selectedItems.remove(uri)
                                } else {
                                    selectedItems.add(uri)
                                }
                            },
                            onView = if (onFileView != null) {
                                { onFileView(uri, fileDetails?.mimeType) }
                            } else null,
                            onRemove = { onFileRemove(uri) },
                            fileTypeIcon = fileTypeIcon,
                            useCheckbox = useCheckboxes,
                            showFileSize = showFileSize,
                            showDimensions = showDimensions,
                            isDarkTheme = isDarkTheme,
                            additionalContent = additionalItemContent?.let { { it(uri, fileDetails) } }
                        )
                    }
                }
            }
            
            Spacer(modifier = Modifier.height(32.dp))
        }
    }
}

/**
 * File list item component
 */
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
    additionalContent: (@Composable () -> Unit)? = null
) {
    val backgroundColor = if (isSelected) {
        if (isDarkTheme) Color(0xFF2D3748).copy(alpha = 0.7f) else Color(0xFFE6F0FF)
    } else {
        if (isDarkTheme) Color(0xFF1D232A) else Color(0xFFF8F9FA)
    }
    
    Card(
        modifier = Modifier
            .fillMaxWidth(),
        colors = CardDefaults.cardColors(
            containerColor = Color.Transparent
        )
    ) {
        Row(
            verticalAlignment = Alignment.CenterVertically,
            horizontalArrangement = Arrangement.spacedBy(8.dp),
            modifier = Modifier.padding(14.dp)
        ) {
            // Selection indicator
            if (useCheckbox) {
                Checkbox(
                    checked = isSelected,
                    onCheckedChange = { onToggleSelection() },
                )
            }
            else {
                Box(
                    modifier = Modifier
                        .size(28.dp)
                        .clickable { onToggleSelection() },
                    contentAlignment = Alignment.Center

                ) {
                    Icon(
                        imageVector = if (isSelected) Icons.Filled.CheckCircle else Icons.Outlined.Circle,
                        contentDescription = if (isSelected) "Selected" else "Not Selected",
                        tint = if (isSelected) MaterialTheme.colorScheme.secondary else MaterialTheme.colorScheme.onSurface,
                        modifier = Modifier.size(28.dp)
                    )
                }
            }
            
            // Index number if enabled
            if (index != null) {
                Box(
                    contentAlignment = Alignment.Center,
                    modifier = Modifier
                        .size(28.dp)
                        .clip(CircleShape)
                        .background(MaterialTheme.colorScheme.primaryContainer)
                ) {
                    Text(
                        text = "$index",
                        style = MaterialTheme.typography.labelMedium,
                        color = MaterialTheme.colorScheme.onPrimaryContainer
                    )
                }
            }
            
            // File icon
            val icon = fileTypeIcon ?: FileUtils.getIconForMimeType(fileDetails?.mimeType)
            Icon(
                imageVector = icon,
                contentDescription = null,
                tint = MaterialTheme.colorScheme.onSurface,
                modifier = Modifier.size(50.dp)
            )
            
            // File info
            Column(
                modifier = Modifier
                    .weight(1f)
                    .clickable { onToggleSelection() }
            ) {
                Text(
                    text = fileDetails?.name ?: FileUtils.getFileName(LocalContext.current, uri) ?: "Unknown File",
                    style = MaterialTheme.typography.titleSmall,
                    color = MaterialTheme.colorScheme.onSurface,
                    fontWeight = FontWeight.SemiBold,
                    overflow = TextOverflow.Ellipsis,
                    maxLines = 1,
                )
                
                if (fileDetails != null) {
                    if (showFileSize) {
                        Spacer(modifier = Modifier.height(2.dp))
                        Text(
                            text = "Size : ${FileUtils.formatFileSize(fileDetails.size)}",
                            style = MaterialTheme.typography.bodySmall,
                            color = MaterialTheme.colorScheme.onSurface,
                            fontSize = 10.sp,
                        )
                    }
                    
                    // Dimensions if available and enabled
                    if (showDimensions && fileDetails.dimensions != null) {
                        Spacer(modifier = Modifier.height(2.dp))
                        Text(
                            text = "Dimensions : ${fileDetails.dimensions.first} x ${fileDetails.dimensions.second}",
                            style = MaterialTheme.typography.bodySmall,
                            color = MaterialTheme.colorScheme.onSurface,
                            fontSize = 10.sp,
                        )
                    }
                }
                
                // Additional custom content if provided
                additionalContent?.invoke()
            }
            
            // View button (if enabled)
            if (onView != null) {
                IconButton(onClick = onView) {
                    Icon(
                        imageVector = Icons.Default.RemoveRedEye,
                        contentDescription = "View",
                        tint = MaterialTheme.colorScheme.onSecondary
                    )
                }
            }
            
            // Remove button - always show it
            IconButton(
                onClick = { 
                    // Call remove function directly
                    onRemove() 
                }
            ) {
                Icon(
                    imageVector = Icons.Default.Delete,
                    contentDescription = "Remove",
                    tint = MaterialTheme.colorScheme.onSecondary
                )
            }
        }

        HorizontalDivider(
            modifier = Modifier.fillMaxWidth(),
            color = MaterialTheme.colorScheme.outline
        )
    }
}
```

### `app\src\main\java\com\example\pdf_img_tools_app\ui\components\FilePickerHandler.kt`

```kt
package com.example.pdf_img_tools_app.ui.components

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
            onResult = { uris: List<Uri>? ->
                uris?.let { newUris ->
                    if (newUris.isNotEmpty()) {
                        selectedUris = newUris
                        onPicked(selectedUris)
                    }
                }
            }
        )
    }
    
    val launchPicker: () -> Unit = {
        launcher.launch(supportedMimeTypes.toTypedArray())
    }
    
    content(launchPicker, selectedUris)
}
```

### `app\src\main\java\com\example\pdf_img_tools_app\ui\components\ImageBatchComponents.kt`

```kt
package com.example.pdf_img_tools_app.ui.components

import android.content.Context
import android.net.Uri
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyRow
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.*
import androidx.compose.material.icons.outlined.Add
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.asImageBitmap
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import com.example.pdf_img_tools_app.service.ImageFormat
import com.example.pdf_img_tools_app.model.ResizeMode
import com.example.pdf_img_tools_app.utils.FileDetails
import com.example.pdf_img_tools_app.utils.FileUtils
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.foundation.Image

/**
 * File selector card that allows selecting multiple files
 */
@Composable
fun FileSelectorCard(
    selectedFiles: List<Uri>,
    onAddFiles: () -> Unit,
    onViewAllFiles: () -> Unit = {},
    modifier: Modifier = Modifier
) {
    Card(
        modifier = modifier
            .fillMaxWidth()
            .border(
                width = 1.dp,
                color = MaterialTheme.colorScheme.outlineVariant,
                shape = MaterialTheme.shapes.medium
            ),
        shape = MaterialTheme.shapes.medium
    ) {
        Column(
            modifier = Modifier.padding(16.dp)
        ) {
            // Section header
            Text(
                "Select Images",
                style = MaterialTheme.typography.titleMedium,
                color = MaterialTheme.colorScheme.onSurface,
                fontWeight = FontWeight.SemiBold
            )
            
            Spacer(modifier = Modifier.height(4.dp))
            
            Text(
                "Choose multiple images to resize in batch",
                style = MaterialTheme.typography.bodySmall,
                color = MaterialTheme.colorScheme.onSurfaceVariant
            )
            
            Spacer(modifier = Modifier.height(16.dp))
            
            // Add image button
            FilledTonalButton(
                onClick = onAddFiles,
                modifier = Modifier.fillMaxWidth()
            ) {
                Icon(
                    imageVector = if (selectedFiles.isEmpty()) Icons.Default.Add else Icons.Default.AddPhotoAlternate,
                    contentDescription = "Add Images"
                )
                Spacer(modifier = Modifier.width(8.dp))
                Text(if (selectedFiles.isEmpty()) "Select Images" else "Add More Images")
            }
            
            // Selected image count & View All button
            if (selectedFiles.isNotEmpty()) {
                Spacer(modifier = Modifier.height(8.dp))
                Row(
                    modifier = Modifier.fillMaxWidth(),
                    horizontalArrangement = Arrangement.SpaceBetween,
                    verticalAlignment = Alignment.CenterVertically
                ) {
                    Text(
                        "${selectedFiles.size} ${if (selectedFiles.size == 1) "image" else "images"} selected",
                        style = MaterialTheme.typography.bodyMedium,
                        color = MaterialTheme.colorScheme.onSurfaceVariant
                    )
                    
                    TextButton(onClick = onViewAllFiles) {
                        Text("See All Files")
                    }
                }
            }
        }
    }
}

/**
 * Image preview item for the batch processing UI
 */
@Composable
fun ImagePreviewItem(
    uri: Uri,
    details: FileDetails?,
    onRemove: () -> Unit,
    modifier: Modifier = Modifier
) {
    val context = LocalContext.current
    val bitmap = remember(uri) {
        FileUtils.getThumbnail(context, uri)
    }
    
    Box(
        modifier = modifier
            .size(80.dp)
            .clip(RoundedCornerShape(8.dp))
            .border(
                width = 1.dp,
                color = MaterialTheme.colorScheme.outlineVariant,
                shape = RoundedCornerShape(8.dp)
            )
    ) {
        // Image preview
        if (bitmap != null) {
            Image(
                bitmap = bitmap!!.asImageBitmap(),
                contentDescription = null,
                contentScale = ContentScale.Crop,
                modifier = Modifier.fillMaxSize()
            )
        } else {
            // Placeholder if bitmap loading failed
            Box(
                modifier = Modifier
                    .fillMaxSize()
                    .background(MaterialTheme.colorScheme.surfaceVariant),
                contentAlignment = Alignment.Center
            ) {
                Icon(
                    imageVector = Icons.Default.Image,
                    contentDescription = null,
                    tint = MaterialTheme.colorScheme.onSurfaceVariant
                )
            }
        }
        
        // Remove button overlay
        IconButton(
            onClick = onRemove,
            modifier = Modifier
                .align(Alignment.TopEnd)
                .size(24.dp)
                .background(
                    color = MaterialTheme.colorScheme.surface.copy(alpha = 0.7f),
                    shape = RoundedCornerShape(4.dp)
                )
        ) {
            Icon(
                imageVector = Icons.Default.Clear,
                contentDescription = "Remove",
                tint = MaterialTheme.colorScheme.onSurface,
                modifier = Modifier.size(16.dp)
            )
        }
    }
}

/**
 * Resize mode selection card
 */
@Composable
fun ResizeModeCard(
    currentMode: ResizeMode,
    onModeChanged: (ResizeMode) -> Unit,
    targetWidth: String,
    targetHeight: String,
    scalePercentage: String,
    preserveAspectRatio: Boolean,
    onTargetWidthChanged: (String) -> Unit,
    onTargetHeightChanged: (String) -> Unit,
    onScalePercentageChanged: (String) -> Unit,
    onPreserveAspectRatioChanged: (Boolean) -> Unit,
    modifier: Modifier = Modifier
) {
    Card(
        modifier = modifier
            .fillMaxWidth()
            .border(
                width = 1.dp,
                color = MaterialTheme.colorScheme.outlineVariant,
                shape = MaterialTheme.shapes.medium
            ),
        shape = MaterialTheme.shapes.medium
    ) {
        Column(
            modifier = Modifier.padding(16.dp)
        ) {
            // Section header
            Text(
                "Resize Options",
                style = MaterialTheme.typography.titleMedium,
                color = MaterialTheme.colorScheme.onSurface,
                fontWeight = FontWeight.SemiBold
            )
            
            Spacer(modifier = Modifier.height(16.dp))
            
            // Mode tabs
            SingleChoiceSegmentedButtonRow(modifier = Modifier.fillMaxWidth()) {
                SegmentedButton(
                    selected = currentMode == ResizeMode.FIXED_DIMENSIONS,
                    onClick = { onModeChanged(ResizeMode.FIXED_DIMENSIONS) },
                    shape = SegmentedButtonDefaults.itemShape(index = 0, count = 3),
                    modifier = Modifier.weight(1f)
                ) {
                    Text("Dimensions")
                }
                SegmentedButton(
                    selected = currentMode == ResizeMode.PERCENTAGE,
                    onClick = { onModeChanged(ResizeMode.PERCENTAGE) },
                    shape = SegmentedButtonDefaults.itemShape(index = 1, count = 3),
                    modifier = Modifier.weight(1f)
                ) {
                    Text("Percentage")
                }
                SegmentedButton(
                    selected = currentMode == ResizeMode.PRESET_SMALL || 
                              currentMode == ResizeMode.PRESET_MEDIUM || 
                              currentMode == ResizeMode.PRESET_LARGE,
                    onClick = { onModeChanged(ResizeMode.PRESET_MEDIUM) },
                    shape = SegmentedButtonDefaults.itemShape(index = 2, count = 3),
                    modifier = Modifier.weight(1f)
                ) {
                    Text("Presets")
                }
            }
            
            Spacer(modifier = Modifier.height(16.dp))
            
            // Content based on selected mode
            when (currentMode) {
                ResizeMode.FIT -> {
                    // Fit within dimensions content
                    Text(
                        "Fit image within target dimensions while maintaining aspect ratio",
                        style = MaterialTheme.typography.bodySmall,
                        color = MaterialTheme.colorScheme.onSurfaceVariant
                    )
                }
                ResizeMode.FILL -> {
                    // Fill dimensions content
                    Text(
                        "Fill target dimensions completely, may crop parts of the image",
                        style = MaterialTheme.typography.bodySmall,
                        color = MaterialTheme.colorScheme.onSurfaceVariant
                    )
                }
                ResizeMode.STRETCH -> {
                    // Stretch content
                    Text(
                        "Stretch to exactly match dimensions, may distort the image",
                        style = MaterialTheme.typography.bodySmall,
                        color = MaterialTheme.colorScheme.onSurfaceVariant
                    )
                }
                ResizeMode.MANUAL -> {
                    // Manual resizing content
                    Text(
                        "Custom manual resizing",
                        style = MaterialTheme.typography.bodySmall,
                        color = MaterialTheme.colorScheme.onSurfaceVariant
                    )
                }
                ResizeMode.FIXED_DIMENSIONS -> {
                    // Dimensions inputs
                    Row(
                        horizontalArrangement = Arrangement.spacedBy(8.dp),
                        modifier = Modifier.fillMaxWidth()
                    ) {
                        OutlinedTextField(
                            value = targetWidth,
                            onValueChange = { onTargetWidthChanged(it.filter { it.isDigit() }) },
                            label = { Text("Width (px)") },
                            keyboardOptions = androidx.compose.foundation.text.KeyboardOptions(
                                keyboardType = KeyboardType.Number
                            ),
                            singleLine = true,
                            modifier = Modifier.weight(1f)
                        )
                        
                        OutlinedTextField(
                            value = targetHeight,
                            onValueChange = { onTargetHeightChanged(it.filter { it.isDigit() }) },
                            label = { Text("Height (px)") },
                            keyboardOptions = androidx.compose.foundation.text.KeyboardOptions(
                                keyboardType = KeyboardType.Number
                            ),
                            singleLine = true,
                            modifier = Modifier.weight(1f)
                        )
                    }
                    
                    Spacer(modifier = Modifier.height(8.dp))
                    
                    // Preserve aspect ratio checkbox
                    Row(
                        verticalAlignment = Alignment.CenterVertically,
                        modifier = Modifier
                            .clickable { onPreserveAspectRatioChanged(!preserveAspectRatio) }
                            .fillMaxWidth()
                    ) {
                        Checkbox(
                            checked = preserveAspectRatio,
                            onCheckedChange = { onPreserveAspectRatioChanged(it) }
                        )
                        Text(
                            text = "Preserve aspect ratio",
                            style = MaterialTheme.typography.bodyMedium
                        )
                    }
                    
                    Spacer(modifier = Modifier.height(4.dp))
                    Text(
                        "Leave one dimension empty to auto-calculate based on aspect ratio",
                        style = MaterialTheme.typography.bodySmall,
                        color = MaterialTheme.colorScheme.onSurfaceVariant
                    )
                }
                
                ResizeMode.PERCENTAGE -> {
                    // Percentage slider
                    Column(
                        modifier = Modifier.fillMaxWidth()
                    ) {
                        Text(
                            "Scale: ${scalePercentage}%", 
                            style = MaterialTheme.typography.bodyMedium,
                            modifier = Modifier.fillMaxWidth(),
                            textAlign = TextAlign.Center
                        )
                        
                        Spacer(modifier = Modifier.height(8.dp))
                        
                        Slider(
                            value = scalePercentage.toFloatOrNull() ?: 50f,
                            onValueChange = { onScalePercentageChanged(it.toInt().toString()) },
                            valueRange = 10f..100f,
                            steps = 9,
                            modifier = Modifier.fillMaxWidth()
                        )
                        
                        Row(
                            modifier = Modifier.fillMaxWidth(),
                            horizontalArrangement = Arrangement.SpaceBetween
                        ) {
                            Text("10%", style = MaterialTheme.typography.bodySmall)
                            Text("50%", style = MaterialTheme.typography.bodySmall)
                            Text("100%", style = MaterialTheme.typography.bodySmall)
                        }
                        
                        Spacer(modifier = Modifier.height(8.dp))
                        
                        OutlinedTextField(
                            value = scalePercentage,
                            onValueChange = { 
                                val filtered = it.filter { it.isDigit() }
                                val value = filtered.toIntOrNull() ?: 0
                                if (value in 1..100) {
                                    onScalePercentageChanged(filtered) 
                                }
                            },
                            label = { Text("Custom scale (%)") },
                            keyboardOptions = androidx.compose.foundation.text.KeyboardOptions(
                                keyboardType = KeyboardType.Number
                            ),
                            singleLine = true,
                            modifier = Modifier.fillMaxWidth()
                        )
                    }
                }
                
                ResizeMode.PRESET_SMALL, ResizeMode.PRESET_MEDIUM, ResizeMode.PRESET_LARGE -> {
                    // Preset options
                    Column(
                        modifier = Modifier.fillMaxWidth()
                    ) {
                        PresetOption(
                            title = "Small Thumbnail",
                            description = "240 × 240 px",
                            icon = Icons.Default.PhotoSizeSelectSmall,
                            isSelected = currentMode == ResizeMode.PRESET_SMALL,
                            onClick = { onModeChanged(ResizeMode.PRESET_SMALL) }
                        )
                        
                        Spacer(modifier = Modifier.height(8.dp))
                        
                        PresetOption(
                            title = "Medium Size",
                            description = "800 × 600 px",
                            icon = Icons.Default.PhotoSizeSelectActual,
                            isSelected = currentMode == ResizeMode.PRESET_MEDIUM,
                            onClick = { onModeChanged(ResizeMode.PRESET_MEDIUM) }
                        )
                        
                        Spacer(modifier = Modifier.height(8.dp))
                        
                        PresetOption(
                            title = "Large Size",
                            description = "1920 × 1080 px",
                            icon = Icons.Default.PhotoSizeSelectLarge,
                            isSelected = currentMode == ResizeMode.PRESET_LARGE,
                            onClick = { onModeChanged(ResizeMode.PRESET_LARGE) }
                        )
                    }
                }
            }
        }
    }
}

/**
 * Preset option item for resize presets
 */
@Composable
private fun PresetOption(
    title: String,
    description: String,
    icon: ImageVector,
    isSelected: Boolean,
    onClick: () -> Unit
) {
    val backgroundColor = if (isSelected) {
        MaterialTheme.colorScheme.primaryContainer
    } else {
        MaterialTheme.colorScheme.surfaceVariant.copy(alpha = 0.5f)
    }
    
    val contentColor = if (isSelected) {
        MaterialTheme.colorScheme.onPrimaryContainer
    } else {
        MaterialTheme.colorScheme.onSurfaceVariant
    }
    
    Surface(
        color = backgroundColor,
        shape = RoundedCornerShape(8.dp),
        modifier = Modifier
            .fillMaxWidth()
            .clickable(onClick = onClick)
    ) {
        Row(
            verticalAlignment = Alignment.CenterVertically,
            modifier = Modifier.padding(12.dp)
        ) {
            Icon(
                imageVector = icon,
                contentDescription = null,
                tint = contentColor
            )
            
            Spacer(modifier = Modifier.width(12.dp))
            
            Column(
                modifier = Modifier.weight(1f)
            ) {
                Text(
                    text = title,
                    style = MaterialTheme.typography.bodyMedium,
                    color = contentColor
                )
                
                Text(
                    text = description,
                    style = MaterialTheme.typography.bodySmall,
                    color = contentColor.copy(alpha = 0.7f)
                )
            }
            
            if (isSelected) {
                Icon(
                    imageVector = Icons.Default.CheckCircle,
                    contentDescription = null,
                    tint = MaterialTheme.colorScheme.primary
                )
            }
        }
    }
}

/**
 * Output options card for image format and filename pattern
 */
@Composable
fun OutputOptionsCard(
    outputFormat: ImageFormat,
    onOutputFormatChanged: (ImageFormat) -> Unit,
    filenamePattern: String,
    onFilenamePatternChanged: (String) -> Unit,
    modifier: Modifier = Modifier
) {
    Card(
        modifier = modifier
            .fillMaxWidth()
            .border(
                width = 1.dp,
                color = MaterialTheme.colorScheme.outlineVariant,
                shape = MaterialTheme.shapes.medium
            ),
        shape = MaterialTheme.shapes.medium
    ) {
        Column(
            modifier = Modifier.padding(16.dp)
        ) {
            // Section header
            Text(
                "Output Options",
                style = MaterialTheme.typography.titleMedium,
                color = MaterialTheme.colorScheme.onSurface,
                fontWeight = FontWeight.SemiBold
            )
            
            Spacer(modifier = Modifier.height(16.dp))
            
            // Format selector
            Text(
                "Output Format",
                style = MaterialTheme.typography.bodyMedium,
                fontWeight = FontWeight.Medium
            )
            
            Spacer(modifier = Modifier.height(8.dp))
            
            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.spacedBy(8.dp)
            ) {
                FormatOption(
                    title = "JPEG",
                    isSelected = outputFormat == ImageFormat.JPG,
                    onClick = { onOutputFormatChanged(ImageFormat.JPG) },
                    modifier = Modifier.weight(1f)
                )
                
                FormatOption(
                    title = "PNG",
                    isSelected = outputFormat == ImageFormat.PNG,
                    onClick = { onOutputFormatChanged(ImageFormat.PNG) },
                    modifier = Modifier.weight(1f)
                )
                
                FormatOption(
                    title = "WebP",
                    isSelected = outputFormat == ImageFormat.WEBP_LOSSY,
                    onClick = { onOutputFormatChanged(ImageFormat.WEBP_LOSSY) },
                    modifier = Modifier.weight(1f)
                )
            }
            
            Spacer(modifier = Modifier.height(16.dp))
            
            // Filename pattern
            Text(
                "Filename Pattern",
                style = MaterialTheme.typography.bodyMedium,
                fontWeight = FontWeight.Medium
            )
            
            Spacer(modifier = Modifier.height(8.dp))
            
            OutlinedTextField(
                value = filenamePattern,
                onValueChange = onFilenamePatternChanged,
                label = { Text("Pattern") },
                modifier = Modifier.fillMaxWidth(),
                singleLine = true
            )
            
            Spacer(modifier = Modifier.height(4.dp))
            
            Text(
                "Available variables: {filename}, {uuid}",
                style = MaterialTheme.typography.bodySmall,
                color = MaterialTheme.colorScheme.onSurfaceVariant
            )
        }
    }
}

/**
 * Format option for output format selector
 */
@Composable
private fun FormatOption(
    title: String,
    isSelected: Boolean,
    onClick: () -> Unit,
    modifier: Modifier = Modifier
) {
    val backgroundColor = if (isSelected) {
        MaterialTheme.colorScheme.primaryContainer
    } else {
        MaterialTheme.colorScheme.surfaceVariant.copy(alpha = 0.5f)
    }
    
    val contentColor = if (isSelected) {
        MaterialTheme.colorScheme.onPrimaryContainer
    } else {
        MaterialTheme.colorScheme.onSurfaceVariant
    }
    
    Surface(
        color = backgroundColor,
        shape = RoundedCornerShape(8.dp),
        modifier = modifier
            .height(48.dp)
            .clickable(onClick = onClick)
    ) {
        Box(
            contentAlignment = Alignment.Center,
            modifier = Modifier.fillMaxSize()
        ) {
            Text(
                text = title,
                style = MaterialTheme.typography.bodyMedium,
                fontWeight = if (isSelected) FontWeight.SemiBold else FontWeight.Normal,
                color = contentColor
            )
        }
    }
}

/**
 * Horizontal thumbnails list for selected image files
 */
@Composable
fun ImageThumbnailList(
    images: List<Uri>,
    fileDetails: Map<Uri, FileDetails>?,
    onRemoveImage: (Uri) -> Unit,
    modifier: Modifier = Modifier
) {
    if (images.isEmpty()) {
        return
    }
    
    LazyRow(
        horizontalArrangement = Arrangement.spacedBy(8.dp),
        modifier = modifier.fillMaxWidth()
    ) {
        items(images) { uri ->
            val details = fileDetails?.get(uri)
            ImagePreviewItem(
                uri = uri,
                details = details,
                onRemove = { onRemoveImage(uri) },
                modifier = Modifier
            )
        }
    }
}
```

### `app\src\main\java\com\example\pdf_img_tools_app\ui\components\InlineMessage.kt`

```kt
package com.example.pdf_img_tools_app.ui.components

import androidx.compose.animation.AnimatedVisibility
import androidx.compose.animation.core.tween
import androidx.compose.animation.expandVertically
import androidx.compose.animation.fadeIn
import androidx.compose.animation.fadeOut
import androidx.compose.animation.shrinkVertically
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Check
import androidx.compose.material.icons.filled.Close
import androidx.compose.material.icons.filled.Error
import androidx.compose.material.icons.filled.Info
import androidx.compose.material.icons.filled.Warning
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import com.example.pdf_img_tools_app.model.MessageType
import com.example.pdf_img_tools_app.model.UiMessageData

/**
 * A reusable composable for displaying inline messages with different types (info, success, warning, error)
 */
@Composable
fun InlineMessage(
    message: UiMessageData,
    onDismiss: () -> Unit = {},
    modifier: Modifier = Modifier
) {
    // Apply proper Material 3 color scheme mapping based on the message type
    val (backgroundColor, contentColor, icon) = when (message.type) {
        MessageType.SUCCESS -> Triple(
            MaterialTheme.colorScheme.primaryContainer,  // Success messages use primary colors
            MaterialTheme.colorScheme.onPrimaryContainer,
            Icons.Filled.Check
        )
        MessageType.ERROR -> Triple(
            MaterialTheme.colorScheme.errorContainer,  // Error messages use error colors
            MaterialTheme.colorScheme.onErrorContainer,
            Icons.Filled.Error
        )
        MessageType.WARNING -> Triple(
            MaterialTheme.colorScheme.secondaryContainer,  // Warnings use secondary colors
            MaterialTheme.colorScheme.onSecondaryContainer,
            Icons.Filled.Warning
        )
        MessageType.INFO -> Triple(
            MaterialTheme.colorScheme.tertiaryContainer,  // Info messages use tertiary colors
            MaterialTheme.colorScheme.onTertiaryContainer,
            Icons.Filled.Info
        )
    }

    AnimatedVisibility(
        visible = true,
        enter = fadeIn(animationSpec = tween(300)) + expandVertically(animationSpec = tween(300)),
        exit = fadeOut(animationSpec = tween(300)) + shrinkVertically(animationSpec = tween(300))
    ) {
        Box(
            modifier = modifier
                .fillMaxWidth()
                .padding(horizontal = 16.dp, vertical = 8.dp)
                .clip(RoundedCornerShape(8.dp))
                .background(backgroundColor)
                .border(
                    width = 1.dp,
                    color = contentColor.copy(alpha = 0.2f),
                    shape = RoundedCornerShape(8.dp)
                )
        ) {
            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(12.dp),
                verticalAlignment = Alignment.CenterVertically
            ) {
                Icon(
                    imageVector = icon,
                    contentDescription = message.type.name.lowercase(),
                    tint = contentColor,
                    modifier = Modifier.size(24.dp)
                )
                
                Spacer(modifier = Modifier.width(12.dp))
                
                Text(
                    text = message.text,
                    style = MaterialTheme.typography.bodyMedium,
                    color = contentColor,
                    modifier = Modifier.weight(1f),
                    overflow = TextOverflow.Ellipsis
                )
                
                if (message.dismissible) {
                    Spacer(modifier = Modifier.width(8.dp))
                    
                    Icon(
                        imageVector = Icons.Filled.Close,
                        contentDescription = "Dismiss",
                        tint = contentColor.copy(alpha = 0.7f),
                        modifier = Modifier
                            .size(20.dp)
                            .clickable { onDismiss() }
                    )
                }
            }
        }
    }
}
```

### `app\src\main\java\com\example\pdf_img_tools_app\ui\components\MessageDialog.kt`

```kt
package com.example.pdf_img_tools_app.ui.components

import androidx.compose.material3.AlertDialog
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Check
import androidx.compose.material.icons.filled.Error
import androidx.compose.material.icons.filled.Info
import androidx.compose.material.icons.filled.Warning
import com.example.pdf_img_tools_app.model.MessageType
import com.example.pdf_img_tools_app.model.UiMessageData
import com.example.pdf_img_tools_app.utils.DisplayMethod
import com.example.pdf_img_tools_app.utils.MessageDisplayManager
import com.example.pdf_img_tools_app.utils.UiMessageBus

/**
 * A composable that displays error and critical warning messages as dialogs
 */
@Composable
fun MessageDialogHandler() {
    val messages by UiMessageBus.messages.collectAsState()
    var currentDialog by remember { mutableStateOf<UiMessageData?>(null) }
    
    // Filter messages that should be shown as dialogs
    val dialogMessages = messages.filter {
        MessageDisplayManager.determineDisplayMethod(it) == DisplayMethod.DIALOG
    }
    
    // Update the current dialog when messages change
    if (dialogMessages.isNotEmpty() && currentDialog == null) {
        currentDialog = dialogMessages.first()
    }
    
    // Show the dialog if there's a message to display
    currentDialog?.let { message ->
        // Use semantic color mapping based on message type following Material 3 guidelines
        val (icon, iconTint) = when (message.type) {
            MessageType.ERROR -> Pair(Icons.Filled.Error, MaterialTheme.colorScheme.error)
            MessageType.WARNING -> Pair(Icons.Filled.Warning, MaterialTheme.colorScheme.secondary)
            MessageType.INFO -> Pair(Icons.Filled.Info, MaterialTheme.colorScheme.tertiary)
            MessageType.SUCCESS -> Pair(Icons.Filled.Check, MaterialTheme.colorScheme.primary)
        }
        
        AlertDialog(
            onDismissRequest = {
                if (message.dismissible) {
                    UiMessageBus.dismissMessage(message.id)
                    currentDialog = null
                }
            },
            containerColor = MaterialTheme.colorScheme.surface,
            iconContentColor = iconTint,
            titleContentColor = MaterialTheme.colorScheme.onSurface,
            textContentColor = MaterialTheme.colorScheme.onSurfaceVariant,
            icon = { 
                Icon(
                    imageVector = icon,
                    contentDescription = message.type.name
                )
            },
            title = {
                Text(
                    text = when (message.type) {
                        MessageType.ERROR -> "Error"
                        MessageType.WARNING -> "Warning"
                        MessageType.INFO -> "Information"
                        MessageType.SUCCESS -> "Success"
                    }
                )
            },
            text = {
                Text(text = message.text)
            },
            confirmButton = {
                TextButton(
                    onClick = {
                        UiMessageBus.dismissMessage(message.id)
                        currentDialog = null
                    },
                    colors = ButtonDefaults.textButtonColors(
                        contentColor = MaterialTheme.colorScheme.primary
                    )
                ) {
                    Text("OK")
                }
            }
        )
    }
}
```

### `app\src\main\java\com\example\pdf_img_tools_app\ui\components\OutputFileDetails.kt`

```kt
package com.example.pdf_img_tools_app.ui.components

import android.content.Context
import android.net.Uri
import androidx.compose.animation.AnimatedVisibility
import androidx.compose.animation.core.Spring
import androidx.compose.animation.core.spring
import androidx.compose.animation.expandVertically
import androidx.compose.animation.fadeIn
import androidx.compose.foundation.background
import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.foundation.layout.*
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
import com.example.pdf_img_tools_app.utils.FileDetails
import com.example.pdf_img_tools_app.utils.FileUtils
import androidx.compose.material3.HorizontalDivider
import androidx.core.content.FileProvider
import java.io.File

/**
 * Modern file output details component with configurable display options
 * Redesigned with compact layout, small icons, and modern UI elements
 * Now with flexible boolean flags for controlling what details to show
 */

@OptIn(ExperimentalLayoutApi::class)
@Composable
fun OutputFileDetails(
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
    modifier: Modifier = Modifier

) {

    val context = LocalContext.current

    AnimatedVisibility(
        visible = true,
        enter = fadeIn(animationSpec = spring(stiffness = Spring.StiffnessLow)) + 
               expandVertically(animationSpec = spring(stiffness = Spring.StiffnessLow))
    ) {
        Card(
            modifier = modifier.fillMaxWidth(),
            colors = CardDefaults.cardColors(
                containerColor = MaterialTheme.colorScheme.surfaceVariant,
            ),
            shape = RoundedCornerShape(14.dp)
        ) {
            Column(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(0.dp)
            ) {
                // Header with icon and file name
                if (showName) {
                    Row(
                        verticalAlignment = Alignment.CenterVertically,
                        modifier = Modifier
                            .fillMaxWidth()
                            .padding(12.dp)
                    ) {
                        // File type icon with circular background
                        Box(
                            contentAlignment = Alignment.Center,
                            modifier = Modifier
                                .size(36.dp)
                                .clip(RoundedCornerShape(8.dp))
                                .background(MaterialTheme.colorScheme.secondaryContainer)
                        ) {
                            Icon(
                                imageVector = FileUtils.getIconForMimeType(file.mimeType),
                                contentDescription = null,
                                tint = MaterialTheme.colorScheme.onSurfaceVariant,
                                modifier = Modifier.size(24.dp)
                            )
                        }

                        Spacer(modifier = Modifier.width(14.dp))

                        // File name and type
                        Column(modifier = Modifier.weight(1f)) {
                            Text(
                                text = file.name,
                                style = MaterialTheme.typography.titleMedium,
                                fontWeight = FontWeight.SemiBold,
                                maxLines = 1,
                                overflow = TextOverflow.Ellipsis,
                                color = MaterialTheme.colorScheme.onSurfaceVariant
                            )

                            if (showFormat) {
                                val formatLabel = labelOverrides["format"] ?: "Type"
                                Text(
                                    text = file.mimeType ?: "Unknown type",
                                    style = MaterialTheme.typography.bodySmall,
                                    color = MaterialTheme.colorScheme.onSurfaceVariant,
                                    maxLines = 1,
                                    overflow = TextOverflow.Ellipsis,
                                )
                            }
                        }
                    }
                }

                // Details section with subtle divider
                HorizontalDivider(
                    modifier = Modifier.padding(top = 0.dp, bottom = 0.dp),
                    color = MaterialTheme.colorScheme.outline
                )

                // Details - single column layout for better readability
                Column(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(start = 40.dp, end = 8.dp)
                ) {
                    // File details and metadata
                    FlowRow(modifier = Modifier.padding(start = 12.dp, end = 12.dp, bottom = 12.dp)) {
                        Spacer(modifier = Modifier.height(6.dp))
                        
                        // File size
                        if (showSize) {
                            val sizeLabel = labelOverrides["size"] ?: "Size"
                            CompactDetailRow(
                                icon = Icons.Outlined.Storage,
                                label = sizeLabel,
                                value = FileUtils.formatFileSize(file.size)
                            )
                        }

                        // File format/type
                        if (showFormat) {
                            val formatLabel = labelOverrides["format"] ?: "Type"
                            CompactDetailRow(
                                icon = Icons.Outlined.Description,
                                label = formatLabel,
                                value = file.mimeType
                            )
                        }

                        // Path info if available
                        if (showPath && file.path != null) {
                            val pathLabel = labelOverrides["path"] ?: "Path"
                            CompactDetailRow(
                                icon = Icons.Outlined.Folder,
                                label = pathLabel,
                                value = file.path
                            )
                        }

                        // Dimensions if available (for images)
                        if (showDimensions && file.dimensions != null) {
                            val dimensionsLabel = labelOverrides["dimensions"] ?: "Dimensions"
                            val (width, height) = file.dimensions
                            CompactDetailRow(
                                icon = Icons.Outlined.Fullscreen,
                                label = dimensionsLabel,
                                value = "${width}×${height}"
                            )
                        }

                        // Page count for PDFs
                        if (showPages && file.mimeType == "application/pdf") {
                            val pagesLabel = labelOverrides["pages"] ?: "Pages"
                            CompactDetailRow(
                                icon = Icons.AutoMirrored.Outlined.Article,
                                label = pagesLabel,
                                value = file.pageCount?.toString() ?: "Unknown"
                            )
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
                                CompactDetailRow(
                                    icon = Icons.Outlined.FilePresent,
                                    label = "Original Size",
                                    value = FileUtils.formatFileSize(originalSize)
                                )
                                
                                // Compressed size row
                                CompactDetailRow(
                                    icon = Icons.Outlined.FileDownload,
                                    label = "Compressed Size",
                                    value = FileUtils.formatFileSize(compressedSize)
                                )
                                
                                // Savings percentage row
                                CompactDetailRow(
                                    icon = Icons.AutoMirrored.Outlined.TrendingDown,
                                    label = savingsLabel,
                                    value = if (percentSaved >= 0) {
                                        "$percentSaved% smaller"
                                    } else {
                                        "${-percentSaved}% larger"
                                    }
                                )
                            }
                        }
                    }
                }

                // Action buttons - modern chip-like design
                FlowRow(
                    horizontalArrangement = Arrangement.End,
                    modifier = Modifier.fillMaxWidth().padding(top = 8.dp, bottom = 8.dp, end = 8.dp),
                    maxItemsInEachRow = 4
                ) {
                    // Open button
                    if (onOpen != null) {
                        FilledTonalIconButton(
                            onClick = { onOpen() },
                            modifier = Modifier
                                .padding(end = 8.dp, bottom = 8.dp)
                                .size(width = 80.dp, height = 32.dp),
                            colors = IconButtonDefaults.filledTonalIconButtonColors(
                                containerColor = MaterialTheme.colorScheme.primaryContainer,
                                contentColor = MaterialTheme.colorScheme.onPrimaryContainer
                            )
                        ) {
                            Row(verticalAlignment = Alignment.CenterVertically) {
                                Icon(
                                    imageVector = Icons.Outlined.Visibility,
                                    contentDescription = "Open",
                                    modifier = Modifier.size(16.dp),
                                )
                                Spacer(Modifier.width(6.dp))
                                Text(
                                    text = "View",
                                    style = MaterialTheme.typography.labelMedium,
                                    fontSize = 12.sp
                                )
                            }
                        }
                    }

                    // Share button
                    if (onShare != null) {
                        FilledTonalIconButton(
                            onClick = { onShare() },
                            modifier = Modifier
                                .padding(end = 8.dp, bottom = 8.dp)
                                .size(width = 80.dp, height = 32.dp),
                            colors = IconButtonDefaults.filledTonalIconButtonColors(
                                containerColor = MaterialTheme.colorScheme.secondaryContainer,
                                contentColor = MaterialTheme.colorScheme.onSecondaryContainer
                            )
                        ) {
                            Row(verticalAlignment = Alignment.CenterVertically) {
                                Icon(
                                    imageVector = Icons.Outlined.Share,
                                    contentDescription = "Share",
                                    modifier = Modifier.size(16.dp)
                                )
                                Spacer(modifier = Modifier.width(4.dp))
                                Text(
                                    text = "Share",
                                    style = MaterialTheme.typography.labelMedium,
                                    fontSize = 12.sp
                                )
                            }
                        }
                    }

                    // Delete button
                    if (onDelete != null) {
                        FilledTonalIconButton(
                            onClick = onDelete,
                            modifier = Modifier
                                .padding(end = 8.dp, bottom = 8.dp)
                                .size(width = 80.dp, height = 32.dp),
                            colors = IconButtonDefaults.filledTonalIconButtonColors(
                                containerColor = MaterialTheme.colorScheme.secondaryContainer,
                                contentColor = MaterialTheme.colorScheme.onSecondaryContainer
                            )
                        ) {
                            Row(verticalAlignment = Alignment.CenterVertically) {
                                Icon(
                                    imageVector = Icons.Outlined.Delete,
                                    contentDescription = "Delete",
                                    modifier = Modifier.size(16.dp)
                                )
                                Spacer(modifier = Modifier.width(4.dp))
                                Text(
                                    text = "Remove",
                                    style = MaterialTheme.typography.labelMedium,
                                    fontSize = 12.sp
                                )
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
private fun CompactDetailRow(
    icon: ImageVector,
    label: String,
    value: String,
    modifier: Modifier = Modifier
) {
    Row(modifier = Modifier.padding(top = 16.dp, start = 8.dp, end = 8.dp)) {
        Icon(
            imageVector = icon,
            contentDescription = null,
            tint = MaterialTheme.colorScheme.onSurfaceVariant,
            modifier = Modifier.size(14.dp)
        )

        Spacer(modifier = Modifier.width(4.dp))

        Column {
            Text(
                text = label,
                style = MaterialTheme.typography.labelSmall,
                color = MaterialTheme.colorScheme.onSurfaceVariant,
                fontSize = 12.sp
            )

            Spacer(modifier = Modifier.width(4.dp))

            Text(
                text = value,
                style = MaterialTheme.typography.bodyMedium,
                fontSize = 10.sp,
                maxLines = 1,
                overflow = TextOverflow.Ellipsis
            )
        }
    }
}

/**
 * Reusable function to view PDF files
 */
fun viewPdf(context: Context, uri: Uri?) {
    val intent = android.content.Intent(android.content.Intent.ACTION_VIEW).apply {
        setDataAndType(uri, "application/pdf")
        addFlags(android.content.Intent.FLAG_GRANT_READ_URI_PERMISSION)
    }
    try {
        context.startActivity(intent)
    } catch (e: android.content.ActivityNotFoundException) {
        // Instead of toast, we'll just log the error
        android.util.Log.e("OutputFileDetails", "No PDF viewer found")
    }
}

/**
 * Reusable function to view image files
 */
fun viewImage(context: Context, uri: Uri, mimeType: String?) {
    val intent = android.content.Intent(android.content.Intent.ACTION_VIEW).apply {
        setDataAndType(uri, mimeType ?: "image/*")
        addFlags(android.content.Intent.FLAG_GRANT_READ_URI_PERMISSION)
    }
    try {
        context.startActivity(intent)
    } catch (e: android.content.ActivityNotFoundException) {
        // Instead of toast, we'll just log the error
        android.util.Log.e("OutputFileDetails", "No image viewer found")
    }
}

/**
 * Generic function to view any file based on its MIME type
 */
fun viewFile(context: Context, uri: Uri, mimeType: String?) {
    when {
        mimeType?.startsWith("image/") == true -> viewImage(context, uri, mimeType)
        mimeType == "application/pdf" -> viewPdf(context, uri)
        else -> {
            // Generic file viewer
            val intent = android.content.Intent(android.content.Intent.ACTION_VIEW).apply {
                setDataAndType(uri, mimeType ?: "*/*")
                addFlags(android.content.Intent.FLAG_GRANT_READ_URI_PERMISSION)
            }
            try {
                context.startActivity(intent)
            } catch (e: android.content.ActivityNotFoundException) {
                android.util.Log.e("OutputFileDetails", "No viewer found for $mimeType")
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
        val shareIntent = android.content.Intent().apply {
            action = android.content.Intent.ACTION_SEND

            // If the URI is a file:// URI, convert it to a content:// URI using FileProvider
            if (uri?.scheme == "file") {
                val file = File(uri.path!!)
                val contentUri = FileProvider.getUriForFile(
                    context,
                    context.applicationContext.packageName + ".fileprovider",
                    file
                )
                putExtra(android.content.Intent.EXTRA_STREAM, contentUri)
            } else {
                // If it's already a content:// URI, use it directly
                putExtra(android.content.Intent.EXTRA_STREAM, uri)
            }

            type = mimeType ?: "*/*"
            addFlags(android.content.Intent.FLAG_GRANT_READ_URI_PERMISSION)
        }

        val chooserIntent = android.content.Intent.createChooser(
            shareIntent,
            "Share via"
        )

        context.startActivity(chooserIntent)
    } catch (e: Exception) {
        android.util.Log.e("OutputFileDetails", "Error sharing file: ${e.message}")
    }
}
```

### `app\src\main\java\com\example\pdf_img_tools_app\ui\components\ProgressToolButton.kt`

```kt
package com.example.pdf_img_tools_app.ui.components


import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.material3.Button
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.unit.dp

/**
 * A button that shows a progress indicator when processing is in progress
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
    enabled: Boolean = true
) {
    Button(
        onClick = onClick,
        modifier = modifier.fillMaxWidth(),
        enabled = enabled && !isProcessing
    ) {
        Row(
            verticalAlignment = Alignment.CenterVertically,
            modifier = Modifier.padding(vertical = 12.dp)
        ) {
            // Show icon if provided
            if (icon != null && !isProcessing) {
                Icon(
                    imageVector = icon,
                    contentDescription = null,
                    modifier = Modifier.size(18.dp)
                )
                Spacer(modifier = Modifier.width(8.dp))
            }
            
            // Show either text or progress indicator
            if (isProcessing) {
                CircularProgressIndicator(
                    modifier = Modifier.size(24.dp),
                    color = MaterialTheme.colorScheme.onPrimary,
                    strokeWidth = 1.dp
                )
            } else {
                Text(text = text)
            }
        }
    }
}
```

### `app\src\main\java\com\example\pdf_img_tools_app\ui\components\ReusableSaveLocationSelector.kt`

```kt
package com.example.pdf_img_tools_app.ui.components

import android.net.Uri
import android.content.Context
import android.content.Intent
import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.foundation.background
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
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.window.Dialog
import com.example.pdf_img_tools_app.utils.FileUtils

import com.example.pdf_img_tools_app.model.SaveMode

/**
 * A reusable save location selector component
 * This component only appears after the user selects files
 * 
 * @param visible Whether the component should be visible
 * @param defaultSaveLocation The default save location to display
 * @param onSaveLocationChanged Callback for when the save location is changed
 * @param saveModeEnabled Whether to enable save mode selection (separately or as archive)
 * @param initialSaveMode The initial save mode to use
 * @param onSaveModeChanged Callback for when the save mode is changed
 * @param modifier Modifier for the component
 */
@Composable
fun ReusableSaveLocationSelector(
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
    val dirPickerLauncher = rememberLauncherForActivityResult(
        contract = ActivityResultContracts.OpenDocumentTree()
    ){
        uri: Uri? ->
        uri?.let {
            try {
                // Log the selected URI for debugging
                android.util.Log.d("ReusableSaveLocationSelector", "Selected URI: $it")
                
                // Get permission to write to this location
                val takeFlags = Intent.FLAG_GRANT_READ_URI_PERMISSION or 
                               Intent.FLAG_GRANT_WRITE_URI_PERMISSION
                
                try {
                    // Take persistable URI permission to maintain access across app restarts
                    context.contentResolver.takePersistableUriPermission(it, takeFlags)
                } catch (e: SecurityException) {
                    android.util.Log.w("ReusableSaveLocationSelector", "Could not take persistable permission: ${e.message}")
                    // Continue anyway, might be a permissions issue that we can work around
                }
                
                // Get folder name and path for display
                val directoryName = FileUtils.getDirectoryName(context, it)
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
                    
                    android.util.Log.d("ReusableSaveLocationSelector", "Directory selected: $directoryName, URI: $it")
                } else {
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
                    
                    android.util.Log.d("ReusableSaveLocationSelector", "Using fallback name: $fallbackName")
                }
            } catch (e: SecurityException) {
                hasPermissionError = true
                android.util.Log.e("ReusableSaveLocationSelector", "Security exception: ${e.message}")
                android.widget.Toast.makeText(
                    context, 
                    "Error accessing directory: ${e.message}",
                    android.widget.Toast.LENGTH_LONG
                ).show()
            } catch (e: Exception) {
                hasPermissionError = true
                android.util.Log.e("ReusableSaveLocationSelector", "Failed to access directory: ${e.message}")
                android.widget.Toast.makeText(
                    context, 
                    "Error: ${e.message}",
                    android.widget.Toast.LENGTH_LONG
                ).show()
            }
        }
    }

    Column(
        modifier = Modifier.padding(top = 0.dp)
    ){
        Text(
            text = "Save Location",
            style = MaterialTheme.typography.titleSmall,
            color = MaterialTheme.colorScheme.onSurface,
            modifier = Modifier.padding(bottom = 16.dp)
        )

        // Save location card
        Card(
            modifier = modifier,
            colors = CardDefaults.cardColors(
                containerColor = MaterialTheme.colorScheme.surfaceVariant,
                contentColor = MaterialTheme.colorScheme.onSurfaceVariant
            ),
            shape = RoundedCornerShape(10.dp),
        ){
            Column(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(16.dp),
            ){
                Row(
                    modifier = Modifier.fillMaxWidth(),
                    verticalAlignment = Alignment.CenterVertically,
                    horizontalArrangement = Arrangement.SpaceBetween
                ){
                    Icon(
                        imageVector = Icons.Filled.Save,
                        contentDescription = "Folder Icon",
                        modifier = Modifier.size(34.dp),
                        tint = MaterialTheme.colorScheme.onSurface
                    )

                    Spacer(modifier = Modifier.width(16.dp))

                    Column(modifier = Modifier.weight(1f)){

                        Row(
                            modifier = Modifier.padding(bottom = 2.dp),
                            verticalAlignment = Alignment.CenterVertically
                        ){
                            Text(
                                text = "Save Location : ",
                                style = MaterialTheme.typography.bodySmall,
                                color = MaterialTheme.colorScheme.onSurfaceVariant,
                                modifier = Modifier
                            )

                            // Display selected path with error indication if needed
                            Text(
                                text = selectedSavePath,
                                style = MaterialTheme.typography.bodySmall,
                                color = if (hasPermissionError) MaterialTheme.colorScheme.error else MaterialTheme.colorScheme.onSurface,
                                maxLines = 2,  // Allow 2 lines for better display of long paths
                                overflow = TextOverflow.Ellipsis
                            )
                        }

                        // Display save mode indicator
                        if (saveModeEnabled) {
                            Text(
                                text = "Save Mode : ${if (saveMode == SaveMode.SEPARATELY) "Save Separately" else "Save as Archive"}",
                                style = MaterialTheme.typography.bodySmall,
                                color = MaterialTheme.colorScheme.onSurface
                            )
                        }

                        if (hasPermissionError) {
                            Text(
                                text = "Permission denied. Please select another location.",
                                style = MaterialTheme.typography.bodySmall,
                                color = MaterialTheme.colorScheme.error
                            )
                        }
                    }

                    TextButton(
                        onClick = { showSaveLocationDialog = true },
                        colors = ButtonDefaults.buttonColors(
                            containerColor = MaterialTheme.colorScheme.secondaryContainer,
                            contentColor = MaterialTheme.colorScheme.onSecondaryContainer
                        ),
                        modifier = Modifier.size(width = 80.dp, height = 40.dp)
                    ){
                        Text(
                            text = "Change",
                            style = MaterialTheme.typography.bodySmall,
                        )
                    }
                }
            }
        }

    }

    // Save location dialog
    if (showSaveLocationDialog) {
        SaveLocationDialog(
            initialPath = selectedSavePath,
            initialSaveMode = saveMode,
            saveModeEnabled = saveModeEnabled,
            onDismiss = { showSaveLocationDialog = false },
            onConfirm = { path, mode ->
                if (saveModeEnabled && mode != saveMode) {
                    // Update the save mode - do this first as it's not dependent on user pick location
                    saveMode = mode
                    onSaveModeChanged(mode)
                    android.util.Log.d("ReusableSaveLocationSelector", "Save mode changed to: $mode")
                }
                
                // If user manually entered a path, we launch the picker
                if (path != selectedSavePath) {
                    dirPickerLauncher.launch(null)
                }
                
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
private fun SaveLocationDialog(
    initialPath: String,
    initialSaveMode: SaveMode,
    saveModeEnabled: Boolean,
    onDismiss: () -> Unit,
    onConfirm: (String, SaveMode) -> Unit,
    onPickLocation: () -> Unit
) {
    var path by remember { mutableStateOf(initialPath) }
    var saveMode by remember { mutableStateOf(initialSaveMode) }
    
    Dialog(onDismissRequest = onDismiss) {
        Surface(
            shape = RoundedCornerShape(16.dp),
            color = MaterialTheme.colorScheme.surface,
            tonalElevation = 16.dp,
            contentColor = MaterialTheme.colorScheme.onSurfaceVariant
        ) {
            Column(
                modifier = Modifier
                    .padding(20.dp)
                    .fillMaxWidth()
            ) {
                Text(
                    text = "Save Location Settings",
                    style = MaterialTheme.typography.titleSmall,
                    fontWeight = FontWeight.Normal,
                    modifier = Modifier.padding(bottom = 16.dp)
                )
                
                // Location input
                OutlinedTextField(
                    value = path,
                    onValueChange = { path = it },
                    label = { Text("Save Location") },
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(bottom = 8.dp),
                    trailingIcon = {
                        IconButton(onClick = onPickLocation) {
                            // This would ideally be an icon, but using text for simplicity
                            Icon(
                                imageVector = Icons.Default.Folder,
                                contentDescription = "Pick location"
                            )
                        }
                    }
                )
                
                // Save mode selection
                if (saveModeEnabled) {
                    Column(
                        modifier = Modifier
                            .fillMaxWidth()
                            .padding(vertical = 8.dp)
                    ) {
                        Text(
                            text = "Save Mode",
                            style = MaterialTheme.typography.bodyMedium,
                            modifier = Modifier.padding(bottom = 4.dp)
                        )
                        
                        // Save separately option
                        Row(
                            verticalAlignment = Alignment.CenterVertically,
                            modifier = Modifier.fillMaxWidth()
                        ) {
                            RadioButton(
                                selected = saveMode == SaveMode.SEPARATELY,
                                onClick = { saveMode = SaveMode.SEPARATELY }
                            )
                            Text("Save files separately")
                        }
                        
                        // Save as archive option
                        Row(
                            verticalAlignment = Alignment.CenterVertically,
                            modifier = Modifier.fillMaxWidth()
                        ) {
                            RadioButton(
                                selected = saveMode == SaveMode.AS_ARCHIVE,
                                onClick = { saveMode = SaveMode.AS_ARCHIVE }
                            )
                            Text("Save as archive")
                        }
                    }
                }
                
                // Buttons
                Row(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(top = 16.dp),
                    horizontalArrangement = Arrangement.End
                ) {
                    TextButton(onClick = onDismiss) {
                        Text("Cancel")
                    }
                    Spacer(modifier = Modifier.width(8.dp))
                    Button(
                        onClick = { onConfirm(path, saveMode) },
                        colors = ButtonDefaults.buttonColors(
                            containerColor = MaterialTheme.colorScheme.surfaceVariant,
                            contentColor = MaterialTheme.colorScheme.onSurfaceVariant
                        )
                    ){
                        Text("Save")
                    }
                }
            }
        }
    }
}

/**
 * Preview for the ReusableSaveLocationSelector
 */
@Preview(showBackground = true)
@Composable
fun ReusableSaveLocationSelectorPreview() {
    MaterialTheme {
        ReusableSaveLocationSelector(
            visible = true,
            defaultSaveLocation = "Downloads",
            onSaveLocationChanged = {},
            saveModeEnabled = true,
            initialSaveMode = SaveMode.SEPARATELY,
            onSaveModeChanged = {},
            modifier = Modifier.padding(16.dp)
        )
    }
}

/**
 * Preview for the SaveLocationDialog
 */
@Preview(showBackground = true)
@Composable
fun SaveLocationDialogPreview() {
    MaterialTheme {
        SaveLocationDialog(
            initialPath = "Downloads",
            initialSaveMode = SaveMode.SEPARATELY,
            saveModeEnabled = true,
            onDismiss = {},
            onConfirm = { _, _ -> },
            onPickLocation = {}
        )
    }
}
```

### `app\src\main\java\com\example\pdf_img_tools_app\ui\components\SaveAsArchiveDialog.kt`

```kt
package com.example.pdf_img_tools_app.ui.components

import androidx.compose.foundation.layout.*
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.outlined.Archive
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.input.ImeAction
import androidx.compose.ui.unit.dp
import androidx.compose.ui.window.Dialog
import androidx.compose.ui.window.DialogProperties
import androidx.compose.animation.AnimatedVisibility
import androidx.compose.animation.fadeIn
import androidx.compose.animation.fadeOut
import androidx.compose.animation.expandVertically
import androidx.compose.animation.shrinkVertically
import com.example.pdf_img_tools_app.model.SaveLocationType

/**
 * Dialog for saving files as archive (zip)
 */
@Composable
fun SaveAsArchiveDialog(
    visible: Boolean,
    defaultFileName: String,
    saveLocationType: SaveLocationType,
    customLocationName: String,
    customLocationUri: String?, // URI string of the custom location
    onSaveLocationTypeChanged: (SaveLocationType) -> Unit,
    onDismiss: () -> Unit,
    onConfirm: (String) -> Unit, // String is the filename
    onPickCustomLocation: () -> Unit
) {
    if (!visible) return
    
    var filename by remember(defaultFileName) { mutableStateOf(defaultFileName) }
    
    Dialog(
        onDismissRequest = onDismiss,
        properties = DialogProperties(
            dismissOnBackPress = true,
            dismissOnClickOutside = true
        )
    ) {
        Card(
            modifier = Modifier
                .fillMaxWidth()
                .padding(16.dp),
            elevation = CardDefaults.cardElevation(
                defaultElevation = 8.dp
            )
        ) {
            Column(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(16.dp),
                horizontalAlignment = Alignment.CenterHorizontally
            ) {
                // Title with icon
                Row(
                    verticalAlignment = Alignment.CenterVertically,
                    modifier = Modifier.fillMaxWidth()
                ) {
                    Icon(
                        imageVector = Icons.Outlined.Archive,
                        contentDescription = null,
                        tint = MaterialTheme.colorScheme.primary
                    )
                    Spacer(modifier = Modifier.width(8.dp))
                    Text(
                        text = "Save as Archive",
                        style = MaterialTheme.typography.titleLarge
                    )
                }
                
                Spacer(modifier = Modifier.height(24.dp))
                
                // Filename input
                OutlinedTextField(
                    value = filename,
                    onValueChange = { filename = it },
                    label = { Text("Archive name") },
                    singleLine = true,
                    modifier = Modifier.fillMaxWidth(),
                    keyboardOptions = KeyboardOptions.Default.copy(
                        imeAction = ImeAction.Done
                    ),
                    trailingIcon = {
                        Text(
                            text = ".zip",
                            color = MaterialTheme.colorScheme.onSurfaceVariant
                        )
                    }
                )
                
                Spacer(modifier = Modifier.height(16.dp))
                
                // Save location selector
                Column(
                    modifier = Modifier.fillMaxWidth()
                ) {
                    Text(
                        text = "Save Location",
                        style = MaterialTheme.typography.titleMedium
                    )
                    
                    Spacer(modifier = Modifier.height(8.dp))
                    
                    // Downloads option
                    Row(
                        verticalAlignment = Alignment.CenterVertically,
                        modifier = Modifier.fillMaxWidth()
                    ) {
                        RadioButton(
                            selected = saveLocationType == SaveLocationType.DOWNLOADS,
                            onClick = { onSaveLocationTypeChanged(SaveLocationType.DOWNLOADS) }
                        )
                        Spacer(modifier = Modifier.width(8.dp))
                        Text("Save to Downloads")
                    }
                    
                    // Custom location option
                    Row(
                        verticalAlignment = Alignment.CenterVertically,
                        modifier = Modifier.fillMaxWidth()
                    ) {
                        RadioButton(
                            selected = saveLocationType == SaveLocationType.CUSTOM,
                            onClick = { onSaveLocationTypeChanged(SaveLocationType.CUSTOM) }
                        )
                        Spacer(modifier = Modifier.width(8.dp))
                        Text("Save to Custom Location")
                    }
                    
                    // Custom location selector - wrapped in a composable to fix context issue
                    CustomLocationSelector(
                        visible = saveLocationType == SaveLocationType.CUSTOM,
                        customLocationUri = customLocationUri,
                        customLocationName = customLocationName,
                        onPickCustomLocation = onPickCustomLocation
                    )
                }
                
                Spacer(modifier = Modifier.height(24.dp))
                
                // Action buttons
                Row(
                    modifier = Modifier.fillMaxWidth(),
                    horizontalArrangement = Arrangement.End
                ) {
                    TextButton(
                        onClick = onDismiss
                    ) {
                        Text("Cancel")
                    }
                    
                    Spacer(modifier = Modifier.width(8.dp))
                    
                    val filenameValid = filename.isNotBlank()
                    val locationValid = saveLocationType == SaveLocationType.DOWNLOADS || 
                            (saveLocationType == SaveLocationType.CUSTOM && customLocationUri != null)
                    
                    Button(
                        onClick = { onConfirm(filename) },
                        enabled = filenameValid && locationValid
                    ) {
                        Text("Save")
                    }
                }
            }
        }
    }
}

/**
 * Helper composable for custom location selection
 */
@Composable
private fun CustomLocationSelector(
    visible: Boolean,
    customLocationUri: String?,
    customLocationName: String,
    onPickCustomLocation: () -> Unit
) {
    AnimatedVisibility(visible = visible) {
        Box(
            modifier = Modifier
                .fillMaxWidth()
                .padding(start = 32.dp, top = 8.dp)
        ) {
            if (customLocationUri != null) {
                // Display selected location
                OutlinedCard(
                    modifier = Modifier.fillMaxWidth()
                ) {
                    Row(
                        modifier = Modifier
                            .fillMaxWidth()
                            .padding(horizontal = 16.dp, vertical = 8.dp),
                        verticalAlignment = Alignment.CenterVertically,
                        horizontalArrangement = Arrangement.SpaceBetween
                    ) {
                        Text(
                            text = customLocationName.ifEmpty { "Selected folder" },
                            style = MaterialTheme.typography.bodyMedium,
                            modifier = Modifier.weight(1f)
                        )
                        TextButton(onClick = onPickCustomLocation) {
                            Text("Change")
                        }
                    }
                }
            } else {
                // Show button to pick location
                OutlinedButton(
                    onClick = onPickCustomLocation,
                    modifier = Modifier.fillMaxWidth()
                ) {
                    Text("Select Folder")
                }
            }
        }
    }
}
```

### `app\src\main\java\com\example\pdf_img_tools_app\ui\components\SingleFilePicker.kt`

```kt
package com.example.pdf_img_tools_app.ui.components

import android.net.Uri
import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
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
import androidx.compose.ui.unit.dp

/**
 * File picker component for selecting a single file
 */
@Composable
fun SingleFilePicker(
    onFileSelected: (Uri) -> Unit,
    supportedMimeTypes: List<String> = listOf("*/*"),
    buttonText: String = "Select File",
    modifier: Modifier = Modifier
) {
    // Delegate to FilePickerHandler for consistent behavior
    FilePickerHandler(
        single = true,
        supportedMimeTypes = supportedMimeTypes,
        onPicked = { uris -> 
            if (uris.isNotEmpty()) {
                onFileSelected(uris.first())
            }
        }
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
            modifier = modifier.fillMaxWidth(),
        ) {
            Icon(
                Icons.Rounded.FileOpen,
                contentDescription = null,
                modifier = Modifier.size(ButtonDefaults.IconSize)
            )
            Spacer(modifier = Modifier.size(ButtonDefaults.IconSpacing))
            Text(
                text = buttonText,
            )
        }
    }
}
```

### `app\src\main\java\com\example\pdf_img_tools_app\ui\components\SmartMessageDisplay.kt`

```kt
package com.example.pdf_img_tools_app.ui.components

import android.content.Context
import androidx.compose.material3.SnackbarHostState
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import com.example.pdf_img_tools_app.model.UiMessageData
import com.example.pdf_img_tools_app.utils.DisplayMethod
import com.example.pdf_img_tools_app.utils.MessageDisplayManager
import com.example.pdf_img_tools_app.utils.UiMessageBus

/**
 * A smart message display system that handles different types of messages
 * and displays them using the most appropriate UI component:
 * - Toast for brief, non-critical notifications
 * - Snackbar for actionable messages and warnings
 * - Dialog for critical errors and important messages
 * - Inline messages for context-specific feedback (original implementation)
 *
 * This component handles all these display methods and ensures only relevant
 * messages are shown in each location.
 */
@Composable
fun SmartMessageDisplay(
    scope: String? = null,
    snackbarHostState: SnackbarHostState? = null,
    showInlineMessages: Boolean = true,
    maxInlineMessages: Int = 3,
    modifier: Modifier = Modifier
) {
    val context = LocalContext.current
    val allMessages by UiMessageBus.messages.collectAsState()
    
    // Filter messages by scope if provided
    val filteredMessages = remember(allMessages, scope) {
        if (scope == null) {
            allMessages
        } else {
            allMessages.filter { it.scope == scope || it.scope == null }
        }
    }
    
    // Handle toast messages
    LaunchedEffect(filteredMessages) {
        val toastMessages = filteredMessages.filter { 
            MessageDisplayManager.determineDisplayMethod(it) == DisplayMethod.TOAST 
        }
        
        if (toastMessages.isNotEmpty()) {
            // Only show the most recent toast message to avoid toast queuing
            val message = toastMessages.maxByOrNull { it.timestamp }
            message?.let {
                MessageDisplayManager.showToast(context, it)
                // Remove toast after displaying to avoid re-showing on recomposition
                UiMessageBus.dismissMessage(it.id)
            }
        }
    }
    
    // Show dialogs for critical errors
    MessageDialogHandler()
    
    // Handle snackbar messages if a SnackbarHostState is provided
    snackbarHostState?.let { hostState ->
        MessageDisplayManager.HandleSnackbarMessages(
            snackbarHostState = hostState,
            messages = filteredMessages,
            coroutineScope = androidx.compose.runtime.rememberCoroutineScope()
        )
    }
    
    // Filter messages for inline display (only show those that should be displayed inline)
    if (showInlineMessages) {
        val inlineMessages = filteredMessages.filter {
            MessageDisplayManager.determineDisplayMethod(it) == DisplayMethod.INLINE
        }
        
        if (inlineMessages.isNotEmpty()) {
            // Show the original inline message display for these messages
            UiMessageDisplay(
                scope = scope,
                maxMessages = maxInlineMessages,
                modifier = modifier
            )
        }
    }
}

/**
 * Extension function to show a Toast directly from any Context
 */
fun Context.showToast(
    message: String,
    isLongDuration: Boolean = false,
    scope: String? = null
) {
    val messageData = UiMessageData.info(
        text = message,
        scope = scope,
        timeout = if (isLongDuration) 3500L else 2000L
    )
    MessageDisplayManager.showToast(this, messageData)
}
```

### `app\src\main\java\com\example\pdf_img_tools_app\ui\components\ToolCard.kt`

```kt
package com.example.pdf_img_tools_app.ui.components

import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.example.pdf_img_tools_app.model.ToolCategory
import com.example.pdf_img_tools_app.model.ToolItem

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
    // Use semantic colors based on category
    val accentColor = when (toolItem.category) {
        // Use primary for PDF and secondary for IMAGE to maintain visual distinction
        ToolCategory.PDF -> MaterialTheme.colorScheme.primary
        ToolCategory.IMAGE -> MaterialTheme.colorScheme.secondary
    }
    
    Card(
        modifier = modifier
            .fillMaxWidth()
            .height(140.dp)
            .clickable(onClick = onClick),
        elevation = CardDefaults.cardElevation(defaultElevation = 0.dp),
        colors = CardDefaults.cardColors(
            containerColor = MaterialTheme.colorScheme.surfaceVariant,
            contentColor = MaterialTheme.colorScheme.onSurfaceVariant
        ),
        shape = RoundedCornerShape(14.dp),
        border = null
    ){
        Column(
            modifier = Modifier
                .padding(14.dp)
                .fillMaxWidth(),
        ){
            Row {
                Column(modifier = Modifier){
                    Icon(
                        imageVector = toolItem.icon,
                        contentDescription = toolItem.name,
                        modifier = Modifier.size(24.dp),
                    )
                }

                Spacer(modifier = Modifier.padding(horizontal = 4.dp))

                Column {
                    Text(
                        text = toolItem.name,
                        style = MaterialTheme.typography.titleLarge,
                        fontWeight = FontWeight.Normal,
                        textAlign = TextAlign.Start,
                    )

                    Text(
                        text = toolItem.description,
                        style = MaterialTheme.typography.bodySmall,
                        textAlign = TextAlign.Start,
                        maxLines = 2,
                        modifier = Modifier.padding(vertical = 16.dp),
                    )
                }
            }
        }
    }
}
```

### `app\src\main\java\com\example\pdf_img_tools_app\ui\components\UiMessageDisplay.kt`

```kt
package com.example.pdf_img_tools_app.ui.components

import androidx.compose.animation.AnimatedVisibility
import androidx.compose.animation.core.tween
import androidx.compose.animation.expandVertically
import androidx.compose.animation.fadeIn
import androidx.compose.animation.fadeOut
import androidx.compose.animation.shrinkVertically
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.example.pdf_img_tools_app.model.MessageType
import com.example.pdf_img_tools_app.model.UiMessageData
import com.example.pdf_img_tools_app.utils.UiMessageBus
import kotlinx.coroutines.flow.filter

/**
 * A composable that displays messages from the UiMessageBus for a specific scope.
 * 
 * @param scope The scope to filter messages for. If null, all messages are shown.
 * @param modifier Modifier to be applied to the layout.
 * @param maxMessages Maximum number of messages to show at once. Default is 3.
 */
@Composable
fun UiMessageDisplay(
    scope: String? = null,
    modifier: Modifier = Modifier,
    maxMessages: Int = 3
) {
    // Get messages from the UiMessageBus and filter by scope
    val allMessages by UiMessageBus.messages.collectAsState()
    
    // Filter messages by scope if a scope is provided
    val messages = remember(allMessages, scope) {
        if (scope == null) {
            // Show all messages if no scope is provided
            allMessages
        } else {
            // Filter messages for the given scope or messages with no scope
            allMessages.filter { it.scope == scope || it.scope == null }
        }
    }
    
    // No need to render anything if there are no messages
    if (messages.isEmpty()) return
    
    // Only show the most recent messages, limited by maxMessages
    val visibleMessages = messages.sortedByDescending { it.timestamp }.take(maxMessages)
    
    AnimatedVisibility(
        visible = visibleMessages.isNotEmpty(),
        enter = fadeIn(animationSpec = tween(300)) + expandVertically(animationSpec = tween(300)),
        exit = fadeOut(animationSpec = tween(300)) + shrinkVertically(animationSpec = tween(300))
    ) {
        Column(
            modifier = modifier
                .fillMaxWidth()
                .padding(8.dp),
            verticalArrangement = Arrangement.spacedBy(8.dp)
        ) {
            visibleMessages.forEach { message ->
                InlineMessage(
                    message = message,
                    onDismiss = { UiMessageBus.dismissMessage(message.id) }
                )
            }
        }
    }
}

/**
 * A composable that allows posting a message directly from a composable function.
 * This is useful for showing messages in response to user actions within the composable.
 * 
 * @param scope The scope to associate with messages posted from this hook.
 * @param content A composable lambda that receives a showMessage function to post messages.
 */
@Composable
fun MessageHandlingScope(
    scope: String,
    content: @Composable (showMessage: (String, MessageType) -> Unit) -> Unit
) {
    val showMessage: (String, MessageType) -> Unit = remember(scope) { 
        { text, type ->
            when (type) {
                MessageType.INFO -> UiMessageBus.showInfo(text, scope)
                MessageType.SUCCESS -> UiMessageBus.showSuccess(text, scope)
                MessageType.WARNING -> UiMessageBus.showWarning(text, scope)
                MessageType.ERROR -> UiMessageBus.showError(text, scope)
            }
        }
    }
    
    content(showMessage)
}
```

### `app\src\main\java\com\example\pdf_img_tools_app\utils\ArchiveUtils.kt`

```kt
package com.example.pdf_img_tools_app.utils

import android.content.Context
import android.net.Uri
import java.io.ByteArrayOutputStream
import java.io.File
import java.io.IOException
import java.util.zip.ZipEntry
import java.util.zip.ZipOutputStream
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import com.example.pdf_img_tools_app.model.SaveLocationType

/**
 * Utility class for handling file archive operations
 */
object ArchiveUtils {
    
    /**
     * Create a zip file from a list of files
     * 
     * @param context Context to access content resolver
     * @param files List of URIs to include in the archive
     * @param outputFile The output zip file
     * @param progressCallback Optional callback for progress updates (0.0-1.0)
     * @return True if successful, false otherwise
     */
    suspend fun createZipFile(
        context: Context, 
        files: List<Pair<Uri, String>>, // Uri and desired filename in the archive
        outputFile: File,
        progressCallback: ((Float) -> Unit)? = null
    ): Boolean = withContext(Dispatchers.IO) {
        if (files.isEmpty()) return@withContext false
        
        try {
            ZipOutputStream(outputFile.outputStream()).use { zipOut ->
                files.forEachIndexed { index, (uri, filename) ->
                    try {
                        // Calculate progress
                        val progress = index.toFloat() / files.size
                        progressCallback?.invoke(progress)
                        
                        // Create a zip entry with the filename
                        val zipEntry = ZipEntry(filename)
                        zipOut.putNextEntry(zipEntry)
                        
                        // Copy the file content to the zip output stream
                        context.contentResolver.openInputStream(uri)?.use { inputStream ->
                            val buffer = ByteArray(8192)
                            var len: Int
                            while (inputStream.read(buffer).also { len = it } != -1) {
                                zipOut.write(buffer, 0, len)
                            }
                        }
                        
                        zipOut.closeEntry()
                        
                    } catch (e: Exception) {
                        android.util.Log.e("ArchiveUtils", "Error adding file to archive: ${e.message}")
                        // Continue with other files even if one fails
                    }
                }
            }
            
            // Final progress update
            progressCallback?.invoke(1.0f)
            return@withContext true
            
        } catch (e: IOException) {
            android.util.Log.e("ArchiveUtils", "Error creating zip file: ${e.message}")
            e.printStackTrace()
            return@withContext false
        }
    }
    
    /**
     * Create a zip file and save it using FileUtils to either Downloads or custom location
     * 
     * @param context Context
     * @param files List of files to archive
     * @param fileName Desired filename for the archive
     * @param saveLocationType Where to save (Downloads or Custom)
     * @param customSaveLocationUri Custom location URI if applicable
     * @param progressCallback Optional progress callback
     * @return The URI of the saved archive file, or null if failed
     */
    suspend fun createAndSaveZipFile(
        context: Context,
        files: List<Pair<Uri, String>>,
        fileName: String,
        saveLocationType: SaveLocationType,
        customSaveLocationUri: Uri? = null,
        progressCallback: ((Float) -> Unit)? = null
    ): Uri? = withContext(Dispatchers.IO) {
        try {
            // Create temporary zip file
            val tempFile = FileUtils.createTempFile(context, "archive", ".zip")
                ?: return@withContext null
            
            // Create the zip file
            val success = createZipFile(context, files, tempFile, progressCallback)
            if (!success) {
                tempFile.delete()
                return@withContext null
            }
            
            // Save the zip file to the appropriate location
            val uri = when (saveLocationType) {
                SaveLocationType.DOWNLOADS -> {
                    FileUtils.saveFileToDownloads(
                        context, 
                        tempFile, 
                        "$fileName.zip", 
                        "application/zip"
                    )
                }
                SaveLocationType.CUSTOM -> {
                    if (customSaveLocationUri == null) return@withContext null
                    
                    FileUtils.saveFileToDirectory(
                        context,
                        tempFile,
                        customSaveLocationUri,
                        "$fileName.zip",
                        "application/zip"
                    )
                }
                // Include an else branch to make the when expression exhaustive
                else -> {
                    android.util.Log.e("ArchiveUtils", "Unsupported save location type: $saveLocationType")
                    null
                }
            }
            
            // Clean up temporary file
            tempFile.delete()
            
            return@withContext uri
        } catch (e: Exception) {
            android.util.Log.e("ArchiveUtils", "Error in createAndSaveZipFile: ${e.message}")
            return@withContext null
        }
    }
} ```

### `app\src\main\java\com\example\pdf_img_tools_app\utils\DisplayMethod.kt`

```kt
package com.example.pdf_img_tools_app.utils

/**
 * Enum representing different methods for displaying messages
 */
enum class DisplayMethod {
    TOAST,      // Short-lived message shown at the bottom of the screen
    SNACKBAR,   // Message with possible actions, shown at bottom of the screen
    DIALOG,     // Modal dialog requiring user acknowledgment
    INLINE      // Inline message within the UI (fallback to original implementation)
}
```

### `app\src\main\java\com\example\pdf_img_tools_app\utils\FileUtils.kt`

```kt
package com.example.pdf_img_tools_app.utils

import android.content.ContentResolver
import android.content.ContentValues
import android.content.Context
import android.database.Cursor
import android.graphics.Bitmap
import android.graphics.BitmapFactory
import android.net.Uri
import android.os.Build
import android.os.Environment
import android.provider.MediaStore
import android.provider.OpenableColumns
import android.webkit.MimeTypeMap
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Description // PDF Icon
import androidx.compose.material.icons.filled.Image // Image Icon
import androidx.compose.material.icons.automirrored.filled.InsertDriveFile // Use AutoMirrored version
import androidx.compose.ui.graphics.vector.ImageVector
import java.io.File
import java.io.FileInputStream
import java.io.FileOutputStream
import java.io.IOException
import java.text.SimpleDateFormat
import java.util.Date
import java.util.Locale
import java.util.zip.ZipEntry
import java.util.zip.ZipOutputStream
import kotlin.math.log10
import kotlin.math.pow
import android.provider.DocumentsContract
import android.content.Intent
import com.tom_roush.pdfbox.pdmodel.PDDocument
import java.io.InputStream

data class FileDetails(
    val uri: Uri,
    val name: String,
    val size: Long, // Size in bytes
    val mimeType: String,
    val path: String? = null,
    val dimensions: Pair<Int, Int>? = null,// Width, Height for images
    val pageCount: Int? = null
)

// FileExtraDetails class has been removed as part of the refactoring

/**
 * Utility functions for file operations
 */
object FileUtils {

    // Structure to hold image dimensions
    // data class ImageDimensions(val width: Int, val height: Int) // Replaced by Pair<Int, Int> in FileDetails

    /**
     * Create a temporary file in the app's cache directory
     */
    fun createTempFile(context: Context, prefix: String, suffix: String): File? { // Return nullable
        return try {
            val timeStamp = SimpleDateFormat("yyyyMMdd_HHmmss", Locale.getDefault()).format(Date())
            val fileName = "${prefix}_${timeStamp}"
            File.createTempFile(fileName, suffix, context.cacheDir)
        } catch (e: IOException) {
            e.printStackTrace() // Log error
            null
        }
    }

    /**
     * Create an output file placeholder (primarily for naming/path structure, might not be needed with MediaStore)
     * DEPRECATED if using MediaStore for saving.
     */
    @Deprecated("Use MediaStore or SAF for saving files to shared storage.")
    fun createOutputFileInAppDir(context: Context, prefix: String, suffix: String): File {
        val timeStamp = SimpleDateFormat("yyyyMMdd_HHmmss", Locale.getDefault()).format(Date())
        val fileName = "${prefix}_${timeStamp}${suffix}"
        
        val directory = File(context.getExternalFilesDir(Environment.DIRECTORY_DOWNLOADS), "PDF_IMG_Tools")
        if (!directory.exists()) {
            directory.mkdirs()
        }
        
        return File(directory, fileName)
    }

    /**
     * Get the file name from a URI
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
     * Get MIME type from URI
     */
    fun getMimeType(context: Context, uri: Uri): String? {
        return context.contentResolver.getType(uri)
    }

    /**
     * Get file size from URI
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
     * Format file size into human-readable string (KB, MB, GB)
     */
    fun formatFileSize(sizeBytes: Long): String {
        if (sizeBytes <= 0) return "0 B"
        val units = arrayOf("B", "KB", "MB", "GB", "TB")
        val digitGroups = (log10(sizeBytes.toDouble()) / log10(1024.0)).toInt()
        // Prevent index out of bounds for extremely large files
        val safeDigitGroups = digitGroups.coerceIn(0, units.size - 1) 
        return String.format(Locale.getDefault(), "%.1f %s", sizeBytes / 1024.0.pow(safeDigitGroups.toDouble()), units[safeDigitGroups])
    }

    /**
     * Get image dimensions from URI without loading the full bitmap
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
             // Handle exceptions like FileNotFoundException
             e.printStackTrace()
             return null
        }
        return null
    }

    /**
     * Get the full path from a URI (best effort, might not always be possible)
     */
     fun getPathFromUri(context: Context, uri: Uri): String {
         // This is complex and often unreliable, especially with scoped storage.
         // For display purposes, the URI string itself might be the best representation.
         // A common approach for MediaStore URIs:
         if (ContentResolver.SCHEME_CONTENT == uri.scheme) {
             try {
                 context.contentResolver.query(
                     uri,
                     arrayOf(MediaStore.MediaColumns.DATA), // Deprecated but sometimes works
                     null, null, null
                 )?.use { cursor ->
                     if (cursor.moveToFirst()) {
                         val dataIndex = cursor.getColumnIndex(MediaStore.MediaColumns.DATA)
                         if (dataIndex != -1) {
                             val path = cursor.getString(dataIndex)
                             if (!path.isNullOrEmpty()) return path
                         }
                     }
                 }
             } catch (e: Exception) { /* Ignore */ }
         }
         // Fallback to URI path component or the full URI string
         return uri.path ?: uri.toString()
     }

    // Tries to get a displayable path, might not always work depending on Uri source
    private fun getFilePath(context: Context, uri: Uri): String? {
        // This is complex and might not work for all URIs (especially cloud/SAF ones)
        // For simplicity, we'll often just show the filename or "Content URI"
        if (uri.scheme == "file") {
            return uri.path
        }
        if (uri.scheme == "content") {
             // Attempt to get path from MediaStore for common media types
             val projection = arrayOf(MediaStore.MediaColumns.DATA)
             try {
                 context.contentResolver.query(uri, projection, null, null, null)?.use { cursor ->
                     if (cursor.moveToFirst()) {
                         val columnIndex = cursor.getColumnIndexOrThrow(MediaStore.MediaColumns.DATA)
                         return cursor.getString(columnIndex)
                     }
                 }
             } catch (e: Exception) {
                 // Ignore if column doesn't exist or other error
             }
             // Fallback for content URIs - Return the URI string itself for clarity
             return uri.toString() 
        }
        return uri.toString() // Fallback
    }

    fun getFileDetails(context: Context, uri: Uri): FileDetails {
        val contentResolver = context.contentResolver
        val name = getFileName(context, uri)
        val size = getFileSize(context, uri)
        val path = getFilePath(context, uri)
        val mimeType = getMimeType(context, uri)

        var dimensions: Pair<Int, Int>? = null
        var pageCount: Int? = null

        if (mimeType?.startsWith("image/") == true) {
            dimensions = getImageDimensions(context, uri)
        } else if (mimeType == "application/pdf") {
            pageCount = getPageCount(context, uri)
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


    // Helper to get appropriate icon based on MIME type
     fun getIconForMimeType(mimeType: String?): ImageVector {
         return when {
             mimeType == null -> Icons.AutoMirrored.Filled.InsertDriveFile
             mimeType.startsWith("image/") -> Icons.Default.Image
             mimeType == "application/pdf" -> Icons.Default.Description
             else -> Icons.AutoMirrored.Filled.InsertDriveFile
         }
     }

    // Renamed createOutputFile to createTempOutputFile to avoid confusion
    // fun createOutputFile(...) -> Now createTempOutputFile
    
    // Function to save a file (from cache) to external storage (Downloads)
    // Returns the final Uri if successful, null otherwise
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
        } else {
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
             // Clean up if insert failed or writing failed
             outputUri?.let { resolver.delete(it, null, null) }
             outputUri = null
        } finally {
             // Consider deleting the temporary cache file here or after confirmation
             // sourceFile.delete()
        }
        return outputUri // Uri of the saved file in Downloads
    }
    
    // Make createOutputFile use createTempOutputFile to avoid confusion
    @Deprecated("Use createTempOutputFile for temporary files", ReplaceWith("createTempFile(context, prefix, suffix)"))
    fun createOutputFile(context: Context, prefix: String, suffix: String): File? {
         return createTempFile(context, prefix, suffix)
    }
     
    // Ensure saveToExternalStorage points to the correct implementation
    fun saveToExternalStorage(
         context: Context,
         sourceFile: File,
         outputFileName: String,
         mimeType: String
     ): Uri? {
         // This is the correct function to call
         return saveFileToDownloads(context, sourceFile, outputFileName, mimeType)
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
            android.util.Log.d("FileUtils", "Starting saveFileToDirectory with destination: $destinationDirUri")
            android.util.Log.d("FileUtils", "URI authority: ${destinationDirUri.authority}, scheme: ${destinationDirUri.scheme}")
            
            // Show a toast with the URI for debugging
            android.widget.Toast.makeText(
                context,
                "Trying to save to: ${destinationDirUri.lastPathSegment}",
                android.widget.Toast.LENGTH_SHORT
            ).show()
            
            // First verify the source file exists and is readable
            if (!sourceFile.exists() || !sourceFile.canRead()) {
                android.util.Log.e("FileUtils", "Source file doesn't exist or can't be read: ${sourceFile.absolutePath}")
                android.widget.Toast.makeText(context, "Source file error: ${sourceFile.name}", android.widget.Toast.LENGTH_LONG).show()
                return null
            }
            
            // Log source file details
            android.util.Log.d("FileUtils", "Source file: ${sourceFile.absolutePath}, size: ${sourceFile.length()} bytes")
            
            // Make sure we have the right flags for the destination directory URI
            val takeFlags = Intent.FLAG_GRANT_READ_URI_PERMISSION or Intent.FLAG_GRANT_WRITE_URI_PERMISSION
            
            // Try to persist permissions if we don't already have them
            try {
                context.contentResolver.takePersistableUriPermission(destinationDirUri, takeFlags)
                android.util.Log.d("FileUtils", "Took persistable URI permission for $destinationDirUri")
            } catch (e: SecurityException) {
                // This may fail if we already have the permission or if permission isn't persistable
                android.util.Log.w("FileUtils", "Could not take persistable permission: ${e.message}")
                android.widget.Toast.makeText(context, "Permission warning - continuing anyway", android.widget.Toast.LENGTH_SHORT).show()
                // Continue anyway as we might still have permission for this session
            }
            
            // Sanitize filename to avoid special characters that might cause issues
            val sanitizedFilename = filename.replace("[\\\\/:*?\"<>|]".toRegex(), "_")
            
            android.util.Log.d("FileUtils", "Sanitized filename: $sanitizedFilename")
            
            // Alternative approach that sometimes works better for certain providers
            try {
                // Create a new file URI and get an output stream
                var newFileUri: Uri? = null
                
                // Determine if this is a tree URI that needs special handling
                val isTreeUri = destinationDirUri.toString().contains("/tree/")
                android.util.Log.d("FileUtils", "Destination URI: $destinationDirUri, isTreeUri=$isTreeUri")
                
                if (isTreeUri) {
                    try {
                        // For tree URIs, always use the childDocuments approach
                        val docId = DocumentsContract.getTreeDocumentId(destinationDirUri)
                        android.util.Log.d("FileUtils", "Tree document ID: $docId")
                        
                        // Get the document URI first (not children URI)
                        val documentUri = DocumentsContract.buildDocumentUriUsingTree(
                            destinationDirUri,
                            docId
                        )
                        android.util.Log.d("FileUtils", "Document URI: $documentUri")
                        
                        // Now create the new file in this directory
                        newFileUri = DocumentsContract.createDocument(
                            context.contentResolver,
                            documentUri,
                            mimeType ?: "application/octet-stream",
                            sanitizedFilename
                        )
                        android.util.Log.d("FileUtils", "Created document using tree URI: $newFileUri")
                    } catch (e: Exception) {
                        android.util.Log.e("FileUtils", "Error with tree URI approach: ${e.javaClass.simpleName} - ${e.message}")
                        // Fall back to standard approach as last resort
                    }
                } else {
                    // Standard DocumentsContract approach for non-tree URIs
                    android.util.Log.d("FileUtils", "Attempting to create document using standard DocumentsContract")
                    try {
                        newFileUri = DocumentsContract.createDocument(
                            context.contentResolver,
                            destinationDirUri,
                            mimeType ?: "application/octet-stream",
                            sanitizedFilename
                        )
                        android.util.Log.d("FileUtils", "DocumentsContract created URI: $newFileUri")
                    } catch (e: Exception) {
                        android.util.Log.e("FileUtils", "Error with DocumentsContract: ${e.javaClass.simpleName} - ${e.message}")
                    }
                }
                
                // If we still don't have a file URI, try one more approach for certain providers
                if (newFileUri == null && isTreeUri) {
                    android.util.Log.d("FileUtils", "Trying alternative tree URI approach with children")
                    try {
                        // Last attempt: try using buildChildDocumentsUriUsingTree
                        val docId = DocumentsContract.getTreeDocumentId(destinationDirUri)
                        val childrenUri = DocumentsContract.buildChildDocumentsUriUsingTree(
                            destinationDirUri,
                            docId
                        )
                        
                        android.util.Log.d("FileUtils", "Using children URI: $childrenUri")
                        
                        // Try to create document with children URI
                        newFileUri = DocumentsContract.createDocument(
                            context.contentResolver,
                            destinationDirUri, // Use original URI as last resort
                            mimeType ?: "application/octet-stream",
                            sanitizedFilename
                        )
                        android.util.Log.d("FileUtils", "Created document using alternative approach: $newFileUri")
                    } catch (e: Exception) {
                        android.util.Log.e("FileUtils", "Error with alternative approach: ${e.javaClass.simpleName} - ${e.message}")
                        // At this point, we've tried everything - log failure but continue to try openOutputStream approach
                    }
                }
                
                // If we have a URI, try to write to it
                if (newFileUri != null) {
                    android.util.Log.d("FileUtils", "Got URI for new file: $newFileUri")
                    
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
                        android.util.Log.e("FileUtils", "Error writing to output stream: ${e.message}")
                        android.widget.Toast.makeText(context, "Error writing file: ${e.message}", android.widget.Toast.LENGTH_LONG).show()
                        
                        // Try to delete the partial file
                        try {
                            DocumentsContract.deleteDocument(context.contentResolver, newFileUri)
                        } catch (e2: Exception) {
                            android.util.Log.e("FileUtils", "Could not delete partial file: ${e2.message}")
                        }
                        return null
                    }
                    
                    if (success) {
                        android.util.Log.d("FileUtils", "File successfully saved to $newFileUri")
                        android.widget.Toast.makeText(context, "File saved successfully", android.widget.Toast.LENGTH_SHORT).show()
                        return newFileUri
                    }
                } else {
                    android.util.Log.e("FileUtils", "Could not create document URI")
                    android.widget.Toast.makeText(context, "Could not create file at selected location", android.widget.Toast.LENGTH_LONG).show()
                }
            } catch (e: Exception) {
                android.util.Log.e("FileUtils", "Error in saveFileToDirectory: ${e.javaClass.simpleName} - ${e.message}")
                android.widget.Toast.makeText(context, "Error: ${e.message}", android.widget.Toast.LENGTH_LONG).show()
                e.printStackTrace()
            }
            
            return null
        } catch (e: Exception) {
            android.util.Log.e("FileUtils", "Unexpected error: ${e.javaClass.simpleName} - ${e.message}")
            android.widget.Toast.makeText(context, "Unexpected error: ${e.message}", android.widget.Toast.LENGTH_LONG).show()
            e.printStackTrace()
            return null
        }
    }
    
    /**
     * Creates a ZIP archive containing all provided files
     *
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
                
                // Fallback if pattern doesn't match
                return "Selected: $path"
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

    /**
     * Load a bitmap from a URI with memory efficient options
     * @param context Context
     * @param uri URI of the image
     * @return Bitmap or null if failed
     */
    fun getBitmapFromUri(context: Context, uri: Uri): Bitmap? {
        try {
            // First get the image dimensions to calculate appropriate sample size
            val options = BitmapFactory.Options().apply {
                inJustDecodeBounds = true
            }
            
            context.contentResolver.openInputStream(uri)?.use { inputStream ->
                BitmapFactory.decodeStream(inputStream, null, options)
            }
            
            // Calculate inSampleSize to load a bitmap that's not too large
            val maxTargetSize = 1024 // Target size for preview (1024px)
            var inSampleSize = 1
            
            if (options.outWidth > maxTargetSize || options.outHeight > maxTargetSize) {
                val halfWidth = options.outWidth / 2
                val halfHeight = options.outHeight / 2
                
                // Calculate the largest inSampleSize value that is a power of 2 and keeps both
                // height and width larger than the requested height and width.
                while ((halfWidth / inSampleSize) >= maxTargetSize || 
                       (halfHeight / inSampleSize) >= maxTargetSize) {
                    inSampleSize *= 2
                }
            }
            
            // Decode with the calculated sample size
            options.apply {
                inJustDecodeBounds = false
                inSampleSize = inSampleSize
                inPreferredConfig = Bitmap.Config.ARGB_8888
            }
            
            return context.contentResolver.openInputStream(uri)?.use { inputStream ->
                BitmapFactory.decodeStream(inputStream, null, options)
            }
        } catch (e: Exception) {
            e.printStackTrace()
            return null
        }
    }
    
    /**
     * Get a thumbnail bitmap from a URI with a specific size
     * @param context Context
     * @param uri URI of the image
     * @param size Desired size (max width/height) of the thumbnail
     * @return Bitmap or null if failed
     */
    fun getThumbnail(context: Context, uri: Uri, size: Int = 120): Bitmap? {
        try {
            // First get the image dimensions to calculate appropriate sample size
            val options = BitmapFactory.Options().apply {
                inJustDecodeBounds = true
            }
            
            context.contentResolver.openInputStream(uri)?.use { inputStream ->
                BitmapFactory.decodeStream(inputStream, null, options)
            }
            
            // Calculate inSampleSize to load a thumbnail that's appropriate for the desired size
            var inSampleSize = 1
            
            if (options.outWidth > size || options.outHeight > size) {
                val halfWidth = options.outWidth / 2
                val halfHeight = options.outHeight / 2
                
                while ((halfWidth / inSampleSize) >= size || 
                       (halfHeight / inSampleSize) >= size) {
                    inSampleSize *= 2
                }
            }
            
            // Decode with the calculated sample size
            options.apply {
                inJustDecodeBounds = false
                inSampleSize = inSampleSize
                inPreferredConfig = Bitmap.Config.ARGB_8888
            }
            
            return context.contentResolver.openInputStream(uri)?.use { inputStream ->
                BitmapFactory.decodeStream(inputStream, null, options)
            }
        } catch (e: Exception) {
            e.printStackTrace()
            return null
        }
    }

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
}
```

### `app\src\main\java\com\example\pdf_img_tools_app\utils\MessageDisplayManager.kt`

```kt
package com.example.pdf_img_tools_app.utils

import android.content.Context
import android.widget.Toast
import androidx.compose.material3.SnackbarDuration
import androidx.compose.material3.SnackbarHostState
import androidx.compose.material3.SnackbarResult
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.rememberCoroutineScope
import com.example.pdf_img_tools_app.model.MessageType
import com.example.pdf_img_tools_app.model.UiMessageData
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.launch

/**
 * A manager for displaying messages throughout the application using appropriate UI components
 * based on message type and importance:
 * - Toast: For short, non-critical notifications
 * - Snackbar: For semi-important notifications that may need user action
 * - Dialog: For critical messages requiring user acknowledgment
 */
object MessageDisplayManager {
    
    /**
     * Determines the most appropriate display method for a message.
     * - INFO messages are shown as Toasts
     * - SUCCESS messages are shown as Toasts or Snackbars based on importance
     * - WARNING messages are shown as Snackbars
     * - ERROR messages are shown as Snackbars (dismissible) or Dialogs (for critical errors)
     */
    fun determineDisplayMethod(message: UiMessageData): DisplayMethod {
        // Check if display method is specified in the metadata
        message.metadata["displayMethod"]?.let {
            return try {
                DisplayMethod.valueOf(it)
            } catch (e: IllegalArgumentException) {
                // Fallback to default behavior if the value is invalid
                getDefaultDisplayMethod(message)
            }
        }
        
        return getDefaultDisplayMethod(message)
    }
    
    private fun getDefaultDisplayMethod(message: UiMessageData): DisplayMethod {
        return when (message.type) {
            MessageType.INFO -> DisplayMethod.TOAST
            MessageType.SUCCESS -> DisplayMethod.SNACKBAR
            MessageType.WARNING -> DisplayMethod.SNACKBAR
            MessageType.ERROR -> {
                if (message.text.length > 80 || !message.dismissible) {
                    DisplayMethod.DIALOG
                } else {
                    DisplayMethod.SNACKBAR
                }
            }
        }
    }
    
    /**
     * Display a toast message
     */
    fun showToast(context: Context, message: UiMessageData) {
        val duration = if (message.timeout != null && message.timeout > 3500) {
            Toast.LENGTH_LONG
        } else {
            Toast.LENGTH_SHORT
        }
        
        Toast.makeText(context, message.text, duration).show()
    }
    
    /**
     * Format a message for display, trimming it if necessary
     */
    fun formatMessageForDisplay(message: UiMessageData, maxLength: Int = 200): String {
        return if (message.text.length > maxLength) {
            message.text.take(maxLength - 3) + "..."
        } else {
            message.text
        }
    }
    
    /**
     * Helper function to handle showing messages as Snackbars
     */
    @Composable
    fun HandleSnackbarMessages(
        snackbarHostState: SnackbarHostState,
        messages: List<UiMessageData>,
        coroutineScope: CoroutineScope
    ) {
        // Get only snackbar messages
        val snackbarMessages = messages.filter { 
            determineDisplayMethod(it) == DisplayMethod.SNACKBAR 
        }
        
        if (snackbarMessages.isNotEmpty()) {
            // Get the latest message
            val message = snackbarMessages.maxByOrNull { it.timestamp } ?: return
            
            LaunchedEffect(message.id) {
                val actionLabel = if (message.dismissible) "Dismiss" else null
                val duration = if (message.type == MessageType.ERROR) {
                    SnackbarDuration.Long
                } else {
                    SnackbarDuration.Short
                }
                
                val result = snackbarHostState.showSnackbar(
                    message = formatMessageForDisplay(message),
                    actionLabel = actionLabel,
                    duration = duration
                )
                
                if (result == SnackbarResult.Dismissed || result == SnackbarResult.ActionPerformed) {
                    UiMessageBus.dismissMessage(message.id)
                }
            }
        }
    }
    
    /**
     * Helper extension function for SnackbarHostState
     */
    @Composable
    fun SnackbarHostState.handleMessages(
        messages: List<UiMessageData>,
        coroutineScope: CoroutineScope = rememberCoroutineScope()
    ) {
        HandleSnackbarMessages(this, messages, coroutineScope)
    }
}
```

### `app\src\main\java\com\example\pdf_img_tools_app\utils\NotificationUtils.kt`

```kt
package com.example.pdf_img_tools_app.utils

import android.content.Context
import android.widget.Toast
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Snackbar
import androidx.compose.material3.SnackbarData
import androidx.compose.material3.SnackbarDuration
import androidx.compose.material3.SnackbarHost
import androidx.compose.material3.SnackbarHostState
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.launch

/**
 * Message types
 */
enum class MessageType {
    SUCCESS,
    ERROR,
    INFO,
    WARNING
}

/**
 * Shows a Toast message
 */
fun showToast(context: Context, message: String, duration: Int = Toast.LENGTH_SHORT) {
    Toast.makeText(context, message, duration).show()
}

/**
 * Custom Snackbar host with improved state handling
 */
@Composable
fun AppSnackbarHost(
    hostState: SnackbarHostState,
    modifier: Modifier = Modifier
) {
    // Use a stable context to avoid recomposition issues
    val context = LocalContext.current

    SnackbarHost(
        hostState = hostState,
        modifier = modifier,
        snackbar = { snackbarData ->
            val messageType = try {
                snackbarData.visuals.actionLabel?.let {
                    when (it) {
                        "SUCCESS" -> MessageType.SUCCESS
                        "ERROR" -> MessageType.ERROR
                        "WARNING" -> MessageType.WARNING
                        else -> MessageType.INFO
                    }
                } ?: MessageType.INFO
            } catch (e: Exception) {
                // Fallback to INFO if there's any error
                MessageType.INFO
            }

            CustomSnackbar(
                snackbarData = snackbarData,
                messageType = messageType
            )
        }
    )
}

/**
 * Custom Snackbar with different colors based on message type
 */
@Composable
fun CustomSnackbar(
    snackbarData: SnackbarData,
    messageType: MessageType
) {
    val backgroundColor = when (messageType) {
        MessageType.SUCCESS -> Color(0xFF4CAF50)
        MessageType.ERROR -> Color(0xFFF44336)
        MessageType.INFO -> MaterialTheme.colorScheme.secondary
        MessageType.WARNING -> Color(0xFFFF9800) // Orange color for warnings
    }

    Snackbar(
        snackbarData = snackbarData,
        contentColor = Color.White,
        containerColor = backgroundColor
    )
}

/**
 * Extension function for SnackbarHostState to show a message with type
 */
suspend fun SnackbarHostState.showMessage(
    message: String,
    messageType: MessageType,
    duration: SnackbarDuration = SnackbarDuration.Short
) {
    try {
        this.showSnackbar(
            message = message,
            actionLabel = messageType.name,
            duration = duration
        )
    } catch (e: Exception) {
        // Catch any exceptions that might occur during snackbar display
        // This prevents crashes if the composition is disposed while showing a snackbar
    }
}

/**
 * Helper function to safely show a message in a coroutine scope
 */
fun SnackbarHostState.showMessageInScope(
    scope: CoroutineScope,
    message: String,
    messageType: MessageType,
    duration: SnackbarDuration = SnackbarDuration.Short
) {
    scope.launch {
        showMessage(message, messageType, duration)
    }
} ```

### `app\src\main\java\com\example\pdf_img_tools_app\utils\SaveLocationUtils.kt`

```kt
package com.example.pdf_img_tools_app.utils

import android.content.Context
import android.net.Uri
import java.io.File
import com.example.pdf_img_tools_app.model.SaveMode

/**
 * Utility functions for handling save locations with the new ReusableSaveLocationSelector component
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
                android.util.Log.d("SaveLocationUtils", "Found URI for $savePath: $uriString")
                return Uri.parse(uriString) 
            } catch (e: Exception) {
                android.util.Log.e("SaveLocationUtils", "Error parsing URI: ${e.message}")
            }
        } else {
            android.util.Log.w("SaveLocationUtils", "No URI found for path: $savePath")
        }
        
        // Fallback: check if path starts with 'Selected:' which indicates a fallback path name
        if (savePath.startsWith("Selected:")) {
            // Look through all saved URIs in case the display name doesn't match but we still have the URI
            val allEntries = sharedPrefs.all
            for (entry in allEntries) {
                android.util.Log.d("SaveLocationUtils", "Checking saved location: ${entry.key} = ${entry.value}")
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
        android.util.Log.d("SaveLocationUtils", "Saving file to: $savePath using mode: $saveMode")
        
        // If savePath is Downloads or empty, use the Downloads folder
        val isDefaultDownloads = savePath.isEmpty() || savePath == "Downloads"
        
        // Get the directory URI if using a custom location
        val saveLocationUri = if (!isDefaultDownloads) {
            val uri = getSaveLocationUri(context, savePath)
            android.util.Log.d("SaveLocationUtils", "Custom location URI: $uri")
            uri
        } else {
            android.util.Log.d("SaveLocationUtils", "Using default Downloads location")
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
            val success = FileUtils.createZipArchive(listOf(sourceFile), zipFile)
            android.util.Log.d("SaveLocationUtils", "Created ZIP archive: $success, file exists: ${zipFile.exists()}, size: ${zipFile.length()} bytes")
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
            android.util.Log.w("SaveLocationUtils", "Failed to get URI for manual location. Falling back to Downloads")
            return FileUtils.saveFileToDownloads(context, fileToSave, finalFileName, finalMimeType)
        }
        
        // Save to the appropriate location
        return if (isDefaultDownloads || saveLocationUri == null) {
            // Save to Downloads
            android.util.Log.d("SaveLocationUtils", "Saving to Downloads: $finalFileName")
            FileUtils.saveFileToDownloads(
                context,
                fileToSave,
                finalFileName,
                finalMimeType
            )
        } else {
            // Save to custom location
            android.util.Log.d("SaveLocationUtils", "Saving to custom location: $savePath, $finalFileName")
            FileUtils.saveFileToDirectory(
                context,
                fileToSave,
                saveLocationUri,
                finalFileName,
                finalMimeType
            )
        }
    }
    
    /**
     * Saves a list of files to the selected location
     *
     * @param context The application context
     * @param sourceFiles The list of source files to save
     * @param outputBaseFileName The base name for output files
     * @param mimeType The mime type of the files
     * @param savePath The save path from ReusableSaveLocationSelector
     * @param saveMode The save mode (SEPARATELY or AS_ARCHIVE)
     * @return A list of URIs for the saved files, or an empty list if saving failed
     */
    fun saveMultipleToLocation(
        context: Context,
        sourceFiles: List<File>,
        outputBaseFileName: String,
        mimeType: String,
        savePath: String,
        saveMode: SaveMode
    ): List<Uri> {
        android.util.Log.d("SaveLocationUtils", "Saving ${sourceFiles.size} files to: $savePath using mode: $saveMode")
        
        if (sourceFiles.isEmpty()) return emptyList()
        
        // If savePath is Downloads or empty, use the Downloads folder
        val isDefaultDownloads = savePath.isEmpty() || savePath == "Downloads"
        
        // Get the directory URI if using a custom location
        val saveLocationUri = if (!isDefaultDownloads) {
            val uri = getSaveLocationUri(context, savePath)
            android.util.Log.d("SaveLocationUtils", "Custom location URI: $uri")
            uri
        } else {
            android.util.Log.d("SaveLocationUtils", "Using default Downloads location")
            null
        }
        
        return if (saveMode == SaveMode.AS_ARCHIVE) {
            // Save as a single archive
            val zipFileName = "${outputBaseFileName}.zip"
            val zipFile = File(context.cacheDir, zipFileName)
            val success = FileUtils.createZipArchive(sourceFiles, zipFile)
            android.util.Log.d("SaveLocationUtils", "Created ZIP archive: $success, file exists: ${zipFile.exists()}, size: ${zipFile.length()} bytes")
            
            // Check if we actually got a valid URI for manual location
            if (!isDefaultDownloads && saveLocationUri == null) {
                android.util.Log.w("SaveLocationUtils", "Failed to get URI for manual location. Falling back to Downloads")
                val downloadUri = FileUtils.saveFileToDownloads(context, zipFile, zipFileName, "application/zip")
                downloadUri?.let { listOf(it) } ?: emptyList()
            } else {
                // Save to the appropriate location
                val savedUri = if (isDefaultDownloads || saveLocationUri == null) {
                    android.util.Log.d("SaveLocationUtils", "Saving archive to Downloads: $zipFileName")
                    FileUtils.saveFileToDownloads(context, zipFile, zipFileName, "application/zip")
                } else {
                    android.util.Log.d("SaveLocationUtils", "Saving archive to custom location: $savePath, $zipFileName")
                    FileUtils.saveFileToDirectory(context, zipFile, saveLocationUri, zipFileName, "application/zip")
                }
                
                savedUri?.let { listOf(it) } ?: emptyList()
            }
        } else {
            // Save files separately
            val results = mutableListOf<Uri>()
            
            // Check if we actually got a valid URI for manual location
            if (!isDefaultDownloads && saveLocationUri == null) {
                android.util.Log.w("SaveLocationUtils", "Failed to get URI for manual location. Falling back to Downloads")
                
                sourceFiles.forEachIndexed { index, file ->
                    val fileName = if (sourceFiles.size > 1) {
                        "${outputBaseFileName}_${index + 1}${file.extension.let { if (it.isNotEmpty()) ".$it" else "" }}"
                    } else {
                        "$outputBaseFileName${file.extension.let { if (it.isNotEmpty()) ".$it" else "" }}"
                    }
                    
                    val savedUri = FileUtils.saveFileToDownloads(context, file, fileName, mimeType)
                    savedUri?.let { results.add(it) }
                }
                
                return results
            }
            
            // Normal case - save to selected location
            sourceFiles.forEachIndexed { index, file ->
                val fileName = if (sourceFiles.size > 1) {
                    "${outputBaseFileName}_${index + 1}${file.extension.let { if (it.isNotEmpty()) ".$it" else "" }}"
                } else {
                    "$outputBaseFileName${file.extension.let { if (it.isNotEmpty()) ".$it" else "" }}"
                }
                
                val savedUri = if (isDefaultDownloads || saveLocationUri == null) {
                    android.util.Log.d("SaveLocationUtils", "Saving file to Downloads: $fileName")
                    FileUtils.saveFileToDownloads(context, file, fileName, mimeType)
                } else {
                    android.util.Log.d("SaveLocationUtils", "Saving file to custom location: $savePath, $fileName")
                    FileUtils.saveFileToDirectory(context, file, saveLocationUri, fileName, mimeType)
                }
                
                savedUri?.let { results.add(it) }
            }
            
            results
        }
    }
}
```

### `app\src\main\java\com\example\pdf_img_tools_app\utils\UiMessageBus.kt`

```kt
package com.example.pdf_img_tools_app.utils

import com.example.pdf_img_tools_app.model.MessageType
import com.example.pdf_img_tools_app.model.UiMessageData
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.delay
import kotlinx.coroutines.flow.MutableSharedFlow
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.SharedFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asSharedFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.update
import kotlinx.coroutines.launch

/**
 * Centralized bus for managing UI messages across the application.
 * This singleton provides methods to show, update and dismiss messages,
 * as well as observe messages for specific scopes.
 */
object UiMessageBus {
    private val coroutineScope = CoroutineScope(Dispatchers.Main)
    
    // Holds all active messages
    private val _messages = MutableStateFlow<List<UiMessageData>>(emptyList())
    val messages: StateFlow<List<UiMessageData>> = _messages.asStateFlow()
    
    // Event flow for message actions
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
        // For errors, let the MessageDisplayManager determine the best method
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

### `app\src\main\res\drawable\ic_launcher_background.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="108dp"
    android:height="108dp"
    android:viewportWidth="108"
    android:viewportHeight="108">
    <path
        android:fillColor="#3DDC84"
        android:pathData="M0,0h108v108h-108z" />
    <path
        android:fillColor="#00000000"
        android:pathData="M9,0L9,108"
        android:strokeWidth="0.8"
        android:strokeColor="#33FFFFFF" />
    <path
        android:fillColor="#00000000"
        android:pathData="M19,0L19,108"
        android:strokeWidth="0.8"
        android:strokeColor="#33FFFFFF" />
    <path
        android:fillColor="#00000000"
        android:pathData="M29,0L29,108"
        android:strokeWidth="0.8"
        android:strokeColor="#33FFFFFF" />
    <path
        android:fillColor="#00000000"
        android:pathData="M39,0L39,108"
        android:strokeWidth="0.8"
        android:strokeColor="#33FFFFFF" />
    <path
        android:fillColor="#00000000"
        android:pathData="M49,0L49,108"
        android:strokeWidth="0.8"
        android:strokeColor="#33FFFFFF" />
    <path
        android:fillColor="#00000000"
        android:pathData="M59,0L59,108"
        android:strokeWidth="0.8"
        android:strokeColor="#33FFFFFF" />
    <path
        android:fillColor="#00000000"
        android:pathData="M69,0L69,108"
        android:strokeWidth="0.8"
        android:strokeColor="#33FFFFFF" />
    <path
        android:fillColor="#00000000"
        android:pathData="M79,0L79,108"
        android:strokeWidth="0.8"
        android:strokeColor="#33FFFFFF" />
    <path
        android:fillColor="#00000000"
        android:pathData="M89,0L89,108"
        android:strokeWidth="0.8"
        android:strokeColor="#33FFFFFF" />
    <path
        android:fillColor="#00000000"
        android:pathData="M99,0L99,108"
        android:strokeWidth="0.8"
        android:strokeColor="#33FFFFFF" />
    <path
        android:fillColor="#00000000"
        android:pathData="M0,9L108,9"
        android:strokeWidth="0.8"
        android:strokeColor="#33FFFFFF" />
    <path
        android:fillColor="#00000000"
        android:pathData="M0,19L108,19"
        android:strokeWidth="0.8"
        android:strokeColor="#33FFFFFF" />
    <path
        android:fillColor="#00000000"
        android:pathData="M0,29L108,29"
        android:strokeWidth="0.8"
        android:strokeColor="#33FFFFFF" />
    <path
        android:fillColor="#00000000"
        android:pathData="M0,39L108,39"
        android:strokeWidth="0.8"
        android:strokeColor="#33FFFFFF" />
    <path
        android:fillColor="#00000000"
        android:pathData="M0,49L108,49"
        android:strokeWidth="0.8"
        android:strokeColor="#33FFFFFF" />
    <path
        android:fillColor="#00000000"
        android:pathData="M0,59L108,59"
        android:strokeWidth="0.8"
        android:strokeColor="#33FFFFFF" />
    <path
        android:fillColor="#00000000"
        android:pathData="M0,69L108,69"
        android:strokeWidth="0.8"
        android:strokeColor="#33FFFFFF" />
    <path
        android:fillColor="#00000000"
        android:pathData="M0,79L108,79"
        android:strokeWidth="0.8"
        android:strokeColor="#33FFFFFF" />
    <path
        android:fillColor="#00000000"
        android:pathData="M0,89L108,89"
        android:strokeWidth="0.8"
        android:strokeColor="#33FFFFFF" />
    <path
        android:fillColor="#00000000"
        android:pathData="M0,99L108,99"
        android:strokeWidth="0.8"
        android:strokeColor="#33FFFFFF" />
    <path
        android:fillColor="#00000000"
        android:pathData="M19,29L89,29"
        android:strokeWidth="0.8"
        android:strokeColor="#33FFFFFF" />
    <path
        android:fillColor="#00000000"
        android:pathData="M19,39L89,39"
        android:strokeWidth="0.8"
        android:strokeColor="#33FFFFFF" />
    <path
        android:fillColor="#00000000"
        android:pathData="M19,49L89,49"
        android:strokeWidth="0.8"
        android:strokeColor="#33FFFFFF" />
    <path
        android:fillColor="#00000000"
        android:pathData="M19,59L89,59"
        android:strokeWidth="0.8"
        android:strokeColor="#33FFFFFF" />
    <path
        android:fillColor="#00000000"
        android:pathData="M19,69L89,69"
        android:strokeWidth="0.8"
        android:strokeColor="#33FFFFFF" />
    <path
        android:fillColor="#00000000"
        android:pathData="M19,79L89,79"
        android:strokeWidth="0.8"
        android:strokeColor="#33FFFFFF" />
    <path
        android:fillColor="#00000000"
        android:pathData="M29,19L29,89"
        android:strokeWidth="0.8"
        android:strokeColor="#33FFFFFF" />
    <path
        android:fillColor="#00000000"
        android:pathData="M39,19L39,89"
        android:strokeWidth="0.8"
        android:strokeColor="#33FFFFFF" />
    <path
        android:fillColor="#00000000"
        android:pathData="M49,19L49,89"
        android:strokeWidth="0.8"
        android:strokeColor="#33FFFFFF" />
    <path
        android:fillColor="#00000000"
        android:pathData="M59,19L59,89"
        android:strokeWidth="0.8"
        android:strokeColor="#33FFFFFF" />
    <path
        android:fillColor="#00000000"
        android:pathData="M69,19L69,89"
        android:strokeWidth="0.8"
        android:strokeColor="#33FFFFFF" />
    <path
        android:fillColor="#00000000"
        android:pathData="M79,19L79,89"
        android:strokeWidth="0.8"
        android:strokeColor="#33FFFFFF" />
</vector>
```

### `app\src\main\res\drawable\ic_launcher_foreground.xml`

```xml
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:aapt="http://schemas.android.com/aapt"
    android:width="108dp"
    android:height="108dp"
    android:viewportWidth="108"
    android:viewportHeight="108">
    <path android:pathData="M31,63.928c0,0 6.4,-11 12.1,-13.1c7.2,-2.6 26,-1.4 26,-1.4l38.1,38.1L107,108.928l-32,-1L31,63.928z">
        <aapt:attr name="android:fillColor">
            <gradient
                android:endX="85.84757"
                android:endY="92.4963"
                android:startX="42.9492"
                android:startY="49.59793"
                android:type="linear">
                <item
                    android:color="#44000000"
                    android:offset="0.0" />
                <item
                    android:color="#00000000"
                    android:offset="1.0" />
            </gradient>
        </aapt:attr>
    </path>
    <path
        android:fillColor="#FFFFFF"
        android:fillType="nonZero"
        android:pathData="M65.3,45.828l3.8,-6.6c0.2,-0.4 0.1,-0.9 -0.3,-1.1c-0.4,-0.2 -0.9,-0.1 -1.1,0.3l-3.9,6.7c-6.3,-2.8 -13.4,-2.8 -19.7,0l-3.9,-6.7c-0.2,-0.4 -0.7,-0.5 -1.1,-0.3C38.8,38.328 38.7,38.828 38.9,39.228l3.8,6.6C36.2,49.428 31.7,56.028 31,63.928h46C76.3,56.028 71.8,49.428 65.3,45.828zM43.4,57.328c-0.8,0 -1.5,-0.5 -1.8,-1.2c-0.3,-0.7 -0.1,-1.5 0.4,-2.1c0.5,-0.5 1.4,-0.7 2.1,-0.4c0.7,0.3 1.2,1 1.2,1.8C45.3,56.528 44.5,57.328 43.4,57.328L43.4,57.328zM64.6,57.328c-0.8,0 -1.5,-0.5 -1.8,-1.2s-0.1,-1.5 0.4,-2.1c0.5,-0.5 1.4,-0.7 2.1,-0.4c0.7,0.3 1.2,1 1.2,1.8C66.5,56.528 65.6,57.328 64.6,57.328L64.6,57.328z"
        android:strokeWidth="1"
        android:strokeColor="#00000000" />
</vector>```

### `app\src\main\res\mipmap-anydpi-v26\ic_launcher.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="@drawable/ic_launcher_background" />
    <foreground android:drawable="@drawable/ic_launcher_foreground" />
    <monochrome android:drawable="@drawable/ic_launcher_foreground" />
</adaptive-icon>```

### `app\src\main\res\mipmap-anydpi-v26\ic_launcher_round.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="@drawable/ic_launcher_background" />
    <foreground android:drawable="@drawable/ic_launcher_foreground" />
    <monochrome android:drawable="@drawable/ic_launcher_foreground" />
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

### `app\src\main\res\values\strings.xml`

```xml
<resources>
    <string name="app_name">PDF &amp; Image Toolkit</string>
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
    <external-path
        name="external_files"
        path="." />
    <external-files-path
        name="external_files"
        path="PDF_IMG_Tools" />
    <external-path
        name="images"
        path="Pictures/ImageResizer" />
    <cache-path
        name="cache"
        path="." />
</paths>```

### `app\src\test\java\com\example\pdf_img_tools_app\ExampleUnitTest.kt`

```kt
package com.example.pdf_img_tools_app

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

