// OTW

package id.capstone.AplikasiFarming

// Import TensorFlow lite
import org.tensorflow.lite.support.common.FileUtil;
import org.tensorflow.lite.support.common.TensorOperator;
import org.tensorflow.lite.support.common.TensorProcessor;
import org.tensorflow.lite.support.image.ImageProcessor;
import org.tensorflow.lite.support.image.TensorImage;
import org.tensorflow.lite.support.image.ops.ResizeOp;
import org.tensorflow.lite.support.image.ops.ResizeOp.ResizeMethod;
import org.tensorflow.lite.support.image.ops.ResizeWithCropOrPadOp;
import org.tensorflow.lite.support.image.ops.Rot90Op;
import org.tensorflow.lite.support.label.TensorLabel;
import org.tensorflow.lite.support.tensorbuffer.TensorBuffer;

class PriceForecast : AppCompatActivity() {
	companion object {
		public const val TAG = "Price Forecast Library"
		public const val MODEL_LOCATION = ""
		public enum Model {
			
		}
		public enum Device {
			CPU,
			NNAPI,
			GPU
		}
		// TensorFlow stuff
		private lateinit var outputPriceBuffer: TensorBuffer
		private lateinit var priceProcessor: TensorProcessor
	}

	constructor(){

	}

	fun create: Classifier(Activity activity)
	
}